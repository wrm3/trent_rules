[Przejdź do głównej treści](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=pl)](https://ai.google.dev/)

`/`

- English
- Deutsch
- Español – América Latina
- Français
- Indonesia
- Italiano
- Polski
- Português – Brasil
- Shqip
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어

[Pobierz klucz interfejsu API](https://aistudio.google.com/apikey?hl=pl) [Książka kucharska](https://github.com/google-gemini/cookbook) [Społeczność](https://discuss.ai.google.dev/c/gemini-api/?hl=pl)Zaloguj się


Wersja testowa Gemini 3.1 Flash-Lite jest już dostępna. [Wypróbuj w AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=pl)

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)



 Prześlij opinię



# Gemini

[Modele z serii Gemini 3 i 2.5](https://ai.google.dev/gemini-api/docs/models?hl=pl) wykorzystują wewnętrzny „proces myślowy”, który znacznie poprawia ich zdolność do rozumowania i planowania wieloetapowego, dzięki czemu są bardzo skuteczne w przypadku złożonych zadań, takich jak kodowanie, zaawansowana matematyka i analiza danych.

Z tego przewodnika dowiesz się, jak korzystać z możliwości myślenia Gemini za pomocą interfejsu Gemini API.

## Generowanie treści z myśleniem

Inicjowanie prośby za pomocą modelu myślowego jest podobne do każdej innej prośby o wygenerowanie treści. Kluczowa różnica polega na określeniu jednego z [modeli z obsługą myślenia](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#supported-models) w polu `model`, jak pokazano w tym przykładzie [generowania tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#text-input):

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3-flash-preview"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

````
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [\
     {\
       "parts": [\
         {\
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."\
         }\
       ]\
     }\
   ]
 }'
 ```
````

## Podsumowania myśli

Podsumowania procesu myślowego to skrócone wersje pierwotnych myśli modelu, które pozwalają zrozumieć jego wewnętrzny proces rozumowania. Pamiętaj, że poziomy myślenia i budżety dotyczą surowych myśli modelu, a nie podsumowań myśli.

Aby włączyć podsumowania myśli, ustaw w konfiguracji żądania wartość `includeThoughts` na `true`. Następnie możesz uzyskać dostęp do podsumowania, iterując parametr `response``parts` i sprawdzając wartość logiczną `thought`.

Oto przykład pokazujący, jak włączyć i pobrać podsumowania myśli bez przesyłania strumieniowego, co zwraca jedno końcowe podsumowanie myśli w odpowiedzi:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

A oto przykład użycia funkcji myślenia strumieniowego, która podczas generowania zwraca podsumowania kroczące i przyrostowe:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3-flash-preview",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3-flash-preview"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Kontrolowanie myślenia

Modele Gemini domyślnie korzystają z dynamicznego myślenia, automatycznie dostosowując poziom rozumowania do złożoności zapytania użytkownika.
Jeśli jednak masz określone ograniczenia dotyczące opóźnienia lub wymagasz, aby model przeprowadzał bardziej szczegółowe rozumowanie niż zwykle, możesz opcjonalnie użyć parametrów do kontrolowania sposobu myślenia.

### Poziomy myślenia (Gemini 3)

Parametr `thinkingLevel`, zalecany w przypadku modeli Gemini 3 i nowszych, pozwala kontrolować sposób rozumowania.

W tabeli poniżej znajdziesz szczegółowe informacje o ustawieniach `thinkingLevel` dla każdego typu modelu:

| Poziom myślenia | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Opis |
| --- | --- | --- | --- | --- |
| **`minimal`** | Nieobsługiwane | Obsługiwane (domyślnie) | Obsługiwane | W przypadku większości zapytań odpowiada ustawieniu „bez myślenia”. W przypadku złożonych zadań związanych z kodowaniem model może myśleć w bardzo ograniczonym zakresie. Minimalizuje opóźnienia w przypadku aplikacji do czatu lub aplikacji o wysokiej przepustowości. Pamiętaj, że `minimal` nie gwarantuje, że myślenie jest wyłączone. |
| **`low`** | Obsługiwane | Obsługiwane | Obsługiwane | Minimalizuje opóźnienia i koszty. Najlepiej sprawdza się w przypadku prostych instrukcji, czatów i aplikacji o wysokiej przepustowości. |
| **`medium`** | Obsługiwane | Obsługiwane | Obsługiwane | Zrównoważone myślenie w przypadku większości zadań. |
| **`high`** | Obsługiwane (domyślne, dynamiczne) | Obsługiwane (dynamiczne) | Obsługiwane (domyślne, dynamiczne) | Zwiększa głębokość wnioskowania. Model może potrzebować znacznie więcej czasu, aby wygenerować pierwszy token wyjściowy (niebędący tokenem myślenia), ale wynik będzie bardziej przemyślany. |

Przykład poniżej pokazuje, jak ustawić poziom myślenia.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

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
          "text": "Provide a list of 3 famous physicists and their key contributions"\
        }\
      ]\
    }\
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Nie możesz wyłączyć myślenia w przypadku Gemini 3 Pro. Gemini 3 Flash również nie obsługuje pełnego wyłączenia myślenia, ale ustawienie `minimal` oznacza, że model prawdopodobnie nie będzie myśleć (chociaż nadal może).
Jeśli nie określisz poziomu myślenia, Gemini użyje domyślnego dynamicznego poziomu myślenia modeli Gemini 3, `"high"`.

Modele z serii Gemini 2.5 nie obsługują tego typu pliku: `thinkingLevel`. Zamiast tego użyj `thinkingBudget`.

### Budżety na myślenie

Parametr `thinkingBudget`, wprowadzony w serii Gemini 2.5, określa liczbę tokenów myślenia, których model ma użyć do rozumowania.

Poniżej znajdziesz `thinkingBudget` szczegóły konfiguracji każdego typu modelu.
Możesz wyłączyć myślenie, ustawiając wartość `thinkingBudget` na 0.
Ustawienie wartości `thinkingBudget` na -1 włącza **dynamiczne myślenie**, co oznacza, że model dostosuje budżet do złożoności żądania.

| Model | Ustawienie domyślne<br>(budżet na myślenie nie jest ustawiony) | Zakres | Wyłącz przebieg rozumowania | Włącz myślenie dynamiczne |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Myślenie dynamiczne | Od `128` do `32768` | Nie dotyczy: nie można wyłączyć myślenia | `thinkingBudget = -1` (wartość domyślna) |
| **2.5 Flash** | Myślenie dynamiczne | Od `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (wartość domyślna) |
| **Podgląd 2.5 Flash** | Myślenie dynamiczne | Od `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (wartość domyślna) |
| **2.5 Flash Lite** | Model nie myśli | Od `512` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | Model nie myśli | Od `512` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.5 Preview** | Myślenie dynamiczne | Od `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (wartość domyślna) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Myślenie dynamiczne | Od `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (wartość domyślna) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

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
          "text": "Provide a list of 3 famous physicists and their key contributions"\
        }\
      ]\
    }\
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

W zależności od promptu model może przekroczyć lub nie wykorzystać w pełni budżetu tokenów.

## Podpisy myśli

Interfejs Gemini API jest bezstanowy, więc model traktuje każde żądanie API niezależnie i nie ma dostępu do kontekstu myślowego z poprzednich tur w interakcjach wieloturwych.

Aby umożliwić zachowanie kontekstu myślowego w interakcjach wieloetapowych, Gemini zwraca sygnatury myśli, które są zaszyfrowanymi reprezentacjami wewnętrznego procesu myślowego modelu.

- **Modele Gemini 2.5** zwracają sygnatury myśli, gdy myślenie jest włączone, a żądanie obejmuje [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#thinking), a w szczególności [deklaracje funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#step-2).
- **Modele Gemini 3** mogą zwracać sygnatury myśli dla wszystkich typów [części](https://ai.google.dev/api/caching?hl=pl#Part).
Zalecamy zawsze przekazywać wszystkie podpisy w takiej postaci, w jakiej zostały otrzymane, ale w przypadku podpisów wywołań funkcji jest to _wymagane_. Więcej informacji znajdziesz na stronie [Podpisy myśli](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pl).


[Pakiet SDK generatywnej AI od Google](https://ai.google.dev/gemini-api/docs/libraries?hl=pl) automatycznie obsługuje zwracanie sygnatur myśli. [Ręczne zarządzanie sygnaturami myśli](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#thought-signatures) jest konieczne tylko wtedy, gdy modyfikujesz historię rozmów lub używasz interfejsu REST API.

Inne ograniczenia dotyczące wywoływania funkcji, o których warto pamiętać:

- Sygnatury są zwracane przez model w innych częściach odpowiedzi, np. w wywołaniach funkcji lub częściach tekstowych.
[Zwróć całą odpowiedź](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#step-4)
ze wszystkimi częściami do modelu w kolejnych turach.
- Nie łącz części z sygnaturami.
- Nie łącz części z podpisem z częścią bez podpisu.

## Ceny

Gdy myślenie jest włączone, cena odpowiedzi jest sumą tokenów wyjściowych i tokenów myślenia. Łączną liczbę wygenerowanych tokenów myślenia możesz uzyskać z pola `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
print("Output tokens:",response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println("Thoughts tokens:", string(usageMetadata.thoughts_token_count))
fmt.Println("Output tokens:", string(usageMetadata.candidates_token_count))
```

Modele myślowe generują pełne myśli, aby poprawić jakość ostatecznej odpowiedzi, a następnie wyświetlają [podsumowania](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#summaries), które pozwalają zrozumieć proces myślowy. Ceny są więc oparte na pełnych tokenach myśli, których model potrzebuje do wygenerowania podsumowania, mimo że interfejs API zwraca tylko podsumowanie.

Więcej informacji o tokenach znajdziesz w przewodniku [Liczba tokenów](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

## Sprawdzone metody

W tej sekcji znajdziesz wskazówki dotyczące efektywnego korzystania z modeli myślowych.
Jak zawsze, najlepsze wyniki uzyskasz, jeśli będziesz postępować zgodnie z naszymi [wskazówkami i sprawdzonymi metodami dotyczącymi promptów](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl).

### Debugowanie i sterowanie

- **Sprawdzanie uzasadnienia:** jeśli modele myślowe nie dają oczekiwanych odpowiedzi, warto dokładnie przeanalizować podsumowania myśli Gemini.
Możesz zobaczyć, jak podzielił zadanie i doszedł do wniosku, a także wykorzystać te informacje, aby poprawić wyniki.

- **Podaj wskazówki dotyczące uzasadnienia:** jeśli oczekujesz szczególnie długiego wyniku, możesz podać w prompcie wskazówki, aby ograniczyć [ilość myślenia](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#set-budget), jakiej używa model. Dzięki temu możesz zarezerwować więcej tokenów na swoją odpowiedź.


### Złożoność zadania

- **Proste zadania (myślenie może być wyłączone):**w przypadku prostych żądań, które nie wymagają złożonego rozumowania, np. wyszukiwania faktów lub klasyfikacji, myślenie nie jest potrzebne. Przykłady:

  - „Gdzie powstała firma DeepMind?”
  - „Czy ten e-mail zawiera prośbę o spotkanie, czy tylko informacje?”
- **Średnio złożone zadania (domyślne/wymagające pewnego zastanowienia):**wiele typowych żądań wymaga przetwarzania krok po kroku lub głębszego zrozumienia. Gemini może elastycznie wykorzystywać funkcje myślenia do wykonywania takich zadań jak:
  - Porównaj fotosyntezę i dorastanie.
  - Porównaj samochody elektryczne i hybrydowe.
- **Trudne zadania (maksymalne możliwości rozumowania):**w przypadku naprawdę złożonych wyzwań, takich jak rozwiązywanie skomplikowanych zadań matematycznych lub kodowanie, zalecamy ustawienie wysokiego budżetu na rozumowanie. Tego typu zadania wymagają od modelu pełnego wykorzystania możliwości rozumowania i planowania, często obejmują wiele wewnętrznych kroków przed udzieleniem odpowiedzi. Przykłady:

  - Rozwiąż zadanie 1 z AIME 2025: znajdź sumę wszystkich podstaw całkowitych b > 9, dla których 17b jest dzielnikiem liczby 97b.
  - Napisz kod w Pythonie dla aplikacji internetowej, która wizualizuje dane giełdowe w czasie rzeczywistym, w tym uwierzytelnianie użytkowników. Zadbaj o jak największą wydajność.

## Obsługiwane modele, narzędzia i funkcje

Funkcje myślenia są obsługiwane we wszystkich modelach z serii 3 i 2.5.
Wszystkie możliwości modelu znajdziesz na stronie [informacji o modelu](https://ai.google.dev/gemini-api/docs/models?hl=pl).

Modele myślące działają ze wszystkimi narzędziami i funkcjami Gemini. Umożliwia to modelom interakcję z systemami zewnętrznymi, wykonywanie kodu lub dostęp do informacji w czasie rzeczywistym, a także uwzględnianie wyników w procesie rozumowania i odpowiedzi końcowej.

Przykłady użycia narzędzi z modelami myślącymi znajdziesz w [książce kucharskiej dotyczącej myślenia](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking.ipynb?hl=pl).

## Co dalej?

- Informacje o zakresie znajdziesz w naszym przewodniku [Zgodność z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl#thinking).



 Prześlij opinię



O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-03-03 UTC.


Chcesz przekazać coś jeszcze?






\[\[\["Łatwo zrozumieć","easyToUnderstand","thumb-up"\],\["Rozwiązało to mój problem","solvedMyProblem","thumb-up"\],\["Inne","otherUp","thumb-up"\]\],\[\["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"\],\["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"\],\["Nieaktualne treści","outOfDate","thumb-down"\],\["Problem z tłumaczeniem","translationIssue","thumb-down"\],\["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"\],\["Inne","otherDown","thumb-down"\]\],\["Ostatnia aktualizacja: 2026-03-03 UTC."\],\[\],\[\]\]