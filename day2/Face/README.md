# Face Recognition

⏲️ _est. time to complete: 30 min._ ⏲️

## Here is what you will learn 🎯

In this challenge you will learn how to:

- how to create a Face API service in Azure
- how to connect you Face API service with your App
- how to pass the API key to you App using Github Secrets
- how to take a selfie 😉

## Table of contents

## Getting started

The first step in creating our Face API is to create a new resource.
- Click the **big "+" symbol** on the main page
- Pick the category **"AI + Machine Learning"**
- Create a **Face** service.
![](./images/create-face.png)

## Create Face Cognitive Service

- Choose your **subscription**
- Create a new **Resource Group** (if not already available)
- Choose *West Europe* as **Region**
- Create a **unique name** and select the **Standard S0 Pricing Tier**.
![](./images/create-face-options.png)

## Integrate Face Service Credential into Github Secret

The API key is a unique identifier, which we will add to our code. By doing so, we can connect our code to the API and perform API calls.
![](./images/milligram-face-api-access-keys.png)

In Action Secrets you can store encrypted variables that you create in an organization, repository, or repository environment. These secrets are available to use in GitHub Actions workflows.
- Set the name and value similar to picture and replace the *xxxxxx* part with your values
- Add the secret
![](./images/vue-app-face-api-endpoint-secret.png)

![](./images/vue-app-face-api-key-secret.png)

## Run Frontend Pipeline again

## Take Selfies! How old are you really? Play around!

## Overcharged? We got you covered:
