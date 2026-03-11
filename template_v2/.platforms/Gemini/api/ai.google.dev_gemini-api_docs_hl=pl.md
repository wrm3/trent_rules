[Przejdź do głównej treści](https://ai.google.dev/gemini-api/docs?hl=pl#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=pl)](https://ai.google.dev/)

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

[Pobierz klucz interfejsu API](https://aistudio.google.com/apikey?hl=pl) [Książka kucharska](https://github.com/google-gemini/cookbook) [Społeczność](https://discuss.ai.google.dev/c/gemini-api/?hl=pl)

[Zaloguj się](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dpl&prompt=select_account)


Wersja testowa Gemini 3.1 Flash-Lite jest już dostępna. [Wypróbuj w AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=pl)

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

# Gemini API

Najszybsza droga od prompta do produkcji dzięki Gemini, Veo, Nano Banana i innym narzędziom.

[Python](https://ai.google.dev/gemini-api/docs?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=pl#go)[Java](https://ai.google.dev/gemini-api/docs?hl=pl#java)[C#](https://ai.google.dev/gemini-api/docs?hl=pl#c)[REST](https://ai.google.dev/gemini-api/docs?hl=pl#rest)Więcej

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

[Zacznij tworzyć](https://ai.google.dev/gemini-api/docs/quickstart?hl=pl)

Zapoznaj się z naszym przewodnikiem Szybki start, aby w kilka minut uzyskać klucz interfejsu API i wykonać pierwsze wywołanie interfejsu API.

* * *

## Poznaj modele

[Wyświetl wszystko](https://ai.google.dev/gemini-api/docs/models?hl=pl)

[auto\_awesome\\
Gemini 3.1 Pro\\
Nowość\\
\\
Nasz najbardziej inteligentny model, najlepszy na świecie pod względem rozumienia multimodalnego, zbudowany na bazie najnowocześniejszego rozumowania.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) [spark\\
Gemini 3 Flash\\
Nowość\\
\\
Wydajność klasy Frontier, która dorównuje większym modelom, ale jest dostępna za ułamek ceny.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) [spark\\
Gemini 3.1 Flash-Lite\\
Nowość\\
\\
Wydajny model do obsługi dużego ruchu, w którym istotne są koszty, o wydajności i jakości serii Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=pl) [🍌\\
Nano Banana 2 i Nano Banana Pro\\
\\
\\
Najnowocześniejsze modele do generowania i edytowania obrazów.](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) [video\_library\\
Veo 3.1\\
\\
\\
Nasz najnowocześniejszy model do generowania filmów z wbudowaną funkcją generowania dźwięku.](https://ai.google.dev/gemini-api/docs/video?hl=pl) [spark\\
Gemini Robotics\\
\\
\\
Model wizualno-językowy (VLM), który udostępnia funkcje agenta Gemini w robotyce i umożliwia zaawansowane rozumowanie w świecie fizycznym.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl)

## Poznaj możliwości

[imagesmode\\
\\
Natywne generowanie obrazów (Nano Banana)\\
\\
\\
Generuj i edytuj obrazy o wysokim poziomie kontekstowości w sposób natywny za pomocą Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) [article\\
\\
Długi kontekst\\
\\
\\
Przesyłaj do modeli Gemini miliony tokenów i wyodrębniaj informacje z nieuporządkowanych obrazów, filmów i dokumentów.](https://ai.google.dev/gemini-api/docs/long-context?hl=pl) [code\\
\\
Uporządkowane dane wyjściowe\\
\\
\\
Ogranicz Gemini do odpowiadania w formacie JSON, czyli formacie danych strukturalnych odpowiednim do automatycznego przetwarzania.](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl) [functions\\
\\
Wywoływanie funkcji\\
\\
\\
Twórz przepływy pracy oparte na agentach, łącząc Gemini z zewnętrznymi interfejsami API i narzędziami.](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) [videocam\\
\\
Generowanie filmów za pomocą Veo 3.1\\
\\
\\
Twórz wysokiej jakości treści wideo na podstawie promptów tekstowych lub obrazowych za pomocą naszego najnowocześniejszego modelu.](https://ai.google.dev/gemini-api/docs/video?hl=pl) [android\_recorder\\
\\
Agenci głosowi z interfejsem Live API\\
\\
\\
Twórz aplikacje i agenty głosowe działające w czasie rzeczywistym za pomocą interfejsu Live API.](https://ai.google.dev/gemini-api/docs/live?hl=pl) [build\\
\\
Narzędzia\\
\\
\\
Połącz Gemini ze światem za pomocą wbudowanych narzędzi, takich jak wyszukiwarka Google, kontekst adresu URL, Mapy Google, wykonywanie kodu i korzystanie z komputera.](https://ai.google.dev/gemini-api/docs/tools?hl=pl) [stacks\\
\\
Rozumienie dokumentów\\
\\
\\
Przetwarzaj do 1000 stron plików PDF z pełnym zrozumieniem multimodalnym lub innych typów plików tekstowych.](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl) [cognition\_2\\
\\
Myślę\\
\\
\\
Dowiedz się, jak funkcje myślenia poprawiają rozumowanie w przypadku złożonych zadań i agentów.](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)

[Google AI Studio\\
\\
\\
Testuj prompty, zarządzaj kluczami interfejsu API, monitoruj wykorzystanie i twórz prototypy.](https://aistudio.google.com/?hl=pl) [group\\
\\
Społeczność deweloperów\\
\\
\\
zadawać pytania i znajdować rozwiązania od innych deweloperów i inżynierów Google,](https://discuss.ai.google.dev/c/gemini-api/4?hl=pl) [menu\_book\\
\\
Dokumentacja API\\
\\
\\
Szczegółowe informacje o interfejsie Gemini API znajdziesz w oficjalnej dokumentacji referencyjnej.](https://ai.google.dev/api?hl=pl) [sensors\\
\\
Stan\\
\\
\\
Sprawdź stan Gemini API, Google AI Studio i naszych usług modeli.](https://aistudio.google.com/status?hl=pl)

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-03-03 UTC.




\[\[\["Łatwo zrozumieć","easyToUnderstand","thumb-up"\],\["Rozwiązało to mój problem","solvedMyProblem","thumb-up"\],\["Inne","otherUp","thumb-up"\]\],\[\["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"\],\["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"\],\["Nieaktualne treści","outOfDate","thumb-down"\],\["Problem z tłumaczeniem","translationIssue","thumb-down"\],\["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"\],\["Inne","otherDown","thumb-down"\]\],\["Ostatnia aktualizacja: 2026-03-03 UTC."\],\[\],\[\]\]