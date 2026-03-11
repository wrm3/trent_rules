[Zum Hauptinhalt springen](https://ai.google.dev/api?hl=de#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=de)](https://ai.google.dev/)

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

[API-Schlüssel abrufen](https://aistudio.google.com/apikey?hl=de) [Kochbuch](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=de)

[Anmelden](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi%3Fhl%3Dde&prompt=select_account)

- Auf dieser Seite
- [Primäre Endpunkte](https://ai.google.dev/api?hl=de#primary-endpoints)
- [Authentifizierung](https://ai.google.dev/api?hl=de#authentication)
- [Inhaltserstellung](https://ai.google.dev/api?hl=de#content-generation)
  - [Struktur des Anfragetexts](https://ai.google.dev/api?hl=de#request-body-structure)
  - [Struktur des Antworttexts](https://ai.google.dev/api?hl=de#response-body-structure)
- [Beispielanfragen](https://ai.google.dev/api?hl=de#request-examples)
  - [Nur-Text-Prompt](https://ai.google.dev/api?hl=de#text-only-prompt)
  - [Multimodaler Prompt (Text und Bild)](https://ai.google.dev/api?hl=de#multimodal-prompt)
  - [Unterhaltungen über mehrere Themen (Chat)](https://ai.google.dev/api?hl=de#multi-turn-conversations)
  - [Bedeutende Vorteile](https://ai.google.dev/api?hl=de#key-takeaways)
- [Beispielantworten](https://ai.google.dev/api?hl=de#response-examples)
  - [Reine Textantwort](https://ai.google.dev/api?hl=de#text-only-response)
- [Live API (BidiGenerateContent) WebSockets API](https://ai.google.dev/api?hl=de#live-api)
- [Spezialisierte Modelle](https://ai.google.dev/api?hl=de#specialized-models)
- [Plattform-APIs](https://ai.google.dev/api?hl=de#platform-apis)
- [Nächste Schritte](https://ai.google.dev/api?hl=de#whats-next)


Gemini 3.1 Flash-Lite ist jetzt als Vorabversion verfügbar. [In AI Studio ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=de)

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [API-Referenz](https://ai.google.dev/api?hl=de)

War das hilfreich?



 Feedback geben



# Gemini API reference

- Auf dieser Seite
- [Primäre Endpunkte](https://ai.google.dev/api?hl=de#primary-endpoints)
- [Authentifizierung](https://ai.google.dev/api?hl=de#authentication)
- [Inhaltserstellung](https://ai.google.dev/api?hl=de#content-generation)
  - [Struktur des Anfragetexts](https://ai.google.dev/api?hl=de#request-body-structure)
  - [Struktur des Antworttexts](https://ai.google.dev/api?hl=de#response-body-structure)
- [Beispielanfragen](https://ai.google.dev/api?hl=de#request-examples)
  - [Nur-Text-Prompt](https://ai.google.dev/api?hl=de#text-only-prompt)
  - [Multimodaler Prompt (Text und Bild)](https://ai.google.dev/api?hl=de#multimodal-prompt)
  - [Unterhaltungen über mehrere Themen (Chat)](https://ai.google.dev/api?hl=de#multi-turn-conversations)
  - [Bedeutende Vorteile](https://ai.google.dev/api?hl=de#key-takeaways)
- [Beispielantworten](https://ai.google.dev/api?hl=de#response-examples)
  - [Reine Textantwort](https://ai.google.dev/api?hl=de#text-only-response)
- [Live API (BidiGenerateContent) WebSockets API](https://ai.google.dev/api?hl=de#live-api)
- [Spezialisierte Modelle](https://ai.google.dev/api?hl=de#specialized-models)
- [Plattform-APIs](https://ai.google.dev/api?hl=de#platform-apis)
- [Nächste Schritte](https://ai.google.dev/api?hl=de#whats-next)

In dieser API-Referenz werden die Standard-, Streaming- und Echtzeit-APIs beschrieben, die Sie für die Interaktion mit den Gemini-Modellen verwenden können. Sie können die REST APIs in jeder Umgebung verwenden, die HTTP-Anfragen unterstützt. In der [Kurzanleitung](https://ai.google.dev/gemini-api/docs/quickstart?hl=de) erfahren Sie, wie Sie Ihren ersten API-Aufruf starten. Wenn Sie nach den Referenzen für unsere sprachspezifischen Bibliotheken und SDKs suchen, klicken Sie in der linken Navigationsleiste unter **SDK-Referenzen** auf den Link für die entsprechende Sprache.

## Primäre Endpunkte

Die Gemini API ist in die folgenden Hauptendpunkte unterteilt:

- **Standardmäßige Inhaltserstellung ( [`generateContent`](https://ai.google.dev/api/generate-content?hl=de#method:-models.generatecontent))**:
Ein Standard-REST-Endpunkt, der Ihre Anfrage verarbeitet und die vollständige Antwort des Modells in einem einzigen Paket zurückgibt. Das ist am besten für nicht interaktive Aufgaben geeignet, bei denen Sie auf das gesamte Ergebnis warten können.
- **Streaming-Inhaltsgenerierung ( [`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=de#method:-models.streamgeneratecontent))**: Hier werden vom Server gesendete Ereignisse (SSE) verwendet, um Teile der Antwort an Sie zu senden, sobald sie generiert werden. Das sorgt für eine schnellere und interaktivere Nutzung von Anwendungen wie Chatbots.
- **Live API ( [`BidiGenerateContent`](https://ai.google.dev/api/live?hl=de#send-messages))**: Eine zustandsbehaftete WebSocket-basierte API für bidirektionales Streaming, die für Echtzeit-Konversationsanwendungsfälle entwickelt wurde.
- **Batchmodus ( [`batchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=de))**: Ein Standard-REST-Endpunkt zum Senden von Batches mit `generateContent`-Anfragen.
- **Einbettungen ( [`embedContent`](https://ai.google.dev/api/embeddings?hl=de))**: Ein Standard-REST-Endpunkt, der einen Texteinbettungsvektor aus der Eingabe `Content` generiert.
- **Gen Media APIs**:Endpunkte zum Generieren von Medien mit unseren spezialisierten Modellen wie [Imagen für die Bildgenerierung](https://ai.google.dev/api/models?hl=de#method:-models.predict) und [Veo für die Videogenerierung](https://ai.google.dev/api/models?hl=de#method:-models.predictlongrunning).
Gemini bietet diese Funktionen auch integriert an. Sie können über die `generateContent` API darauf zugreifen.
- **Plattform-APIs**:Utility-Endpunkte, die Kernfunktionen wie das [Hochladen von Dateien](https://ai.google.dev/api/files?hl=de) und das [Zählen von Tokens](https://ai.google.dev/api/tokens?hl=de) unterstützen.

## Authentifizierung

Alle Anfragen an die Gemini API müssen einen `x-goog-api-key`-Header mit Ihrem API-Schlüssel enthalten. Sie können mit wenigen Klicks einen in [Google AI Studio](https://aistudio.google.com/app/apikey?hl=de) erstellen.

Hier sehen Sie ein Beispiel für eine Anfrage mit dem API-Schlüssel im Header:

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

Eine Anleitung dazu, wie Sie Ihren Schlüssel mit den Gemini SDKs an die API übergeben, finden Sie im Leitfaden [Gemini API-Schlüssel verwenden](https://ai.google.dev/gemini-api/docs/api-key?hl=de).

## Inhaltserstellung

Dies ist der zentrale Endpunkt zum Senden von Prompts an das Modell. Es gibt zwei Endpunkte zum Generieren von Inhalten. Der Hauptunterschied besteht darin, wie Sie die Antwort erhalten:

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=de#method:-models.generatecontent) (REST)**:
Empfängt eine Anfrage und gibt eine einzelne Antwort zurück, nachdem das Modell die gesamte Generierung abgeschlossen hat.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=de#method:-models.streamgeneratecontent) (SSE)**: Empfängt genau dieselbe Anfrage, aber das Modell streamt Teile der Antwort zurück, sobald sie generiert werden. Das sorgt für eine bessere Nutzererfahrung bei interaktiven Anwendungen, da Sie Teilergebnisse sofort anzeigen können.

### Struktur des Anfragetexts

Der [Anfragetext](https://ai.google.dev/api/generate-content?hl=de#request-body) ist ein JSON-Objekt, das für den Standard- und den Streamingmodus **identisch** ist und aus einigen Kernobjekten besteht:

- [`Content`](https://ai.google.dev/api/caching?hl=de#Content)-Objekt: Stellt einen einzelnen Zug in einer Unterhaltung dar.
- [`Part`](https://ai.google.dev/api/caching?hl=de#Part)-Objekt: Ein Datenelement in einem `Content`-Turn (z. B. Text oder ein Bild).
- `inline_data` ( [`Blob`](https://ai.google.dev/api/caching?hl=de#Blob)): Ein Container für Rohmediabytes und deren MIME-Typ.

Auf der obersten Ebene enthält der Anfragetext ein `contents`-Objekt, das eine Liste von `Content`-Objekten ist, die jeweils Züge in der Unterhaltung darstellen. In den meisten Fällen haben Sie für die einfache Texterstellung ein einzelnes `Content`-Objekt. Wenn Sie jedoch den Unterhaltungsverlauf beibehalten möchten, können Sie mehrere `Content`-Objekte verwenden.

Das Folgende zeigt einen typischen `generateContent`-Anfragetext:

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

### Struktur des Antworttexts

Der [Antworttext](https://ai.google.dev/api/generate-content?hl=de#response-body) ist für den Streaming- und den Standardmodus ähnlich, mit Ausnahme der folgenden Punkte:

- Standardmodus: Der Antworttext enthält eine Instanz von [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=de#v1beta.GenerateContentResponse).
- Streaming-Modus: Der Antworttext enthält einen Stream von [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=de#v1beta.GenerateContentResponse)-Instanzen.

Auf übergeordneter Ebene enthält der Antworttext ein `candidates`-Objekt, das eine Liste von `Candidate`-Objekten ist. Das `Candidate`-Objekt enthält ein `Content`-Objekt mit der generierten Antwort des Modells.

## Beispielanfragen

Die folgenden Beispiele zeigen, wie diese Komponenten bei verschiedenen Arten von Anfragen zusammenwirken.

### Nur-Text-Prompt

Ein einfacher Text-Prompt besteht aus einem `contents`-Array mit einem einzelnen `Content`-Objekt. Das `parts`-Array dieses Objekts enthält wiederum ein einzelnes `Part`-Objekt mit einem `text`-Feld.

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

### Multimodaler Prompt (Text und Bild)

Wenn Sie sowohl Text als auch ein Bild in einem Prompt angeben möchten, sollte das `parts`-Array zwei `Part`-Objekte enthalten: eines für den Text und eines für das Bild `inline_data`.

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

### Unterhaltungen über mehrere Themen (Chat)

Wenn Sie einen Dialog mit mehreren Zügen erstellen möchten, definieren Sie das `contents`-Array mit mehreren `Content`-Objekten. Die API verwendet den gesamten Verlauf als Kontext für die nächste Antwort. Der `role` für jedes `Content`-Objekt sollte zwischen `user` und `model` wechseln.

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

### Bedeutende Vorteile

- `Content` ist der Umschlag: Er ist der Container der obersten Ebene für einen Nachrichtenabschnitt, unabhängig davon, ob er vom Nutzer oder vom Modell stammt.
- `Part` ermöglicht Multimodalität: Verwenden Sie mehrere `Part`-Objekte in einem einzelnen `Content`-Objekt, um verschiedene Datentypen (Text, Bild, Video-URI usw.) zu kombinieren.
- Wählen Sie eine Datenmethode aus:
  - Verwenden Sie für kleine, direkt eingebettete Medien (wie die meisten Bilder) ein `Part` mit `inline_data`.
  - Für größere Dateien oder Dateien, die Sie in mehreren Anfragen verwenden möchten, können Sie die File API verwenden, um die Datei hochzuladen und mit einem `file_data`-Teil darauf zu verweisen.
- Verlauf von Unterhaltungen verwalten: Erstellen Sie für Chatanwendungen, die die REST API verwenden, das `contents`-Array, indem Sie für jede Runde `Content`-Objekte anhängen und dabei zwischen den Rollen `"user"` und `"model"` wechseln. Wenn Sie ein SDK verwenden, finden Sie in der SDK-Dokumentation Informationen dazu, wie Sie den Unterhaltungsverlauf am besten verwalten.

## Beispielantworten

Die folgenden Beispiele zeigen, wie diese Komponenten bei verschiedenen Arten von Anfragen zusammenwirken.

### Reine Textantwort

Eine Standardtextantwort besteht aus einem `candidates`-Array mit einem oder mehreren `content`-Objekten, die die Antwort des Modells enthalten.

Hier ist ein Beispiel für eine **Standardantwort**:

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

Im Folgenden finden Sie eine Reihe von **Streaming**-Antworten. Jede Antwort enthält ein `responseId`, das die vollständige Antwort zusammenfasst:

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

## Live API (BidiGenerateContent) WebSockets API

Die Live API bietet eine zustandsbehaftete WebSocket-basierte API für bidirektionales Streaming, um Echtzeit-Streaming-Anwendungsfälle zu ermöglichen. Weitere Informationen finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live?hl=de) und in der [Live API-Referenz](https://ai.google.dev/api/live?hl=de).

## Spezialisierte Modelle

Zusätzlich zu den Modellen der Gemini-Familie bietet die Gemini API Endpunkte für spezialisierte Modelle wie [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=de), [Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=de) und [Embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=de). Sie finden diese Anleitungen im Abschnitt „Modelle“.

## Plattform-APIs

Die restlichen Endpunkte ermöglichen zusätzliche Funktionen, die mit den bisher beschriebenen Hauptendpunkten verwendet werden können. Weitere Informationen finden Sie in den Themen [Batch-Modus](https://ai.google.dev/gemini-api/docs/batch-mode?hl=de) und [File API](https://ai.google.dev/gemini-api/docs/files?hl=de) im Abschnitt „Leitfäden“.

## Nächste Schritte

Wenn Sie gerade erst anfangen, sollten Sie sich die folgenden Leitfäden ansehen, die Ihnen helfen, das Programmiermodell der Gemini API zu verstehen:

- [Kurzanleitung: Gemini API](https://ai.google.dev/gemini-api/docs/quickstart?hl=de)
- [Leitfaden zu Gemini-Modellen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de)

Möglicherweise sind auch die Leitfäden zu den Funktionen interessant, in denen verschiedene Gemini API-Funktionen vorgestellt und Codebeispiele bereitgestellt werden:

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de)
- [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de)
- [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de)

War das hilfreich?



 Feedback geben



Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-02-25 (UTC).


Haben Sie Feedback für uns?






\[\[\["Leicht verständlich","easyToUnderstand","thumb-up"\],\["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"\],\["Sonstiges","otherUp","thumb-up"\]\],\[\["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"\],\["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"\],\["Nicht mehr aktuell","outOfDate","thumb-down"\],\["Problem mit der Übersetzung","translationIssue","thumb-down"\],\["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"\],\["Sonstiges","otherDown","thumb-down"\]\],\["Zuletzt aktualisiert: 2026-02-25 (UTC)."\],\[\],\[\]\]