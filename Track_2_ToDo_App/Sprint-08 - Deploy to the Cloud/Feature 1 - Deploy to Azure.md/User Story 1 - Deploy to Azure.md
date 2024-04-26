# User Story: Deploy to Azure Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story

As a user I want to create Azure SQL database to persist my todo items in the cloud, create Azure App Service and deploy my application in the Azure Cloud to access anytime.

## 🎯Acceptance Criteria:

- Azure SQL Database named _todo_ is created and todo items are persisted by the application.
- Azure App Service is with Python runtime environment is created and deployed application.
- Created database connection string using the Azure SQL Database information to connect through my application to persist todo items.
- Configured Azure OpenAI information to access as environment variables using Azure App Service settings in my application.

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

#### 1. Open Visual Studio Code

Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us05/)

### Setting up an Azure SQL Database

#### 2. Login to Azure Resource Management

In VS Code, open new terminal window and run the command below to login to Azure resource management. A browser window will be opened and redirected to Microsoft Entra ID to complete login to Azure resource management.

```powershell
az login
```

#### 3. Set default subscription to deploy Azure resources

Once the login is complete run the command below to verify your tenant and subscriptions. If this command shows more than one subscription, copy Subscription ID that you would lke to deploy application and set as default subscription Azure SQL Database.

```powershell
az account show
az account set --subscription <SubscriptionID>
```

![Show current account](../images/az-account-show.png)

#### 4. Create Azure Resource Group

Create Azure resource group to create Azure resources, all resources created in this sprint will be created in this resource group.

```powershell
$resourcegroup = "rg-everyonecancode"
$azureRegion = "<Azure Region>"
az group create --name $resourcegroup --location $azureRegion
```

> [!NOTE]  
> 📄Using Azure SQL database server is optional. If you are not using Azure SQL database skip steps 5, 6, 8, 11, and 12.

#### 5. Create Azure SQL Database Server

Create Azure SQL Database by running the commands below, provide password that is 18 chars long to create Azure SQL Server.

```powershell
$dbServerName = "everyonecancode-<random>"
$addminPassword = "<random password>"
az sql server create --name $dbServerName --resource-group $resourcegroup --admin-user 'sqladmin' --admin-password  $addminPassword
az sql server firewall-rule create --name AllowAzureServices --server $dbServerName --resource-group $resourcegroup  --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0
```

#### 6. Create Azure SQL Database

Create Azure SQL Database by running the command below.

```powershell
az sql db create --resource-group $resourcegroup --server $dbServerName --name todo --edition Basic
```

### Deploying the Web Application to Azure

To deploy this application to Azure you need an hosting environment to run Python web application. Azure App Service support Python runtime on Linux operating system. Complete steps below before you deploy application to Azure App Service.

Python code in this application depends on other Python modules. These modules are not readily available when you create a new Web Application in Azure App Service. To deploy these dependent modules you need to prepare a requirements.txt file, which is then used by Azure App Service to deploy these modules to run the application.

#### 7. Create requirements.txt file to install Python modules

Review `requirements.txt` file under _app_s08_f01_us01_ folder and make sure this file has libraries listed below. If not replace file content using the code snippet below, and save file.

```python
openai
flask
flask[async]
flask_sqlalchemy
sqlalchemy
semantic_kernel
pyodbc
fastapi
```

#### 8. Update code to use Azure App Service database connection string environment variable

Open `app.py` file under _app_s08_f01_us01_ folder. Replace code lines 16, 17, and 18 with the code below. Pay attention to the _SQLAZURECONNSTR_AZURE_SQL_CONNECTIONSTRING_ environment variable is in this code snippet. The prefix **SQLAZURECONNSTR_** indicates it is a Azure SQL database connection string environment variable. You will create this environment variable later steps.

```python

# mssql+pyodbc://<sql user name>:<password>@<azure sql server>.database.windows.net:1433/todo?driver=ODBC+Driver+17+for+SQL+Server
connection_string = os.environ.get("SQLAZURECONNSTR_AZURE_SQL_CONNECTIONSTRING", '')

# Use local database if Azure SQL server is not configured
if not connection_string:
    print('Azure SQL not configured, Using local SQLLite database')
    basedir = os.path.abspath(os.path.dirname(__file__))   # Get the directory of the this file
    print('Base directory:', basedir)
    todo_file = os.path.join(basedir, 'todo_list.txt')     # Create the path to the to-do list file using the directory
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'todos.db')
else:
    print('Using Azure SQL database')
    app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

```

#### 9. Update recommendations engine code to use Azure App Service environment variables

Open _recommendation_engine.py_ file under _app_s08_f01_us01_ folder and make following changes.

- Delete code lines 17 and 18.
- Replace code lines 1 to 13 using the code snippet below and save file.

```python
import os
import json
import asyncio
from services import Service
from openai import AzureOpenAI

deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", '')
api_key = os.environ.get("AZURE_OPENAI_API_KEY", '')
endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", '')
use_open_ai = os.environ.get("USE_AZURE_OPENAI", 'True')

#uses the USE_AZURE_OPENAI variable from the .env file to determine which AI service to use
#False means use OpenAI, True means use Azure OpenAI
selectedService = Service.AzureOpenAI if use_open_ai == "True" else Service.OpenAI
```

#### 10. Create Azure App Service and Deploy Application

Create Azure App Service and deploy code by executing the commands below in the PowerShell terminal. Make sure your current directory is at _app_s08_f01_us01_ folder, if not change directory to this folder. Provide resource group name and web application to deploy this application and leave other parameters default. Application name must be unique in Azure and provide that do not conflict, typically append or prepend with your name initials. Specify Azure Region as one of the location closest to you, for example _eastus_ if you are on the US East Coast or _westus_ if you are located in US West coast.

```python
$appName = 'everyonecancode-<random>'
az webapp up --resource-group $resourcegroup --name $appName --runtime PYTHON:3.12 --sku Free --plan everyonecancode --location <Azure Region>
```

#### 11. Build database connection string

Run command from the code snippet below to create connection string variable and use it in the next step.

```python
$connection_string = "mssql+pyodbc://sqladmin:$($adminPassword)@$($dbServerName).database.windows.net:1433/todo?driver=ODBC+Driver+17+for+SQL+Server"
```

#### 12. Configure SQL database connection string environment variable

Run command below set database connection string environment variable.

```python
az webapp config connection-string set --resource-group $resourcegroup --name $appName --connection-string-type SQLAzure --settings AZURE_SQL_CONNECTIONSTRING=$connection_string
```

#### 13. Configure Azure Open AI environment variables

Configure Auzre Open AI environment variables by executing the commands below. Copy values from .env file created in the previous sprints.

```python
az webapp config appsettings set --resource-group $resourcegroup --name $appName --settings AZURE_OPENAI_DEPLOYMENT_NAME="gpt-35-turbo" AZURE_OPENAI_ENDPOINT="<Azure Open AI endpoint>" AZURE_OPENAI_API_KEY="<Azure Open AI API Key>" USE_AZURE_OPENAI="True"
```

### Test the application

#### 14. Login to Azure Portal

Login to Azure Portal to view Azure App Service just deployed and configure, and search for App Services as shown below.

  ![Search for App Service in Azure Portal](../images/auzre-portal-search-app-service.png)

#### 15. Location Azure App Service

Locate the App Service just deployed by identifying with the name and click on the name to open service overview.

  ![Search for App Service in Azure Portal](../images/auzre-portal-app-service-list.png)

#### 16. Access Application in Web Browser

Click on the _Browse_ or _Default domain name_ in the App Service overview page. Web page will open in a different tab, and if everything is working expected you should be able to view web page as shown below.

  ![Search for App Service in Azure Portal](../images/auzre-portal-app-service-overview.png)

  ![Search for App Service in Azure Portal](../images/azure-web-app-todo.png)

<br/>
🎉 Congratulations! You have now successfully deployed your to-do application to the Azure cloud.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-08%20-%20Deploy%20to%20the%20Cloud/src/app-s08-f01-us01/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 8 ](/Track_2_ToDo_App/Sprint-08%20-%20Deploy%20to%20the%20Cloud/README.md) | [**◀ Previous user story** (in previous sprint) ](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/Feature%201%20-%20Advanced%20Styling/User%20Story%205%20-%20Show%20Spinner.md)
