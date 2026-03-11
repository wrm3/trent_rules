[Zum Hauptinhalt springen](https://ai.google.dev/gemini-api/docs?hl=de#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=de)](https://ai.google.dev/)

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

[API-Schlüssel abrufen](https://aistudio.google.com/apikey?hl=de) [Kochbuch](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=de)

[Anmelden](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dde&prompt=select_account)


Gemini 3.1 Flash-Lite ist jetzt als Vorabversion verfügbar. [In AI Studio ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=de)

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

# Gemini API

Der schnellste Weg vom Prompt zur Produktion mit Gemini, Veo, Nano Banana und mehr.

[Python](https://ai.google.dev/gemini-api/docs?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs?hl=de#ok)[Java](https://ai.google.dev/gemini-api/docs?hl=de#java)[C#](https://ai.google.dev/gemini-api/docs?hl=de#c)[REST](https://ai.google.dev/gemini-api/docs?hl=de#rest)Mehr

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

[Losstaunen](https://ai.google.dev/gemini-api/docs/quickstart?hl=de)

Folgen Sie unserer Kurzanleitung, um in wenigen Minuten einen API-Schlüssel zu erhalten und Ihren ersten API-Aufruf zu starten.

* * *

## Modelle kennenlernen

[Alle ansehen](https://ai.google.dev/gemini-api/docs/models?hl=de)

[auto\_awesome\\
Gemini 3.1 Pro\\
Neu\\
\\
Unser bisher leistungsstärkstes Modell, das weltweit führend im multimodalen Verstehen ist und auf modernster Technologie für logische Schlussfolgerungen basiert.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) [spark\\
Gemini 3 Flash\\
Neu\\
\\
Leistung auf Frontier-Niveau, die mit größeren Modellen mithalten kann, aber nur einen Bruchteil der Kosten verursacht.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) [spark\\
Gemini 3.1 Flash-Lite\\
Neu\\
\\
Kostengünstiges Modell für hohe Volumina mit der Leistung und Qualität der Gemini 3-Serie.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=de) [🍌\\
Nano Banana 2 und Nano Banana Pro\\
\\
\\
Hochmoderne Modelle für die Bildgenerierung und ‑bearbeitung.](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) [video\_library\\
Veo 3.1\\
\\
\\
Unser leistungsstarkes Modell zur Videogenerierung mit nativer Audiofunktion.](https://ai.google.dev/gemini-api/docs/video?hl=de) [spark\\
Gemini Robotics\\
\\
\\
Ein Vision-Language-Modell (VLM), das die Agentenfunktionen von Gemini in die Robotik einbringt und fortschrittliche Schlussfolgerungen in der physischen Welt ermöglicht.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de)

## Funktionen entdecken

[imagesmode\\
\\
Native Bildgenerierung (Nano Banana)\\
\\
\\
Mit Gemini 2.5 Flash Image können Sie kontextbezogene Bilder erstellen und bearbeiten.](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) [article\\
\\
Langer Kontext\\
\\
\\
Sie können Millionen von Tokens in Gemini-Modelle eingeben und Informationen aus unstrukturierten Bildern, Videos und Dokumenten ableiten.](https://ai.google.dev/gemini-api/docs/long-context?hl=de) [code\\
\\
Strukturierte Ausgaben\\
\\
\\
Weisen Sie Gemini an, mit JSON zu antworten. JSON ist ein strukturiertes Datenformat, das sich für die automatisierte Verarbeitung eignet.](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) [functions\\
\\
Funktionsaufrufe\\
\\
\\
Agentgestützte Workflows erstellen, indem Sie Gemini mit externen APIs und Tools verbinden.](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) [videocam\\
\\
Videogenerierung mit Veo 3.1\\
\\
\\
Mit unserem innovativen Modell können Sie hochwertige Videoinhalte aus Text- oder Bild-Prompts erstellen.](https://ai.google.dev/gemini-api/docs/video?hl=de) [android\_recorder\\
\\
Voice Agents mit Live API\\
\\
\\
Mit der Live API können Sie Echtzeit-Sprachanwendungen und ‑Agenten entwickeln.](https://ai.google.dev/gemini-api/docs/live?hl=de) [build\\
\\
Tools\\
\\
\\
Gemini kann über integrierte Tools wie die Google Suche, URL-Kontext, Google Maps, Codeausführung und Computernutzung mit der Welt verbunden werden.](https://ai.google.dev/gemini-api/docs/tools?hl=de) [stacks\\
\\
Verständnis von Dokumenten\\
\\
\\
Bis zu 1.000 Seiten von PDF-Dateien mit vollständigem multimodalen Verständnis oder anderen textbasierten Dateitypen verarbeiten](https://ai.google.dev/gemini-api/docs/document-processing?hl=de) [cognition\_2\\
\\
Thinking\\
\\
\\
Hier erfahren Sie, wie die Denkfunktionen das logische Denken bei komplexen Aufgaben und Agenten verbessern.](https://ai.google.dev/gemini-api/docs/thinking?hl=de)

[Google AI Studio\\
\\
\\
Sie können Prompts testen, Ihre API-Schlüssel verwalten, die Nutzung überwachen und Prototypen erstellen.](https://aistudio.google.com/?hl=de) [group\\
\\
Entwickler-Community\\
\\
\\
Sie können Fragen stellen und Lösungen von anderen Entwicklern und Google-Entwicklern finden.](https://discuss.ai.google.dev/c/gemini-api/4?hl=de) [menu\_book\\
\\
API-Referenz\\
\\
\\
Detaillierte Informationen zur Gemini API finden Sie in der offiziellen Referenzdokumentation.](https://ai.google.dev/api?hl=de) [sensors\\
\\
Status\\
\\
\\
Hier können Sie den Status der Gemini API, von Google AI Studio und unserer Modelldienste prüfen.](https://aistudio.google.com/status?hl=de)

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-03-03 (UTC).




\[\[\["Leicht verständlich","easyToUnderstand","thumb-up"\],\["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"\],\["Sonstiges","otherUp","thumb-up"\]\],\[\["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"\],\["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"\],\["Nicht mehr aktuell","outOfDate","thumb-down"\],\["Problem mit der Übersetzung","translationIssue","thumb-down"\],\["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"\],\["Sonstiges","otherDown","thumb-down"\]\],\["Zuletzt aktualisiert: 2026-03-03 (UTC)."\],\[\],\[\]\]