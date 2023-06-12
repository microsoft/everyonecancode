# Challenge 5: Speech Recognition

⏲️ _est. time to complete: 30 min._ ⏲️

## Here is what you will learn 🎯

In this challenge you will learn how to:

- Create a Speech API service in Azure
- Connect you Speech API service with your app
- Pass the API key to you app using GitHub Secrets
- How to talk to our application

## Table of contents

### Further informative resources:

- [What is a Resource / Resource Group / Subscription?](https://docs.microsoft.com/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)
- [Speech API](https://azure.microsoft.com/services/cognitive-services/speech-services/#overview)
- [Regions and Availability Zones in Azure](https://docs.microsoft.com/azure/availability-zones/az-overview)
- [GitHub Encrypted secrets](https://docs.GitHub.com/en/actions/reference/encrypted-secrets)

## Getting started

- Use the same Cognitive Service you created in the [Vision challenge](../Vision/README.md)

## Integrate Speech Service credentials into GitHub Secret

Again you need to share the information of this resource with the web app, so that it can utilize the Speech service's _intelligence_. Therefore, we will create another GitHub Secret and share this with the app.

- Navigate to GitHub > Settings > Secrets > Actions and add a `New repository secret`.
- Name: `VITE_SPEECH_API_KEY`
- Value: The Key of your Speech service you copied before
- Add Secret.

  ![Screenshot of creating secret](./images/light/vue-app-speech-api-key-secret.png)

Now we will make our app understand when we talk to our Milligram social media application.

## Run Frontend Pipeline again

- Navigate to **Actions** > **Pages** and **Run workflow**
  ![](./images/light/runworkflow.png)

  ![](./images/light/rerunalljobs.png)

Click on the frontend link displayed under the deploy step under your pipeline `https://<yourgithubhandle>.github.io/...` or open the app on your phone.

Our frontend application should now have a new button with a microphone symbol that allows us to talk to our app in English and German and have our speech transcribed.

Neither what you say nor what is transcribed will be saved and will **not** appear on the timeline or news feed.

## Talk to me! What do you have to say? Play around!

So go ahead and say at least 5 sentences and tell us how great your application understands you.

Take also a look and read to your application or ask other people to talk to your phone, you might be surprised.

By default, it will only understand German and English, if you want to change the language you could change the repo in `Frontend` > `scr` > `views` > `Microphone.vue` on line 7 and add e.g. Ukrainian
`<option value="uk-UA">Ukrainian</option>`

As you can see, the language is represented by four letters. For German it's de-DE, for English (USA) it is en-US and for Ukrainian it is uk-UA. [Here](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support) you can find all supported languages with their code.

That's a wrap for our 2 days. Congrats!

### Overcharged? We got you covered

Ask your coach if you did not succeed. We have you covered with a back up. ⚠️

### Use prepared Milligram Backend Service

Look at the prepared application with our pictures for you to play around [Milligram](https://codeunicornmartha.GitHub.io/FemaleAIappInnovationEcosystem/#/?stack-key=a78e2b9a).

### What's next?

Start your own coding journey now or try out an Azure certification as we did using Udacity, Udemy, Pluralsight, Edx etc., make sure to check out the links posted below:

_Tipps 📝_

> - [Programming course on Udacity](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000)
> - [Microsoft Azure AI Fundamentals learning path (with optional certification)](https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/)
> - [Microsoft Azure Fundamentals learning path (with optional certification)](https://learn.microsoft.com/en-gb/certifications/exams/az-900)

Be sure to check out our Microsoft Programs:

- [Microsoft Aspire Program for early in career hires](https://www.microsoft.com/en-ie/earlycareers/aspire-program)
- Internships at MS
- [Professional Careers at Microsoft](https://careers.microsoft.com/)

[◀ Previous challenge](../Vision/README.md) | [🔼 Home](../../../README.md)