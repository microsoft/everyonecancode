# Défi 4: Github Copilot 

⏲️ _Temps estimé pour terminer: 15 min._ ⏲️

## Voici ce que vous allez apprendre 🎯

Aujourd'hui, vous apprendrez comment :

- Ajouter GitHub Copilot à votre espace de travail
- Ajouter un pied de page à l'application
- Générer du code avec Github Copilot
- Expliquer le code avec Github Copilot


## Table des matières

1. [Commencer](#commencer)
2. [Ajouter un pied de page](#ajouter-un-pied-de-page)
3. [Générer du code avec Github Copilot](#générer-du-code-avec-github-copilot)
4. [Expliquer le code avec Github Copilot](#expliquer-le-code-avec-github-copilot) 

### Ressources informatives supplémentaires

- [Qu'est-ce que CSS?](https://developer.mozilla.org/fr/docs/Web/CSS)
- [Documentation de GitHub Copilot](https://docs.github.com/fr/copilot)


## Commencer

Dans ce défi, nous allons affiner notre code en initiant une nouvelle *Pull Request* tout en explorant les capacités de GitHub Copilot, un assistant de codage piloté par l'IA. Notre objectif est d'intégrer un pied de page dans notre application avec l'aide de cet outil. Commençons le processus en intégrant GitHub Copilot dans notre environnement Codespace.

Voici les étapes à suivre :

1. Naviguez vers le marché des extensions et recherchez GitHub Copilot.
2. Cliquez sur le bouton "Installer" pour l'ajouter à notre environnement.  

![Installation de Github Copilot](./images/github-copilot-installation.png)  

3. Vérifiez l'installation en testant sa fonctionnalité : Ouvrez n'importe quel fichier dans le dépôt et, à n'importe quel point du code, appuyez sur **Ctrl+I**. Si une invite apparaît vous demandant quoi générer avec Copilot, alors l'installation est réussie !  

![Installation de Github Copilot](./images/copilot-ask.png)

## Ajouter un pied de page

Un pied de page de site web est une section située en bas d'une page web. Il contient souvent des liens ou des mentions de droits d'auteur. Notre objectif est d'intégrer cette section dans l'application. Commençons ce processus en créant une nouvelle branche :

1. Dans notre environnement Codespace, dans le terminal, tapez la commande `git checkout -b add-footer`. Cette commande créera une nouvelle branche nommée **add-footer** et vous basculera automatiquement sur cette nouvelle branche créée.
2. Naviguez vers le fichier situé à **frontend > src > App.vue**.
3. Dans ce fichier, localisez la balise de fermeture `</transition>`, vous pouvez la trouver à **ligne 11**. En dessous, insérez le code suivant : ``<footer>Fait avec amour ❤️</footer>``. Cet ajout intégrera une section de pied de page dans notre application.

Comme nous l'avons appris dans nos défis précédents, il est crucial de tester nos modifications dans l'environnement Codespace pour s'assurer que tout fonctionne comme prévu. Pour ce faire :

1. Dans le terminal, changez le répertoire vers le dossier frontend en exécutant ``cd frontend``.
2. Exécutez la commande ``npm run dev`` pour démarrer le serveur de développement.
3. Cliquez sur **Exécuter dans le navigateur** pour lancer l'application dans votre navigateur préféré. Une fois chargé, faites défiler jusqu'en bas de l'interface de l'application et vous devriez maintenant pouvoir voir le nouveau pied de page ajouté.  

Le pied de page actuel a quelques problèmes d'affichage que nous allons essayer de résoudre avec GitHub Copilot!


## Générer du code avec GitHub Copilot

Vous avez peut-être remarqué que le pied de page n'a pas le même visuel que le reste de la page et que lorsque vous relâchez la barre de défilement, le pied de page disparaît rapidement dans la section principale de l'application. **Cascading Style Sheets (CSS)** est un langage fondamental dans le développement web utilisé pour manipuler la présentation visuelle des pages web, y compris des éléments tels que la mise en page, les couleurs et les polices.

Maintenant, considérons le scénario où vous êtes un développeur qui n'a aucune expérience en travaillant avec CSS mais qui veut toujours améliorer l'apparence du pied de page et veut résoudre le problème de la barre de défilement. C'est là que GitHub Copilot devient incroyablement utile !

1. Supprimez la ligne de code que nous avons ajoutée à la ligne 12 ``<footer>Fait avec amour ❤️</footer>``
2. Sélectionnez tout le code en utilisant **Ctrl+A** puis appuyez sur **Ctrl+I**, écrivez dans l'invite:
   *Veuillez ajouter un pied de page à cette application qui a le texte "Fait avec amour ❤️" et veuillez ajouter un style approprié*
3. Copilot générera des suggestions de code. Cliquez sur **Accepter**.  

![Génération de code Copilot, pied de page](./images/github-copilot-add-code-1.png)
![Génération de code Copilot, style](./images/github-copilot-add-code-2.png)  

4. Relancez l'application avec ``npm run dev`` et visualisez à nouveau la page, vous devriez maintenant voir le pied de page avec le style et le problème de la barre de défilement devrait disparaître.

![Pied de page de l'application](./images/footer-in-milligram.png)



| :warning: Avertissement          |
|:---------------------------|
| Github Copilot peut générer des résultats différents pour chaque participant. Veuillez vous attendre à ce que votre interface utilisateur puisse être différente de celle montrée sur la photo. Si vous rencontrez des problèmes avec le code généré, n'hésitez pas à demander aux instructeurs.   |



## Expliquer le code avec GitHub Copilot


GitHub Copilot sert non seulement à coder, mais aussi à comprendre des sections de code inconnues. Ses capacités vont au-delà de la simple génération de code ; il peut aider à corriger les bugs, à générer de la documentation de code, et même à créer des tests.

Maintenant, regardons comment GitHub Copilot explique le code. Suivez ces étapes :

1. Identifiez une section de code que vous ne comprenez pas entièrement, comme le bloc de style `.footer`.
2. Appuyez sur **Ctrl+I** et tapez **/explain**. Cette action déclenche une liste de commandes, y compris **/tests**, **/fix**, et **/docs**.
3. En appuyant sur entrée, vous verrez une explication dans la section de chat de GitHub Copilot, située dans la barre latérale gauche. Cette interface de chat vous permet d'interagir avec Copilot de manière conversationnelle tant que vous posez des questions liées à la programmation. Ainsi, il ne fournira pas d'informations sur des sujets non liés à la programmation, comme où acheter une nouvelle guitare.  

![Expliquer le code](./images/github-copilot-commands.png)  

Avant de passer au prochain défi, essayez d'interagir davantage avec Copilot. Demandez des éclaircissements sur diverses sections du code qui peuvent vous intéresser. N'hésitez pas à expérimenter avec différentes commandes et à tirer parti des capacités de Copilot pour générer de nouveaux extraits de code. Chaque fois que vous faites une modification, assurez-vous de la tester pour observer son impact sur l'application.

[◀ Défi précédent](../ApplicationPart2/README_FR.md) | [🔼 Accueil](../../../README_FR.md) | [Prochain défi ▶](../../day2/Vision/README.md)
