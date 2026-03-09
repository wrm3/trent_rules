[Перейти к основному контенту](https://ai.google.dev/gemini-api/docs?hl=ru#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=ru)](https://ai.google.dev/)

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

[Как получить ключ API](https://aistudio.google.com/apikey?hl=ru) [Кулинарная книга](https://github.com/google-gemini/cookbook) [Сообщество](https://discuss.ai.google.dev/c/gemini-api/?hl=ru)

[Войти](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dru&prompt=select_account)

Предварительная версия Gemini 3.1 Flash-Lite теперь доступна. [Попробуйте её в AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=ru) .


![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Эта страница переведена с помощью [Cloud Translation API](https://cloud.google.com/translate/?hl=ru).


Switch to English


- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

# API Gemini

Самый быстрый путь от идеи до внедрения в производство с помощью Gemini, Veo, Nano Banana и других решений.

[Python](https://ai.google.dev/gemini-api/docs?hl=ru#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=ru#javascript)[Идти](https://ai.google.dev/gemini-api/docs?hl=ru#%D0%B8%D0%B4%D1%82%D0%B8)[Java](https://ai.google.dev/gemini-api/docs?hl=ru#java)[C#](https://ai.google.dev/gemini-api/docs?hl=ru#c)[ОТДЫХ](https://ai.google.dev/gemini-api/docs?hl=ru#%D0%BE%D1%82%D0%B4%D1%8B%D1%85)Ещё

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

[Начните строительство](https://ai.google.dev/gemini-api/docs/quickstart?hl=ru)

Следуйте нашему краткому руководству, чтобы получить ключ API и совершить свой первый вызов API за считанные минуты.

* * *

## Познакомьтесь с моделями

[Просмотреть все](https://ai.google.dev/gemini-api/docs/models?hl=ru)

auto\_awesome Gemini 3.1 Pro New

Наша самая интеллектуальная модель, лучшая в мире для понимания мультимодальных данных, построена на самых современных аналитических методах.

spark Gemini 3 Flash New

Характеристики уровня Frontier, сопоставимые с более крупными моделями, но по гораздо более низкой цене.

Новый фонарик spark Gemini 3.1

Высокопроизводительная, экономичная и надежная рабочая лошадка, обладающая производительностью и качеством серии Gemini 3.

🍌 Nano Banana 2 и Nano Banana Pro

Современные модели генерации и редактирования изображений.

video\_library Veo 3.1

Наша передовая модель генерации видео с нативным звуком.

spark Gemini Robotics

Модель визуально-языкового восприятия (VLM), которая переносит агентные возможности Gemini в робототехнику и позволяет осуществлять сложные рассуждения в физическом мире.

## Изучите возможности

imagesmode

Генерация изображений нативно (Nano Banana)

Создавайте и редактируйте изображения с высокой степенью контекстной информативности непосредственно в Gemini 2.5 Flash Image.

article

Длинный контекст

Вводите миллионы токенов в модели Gemini и извлекайте информацию из неструктурированных изображений, видео и документов.

code

Структурированные выходные данные

Настройте Gemini на отправку данных в формате JSON — структурированном формате, подходящем для автоматической обработки.

functions

Вызов функции

Создавайте рабочие процессы для агентов, подключая Gemini к внешним API и инструментам.

videocam

Создание видео с помощью Veo 3.1

Создавайте высококачественный видеоконтент на основе текстовых или графических подсказок с помощью нашей современной модели.

android\_recorder

Голосовые агенты с API в реальном времени

Создавайте голосовые приложения и агентов в режиме реального времени с помощью Live API.

build

Инструменты

Подключите Gemini к миру с помощью встроенных инструментов, таких как поиск Google, контекст URL, Google Maps, выполнение кода и использование компьютера.

stacks

Понимание документа

Обрабатывайте до 1000 страниц PDF-файлов с полным пониманием мультимодальных данных или других текстовых типов файлов.

cognition\_2

Мышление

Изучите, как мыслительные способности улучшают способность к рассуждению при решении сложных задач и работе со сложными агентами.

Google AI Studio

Тестируйте запросы, управляйте ключами API, отслеживайте использование и создавайте прототипы.

group

Сообщество разработчиков

Задавайте вопросы и находите решения у других разработчиков и инженеров Google.

menu\_book

Справочник API

Подробную информацию об API Gemini можно найти в официальной справочной документации.

sensors

Статус

Проверьте статус Gemini API, Google AI Studio и наших сервисов моделей.

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-03-03 UTC.




\[\[\["Прост для понимания","easyToUnderstand","thumb-up"\],\["Помог мне решить мою проблему","solvedMyProblem","thumb-up"\],\["Другое","otherUp","thumb-up"\]\],\[\["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"\],\["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"\],\["Устарел","outOfDate","thumb-down"\],\["Проблема с переводом текста","translationIssue","thumb-down"\],\["Проблемы образцов/кода","samplesCodeIssue","thumb-down"\],\["Другое","otherDown","thumb-down"\]\],\["Последнее обновление: 2026-03-03 UTC."\],\[\],\[\]\]