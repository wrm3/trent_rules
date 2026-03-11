[Kapërce te përmbajtja kryesore](https://ai.google.dev/gemini-api/docs?hl=sq#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=sq)](https://ai.google.dev/)

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

[Merr çelësin API](https://aistudio.google.com/apikey?hl=sq) [Libër gatimi](https://github.com/google-gemini/cookbook) [Komuniteti](https://discuss.ai.google.dev/c/gemini-api/?hl=sq)

[Identifikohu](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dsq&prompt=select_account)

Pamja paraprake e Gemini 3.1 Flash-Lite është tani e disponueshme. [Provojeni në AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=sq) .


![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Kjo faqe është përkthyer nga [Cloud Translation API](https://cloud.google.com/translate/?hl=sq).


Switch to English


- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet, Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

# API-ja e Gemini-t

Rruga më e shpejtë nga prompt në prodhim me Gemini, Veo, Nano Banana dhe të tjera.

[Python](https://ai.google.dev/gemini-api/docs?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs?hl=sq#shko)[Java](https://ai.google.dev/gemini-api/docs?hl=sq#java)[C#](https://ai.google.dev/gemini-api/docs?hl=sq#c)[PUSHTIM](https://ai.google.dev/gemini-api/docs?hl=sq#pushtim)Më shumë

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

[Filloni ndërtimin](https://ai.google.dev/gemini-api/docs/quickstart?hl=sq)

Ndiqni udhëzuesin tonë të Fillimit të Shpejtë për të marrë një çelës API dhe për të bërë thirrjen tuaj të parë API brenda pak minutash.

* * *

## Takoni modelet

[Shiko të gjitha](https://ai.google.dev/gemini-api/docs/models?hl=sq)

auto\_awesome Gemini 3.1 Pro E re

Modeli ynë më inteligjent, më i miri në botë për të kuptuarit multimodal, i gjithi i ndërtuar mbi arsyetimin më të fundit.

spark Gemini 3 Flash i Ri

Performancë e klasit të parë që rivalizon modelet më të mëdha me një kosto shumë më të ulët.

spark Gemini 3.1 Flash-Lite i Ri

Model pune me vëllim të lartë dhe i ndjeshëm ndaj kostos, me performancën dhe cilësinë e serisë Gemini 3.

🍌 Nano Banana 2 dhe Nano Banana Pro

Modele të gjenerimit dhe redaktimit të imazheve të teknologjisë së fundit.

video\_library Veo 3.1

Modeli ynë i gjenerimit të videove, i teknologjisë së fundit, me audio native.

spark Gemini Robotics

Një model i gjuhës së vizionit (VLM) që sjell aftësitë agjentike të Gemini në robotikë dhe mundëson arsyetim të avancuar në botën fizike.

## Eksploro Aftësitë

imagesmode

Gjenerimi i Imazhit Nativ (Nano Banana)

Gjeneroni dhe modifikoni imazhe me kontekst të lartë në mënyrë native me Gemini 2.5 Flash Image.

article

Kontekst i gjatë

Futni miliona tokena në modelet Gemini dhe nxirrni njohuri nga imazhe, video dhe dokumente të pastrukturuara.

code

Rezultatet e strukturuara

Kufizoni Gemini-n që të përgjigjet me JSON, një format të strukturuar të të dhënave i përshtatshëm për përpunim të automatizuar.

functions

Thirrja e funksionit

Ndërtoni rrjedha pune agjentësh duke lidhur Gemini me API dhe mjete të jashtme.

videocam

Gjenerimi i videos me Veo 3.1

Krijoni përmbajtje video me cilësi të lartë nga tekst ose imazhe me modelin tonë të teknologjisë së fundit.

android\_recorder

Agjentë Zëri me API Live

Ndërtoni aplikacione dhe agjentë zanorë në kohë reale me Live API.

build

Mjete

Lidhni Binjakët me botën përmes mjeteve të integruara si Kërkimi në Google, Konteksti i URL-së, Hartat e Google-it, Ekzekutimi i Kodit dhe Përdorimi i Kompjuterit.

stacks

Kuptimi i Dokumenteve

Përpunoni deri në 1000 faqe skedarë PDF me kuptim të plotë multimodal ose lloje të tjera skedarësh të bazuar në tekst.

cognition\_2

Të menduarit

Eksploroni se si aftësitë e të menduarit përmirësojnë arsyetimin për detyra dhe agjentë kompleksë.

Studioja e AI-së e Google-it

Testoni kërkesat, menaxhoni çelësat API, monitoroni përdorimin dhe ndërtoni prototipa.

group

Komuniteti i Zhvilluesve

Bëni pyetje dhe gjeni zgjidhje nga zhvillues të tjerë dhe inxhinierë të Google.

menu\_book

Referenca e API-t

Gjeni informacion të detajuar rreth Gemini API në dokumentacionin zyrtar të referencës.

sensors

Statusi

Kontrolloni statusin e Gemini API, Google AI Studio dhe shërbimeve tona model.

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-03-03 UTC.




\[\[\["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"\],\["E zgjidhi problemin tim","solvedMyProblem","thumb-up"\],\["Tjetër","otherUp","thumb-up"\]\],\[\["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"\],\["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"\],\["E papërditësuar","outOfDate","thumb-down"\],\["Problem përkthimi","translationIssue","thumb-down"\],\["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"\],\["Tjetër","otherDown","thumb-down"\]\],\["Përditësimi i fundit: 2026-03-03 UTC."\],\[\],\[\]\]