# Défi 3 : Créer une application Milligram sur Azure

⏲️ _Temps estimé pour terminer : 60 min._ ⏲️

## Voici ce que vous allez apprendre 🎯

Aujourd'hui, vous allez apprendre comment :

- Commencer avec GitHub Actions
- Déployer le frontend de Milligram sur GitHub Pages
- Créer une application web Python sur Azure
- Déployer le backend de Milligram sur Azure avec GitHub Actions

## Table des matières

1. [Frontend de l'application Milligram](#frontend-de-lapplication-milligram)
  1. [Activer GitHub Actions](#activer-github-actions)
  2. [Exécuter GitHub Actions](#exécuter-github-actions)
  3. [Activer GitHub Pages dans les paramètres du projet](#activer-github-pages-dans-les-paramètres-du-projet)
  4. [Ouvrir GitHub Page sur votre téléphone](#ouvrir-github-page-sur-votre-téléphone)
  5. [Ajouter l'application à l'écran d'accueil](#ajouter-lapplication-à-lécran-daccueil)
2. [Backend de l'application Milligram](#backend-de-lapplication-milligram)
  1. [Préparer le téléchargement de l'image](#préparer-le-téléchargement-de-limage)
  2. [Faire fonctionner le backend de l'application dans le cloud](#faire-fonctionner-le-backend-de-lapplication-dans-le-cloud)
  3. [Déployer le téléchargement de l'image](#déployer-le-téléchargement-de-limage)
3. [Surfacturé ? Nous avons ce qu'il vous faut](#surfacturé-nous-avons-ce-quil-vous-faut)

### Ressources informatives supplémentaires

- [Qu'est-ce que GitHub Actions ?](https://github.com/features/actions)
- [Documentation de GitHub Actions](https://docs.github.com/actions)
- [Qu'est-ce qu'un dépôt ?](https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-repositories)
- [Qu'est-ce qu'une Ressource / Groupe de ressources / Abonnement ?](https://docs.microsoft.com/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)

## Frontend de l'application Milligram

Tout d'abord, commençons par l'application frontend - La partie que vous verrez et utiliserez sur votre téléphone mobile ou votre navigateur web. C'est le principal moyen d'interagir avec les services de Milligram.

<details>
<summary>Que signifie frontend ?</summary>

Imaginons une simple voiture. Tout ce que vous voyez - les sièges, le toit, le sol, l'interface utilisateur (tableau de bord, volant, etc.) - c'est tout le **frontend**.
Puis vous ouvrez le capot : et là il est ! Le **backend** et l'**API**. Vous pouvez voir le moteur, la transmission et quelques autres éléments.

Mais comment comprendre cet exemple maintenant... assez simple. Le **frontend** est ce que l'utilisateur utilise pour donner des instructions au **backend** via une **API**. Donc, lorsque vous appuyez sur la pédale d'accélérateur, le moteur accélère.

_Appuyer sur la pédale d'accélérateur déclenche une demande dans le frontend à l'API dans le backend pour que le moteur accélère, et la partie requise du backend (dans ce cas, le moteur) l'exécute._

</details>

### Activer GitHub Actions

Nous avons préparé une manière automatisée de créer et de mettre à jour le site web pour vous. Vous utiliserez deux des fonctionnalités géniales de GitHub. GitHub Pages et GitHub Actions. Commençons par les actions.

- Allez aux **Actions** de votre dépôt
- Cliquez sur le bouton qui dit _I understand my workflows, go ahead and enable them_ pour activer GitHub Actions

_Un [dépôt](https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-repositories) contient tous les fichiers de votre projet et l'historique des révisions de chaque fichier. Vous pouvez discuter et gérer le travail de votre projet au sein du dépôt._

![Activer GitHub Actions](./images/EnableGithubActions.png)

Assurez-vous que les Actions ont des permissions de lecture/écriture. Vérifiez cela via Paramètres->Actions->Général et descendez jusqu'à la section _Workflow Permissions_. Cliquez sur l'option _Read and write permissions_. Cliquez sur _Save_.
![Vérifier les paramètres](./images/gh-actions-read.png)

### Exécuter GitHub Actions

- Dans l'onglet **Actions** de votre dépôt, cliquez sur le workflow **pages**.
- Ouvrez le menu déroulant **Run workflow** et cliquez sur le bouton **Run workflow** pour confirmer l'exécution du workflow.

Maintenant, observez comment le workflow est exécuté et jetez un œil aux étapes individuelles qui sont exécutées pour vous par GitHub.

![Exécuter le workflow](./images/FrontendRunWorkflow.png)

### Activer GitHub Pages dans les paramètres du projet

Pour pouvoir afficher le site web (frontend) que nous avons construit et déployé en utilisant
GitHub Actions, nous devons activer GitHub Pages pour votre dépôt. GitHub
Pages est une manière facile d'afficher un site web statique lié à votre dépôt.
Beaucoup de gens l'utilisent pour afficher la documentation de leurs projets. Nous l'utiliserons
pour servir le frontend pour Milligram.

- Allez aux paramètres de votre dépôt-
  ![Paramètres du dépôt](./images/RepoSettingsTab.png)
- Naviguez jusqu'à **Pages**, sélectionnez la branche _gh-pages_ et appuyez sur le bouton de sauvegarde.
  ![Activer Pages](./images/FrontendPagesUpdated.png)
- Le déploiement prendra 1 à 2 minutes. Après cela, le site web de Milligram est
  accessible via `https://<votre nom d'utilisateur github>.github.io/everyonecancode/`.

Jetez un œil au site web. Essayez de changer le profil pour votre nom de compte GitHub
et voyez qu'il est stocké même si vous actualisez le navigateur.

### Ouvrez la page GitHub sur votre téléphone

Milligram est une petite application amusante similaire aux médias sociaux basés sur des photos que vous pourriez
connaître. Bien sûr, nous voulons l'utiliser sur nos téléphones mobiles pour pouvoir utiliser
les caméras pour prendre des selfies et des photos géniales pour Milligram. Ses principales
caractéristiques sont :

- Afficher des informations simples de compte GitHub de votre propre profil
- Prendre des photos et les ajouter au flux d'images
- Détecter des objets dans les images et créer des descriptions d'images (implémenté le jour 2)
- Transcrire les phrases que vous prononcez en utilisant Azure Speech Service (implémenté le jour 2)

Votre application est disponible. Mais il n'y a pas de stockage ou de base de données derrière. Donc, elle ne pourra pas stocker de données. Nous installerons cela à l'étape suivante.

Maintenant, pour faire les premières modifications, ouvrez votre site web personnel Milligram sur votre téléphone et explorez son contenu. Ensuite, modifiez le profil dans l'application pour afficher votre propre photo de profil GitHub dans l'application.

![Ajouter à l'écran d'accueil 1](./images/FrontendHomescreen0.jpg)

### Ajoutez l'application à votre écran d'accueil

Sur les téléphones mobiles modernes, vous pouvez "installer" des applications web sur votre écran d'accueil pour les rendre
plus accessibles et leur donner l'apparence d'une application d'un
appstore officiel. Par conséquent, nous n'ajouterons pas l'application à l'écran d'accueil de nos téléphones.

- Ouvrez le menu du navigateur pour ajouter le site web à votre écran d'accueil.
  - Voici à quoi cela devrait ressembler sur ios :
    ![Ajouter à l'écran d'accueil ios](./images/FrontendHomescreen1.jpg)
  - Voici à quoi cela devrait ressembler sur Android :
    ![Ajouter à l'écran d'accueil Android](./images/FrontendHomescreenAndroid.jpg)
- Maintenant, vous pouvez ouvrir le site web comme une application normale depuis l'écran d'accueil de votre téléphone.

## Backend de l'application Milligram

Le backend de l'application recevra les photos téléchargées, les stockera pour nous et les renverra lorsque nécessaire.

Notre application peut être divisée en un frontend (quelque chose que vous voyez et qui s'exécute localement sur votre téléphone) et un backend (quelque chose qui traite vos informations et qui s'exécute sur un serveur). Dans ce cas, comme nous voulons créer notre propre application de médias sociaux, nous avons besoin de photos pour notre "Fil d'actualités". Cela signifie que nous avons besoin d'un endroit pour stocker de nombreux fichiers et d'un endroit pour exécuter notre logique d'application (qui est notre code de programmation).

Pour stocker les fichiers, nous utiliserons un "Compte de stockage Azure" et pour exécuter notre application, nous utiliserons une "Application web Azure".
Tout d'abord, connectez-vous à votre "Compte Azure".

### Se connecter à Azure

- Allez sur votre navigateur et visitez [portal.azure.com](https://ms.portal.azure.com/?l=en.en-us#home).

- Connectez-vous avec `votre compte Azure`. Les informations de connexion vous sont fournies par votre formateur. Demandez-leur si vous ne savez pas où les trouver.

![Se connecter à Azure](./images/light/LogInAzure.png)

### Créer un compte de stockage

Notre compte de stockage est l'endroit où nous "sauvegardons" nos photos pour notre fil d'actualités.
À l'intérieur du compte de stockage, nous utilisons un [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/). Le Blob Storage peut contenir une quantité massive de fichiers.
Tout comme le disque ou le stockage sur votre ordinateur. Un point intéresant est que vous pouvez stocker autant de photos sur le compte de stockage que vous le souhaitez et vous n'avez pas à vous soucier de votre espace de stockage.

> **Ressource Azure** : Dans Azure, le terme ressource fait référence à une entité gérée par Azure. Par exemple, les machines virtuelles, les réseaux virtuels, et les comptes de stockage sont tous appelés ressources Azure.

> **Groupe de ressources Azure**: Un groupe de ressources est un conteneur qui contient des ressources liées à une solution Azure. Le groupe de ressources peut inclure toutes les ressources > pour la solution, ou seulement celles que vous souhaitez gérer en groupe.

- Allez à la page d'accueil du portail Azure.
- Cliquez sur _+ Créer une ressource_.
- Recherchez _Storage Account_ et cliquez sur _Create_.
- Sélectionnez votre abonnement et le groupe de ressources avec le nom que vous avez utilisé pour vous connecter au portail Azure.
- Le nom de votre compte de stockage Azure doit être unique à l'échelle mondiale. Il doit également utiliser des petites lettres et aucun caractère spécial.
- Assurez-vous de sélectionner `Standard` pour _Performance_ et `Locally-redundant storage (LRS)` pour _Redundancy_.
  ![Storage](./images/light/BackendStorage1.png)
- Cliquez sur _Review_ puis sur _Create_ pour terminer la création du compte de stockage.
- Une fois le compte de stockage créé, il devrait y avoir un bouton _Go to resource_. Cliquez dessus.
- Vous devriez maintenant voir votre compte de stockage. Sélectionnez _Containers_ sur le côté gauche.
- Cliquez sur le bouton _New Container_ et créez un conteneur nommé `images`. Laissez tout dans les paramètres préconfigurés tels quels.

C'est l'endroit où toutes les images téléchargées sur notre application Milligram seront stockées.

### Créer une application Web

Notre [Azure Web App](https://learn.microsoft.com/en-us/azure/static-web-apps/) est un ordinateur géré par Microsoft où vous pouvez facilement exécuter votre propre application sans vous soucier des mises à jour logicielles, des problèmes de sécurité, des sauvegardes ou des problèmes matériels (comme vous avez peut-être déjà expérimenté sur votre téléphone).

- Retournez à la page d'accueil du portail Azure.
- Cliquez sur _+ Créer une ressource_ comme vous l'avez fait précédemment.
- Recherchez _Web App_ et cliquez sur _Create_.
- Sélectionnez votre abonnement et votre groupe de ressources.
- Assurez-vous d'ajuster les paramètres selon l'image ci-dessous :
  - Nom : `<choisissez votre propre nom unique>`
  - Publier : `Code`
  - Pile d'exécution : `Python 3.8`
  - Système d'exploitation : `Linux`
  - Région : `West Europe`
    ![backend 0](./images/light/BackendApp0.png)
- Créez un nouveau plan de service App et `<choisissez votre propre nom>`.
  ![backend 1](./images/light/BackendApp1.png)
- Dans le menu déroulant du plan tarifaire, sélectionnez **Free F1** qui est gratuit, sinon vous pourriez être facturé en créant un plan plus grand.
- Cliquez sur _Review + Create_ en bas de l'écran.
- Revoyez les informations affichées et cliquez sur _Create_ sur l'écran suivant pour lancer l'application backend.

> 📝 Sur la page de révision, vous pouvez trouver des informations sur le coût estimé de votre service. Assurez-vous qu'il affiche _Estimated price - Free_


### Intégrer le stockage et configurer l'application Web

Maintenant, connectons notre application à notre stockage afin que vous puissiez prendre des photos sur votre téléphone et les stocker. Nous devons indiquer à l'application Web où elle peut trouver notre service de stockage. L'application peut prendre des configurations externes pour configurer la connexion au compte de stockage.

- Pour cela, naviguez à nouveau vers votre _Storage account_. Vous devriez pouvoir le trouver via la barre de recherche en haut soit en recherchant son nom unique, soit simplement en recherchant le compte de stockage.
- Sous _Access keys_, vous pouvez trouver la _Connection string_ de notre compte de stockage. Cliquez sur le bouton _👀 Show keys_ pour pouvoir copier sa valeur, par exemple, dans un bloc-notes.
  ![Capture d'écran de la page Access key dans le portail Azure](./images/light/SecretAccessKeys.png)
- Revenez à l'application web et ouvrez l'onglet _Configuration_, cliquez sur _New connection string_ et créez une nouvelle chaîne de connexion avec les paramètres suivants :
  | Chaîne de connexion | Type | Valeur |
  |-|-|-|
  | `STORAGE` | Custom | `<collez votre chaîne de connexion (copiée plus tôt) du Storage Account>` |
- Cliquez sur `ok` et `Save`.
- Naviguez et descendez jusqu'à l'onglet _CORS_ sur le côté gauche de votre service d'application et entrez `https://<YourGithubHandle>.github.io` sous _Allowed Origins_.
- Cliquez à nouveau sur `Save`.

Maintenant, votre compte de stockage et votre application web sont correctement connectés et peuvent communiquer entre eux.

### Configuration de l'application Web Azure

Il manque encore une petite configuration. Notre application utilise un module prêt à l'emploi pour que les utilisateurs puissent interagir avec leur contenu. Mais ce module n'est pas encore installé. Pour qu'il soit installé, nous fournissons à l'application web une configuration qui est exécutée lorsque l'application est lancée, permettant aux utilisateurs d'interagir avec les données de notre application.

- Naviguez vers **_Configuration_** sous _Settings_.
- Sous l'onglet **_General settings_**, vous devriez trouver les _Stack settings_. Pour notre backend, nous travaillons avec le langage de programmation Python - plus précisément Python 3.8.
- Derrière **_Startup Command_**, entrez `gunicorn -k uvicorn.workers.UvicornWorker` et cliquez sur _Save_.
  ![Comment configurer la commande de démarrage de l'application Web](./images/light/AppServiceStartupCommand.png)

### Déployer le code backend de Milligram sur Azure Web App via GitHub Actions

Pour que notre application de médias sociaux puisse réellement faire quelque chose, nous devons amener notre code source sur l'application Web Azure. Pour ce faire, nous automatiserons ce soi-disant "déploiement". Ainsi, nous n'avons pas à compter sur un processus manuel chaque fois que nous voulons apporter des modifications (par exemple, changer le titre de l'application) à notre application et ainsi, nous évitons de nombreuses erreurs.

- Naviguez vers l'onglet _Deployment Center_ sur le côté gauche de votre application Web dans le portail Azure.
- Sous l'onglet _Settings_, sélectionnez _GitHub_ comme _Source_ et cliquez sur _Authorize_.
- Sous _Organization_, sélectionnez votre identifiant GitHub et sous _Repository_, sélectionnez `anyonecancode` ainsi que la branche `main`.
- Cliquez sur `Save`.

Une fois que vous avez cliqué sur `Save`, le service crée automatiquement un fichier de workflow dans votre dépôt GitHub. Ce workflow est immédiatement exécuté et après environ 2 minutes, votre application web est prête. Vous pouvez également vérifier votre déploiement dans l'onglet "Actions" de votre dépôt. La couleur verte est toujours un bon signe.

### Vérifiez si l'application Milligram fonctionne correctement

Faisons une pause. Pour vous assurer que vous êtes sur la bonne voie, testez si le frontend de notre application obtient une réponse de notre service backend. Avant de tout rassembler, nous voulons nous assurer que le service backend fonctionne comme prévu.

- Naviguez vers l'onglet _Overview_ sur le côté gauche du Web App Service.
  ![URL du service d'application](./images/light/AppServicesDocLink.png)
- Cliquez sur Domaine par défaut, ajoutez `/docs` à la fin, puis testez le site web en utilisant la documentation interactive pour déterminer si les fonctionnalités de notre Milligram fonctionneront.
- Dans votre navigateur, vous aurez la vue suivante :
  ![Page de test de l'API](./images/light/TestAPIGetImages.png)

  :::tip
  📝 Si vous voulez en savoir plus sur OpenAPI, consultez [Wikipedia](<https://fr.wikipedia.org/wiki/OpenAPI_(logiciel)>).
  :::

- Sélectionnez le point de terminaison _GET/images_, cliquez sur `Try it Out` puis sur `Execute`. Une fois que vous obtenez le code de réponse 200, vous avez un service en cours d'exécution réussi. Félicitations !

  :::tip
  📝 Consultez les codes de réponse HTTP sur [Wikipedia](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP). Les codes 2xx signifient généralement le succès, tandis que les codes 4xx et 5xx indiquent différents types d'erreurs. Vous connaissez probablement 404 - Non trouvé.
  :::

### Clarifications, qu'avons-nous fait jusqu'à présent ?

Félicitations, vous venez de déployer le backend de votre application web ! Résumons ce que nous avons fait jusqu'à présent.

D'abord, nous avons déployé le frontend (interface utilisateur) de notre application web en utilisant les pages github. C'est ce que vous voyez lorsque vous allez sur votre lien de pages github. Le frontend avait besoin d'un serveur pour servir des images et exécuter une certaine logique. C'est là que la partie azure est intervenue. 

Nous avons créé une ressource de stockage, elle est responsable du stockage de nos images. Ensuite, nous avons créé une ressource d'application web, ici nous exécuterons notre logique de serveur. La logique du serveur est écrite en Python en utilisant un framework appelé FastAPI. Le code de la logique du serveur est hébergé dans le dépôt github de everyonecancode. 

Nous avons connecté notre application web au dépôt github et nous avons demandé au serveur d'exécuter une commande spécifique lors du démarrage de l'application web. Cette commande commencera à exécuter notre logique de serveur, c'est pourquoi vous pouvez voir les docs dans votre navigateur sous `/docs`. Ensuite, nous essaierons de connecter le Frontend au Backend.

### Intégrer l'URL de l'application web Azure dans les secrets de GitHub

Maintenant que nous sommes sûrs que notre service backend fonctionne comme prévu, nous pouvons tout rassembler.

Pour ce faire, nous utiliserons une fonctionnalité de GitHub appelée _Secrets_, où vous pouvez stocker votre URL de backend pour faire parler votre frontend avec le service backend.

- Sur la page de votre dépôt dans GitHub, sélectionnez _Settings_ et naviguez vers _Secrets and Variables_ > _Actions_.
- Ajoutez un _New repository secret_ nommé `VITE_IMAGE_API_URL` et comme valeur mettez `<l'URL de votre WebApp>`.
  > ⚠️⚠️ Votre URL doit se terminer par un **/**. Elle devrait ressembler à ceci : `https://xxxx.azurewebsites.net/` > ![Création de secrets GitHub](./images/light/VITE_IMAGE_API_URL.png)

### Exécutez à nouveau le pipeline frontend

Pour que le changement d'ajout du secret prenne effet dans le frontend, nous devons exécuter à nouveau notre pipeline de construction afin que le processus puisse récupérer le nouveau paramètre créé.

- Naviguez vers l'onglet _Actions_, sélectionnez le workflow _pages_ et relancez le workflow :
  ![Workflow frontend GitHub](./images/light/RunWorkflowFrontend.png)

- Une fois le workflow démarré, vous verrez le workflow en cours d'exécution. Vous pouvez accéder à la vue ci-dessous en cliquant sur l'exécution du workflow.
  ![Progression du workflow frontend GitHub](./images/light/FrontendInProgress.png)
- Enfin, terminons le service Milligram.
  ![Workflow frontend GitHub terminé](./images/light/FrontendDone.png)

### Ouvrez l'application - Prenez un selfie et consultez votre fil d'actualités

Cliquez sur le lien frontend affiché sous l'étape de déploiement sous votre pipeline `https://<votreNomGithub>.github.io/...` ou rouvrez l'application sur votre téléphone.

Notre application frontend devrait maintenant avoir un nouveau bouton avec un symbole de caméra qui nous permet de prendre des photos. Ces photos devraient ensuite apparaître sur la chronologie ou le fil d'actualités.

Alors allez-y et prenez au moins 5 photos et assurez-vous qu'elles apparaissent dans votre application. Assurez-vous de les partager avec au moins 1-2 amis pour qu'ils puissent également télécharger leurs photos sur votre fil d'actualités.

C'est tout pour aujourd'hui. Félicitations ! 🎉

Demain, nous rendrons notre application intelligente en ajoutant de l'intelligence artificielle pour détecter les objets dans vos images ainsi que pour parler à notre application.

## Vous coincez ? Nous avons ce qu'il vous faut

Demandez à votre coach si vous n'avez pas réussi. Nous avons une solution de secours pour vous.

### Utilisez le service backend Milligram préparé

Regardez l'application préparée avec nos photos pour que vous puissiez jouer [Milligram](https://codeunicornmartha.github.io/FemaleAIAppInnovationEcosystem/#/?stack-key=a78e2b9a).

[◀ Défi précédent](../ApplicationPart1/README_FR.md) | [🔼 Accueil](../../../README_FR.md) | [Prochain défi ▶](../../day2/Vision/README_FR.md)