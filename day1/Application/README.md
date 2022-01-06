# Day 1: Deployment of Miligram application on Azure with Github Actions

⏲️ _Est. time to complete: 60 min._ ⏲️

## Here is what you will learn 🎯

In this day you will learn how to:

- get started with Github Actions
- deploy the Milligram frontend to Github Pages
- create a Python Web App on Azure
- deploy the Milligram backend on Azure with Github Actions

## Table Of Contents

1. [Milligram Application Frontend](#milligram-application-frontend)
   1. [Enable Github Action](#enable-github-action)
   2. [Run Github Action](#run-github-action)
   3. [Enable Github Page in Project Settings](#enable-github-page-in-project-settings)
   4. [Open Github Page on your phone](#open-github-page-on-your-phone)
   5. [Add Application to home screen](#add-application-to-home-screen)
2. [Milligram Application Backend](#milligram-application-backend)
   1. [Prepare Image Upload](#prepare-image-upload)
   2. [Make Application Backend run in the Cloud](#make-application-backend-run-in-the-cloud)
   3. [Deploy Image Upload](#deploy-image-upload)
3. [Overcharged? We got you covered](#overcharged-we-got-you-covered)

### Further informative resources

- [What is Github Action?](https://github.com/features/actions)
- [Github Action Documentation](https://docs.github.com/actions)
- [What is a repository?](https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-repositories)
- [What is a Resource / Resource Group / Subscription?](https://docs.microsoft.com/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)

## Milligram Application Frontend

First let's get started with the front end application. The part that you will
see and use on your mobile phone or you web browser. This is the main way to
interact with milligrams services.


### Enable Github Action

We've prepared an automated way to create and update the website for you. You
will use two of GitHubs awesome features. GitHub Pages and GitHub Actions. Let's
get started with the actions.

- Go to your repository **Actions**
- Click the button which says _I understand my workflows, go ahead and enable them_ to enable Github Actions

_A [repository](https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-repositories) contains all of your project's files and each file's revision history. You can discuss and manage your project's work within the repository._

![Enable Github Actions](images/frontend_enable_action.png)

### Run Github Action

- In the **Actions** tab of your repository, click on the **pages** Action
- Open the **Run Workflow** dropdown and click the **Run Workflow** button to confirm the Action execution

Now observe how the workflow is beeing run and take a look at the individual steps that are run for you by GitHub.

![Run Github Action](images/frontend_run_action.png)

### Enable Github Page in Project Settings

To be able to display the website (frontend) we've built and deployed using
GitHub Actions, we need to enable the GitHub Pages for your repository.  GitHub
Pages are an easy way to display a static website related to your repository.
Many people use it to display the documentation for their projects. We will use
it to serve the frontend for milligram.

- Go to your repository settings
  ![Repository Settings](images/repo_main.png)
- Navigate to **Pages**, select the branch _gh-pages_ and hit the save button
  ![Enable Pages](images/frontend_pages.png)
- The deployment will take 1-2 minutes. After that, the Milligram website is
  accessible through `https://<your github username>.github.io/FemaleAIAppInnovationEcosystem/`

Take a look at the website. Try changing the profile to your GitHub account name
and see that it is stored even if you refresh the browser.

// TODO: Add Challenge to hange in Codespace + push

### Open Github Page on your phone

Milligram is a fun litte app similar to photo based social media that you might
be familiar with. Of course we want to use it on our mobile phones so we can use
the cameras to take awesome selfies and picture for milligram. It's main
features are:

- Display simple GitHub account information from your own profile
- Take fotos and add them to the stream of images
- Check your age and facial expression using Azure Face Recognition (implemented on day 2)
- Transcribe sentences you speak using Azure Speech Service (implemented on day2)

- Open your personal Milligram website on your phone and explore it's content
- Edit the profile in the app to show your own Github profile picture in the app
  ![Add to homescreen 1](images/frontend_homescreen_0.jpg)

### Add The application to your homescreen

On modern mobile phone you can "install" webapps on you homescreen to make them
easier accessible and make them look more like an app from the official
Appstores.

- Open the browser menu to add the website to your homescreen
  ![Add to homescreen 2](images/frontend_homescreen_1.jpg) ![Add to homescreen 2](images/frontend_homescreen_2.jpg)
- Now you can open the website like a normal app from the homescreen of your phone

## Milligram Application Backend

The Application Backend will receive uploaded photos, store them for us and return them when needed.  

Our Application can be divided into a Frontend (something you see and runs locally on your phone) and a Backend (something which processes your information). In this case as we want to create our own social media application we need pictures to be stored for our "News Feed". That means we need a place to store many files and a place to run our application logic (which is our programming code). 

To store the files we will use the "Azure Storage Account" and to run our application we will use an "Azure Web App". 
First things first we will create our first "Azure Account".

### Create Azure Account

- Browser: portal.azure.com
- Create Azure Pass 

![](./images/CreateAzurePass.png)

![](./images/EnterPromoCode.png)

// Create Account + Subscription

### Create Resource Group

- Visit portal.azure.com & log in with your Azure Account
- Click on _Create a resource_

_Azure Resource: In Azure, the term resource refers to an entity managed by Azure. For example, virtual machines, virtual networks, and storage accounts are all referred to as Azure resources._

![Create RG 1](images/backend_create_rg_0.png)

- Search & select _Resource Group_ (A storage for multiple resources) from the text field
  ![Create RG 2](images/backend_create_rg_1.png)
- Select your subscription
- Choose a name like `Milligram` to group all your resources related to this application
- Last but not least, select a region near you to host all your services
  ![Create RG 3](images/backend_create_rg_2.png)

### Create Storage Account

- Go to the start page of the Azure Portal
- Click on _Create a resource_ as you did before for the Resource Group
- Search for _Storage Account_ and click _Create_
- Select your subscription & the recently created resource group
- Make sure to select `Standard` for _Performance_ and `Locally-redundant storage (LRS)` for _Redundancy_
  ![Storage](images/backend_storage_0.png)
- Hit _Review & create_ to finish creating the storage account
- Once the Storage Account is created select _Containers_ on the left hand side
- Click the _New Container_ button and create a container named `images`

### Create Web App

- Go to the start page of the Azure Portal again
- Click on _Create a resource_ as you did before
- Search for _Web App_ and click _Create_
- Select your subscription & previously created Resource Group
- Make sure to adjust the settings according to the image below:
  - Name: `<pick your own unique name>`
  - Publish: `Code`
  - Runtime stack: `Python 3.8`
  - Operating System: `Linux`
  - Region: `West Europe`
    ![Backend 0](images/backend_app_0.png)
- Create a new App Service Plan and `<pick your own name>`
  ![Backend 1](images/backend_app_1.png)
- Click the _Dev/Test_ tab and select the **F1** which is free, otherwise you might be charged when creating a larger plan
  ![Backend 2](images/backend_app_2.png)
- Click _Review + Create_ at the bottom of the screen
- Review the displayed information and click _Create_ on the next screen to spin up the backend application

:::tip
📝 On the review page, you can find information about the estimated costs of your service. Make sure it displays _Estimated price - Free_
:::

### Integrate Storage and configure Web App

- Copy secret _Connection String_ from Storage Account from _access keys_

![](./images/secretaccesskeys.png)

- Navigate back to the Web App and open the _Configuration_ tab, click _New connection string_ and create a new connection string with the following settings:
  - Name: `STORAGE`
  - Value: `<paste your connection string from Storage Account>`
  - Type: `Custom`
- Hit `ok` and `Save`
- Navigate and Scroll down to the _CORS_ tab on the left hand side of your App Service and enter `https://<YourGithubHandle>.github.io` under _Allowed Origins_
- Hit `Save`

### Deploy Milligram Backend Code to Azure Web App via Github Action

- Navigate to the _Deployment Center_ tab on the left hand side of your App
- Under _Settings_ tab connect your _Github Account_ and under _Organization_ select your Github Handle and under _Repository_ select `FemaleAIAppInnovationEcosystem` as well as the `main` _Branch_
- Hit `Save`

### Check if Milligram Service is running correctly

- Navigate to the _Overview_ tab on the left hand side of the App

![App Service URL](./images/appservicedoclink.png)

- Hit the _URL_ and test the website using the docs to figure out if the features of our Milligram will work
- In your Browser you will have the following view:

![Test API Page](./images/TestAPIGetImages.png)

- Select GET/images endpoint hit `Try it Out` and then hit `Execute`, once you get the 200 Response Code you have a successful running service! Congratulations!

### Integrate Azure Web App Url in Github Secret

- On your Repository page select settings and navigate to secrets
- Add a _new secret_ named `VUE_APP_IMAGE_API_URL` and as value set `<your WebApp's URL>`
![Github Frontend Url](./images/FrontendAPIUrl.png)

### Run Frontend Pipeline again

- Navigate to Actions and select the pages workflow and rerun the workflow: 

![Github Frontend Workflow](./images/RunWorkflowFrontend.png)

- Once the Workflow is started you will see the Github Action running and finally finishing.

![Github Frontend Workflow Progress](./images/FrontendInProgress.png)

- and finally finishing up the Milligram Service.

![Github Frontend Workflow Done](./images/FrontendDone.png)

- Click on the frontend link displayed under the deploy step under your pipeline `https://<yourGithubHandle>.github.io/...`

### Open the App - Take a Selfie and review your News Feed

## Overcharged? We got you covered

### Use prepared Milligram Backend Service

Tipp template

:::tip
📝 This is a special hint.
:::
