provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "default" {
  name     = "anyonecancode-rg"
  location = "West Europe"
}

resource "azurerm_storage_account" "images" {
  name = "anyonecancodeimages"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "images" {
  name = "images"

  storage_account_name = azurerm_storage_account.images.name
}

resource "azurerm_service_plan" "default" {
  name = "anyonecancode-sp"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  os_type  = "Linux"
  sku_name = "B1"
}

resource "azurerm_linux_web_app" "backend" {
  name = "anyonecancode-backend"

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
      allowed_origins = [var.STATIC_WEBSITE_URL]
    }

    application_stack {
      python_version = "3.8"
    }
  }
}

resource "azurerm_cognitive_account" "face" {
  name = "anyonecancode-face"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  kind     = "Face"
  sku_name = "S0"
}

resource "azurerm_cognitive_account" "speech" {
  name = "anyonecancode-speech"

  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  kind     = "SpeechServices"
  sku_name = "S0"
}
