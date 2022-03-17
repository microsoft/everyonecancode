# Spracherkennung

⏲️ _geschätzte Bearbeitungszeit: 30 min._ ⏲️

## Das wirst du lernen 🎯

In dieser Aufgabe wirst du lernen:

- wie man einen Speech-API-Dienst in Azure erstellt
- wie du deinen Sprach-API-Dienst mit deiner App verbindest
- wie man den API-Schlüssel mit Hilfe von Github Secrets an seine App weitergibt
- wie man mit unserer App spricht 🗣️.

## Inhaltsverzeichnis

### Weitere Ressourcen:

- [Was ist eine Ressource / Ressourcengruppe / Abonnement?](https://docs.microsoft.com/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)
- [Speech API](https://azure.microsoft.com/services/cognitive-services/speech-services/#overview)
- [Regionen und Availability Zones in Azure](https://docs.microsoft.com/azure/availability-zones/az-overview)
- [Github Verschlüsselte Geheimnisse](https://docs.github.com/en/actions/reference/encrypted-secrets)

## Erste Schritte

- Navigier zu der **Ressourcengruppe**, die wir während der Challenge "Speech" erstellt haben
- Erstelle eine neue **Ressource** und such nach **Speech**
  ![](./images/light/createresource.png)

![](./images/light/selectspeech.png)

## Kognitiven Sprachdienst erstellen

- Erstelle die neue Ressource und setz die Werte wie im Screenshot
  ![](./images/light/createspeech.png)

![](./images/light/createspeechresource.png)

- Ähnlich wie bei der "Speech"-Challenge, kopier den Schlüssel, um ihn in **Github Secrets** zu speichern
  ![](./images/light/copykeys.png)

## Speech Service Credential in Github Secret einbinden

![](./images/light/vue-app-speech-api-key-secret.png#gh-light-mode-only)
![](./images/dark/vue-app-speech-api-key-secret.png#gh-dark-mode-only)

Jetzt werden wir dafür sorgen, dass unsere Milligram Social Media App versteht, wenn wir 🗣️ mit ihr sprechen.

## Frontend Pipeline erneut ausführen

- Navigiere nun zu **Aktionen** > **Seiten** und **Alle Jobs erneut ausführen**
  ![](./images/light/runworkflow.png#gh-light-mode-only)
  ![](./images/dark/runworkflow.png#gh-dark-mode-only)

![](./images/light/rerunalljobs.png#gh-light-mode-only)
![](./images/dark/rerunalljobs.png#gh-dark-mode-only)

Klick auf den Frontend-Link, der unter dem Deploy-Schritt in deiner Pipeline angezeigt wird `https://<IhrGithubHandle>.github.io/...`

Unsere Frontend-App sollte nun einen neuen Button mit einem Selfie-Symbol 🤩 haben, mit dem wir Selfies machen und schätzen können, wie alt wir sind.
Diese Selfies werden **nicht** gespeichert und **nicht** in der Timeline oder im News Feed angezeigt.

## Sprich mit mir! Was hast du zu sagen? Spielt herum!

Also leg los und sag mindestens 5 Sätze und erzähl uns, wie toll dich deine App versteht.

Nimm auch ein Buch und lese deiner App vor oder bitte andere Leute, mit deinem Telefon zu sprechen, du wirst überrascht sein. 😁

Standardmäßig wird nur Deutsch verstanden, wenn du die Sprache ändern möchtest, kannst du die `Microphone.vue` in Zeile 33 ändern und sie zum Beispiel auf Englisch setzen:
`speechConfig.speechRecognitionLanguage = "en-US";`

Das war's für unsere zwei Tage! Glückwunsch! 🥳🙏

## Zu viel? Wir haben die Lösung für dich!

Frag deinen Coach, wenn du nicht fertig geworden bist. Wir haben ein Back-up für dich. ⚠️

### Verwende den vorbereiteten Milligram Backend Service

Sieh dir die vorbereitete App mit unseren Bildern an, damit du herumspielen kannst [Milligram](https://codeunicornmartha.github.io/FemaleAIAppInnovationEcosystem/#/?stack-key=a78e2b9a).

### Was kommt als nächstes?

Starte deine eigene Coding Journey oder probier eine Azure-Zertifizierung aus, so wie wir es mit Udacity, Udemy, Pluralsight, Edx etc. gemacht haben, schau dir die unten stehenden Links an:

_Tipps 📝.

> - [Programmierkurse](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000)
> - Lernpfade

Informier dich auch über unsere Microsoft-Programme:

- MS Aspire Programm
- Praktika bei MS
- Berufliche Laufbahnen bei Microsoft

[◀ vorherige Challenge](../Face/DE_README.md) | [🔼 Home](../../README.md)
