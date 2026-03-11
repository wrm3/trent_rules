[Passer au contenu principal](https://ai.google.dev/gemini-api/docs?hl=fr#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=fr)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs)
- [Deutsch](https://ai.google.dev/gemini-api/docs?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs?hl=ko)

[Obtenir une clé API](https://aistudio.google.com/apikey?hl=fr) [Liste de recettes](https://github.com/google-gemini/cookbook) [Communauté](https://discuss.ai.google.dev/c/gemini-api/?hl=fr)

[Connexion](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dfr&prompt=select_account)


La version Preview de Gemini 3.1 Flash-Lite est désormais disponible. [Essayez-le dans AI Studio.](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=fr)

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

# API Gemini

Le chemin le plus rapide du prompt à la production avec Gemini, Veo, Nano Banana et plus encore.

[Python](https://ai.google.dev/gemini-api/docs?hl=fr#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=fr#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=fr#go)[Java](https://ai.google.dev/gemini-api/docs?hl=fr#java)[C#](https://ai.google.dev/gemini-api/docs?hl=fr#c)[REST](https://ai.google.dev/gemini-api/docs?hl=fr#rest)Plus

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

[À vos briques](https://ai.google.dev/gemini-api/docs/quickstart?hl=fr)

Suivez notre guide de démarrage rapide pour obtenir une clé API et effectuer votre premier appel d'API en quelques minutes.

* * *

## Découvrir les modèles

[Tout afficher](https://ai.google.dev/gemini-api/docs/models?hl=fr)

[auto\_awesome\\
Gemini 3.1 Pro\\
Nouveau\\
\\
Notre modèle le plus intelligent, le meilleur au monde pour la compréhension multimodale, basé sur un raisonnement de pointe.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) [spark\\
Gemini 3 Flash\\
Nouveau\\
\\
Des performances de pointe rivalisant avec celles de modèles plus volumineux, à un coût bien inférieur.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr) [spark\\
Gemini 3.1 Flash-Lite\\
Nouveau\\
\\
Modèle de travail à volume élevé et sensible aux coûts, avec les performances et la qualité de la gamme Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=fr) [🍌\\
Nano Banana 2 et Nano Banana Pro\\
\\
\\
Modèles de pointe pour la génération et la retouche d'images.](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) [video\_library\\
Veo 3.1\\
\\
\\
Notre modèle de génération de vidéos de pointe, avec audio natif.](https://ai.google.dev/gemini-api/docs/video?hl=fr) [spark\\
Gemini Robotics\\
\\
\\
Un modèle de vision-langage (VLM) qui apporte les capacités agentiques de Gemini à la robotique et permet un raisonnement avancé dans le monde physique.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fr)

## Explorer les fonctionnalités

[imagesmode\\
\\
Génération d'images native (Nano Banana)\\
\\
\\
Générez et retouchez des images très contextuelles de manière native avec Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) [article\\
\\
Contexte long\\
\\
\\
Saisissez des millions de jetons dans les modèles Gemini et obtenez des informations à partir d'images, de vidéos et de documents non structurés.](https://ai.google.dev/gemini-api/docs/long-context?hl=fr) [code\\
\\
Sorties structurées\\
\\
\\
Contrains Gemini à répondre au format JSON, un format de données structurées adapté au traitement automatisé.](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr) [functions\\
\\
Appel de fonction\\
\\
\\
Créez des workflows agentifs en connectant Gemini à des API et outils externes.](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) [videocam\\
\\
Génération de vidéos avec Veo 3.1\\
\\
\\
Créez des contenus vidéo de haute qualité à partir de requêtes textuelles ou d'images grâce à notre modèle de pointe.](https://ai.google.dev/gemini-api/docs/video?hl=fr) [android\_recorder\\
\\
Agents vocaux avec l'API Live\\
\\
\\
Créez des applications et des agents vocaux en temps réel avec l'API Live.](https://ai.google.dev/gemini-api/docs/live?hl=fr) [build\\
\\
Outils\\
\\
\\
Connectez Gemini au monde grâce à des outils intégrés tels que la recherche Google, le contexte d'URL, Google Maps, l'exécution de code et l'utilisation de l'ordinateur.](https://ai.google.dev/gemini-api/docs/tools?hl=fr) [stacks\\
\\
Compréhension des documents\\
\\
\\
Traitez jusqu'à 1 000 pages de fichiers PDF avec une compréhension multimodale complète ou d'autres types de fichiers textuels.](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr) [cognition\_2\\
\\
Raisonnement\\
\\
\\
Découvrez comment les capacités de réflexion améliorent le raisonnement pour les tâches et les agents complexes.](https://ai.google.dev/gemini-api/docs/thinking?hl=fr)

[Google AI Studio\\
\\
\\
Testez des requêtes, gérez vos clés API, surveillez l'utilisation et créez des prototypes.](https://aistudio.google.com/?hl=fr) [group\\
\\
Communauté de développeurs\\
\\
\\
Posez des questions et trouvez des solutions auprès d'autres développeurs et ingénieurs Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=fr) [menu\_book\\
\\
Documentation de référence de l'API\\
\\
\\
Pour en savoir plus sur l'API Gemini, consultez la documentation de référence officielle.](https://ai.google.dev/api?hl=fr) [sensors\\
\\
État\\
\\
\\
Vérifiez l'état de l'API Gemini, de Google AI Studio et de nos services de modèles.](https://aistudio.google.com/status?hl=fr)

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/03/03 (UTC).




\[\[\["Facile à comprendre","easyToUnderstand","thumb-up"\],\["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"\],\["Autre","otherUp","thumb-up"\]\],\[\["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"\],\["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"\],\["Obsolète","outOfDate","thumb-down"\],\["Problème de traduction","translationIssue","thumb-down"\],\["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"\],\["Autre","otherDown","thumb-down"\]\],\["Dernière mise à jour le 2026/03/03 (UTC)."\],\[\],\[\]\]