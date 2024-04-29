# Défi 7: Chat Bot

⏲️ _temps estimé pour terminer: 30 min._ ⏲️

## Voici ce que vous allez apprendre 🎯

Dans ce défi, vous apprendrez comment:

- Créer un service OpenAI dans Azure
- Déployer un modèle OpenAI et le connecter à votre application
- Transmettre la clé API à votre application en utilisant GitHub Secrets
- Commencer à discuter avec l'assistant alimenté par le modèle dans l'application

## Table des matières

1. [Commencer](#commencer)
2. [Créer une instance de service OpenAI Azure](#créer-une-instance-de-service-openai-azure)
3. [Déployer le grand modèle de langage OpenAI](#déployer-le-grand-modèle-de-langage-openai)
4. [Identifiants OpenAI Azure](#identifiants-openai-azure)
5. [Exécutez à nouveau le pipeline Frontend](#exécutez-à-nouveau-le-pipeline-frontend)

### Ressources informatives supplémentaires

- [Documentation OpenAI Azure](https://learn.microsoft.com/en-us/azure/ai-services/openai/)


## Commencer
- Naviguez vers votre **Groupe de ressources** que nous avons créé le jour 1 lors des défis précédents
- Créez une nouvelle **Ressource** et recherchez **Azure OpenAI**

    ![Capture d'écran de comment créer une ressource](./images/resource-azure-openai.png)

## Créer une instance de service OpenAI Azure

- Sélectionnez **Azure OpenAI** et cliquez sur **Créer**.
- Votre abonnement et votre groupe de ressources doivent déjà être définis. Sélectionnez **westeurope** comme région et **Standard S0**.
- Donnez un nom unique à la ressource.
- Cliquez sur **Suivant** et dans le réseau, vous devez sélectionner "Tous les réseaux, y compris Internet, peuvent accéder à cette ressource."
- Cliquez sur **Suivant** deux fois et créez la ressource
  ![Capture d'écran de la page de création du portail Azure pour openAI Azure](./images/resource-azure-openai-settings.png)
  ![Capture d'écran de la page de création du portail Azure pour openAI Azure, réseau](./images/resource-azure-openai-network.png)

## Déployer le grand modèle de langage OpenAI 
- Allez à la ressource Azure openAI que vous avez créée et cliquez sur **Déploiements de modèles**
- Ensuite, cliquez sur **Créer un nouveau déploiement** ici, nous choisirons le modèle OpenAI que nous voulons déployer
- Sélectionnez le modèle **gpt-35-turbo** et la version du modèle **Mise à jour automatique par défaut**
- Donnez un nom unique à votre nom de déploiement puis cliquez sur créer  

  ![Capture d'écran du déploiement du modèle turbo Gpt](./images/gpt-turbo-deployment.png)

Félicitations! Vous venez de déployer une instance du modèle turbo gpt openAI, nous ajouterons plus tard ce modèle à notre application Milligram pour construire un chat bot. Pour l'instant, vous pouvez en fait le tester à l'intérieur d'azure et lui poser quelques questions. Allez au modèle que vous avez déployé et cliquez sur **Ouvrir dans Playground**, là vous pouvez discuter avec l'assistant de chat. Vous pouvez également modifier les paramètres du modèle sous **Configuration > Paramètres**
 
![Capture d'écran du terrain de jeu du modèle turbo Gpt](./images/gpt-playground.png)

## Identifiants OpenAI Azure
Pour connecter notre interface utilisateur avec le modèle openAI, nous devons intégrer les identifiants openAI dans le processus. Pour cela, il y a 2 options. Nous pouvons ajouter nos clés dans l'application web Azure (Option 1) ou nous pouvons l'automatiser en ajoutant les clés dans notre flux de travail github.

### Option 1: Ajouter les identifiants OpenAI Azure à l'application web
Retournez à Azure et ouvrez à nouveau l'application web Milligram:
- Allez à **variables d'environnement**  
- Créez une nouvelle variable avec le nom **CHAT_API_KEY** et collez la clé 1
- Créez une autre variable avec le nom **CHAT_API_ENDPOINT** et collez l'URL de l'endpoint
- Enfin, créez une autre variable avec le nom **AZURE_OPENAI_MODEL_NAME** Et collez le nom que vous avez choisi lorsque vous avez déployé le modèle turbo gpt.

![Capture d'écran du terrain de jeu du modèle turbo Gpt](./images/milligram-env-vars.png)

### Option 2: Intégrer les identifiants OpenAI Azure dans GitHub Secret 
Semblable à ce que nous avons fait dans les défis du jour 1, nous voulons maintenant ajouter les clés secrètes à Github 
- Allez au tableau de bord de la ressource Azure openAI et cliquez sur **Clés et Endpoint**
- Sur Github, allez à votre dépôt, **Paramètres > Secrets et Variables > Actions** puis cliquez sur **créer un nouveau secret de dépôt**
- Créez un nouveau secret avec le nom **CHAT_API_KEY** et collez la clé 1
- Créez un autre secret avec le nom **CHAT_API_ENDPOINT** et collez l'URL de l'endpoint
- Enfin, créez un autre secret avec le nom **AZURE_OPENAI_MODEL_NAME** Et collez le nom que vous avez choisi lorsque vous avez déployé le modèle turbo gpt.

Maintenant, nous voulons également ajouter les secrets à notre flux de travail github:  

1. Ajoutez le code suivant sous `subscription-id` autour de la ligne 74 dans le fichier situé à **.github/workflows/main_milligram.yml**
```
      - uses: azure/appservice-settings@v1
        with:
          app-name: 'milligram'
          slot-name: 'Production'  # Facultatif et nécessaire uniquement si les paramètres doivent être configurés sur le slot de déploiement spécifique
          app-settings-json: '[{ "name": "CHAT_API_KEY", "value": "${{ secrets.CHAT_API_KEY }}", "slotSetting": false }, { "name": "CHAT_API_ENDPOINT", "value":  "${{ secrets.CHAT_API_ENDPOINT }}", "slotSetting": false }, { "name": "AZURE_OPENAI_MODEL_NAME", "value": "${{ secrets.AZURE_OPENAI_MODEL_NAME }}", "slotSetting": false }]'
        id: settings
```

## Exécutez à nouveau le pipeline Frontend

- Naviguez vers **Actions** > **Pages** et **Exécutez le workflow**

Cliquez sur le lien frontend affiché sous l'étape de déploiement sous votre pipeline `https://<yourgithubhandle>.github.io/...` ou ouvrez l'application sur votre téléphone.

Notre application frontend devrait maintenant avoir un nouveau bouton avec un symbole de chat qui nous permet de discuter avec notre assistant. L'assistant est alimenté par le modèle que nous avons déployé via le service Azure OpenAI. Discutez avec votre bot 🎉