[Passa ai contenuti principali](https://ai.google.dev/gemini-api/docs?hl=it#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=it)](https://ai.google.dev/)

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

[Recupera chiave API](https://aistudio.google.com/apikey?hl=it) [Libro di ricette](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=it)

[Accedi](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dit&prompt=select_account)


L'anteprima di Gemini 3.1 Flash-Lite è ora disponibile. [Provalo in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=it).




- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

# API Gemini

Il percorso più veloce dal prompt alla produzione con Gemini, Veo, Nano Banana e altro ancora.

[Python](https://ai.google.dev/gemini-api/docs?hl=it#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=it#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=it#go)[Java](https://ai.google.dev/gemini-api/docs?hl=it#java)[C#](https://ai.google.dev/gemini-api/docs?hl=it#c)[REST](https://ai.google.dev/gemini-api/docs?hl=it#rest)Altro

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

[Inizia a creare](https://ai.google.dev/gemini-api/docs/quickstart?hl=it)

Segui la nostra guida rapida per ottenere una chiave API ed effettuare la tua prima chiamata API in pochi minuti.

* * *

## Scopri i modelli

[Visualizza tutto](https://ai.google.dev/gemini-api/docs/models?hl=it)

[auto\_awesome\\
Gemini 3.1 Pro\\
Novità\\
\\
Il nostro modello più intelligente, il migliore al mondo per la comprensione multimodale, il tutto basato su un ragionamento all'avanguardia.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) [spark\\
Gemini 3 Flash\\
Novità\\
\\
Prestazioni di classe Frontier paragonabili a quelle di modelli più grandi a una frazione del costo.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) [spark\\
Gemini 3.1 Flash-Lite\\
Novità\\
\\
Modello di base ad alto volume e sensibile ai costi con le prestazioni e la qualità della serie Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=it) [🍌\\
Nano Banana 2 e Nano Banana Pro\\
\\
\\
Modelli all'avanguardia per la generazione e la modifica di immagini.](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) [video\_library\\
Veo 3.1\\
\\
\\
Il nostro modello di generazione video all'avanguardia, con audio nativo.](https://ai.google.dev/gemini-api/docs/video?hl=it) [spark\\
Gemini Robotics\\
\\
\\
Un modello di visione-linguaggio (VLM) che porta le funzionalità agentiche di Gemini nella robotica e consente un ragionamento avanzato nel mondo fisico.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=it)

## Esplora le funzionalità

[imagesmode\\
\\
Generazione di immagini nativa (Nano Banana)\\
\\
\\
Genera e modifica immagini altamente contestuali in modo nativo con Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) [article\\
\\
Contesto lungo\\
\\
\\
Inserisci milioni di token nei modelli Gemini ed estrai informazioni da immagini, video e documenti non strutturati.](https://ai.google.dev/gemini-api/docs/long-context?hl=it) [code\\
\\
Output strutturati\\
\\
\\
Limita Gemini a rispondere con JSON, un formato di dati strutturati adatto all'elaborazione automatica.](https://ai.google.dev/gemini-api/docs/structured-output?hl=it) [functions\\
\\
Chiamata di funzione\\
\\
\\
Crea flussi di lavoro agentici collegando Gemini ad API e strumenti esterni.](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) [videocam\\
\\
Generazione di video con Veo 3.1\\
\\
\\
Crea contenuti video di alta qualità da prompt di testo o immagini con il nostro modello all'avanguardia.](https://ai.google.dev/gemini-api/docs/video?hl=it) [android\_recorder\\
\\
Voice Agents con l'API Live\\
\\
\\
Crea applicazioni e agenti vocali in tempo reale con l'API Live.](https://ai.google.dev/gemini-api/docs/live?hl=it) [build\\
\\
Strumenti\\
\\
\\
Connetti Gemini al mondo tramite strumenti integrati come la Ricerca Google, il contesto URL, Google Maps, l'esecuzione di codice e l'utilizzo del computer.](https://ai.google.dev/gemini-api/docs/tools?hl=it) [stacks\\
\\
Comprensione dei documenti\\
\\
\\
Elabora fino a 1000 pagine di file PDF con comprensione multimodale completa o altri tipi di file basati su testo.](https://ai.google.dev/gemini-api/docs/document-processing?hl=it) [cognition\_2\\
\\
Ragionamento\\
\\
\\
Scopri come le capacità di pensiero migliorano il ragionamento per attività e agenti complessi.](https://ai.google.dev/gemini-api/docs/thinking?hl=it)

[Google AI Studio\\
\\
\\
Testa i prompt, gestisci le chiavi API, monitora l'utilizzo e crea prototipi.](https://aistudio.google.com/?hl=it) [group\\
\\
Community di sviluppatori\\
\\
\\
Poni domande e trova soluzioni da altri sviluppatori e ingegneri di Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=it) [menu\_book\\
\\
Riferimento API\\
\\
\\
Trova informazioni dettagliate sull'API Gemini nella documentazione di riferimento ufficiale.](https://ai.google.dev/api?hl=it) [sensors\\
\\
Stato\\
\\
\\
Controlla lo stato dell'API Gemini, di Google AI Studio e dei nostri servizi di modelli.](https://aistudio.google.com/status?hl=it)

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-03-03 UTC.




\[\[\["Facile da capire","easyToUnderstand","thumb-up"\],\["Il problema è stato risolto","solvedMyProblem","thumb-up"\],\["Altra","otherUp","thumb-up"\]\],\[\["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"\],\["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"\],\["Obsoleti","outOfDate","thumb-down"\],\["Problema di traduzione","translationIssue","thumb-down"\],\["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"\],\["Altra","otherDown","thumb-down"\]\],\["Ultimo aggiornamento 2026-03-03 UTC."\],\[\],\[\]\]