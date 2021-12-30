# Speech Recognition

⏲️ _est. time to complete: 30 min._ ⏲️

## Here is what you will learn 🎯

In this challenge you will learn how to:

- how to create a Speech API service in Azure
- how to connect you Speech API service with your App
- how to pass the API key to you App using Github Secrets
- how to take a selfie 😉

## Table of contents

### Further informative resources:

- [What is a Resource / Resource Group / Subscription?](https://docs.microsoft.com/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)
- [Speech API](https://azure.microsoft.com/services/cognitive-services/speech-services/#overview)
- [Regions and Availability Zones in Azure](https://docs.microsoft.com/azure/availability-zones/az-overview)
- [Github Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)

## Getting started

- Navigate to the **Resource Group** we created during the "Speech" challenge
- Create a new **Resource** and search for **Speech**
![](./images/createresource.png)

![](./images/selectspeech.png)

## Create Speech Cognitive Service

- Create the new resource and set the values as in the screenshot
![](./images/createspeech.png)

![](./images/createspeechresource.png)

- Similar to the "Speech" challenge, copy the key to store it in **Github Secrets**
![](./images/copykeys.png)

## Integrate Speech Service Credential into Github Secret

![](./images/vue-app-speech-api-key-secret.png)

## Run Frontend Pipeline again

- Now navigate to **Actions** > **pages** and **Re-run all jobs**
![](./images/runworkflow.png)

![](./images/rerunalljobs.png)

## Talk to me! What do you have to say? Play around!
