terraform {
  backend "azurerm" {
    resource_group_name  = "FemaleTechGen"
    storage_account_name = "femaletechgen"
    container_name       = "tfstate"
    key                  = "femaletechgen.prod.terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

variable "frontend_url" {
  type    = string
  default = "*"
}

locals {
  location = "northeurope"
}

resource "random_string" "suffix" {
  length    = 6
  min_lower = 6
  special   = false
}

resource "azurerm_resource_group" "devops" {
  name     = "female_tech_infra_${random_string.suffix.result}"
  location = local.location
}


resource "azurerm_storage_account" "upload" {
  name = "storageforpics${random_string.suffix.result}"

  location            = local.location
  resource_group_name = azurerm_resource_group.devops.name

  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_app_service_plan" "linux" {
  name                = "appservice-plan"
  location            = azurerm_resource_group.devops.location
  resource_group_name = azurerm_resource_group.devops.name
  kind                = "Linux"
  reserved            = true
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "api" {
  name = "apiforpics${random_string.suffix.result}"

  resource_group_name = azurerm_resource_group.devops.name
  location            = local.location

  storage_account {
    name         = "upload"
    account_name = azurerm_storage_account.upload.name
    access_key   = azurerm_storage_account.upload.primary_access_key
    share_name   = "images"
    type         = "AzureBlob"

  }

  site_config {
    linuxFxVersion   = "PYTHON|3.8"
    http2_enabled    = true
    app_command_line = "gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app"

    cors {
      allowed_origins = ["${var.frontend_url}"]
    }
  }


  app_service_plan_id = azurerm_app_service_plan.linux.id
}


resource "azurerm_cognitive_account" "faceapi" {
  name                = "faceapi-account"
  location            = azurerm_resource_group.devops.location
  resource_group_name = azurerm_resource_group.devops.name
  kind                = "Face"

  sku_name = "S0"

  tags = {
    Acceptance = "Test"
  }
}

resource "azurerm_cognitive_account" "speechapi" {
  name                = "speechapi-account"
  location            = azurerm_resource_group.devops.location
  resource_group_name = azurerm_resource_group.devops.name
  kind                = "SpeechServices"

  sku_name = "S0"

  tags = {
    Acceptance = "Test"
  }
}

output "webapp_name" {
  value = azurerm_app_service.api.name
}
output "face_api_key" {
  value     = azurerm_cognitive_account.faceapi.primary_access_key
  sensitive = true
}
output "speech_api_key" {
  value     = azurerm_cognitive_account.speechapi.primary_access_key
  sensitive = true
}
output "speech_api_endpoint" {
  value = azurerm_cognitive_account.speechapi.endpoint
}
