# Speech Recognition

⏲️ _est. time to complete: 30 min._ ⏲️

## Here is what you will learn 🎯

In this challenge you will learn how to:

- how to create a Speech API service in Azure
- how to connect you Speech API service with your App
- how to pass the API key to you App using Github Secrets
- how to talk to our application 🗣️

## Table of contents

### Further informative resources:

- [What is a Resource / Resource Group / Subscription?](https://docs.microsoft.com/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)
- [Speech API](https://azure.microsoft.com/services/cognitive-services/speech-services/#overview)
- [Regions and Availability Zones in Azure](https://docs.microsoft.com/azure/availability-zones/az-overview)
- [Github Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)

## Getting started

- Navigate to the **Resource Group** we created during the "Speech" challenge
- Create a new **Resource** and search for **Speech**
![](./images/light/createresource.png)

![](./images/light/selectspeech.png)

## Create Speech Cognitive Service

- Create the new resource and set the values as in the screenshot
![](./images/light/createspeech.png)

![](./images/light/createspeechresource.png)

- Similar to the "Speech" challenge, copy the key to store it in **Github Secrets**
![](./images/light/copykeys.png)

## Integrate Speech Service Credential into Github Secret

![](./images/light/vue-app-speech-api-key-secret.png#gh-light-mode-only)
![](./images/dark/vue-app-speech-api-key-secret.png#gh-dark-mode-only)

Now we will make our app understand when we talk 🗣️ to our Milligram Social Media App. 

## Run Frontend Pipeline again

- Now navigate to **Actions** > **pages** and **Re-run all jobs**
![](./images/light/runworkflow.png#gh-light-mode-only)
![](./images/dark/runworkflow.png#gh-dark-mode-only)

![](./images/light/rerunalljobs.png#gh-light-mode-only)
![](./images/dark/rerunalljobs.png#gh-dark-mode-only)

Click on the frontend link displayed under the deploy step under your pipeline `https://<yourGithubHandle>.github.io/...`

Our frontend application should now have a new button with a selfie 🤩 symbol that allows us to take selfies and estimate how old we are.
These selfies will __not__ be saved and will __not__ appear on the timeline or News Feed.

## Talk to me! What do you have to say? Play around!

So go ahead and say at least 5 sentences and tell us how great your application understands you.

Take also a book and read to your application or ask other people to talk to your phone, you might be surprised. 😁

By default it will only understand German, if you want to change the language you could change the `Microphone.vue` on line 33 and change it to 
`speechConfig.speechRecognitionLanguage = "en-US";`

That's a wrap for our 2 days! Congrats! 🥳🙏


## Overcharged? We got you covered

Ask your coach if you did not succeed. We have you covered with a back up. ⚠️

### Use prepared Milligram Backend Service

Look at the prepared application with our pictures for you to play around [Milligram](https://codeunicornmartha.github.io/FemaleAIAppInnovationEcosystem/#/?stack-key=a78e2b9a).

# What's next?

Start your own Coding Journey or try out an Azure certification as we did using Udacity, Udemy, Pluralsight, Edx etc., make sure to check out the links posted below:

_Tipps 📝_
  > - [Programming Cours](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000)
  > - Learning Paths

Be sure to check out our Microsoft Programs for you:

 - MS Aspire Program
 - Internships at MS
 - Professional Careers at Microsoft

[◀ Previous challenge](../Face/README.md) | [🔼 Home](../../README.md)