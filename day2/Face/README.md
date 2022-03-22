# Face Recognition

⏲️ _est. time to complete: 30 min._ ⏲️

## Here is what you will learn 🎯

In this challenge you will learn how to:

- how to create a Face API service in Azure
- how to connect you Face API service with your App
- how to pass the API key to you App using GitHub Secrets
- how to take a selfie 😉

_API - Application Programming Interface: A software intermediary that allows two applications to talk to each other_

### Further informative resources:

- [What is a Resource / Resource Group / Subscription?](https://docs.microsoft.com/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)
- [Face API](https://azure.microsoft.com/services/cognitive-services/face/)
- [Regions and Availability Zones in Azure](https://docs.microsoft.com/azure/availability-zones/az-overview)
- [Github Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)

## Table of contents

## Getting started

The first step in creating our Face API is to create a new resource.

_Azure Resource: In Azure, the term resource refers to an entity managed by Azure. For example, virtual machines, virtual networks, and storage accounts are all referred to as Azure resources._

- Click the **+ Create a resource** on the home page
- Pick the category **"AI + Machine Learning"**
- Create a **Face** service.
  ![](./images/dark/create-face.png)

## Create Face Cognitive Service

- Choose your **Subscription**
- Choose your **Resource Group** (A storage for multiple resources)
- Choose _West Europe_ as **Region** (Location of datacenter where the service is deployed)
- Create a **unique name** and select the **Standard S0 Pricing Tier**.
  ![](./images/dark/create-face-options.png)
- Hit **Review + create** and than **Create**

## Integrate Face Service Credential into GitHub Secrets

The API key is a unique identifier, which we will add to our code. By doing so, we can connect our code to the API and perform API calls.

- Navigate to the _Face_ service in the Azure portal and there to _Keys and Endpoint_
- Copy the _Endpoint_ and the _Key_ into a notepad.
  ![](./images/dark/milligram-face-api-access-keys.png)

In Action Secrets you can store encrypted variables that you create in an organization, repository, or repository environment. These secrets are available to use in GitHub Actions workflows.

- Navigate to your GitHub repository's _Settings_, then to _Secrets_ and _Actions_
- Click on _New repository secret_
- Set the name to `VUE_APP_FACE_API_ENDPOINT`
- Set the value to your FACE service's endpoint: https://xxxxxxx.cognitiveservices.azure.com/
- Add the secret
  ![](./images/dark/vue-app-face-api-endpoint-secret.png#gh-dark-mode-only)
  ![](./images/light/vue-app-face-api-endpoint-secret.png#gh-light-mode-only)

- Create another _New repository secret_
- Set the name to `VUE_APP_FACE_API_KEY`
- Set the value to your FACE service's key that should be a string of letters and numbers.
- Add the secret
  ![](./images/dark/vue-app-face-api-key-secret.png#gh-dark-mode-only)
  ![](./images/light/vue-app-face-api-key-secret.png#gh-light-mode-only)

## Run Frontend Pipeline again

- Navigate to _Actions_, than to your _pages_ workflow and hit _run workflow_.

- Wait a moment for your workflow to run and your changes to kick in. Click on the frontend link displayed under the deploy step under your pipeline `https://<yourGithubHandle>.github.io/...` or restart the App on your phone.

Our frontend application should now have a new button with a selfie 🤩 symbol that allows us to take selfies and estimate how old we are.
These selfies will **not** be saved and will **not** appear on the timeline or News Feed.

## Take Selfies! How old are you really? Play around!

So go ahead and take at least 5 selfies and tell us how old you are in all of them.

Take also pictures of people who are around you and estimate their age, you might surprise them. 😁

That's a wrap for today! Congrats! 🥳🙏

Now we will make our app understand when we talk 🗣️ to our Milligram Social Media App.

## Overcharged? We got you covered

Ask your coach if you did not succeed. We have you covered with a back up. ⚠️

### Use prepared Milligram Backend Service

Look at the prepared application with our pictures for you to play around [Milligram](https://codeunicornmartha.github.io/FemaleAIAppInnovationEcosystem/#/?stack-key=a78e2b9a).

_Tipps 📝_

> - [Machine Learning in 5 Levels of Difficulty](https://youtu.be/5q87K1WaoFI)

[◀ Previous challenge](../../day1/Application/README.md) | [🔼 Home](../../README.md) | [Next challenge ▶](../Speech/README.md)
