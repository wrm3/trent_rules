[Passer au contenu principal](https://ai.google.dev/api?hl=fr#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=fr)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/api)
- [Deutsch](https://ai.google.dev/api?hl=de)
- [Español – América Latina](https://ai.google.dev/api?hl=es-419)
- [Français](https://ai.google.dev/api?hl=fr)
- [Indonesia](https://ai.google.dev/api?hl=id)
- [Italiano](https://ai.google.dev/api?hl=it)
- [Polski](https://ai.google.dev/api?hl=pl)
- [Português – Brasil](https://ai.google.dev/api?hl=pt-br)
- [Shqip](https://ai.google.dev/api?hl=sq)
- [Tiếng Việt](https://ai.google.dev/api?hl=vi)
- [Türkçe](https://ai.google.dev/api?hl=tr)
- [Русский](https://ai.google.dev/api?hl=ru)
- [עברית](https://ai.google.dev/api?hl=he)
- [العربيّة](https://ai.google.dev/api?hl=ar)
- [فارسی](https://ai.google.dev/api?hl=fa)
- [हिंदी](https://ai.google.dev/api?hl=hi)
- [বাংলা](https://ai.google.dev/api?hl=bn)
- [ภาษาไทย](https://ai.google.dev/api?hl=th)
- [中文 – 简体](https://ai.google.dev/api?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/api?hl=zh-tw)
- [日本語](https://ai.google.dev/api?hl=ja)
- [한국어](https://ai.google.dev/api?hl=ko)

[Obtenir une clé API](https://aistudio.google.com/apikey?hl=fr) [Liste de recettes](https://github.com/google-gemini/cookbook) [Communauté](https://discuss.ai.google.dev/c/gemini-api/?hl=fr)

[Connexion](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi%3Fhl%3Dfr&prompt=select_account)

- Sur cette page
- [Points de terminaison principaux](https://ai.google.dev/api?hl=fr#primary-endpoints)
- [Authentification](https://ai.google.dev/api?hl=fr#authentication)
- [Génération de contenu](https://ai.google.dev/api?hl=fr#content-generation)
  - [Structure du corps de la requête](https://ai.google.dev/api?hl=fr#request-body-structure)
  - [Structure du corps de la réponse](https://ai.google.dev/api?hl=fr#response-body-structure)
- [Exemples de requêtes](https://ai.google.dev/api?hl=fr#request-examples)
  - [Requête textuelle uniquement](https://ai.google.dev/api?hl=fr#text-only-prompt)
  - [Requête multimodale (texte et image)](https://ai.google.dev/api?hl=fr#multimodal-prompt)
  - [Conversations multitours (chat)](https://ai.google.dev/api?hl=fr#multi-turn-conversations)
  - [Points à retenir](https://ai.google.dev/api?hl=fr#key-takeaways)
- [Exemples de réponses](https://ai.google.dev/api?hl=fr#response-examples)
  - [Réponse textuelle uniquement](https://ai.google.dev/api?hl=fr#text-only-response)
- [API Live (BidiGenerateContent) WebSockets](https://ai.google.dev/api?hl=fr#live-api)
- [Modèles spécialisés](https://ai.google.dev/api?hl=fr#specialized-models)
- [API de plate-forme](https://ai.google.dev/api?hl=fr#platform-apis)
- [Étape suivante](https://ai.google.dev/api?hl=fr#whats-next)


La version Preview de Gemini 3.1 Flash-Lite est désormais disponible. [Essayez-le dans AI Studio.](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=fr)

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Documentation de référence de l'API](https://ai.google.dev/api?hl=fr)



 Envoyer des commentaires



# Gemini API reference

- Sur cette page
- [Points de terminaison principaux](https://ai.google.dev/api?hl=fr#primary-endpoints)
- [Authentification](https://ai.google.dev/api?hl=fr#authentication)
- [Génération de contenu](https://ai.google.dev/api?hl=fr#content-generation)
  - [Structure du corps de la requête](https://ai.google.dev/api?hl=fr#request-body-structure)
  - [Structure du corps de la réponse](https://ai.google.dev/api?hl=fr#response-body-structure)
- [Exemples de requêtes](https://ai.google.dev/api?hl=fr#request-examples)
  - [Requête textuelle uniquement](https://ai.google.dev/api?hl=fr#text-only-prompt)
  - [Requête multimodale (texte et image)](https://ai.google.dev/api?hl=fr#multimodal-prompt)
  - [Conversations multitours (chat)](https://ai.google.dev/api?hl=fr#multi-turn-conversations)
  - [Points à retenir](https://ai.google.dev/api?hl=fr#key-takeaways)
- [Exemples de réponses](https://ai.google.dev/api?hl=fr#response-examples)
  - [Réponse textuelle uniquement](https://ai.google.dev/api?hl=fr#text-only-response)
- [API Live (BidiGenerateContent) WebSockets](https://ai.google.dev/api?hl=fr#live-api)
- [Modèles spécialisés](https://ai.google.dev/api?hl=fr#specialized-models)
- [API de plate-forme](https://ai.google.dev/api?hl=fr#platform-apis)
- [Étape suivante](https://ai.google.dev/api?hl=fr#whats-next)

Cette référence d'API décrit les API standards, de streaming et en temps réel que vous pouvez utiliser pour interagir avec les modèles Gemini. Vous pouvez utiliser les API REST dans n'importe quel environnement compatible avec les requêtes HTTP. Consultez le [guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/quickstart?hl=fr) pour savoir comment effectuer votre premier appel d'API. Si vous recherchez les références de nos bibliothèques et SDK spécifiques à chaque langage, accédez au lien correspondant dans le panneau de navigation de gauche, sous **Références du SDK**.

## Points de terminaison principaux

L'API Gemini est organisée autour des principaux points de terminaison suivants :

- **Génération de contenu standard ( [`generateContent`](https://ai.google.dev/api/generate-content?hl=fr#method:-models.generatecontent))** : point de terminaison REST standard qui traite votre demande et renvoie la réponse complète du modèle dans un seul package. Cette option est idéale pour les tâches non interactives pour lesquelles vous pouvez attendre le résultat complet.
- **Génération de contenu en streaming ( [`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=fr#method:-models.streamgeneratecontent))** : utilise les événements envoyés par le serveur (SSE) pour vous envoyer des blocs de la réponse à mesure qu'ils sont générés. Cela permet d'offrir une expérience plus rapide et plus interactive pour les applications telles que les chatbots.
- **API Live ( [`BidiGenerateContent`](https://ai.google.dev/api/live?hl=fr#send-messages))** : API avec état basée sur WebSocket pour le streaming bidirectionnel, conçue pour les cas d'utilisation conversationnels en temps réel.
- **Mode par lot ( [`batchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=fr))** : point de terminaison REST standard pour envoyer des lots de requêtes `generateContent`.
- **Embeddings ( [`embedContent`](https://ai.google.dev/api/embeddings?hl=fr))** : point de terminaison REST standard qui génère un vecteur d'embedding de texte à partir de l'entrée `Content`.
- **API Gen Media** : points de terminaison pour générer des contenus multimédias avec nos modèles spécialisés tels qu' [Imagen pour la génération d'images](https://ai.google.dev/api/models?hl=fr#method:-models.predict) et [Veo pour la génération de vidéos](https://ai.google.dev/api/models?hl=fr#method:-models.predictlongrunning).
Ces fonctionnalités sont également intégrées à Gemini, et vous pouvez y accéder à l'aide de l'API `generateContent`.
- **API de plate-forme** : points de terminaison utilitaires qui prennent en charge les fonctionnalités de base telles que l' [importation de fichiers](https://ai.google.dev/api/files?hl=fr) et le [comptage de jetons](https://ai.google.dev/api/tokens?hl=fr).

## Authentification

Toutes les requêtes envoyées à l'API Gemini doivent inclure un en-tête `x-goog-api-key` avec votre clé API. Créez-en une en quelques clics dans [Google AI Studio](https://aistudio.google.com/app/apikey?hl=fr).

Voici un exemple de requête avec la clé API incluse dans l'en-tête :

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "parts": [\
          {\
            "text": "Explain how AI works in a few words"\
          }\
        ]\
      }\
    ]
  }'
```

Pour savoir comment transmettre votre clé à l'API à l'aide des SDK Gemini, consultez le guide [Utiliser les clés API Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=fr).

## Génération de contenu

Il s'agit du point de terminaison central pour envoyer des requêtes au modèle. Il existe deux points de terminaison pour générer du contenu. La principale différence réside dans la façon dont vous recevez la réponse :

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=fr#method:-models.generatecontent)**
**(REST)** :
reçoit une requête et fournit une seule réponse une fois que le modèle a terminé toute sa génération.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=fr#method:-models.streamgeneratecontent)**
**(SSE)** : reçoit exactement la même requête, mais le modèle renvoie des fragments de la réponse au fur et à mesure de leur génération. Cela améliore l'expérience utilisateur pour les applications interactives, car cela vous permet d'afficher immédiatement les résultats partiels.

### Structure du corps de la requête

Le [corps de la requête](https://ai.google.dev/api/generate-content?hl=fr#request-body) est un objet JSON **identique** pour les modes standard et streaming. Il est construit à partir de quelques objets principaux :

- Objet [`Content`](https://ai.google.dev/api/caching?hl=fr#Content) : représente un seul tour de conversation.
- Objet [`Part`](https://ai.google.dev/api/caching?hl=fr#Part) : élément de données dans un tour `Content` (comme du texte ou une image).
- `inline_data` ( [`Blob`](https://ai.google.dev/api/caching?hl=fr#Blob)) : conteneur pour les octets média bruts et leur type MIME.

Au plus haut niveau, le corps de la requête contient un objet `contents`, qui est une liste d'objets `Content`, chacun représentant un tour de conversation. Dans la plupart des cas, pour la génération de texte de base, vous disposerez d'un seul objet `Content`. Toutefois, si vous souhaitez conserver l'historique des conversations, vous pouvez utiliser plusieurs objets `Content`.

Voici un exemple de corps de requête `generateContent` :

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
          "role": "user",\
          "parts": [\
              // A list of Part objects goes here\
          ]\
      },\
      {\
          "role": "model",\
          "parts": [\
              // A list of Part objects goes here\
          ]\
      }\
    ]
  }'
```

### Structure du corps de la réponse

Le [corps de la réponse](https://ai.google.dev/api/generate-content?hl=fr#response-body) est semblable pour les modes streaming et standard, à l'exception des éléments suivants :

- Mode standard : le corps de la réponse contient une instance de [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=fr#v1beta.GenerateContentResponse).
- Mode flux : le corps de la réponse contient un flux d'instances [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=fr#v1beta.GenerateContentResponse).

De manière générale, le corps de la réponse contient un objet `candidates`, qui est une liste d'objets `Candidate`. L'objet `Candidate` contient un objet `Content` qui contient la réponse générée renvoyée par le modèle.

## Exemples de requêtes

Les exemples suivants montrent comment ces composants s'assemblent pour différents types de requêtes.

### Requête textuelle uniquement

Un simple prompt textuel se compose d'un tableau `contents` avec un seul objet `Content`. Le tableau `parts` de cet objet contient à son tour un seul objet `Part` avec un champ `text`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "parts": [\
          {\
            "text": "Explain how AI works in a single paragraph."\
          }\
        ]\
      }\
    ]
  }'
```

### Requête multimodale (texte et image)

Pour fournir à la fois du texte et une image dans une requête, le tableau `parts` doit contenir deux objets `Part` : un pour le texte et un pour l'image `inline_data`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{\
    "parts":[\
        {\
            "inline_data": {\
            "mime_type":"image/jpeg",\
            "data": "/9j/4AAQSkZJRgABAQ... (base64-encoded image)"\
            }\
        },\
        {"text": "What is in this picture?"},\
      ]\
    }]
  }'
```

### Conversations multitours (chat)

Pour créer une conversation avec plusieurs tours, vous devez définir le tableau `contents` avec plusieurs objets `Content`. L'API utilisera l'intégralité de cet historique comme contexte pour la prochaine réponse. La valeur `role` de chaque objet `Content` doit alterner entre `user` et `model`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "role": "user",\
        "parts": [\
          { "text": "Hello." }\
        ]\
      },\
      {\
        "role": "model",\
        "parts": [\
          { "text": "Hello! How can I help you today?" }\
        ]\
      },\
      {\
        "role": "user",\
        "parts": [\
          { "text": "Please write a four-line poem about the ocean." }\
        ]\
      }\
    ]
  }'
```

### Points à retenir

- `Content` est l'enveloppe : il s'agit du conteneur de premier niveau pour un tour de message, qu'il provienne de l'utilisateur ou du modèle.
- `Part` permet la multimodalité : utilisez plusieurs objets `Part` dans un même objet `Content` pour combiner différents types de données (texte, URI d'image, URI de vidéo, etc.).
- Choisissez votre méthode de données :
  - Pour les petits éléments multimédias intégrés directement (comme la plupart des images), utilisez un `Part` avec `inline_data`.
  - Pour les fichiers volumineux ou ceux que vous souhaitez réutiliser dans plusieurs requêtes, utilisez l'API File pour importer le fichier et le référencer avec une partie `file_data`.
- Gérer l'historique des conversations : pour les applications de chat utilisant l'API REST, créez le tableau `contents` en ajoutant des objets `Content` pour chaque tour, en alternant les rôles `"user"` et `"model"`. Si vous utilisez un SDK, consultez sa documentation pour connaître la méthode recommandée pour gérer l'historique des conversations.

## Exemples de réponses

Les exemples suivants montrent comment ces composants s'assemblent pour différents types de requêtes.

### Réponse textuelle uniquement

Une réponse textuelle par défaut se compose d'un tableau `candidates` avec un ou plusieurs objets `content` contenant la réponse du modèle.

Voici un exemple de réponse **standard** :

```
{
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "text": "At its core, Artificial Intelligence works by learning from vast amounts of data ..."\
          }\
        ],\
        "role": "model"\
      },\
      "finishReason": "STOP",\
      "index": 1\
    }\
  ],
}
```

Voici une série de réponses **en flux continu**. Chaque réponse contient un `responseId` qui relie l'ensemble de la réponse :

```
{
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "text": "The image displays"\
          }\
        ],\
        "role": "model"\
      },\
      "index": 0\
    }\
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  },
  "modelVersion": "gemini-2.5-flash-lite",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}

...

{
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "text": " the following materials:\n\n*   **Wood:** The accordion and the violin are primarily"\
          }\
        ],\
        "role": "model"\
      },\
      "index": 0\
    }\
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  }
  "modelVersion": "gemini-2.5-flash-lite",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}
```

## API Live (BidiGenerateContent) WebSockets

L'API Live propose une API avec état basée sur WebSocket pour le streaming bidirectionnel afin d'activer les cas d'utilisation du streaming en temps réel. Pour en savoir plus, consultez le [guide de l'API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr) et la [documentation de référence de l'API Live](https://ai.google.dev/api/live?hl=fr).

## Modèles spécialisés

En plus de la famille de modèles Gemini, l'API Gemini propose des points de terminaison pour des modèles spécialisés tels que les modèles [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=fr), [Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr) et [embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr). Vous trouverez ces guides dans la section "Modèles".

## API de plate-forme

Le reste des points de terminaison permet d'utiliser des fonctionnalités supplémentaires avec les points de terminaison principaux décrits jusqu'à présent. Pour en savoir plus, consultez les rubriques [Mode batch](https://ai.google.dev/gemini-api/docs/batch-mode?hl=fr) et [API File](https://ai.google.dev/gemini-api/docs/files?hl=fr) dans la section "Guides".

## Étape suivante

Si vous débutez, consultez les guides suivants, qui vous aideront à comprendre le modèle de programmation de l'API Gemini :

- [Guide de démarrage rapide de l'API Gemini](https://ai.google.dev/gemini-api/docs/quickstart?hl=fr)
- [Guide des modèles Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fr)

Vous pouvez également consulter les guides sur les fonctionnalités, qui présentent différentes fonctionnalités de l'API Gemini et fournissent des exemples de code :

- [Génération de texte](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr)
- [Mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr)



 Envoyer des commentaires



Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/02/25 (UTC).


Voulez-vous nous donner plus d'informations ?






\[\[\["Facile à comprendre","easyToUnderstand","thumb-up"\],\["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"\],\["Autre","otherUp","thumb-up"\]\],\[\["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"\],\["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"\],\["Obsolète","outOfDate","thumb-down"\],\["Problème de traduction","translationIssue","thumb-down"\],\["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"\],\["Autre","otherDown","thumb-down"\]\],\["Dernière mise à jour le 2026/02/25 (UTC)."\],\[\],\[\]\]