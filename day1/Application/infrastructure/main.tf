provider "azurerm" {
    features {}
}

locals {
    location = "westeurope"
}

resource "random_string" "suffix" {
  length           = 6
  special          = false
}

resource "azurerm_resource_group" "devops" {
    name = "female_tech_infra_${random_string.suffix.result}"
    location = local.location
}


resource "azurerm_storage_account" "upload" {
  name = "uploadstoragefornewpics_${random_string.suffix.result}"

  location            = local.location
  resource_group_name = azurerm_resource_group.devops.name

  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_app_service_plan" "function" {
  name                = "function-appservice-plan"
  location            = azurerm_resource_group.devops.location
  resource_group_name = azurerm_resource_group.devops.name

  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_function_app" "upload" {
  name = "uploadstoragefornewdocs"

  resource_group_name = azurerm_resource_group.devops.name
  location            = local.location

  storage_account_name       = azurerm_storage_account.upload.name
  storage_account_access_key = azurerm_storage_account.upload.primary_access_key


  app_service_plan_id = azurerm_app_service_plan.function.id
}


resource "azurerm_cognitive_account" "faceapi" {
  name                = "faceapi-account"
  location            = azurerm_resource_group.devops.location
  resource_group_name = azurerm_resource_group.devops.name
  kind                = "FaceApi"

  sku_name = "S0"

  tags = {
    Acceptance = "Test"
  }
}

resource "azurerm_cognitive_account" "speechapi" {
  name                = "speechapi-account"
  location            = azurerm_resource_group.devops.location
  resource_group_name = azurerm_resource_group.devops.name
  kind                = "SpeechApi"

  sku_name = "S0"

  tags = {
    Acceptance = "Test"
  }
}



