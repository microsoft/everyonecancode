# Challenge 6: Chat Bot

⏲️ _est. time to complete: 30 min._ ⏲️

## Here is what you will learn 🎯

In this challenge you will learn how to:

- Create an OpenAI service in Azure
- Deploy an OpenAI model and connect it to your app
- Pass the API key to your app using GitHub Secrets
- Start chatting with model powered assistant in the app

## Getting started
- Navigate to your **Resource Group** we created on Day 1 during the previous challenges again
- Create a new **Resource** and search for **Azure OpenAI**

    ![Screenshot of how to create a resource](./images/resource-azure-openai.png)

## Create OpenAI Azure service

-  Select **Azure OpenAI** and hit **Create**.
-  Your subscription and resource group should already be set. Select **westeurope** as region and **Standard S0**.
- Give the resource a unique name.
- Hit **Next** and in network you should select "All networks, including the internet, can access this resource."
- Hit **Next** twice and create the resource
  ![Screenshot of Azure Portal create page for openAI Azure](./images/resource-azure-openai-settings.png)
  ![Screenshot of Azure Portal create page for openAI Azure, networking](./images/resource-azure-openai-network.png)

## Deploying openAI Large Language Model 
- Go to the Azure openAI resource you created and click on **Model deployments**
- Next, click on **Create new deployment** here we will choose the OpenAI model we want to deploy
- Select model **gpt-35-turbo** and model version **Auto-update to default**
- Give a unique name to your deployment name then click on create  

  ![Screenshot of Gpt turbo model deployment](./images/gpt-turbo-deployment.png)

Congratulations! You just deployed an instance of the openAI gpt turbo model, we will later add this model to our Milligram app to build a chat bot. For now you can actually test it out inside azure and ask it a few questions. Go to the model you deployed and click on **Open in Playground**, there you can chat with the chat assistant. You can also change the parameters of the model under **Configuration > Parameters**
 
![Screenshot of Gpt turbo model playground](./images/gpt-playground.png)

##  Integrate OpenAI Azure credentials into GitHub Secret 
Similar to what we did in the challenges on Day 1 we now want to add the secret keys to Github 
- Go to the Azure openAI resource dashboard and click on **Keys and Endpoint**
- On Github Go to your repository, **Settings > Secrets and Variables > Actions** then click on **create new repository secret**
- Create new secret with name **VITE_CHAT_API_KEY** and paste Key 1
- Create another secret with name **VITE_CHAT_API_ENDPOINT** and paste the endpoint url
- Finally create another secret with name **AZURE_OPENAI_MODEL_NAME** And paste the name you chose when you deployed the gpt turbo model.

## Run Frontend Pipeline again

- Navigate to **Actions** > **Pages** and **Run workflow**

Click on the frontend link displayed under the deploy step under your pipeline `https://<yourgithubhandle>.github.io/...` or open the app on your phone.

Our frontend application should now have a new button with a chat symbol that allows us to chat with our assistant. The assistant is powered by the model we deployed through the Azure OpenAI service. Have a chat with your bot 🎉