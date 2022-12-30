provider "azurerm" {
  features {}
}

resource "random_id" "suffix" {
  byte_length = 2
}

locals {
  unique_suffix = var.PARTICIPANT_ID != "" ? var.PARTICIPANT_ID : random_id.suffix.hex
}

resource "azurerm_resource_group" "default" {
  name     = "anyonecancode-rg-${local.unique_suffix}"
  location = "West Europe"
}

resource "azurerm_storage_account" "images" {
  name = "anyonecancodeimages${local.unique_suffix}"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_management_policy" "auto_delete" {
  storage_account_id = azurerm_storage_account.images.id

  rule {
    name    = "delete_after_14_days"
    enabled = true

    actions {
      version {
        delete_after_days_since_creation = 14
      }
      base_blob {
        delete_after_days_since_modification_greater_than = 14
      }
    }

    filters {
      blob_types   = ["blockBlob", "appendBlob"]
      prefix_match = ["images/"]
    }
  }
}

resource "azurerm_storage_container" "images" {
  name = "images"

  storage_account_name = azurerm_storage_account.images.name
}

resource "azurerm_service_plan" "default" {
  name = "anyonecancode-sp-${local.unique_suffix}"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  os_type  = "Linux"
  sku_name = "B1"
}

resource "azurerm_linux_web_app" "backend" {
  name = "anyonecancode-backend-${local.unique_suffix}"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  service_plan_id     = azurerm_service_plan.default.id

  https_only = true

  connection_string {
    name  = "STORAGE"
    type  = "Custom"
    value = azurerm_storage_account.images.primary_connection_string
  }

  site_config {
    app_command_line = "gunicorn -k uvicorn.workers.UvicornWorker"

    cors {
      allowed_origins = var.STATIC_WEBSITE_URL
    }

    application_stack {
      python_version = "3.8"
    }
  }
}

resource "azurerm_cognitive_account" "speech" {
  name = "anyonecancode-speech-${local.unique_suffix}"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  kind     = "SpeechServices"
  sku_name = "S0"
}
