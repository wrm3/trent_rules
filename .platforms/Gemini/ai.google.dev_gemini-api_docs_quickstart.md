[Skip to main content](https://ai.google.dev/gemini-api/docs/quickstart#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/quickstart)
- [Deutsch](https://ai.google.dev/gemini-api/docs/quickstart?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/quickstart?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/quickstart?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/quickstart?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/quickstart?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/quickstart?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/quickstart?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/quickstart?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/quickstart?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/quickstart?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/quickstart?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/quickstart?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/quickstart?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/quickstart?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fquickstart&prompt=select_account)

- On this page
- [Before you begin](https://ai.google.dev/gemini-api/docs/quickstart#before_you_begin)
- [Install the Google GenAI SDK](https://ai.google.dev/gemini-api/docs/quickstart#install-gemini-library)
- [Make your first request](https://ai.google.dev/gemini-api/docs/quickstart#make-first-request)
- [What's next](https://ai.google.dev/gemini-api/docs/quickstart#what's-next)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Gemini API quickstart

- On this page
- [Before you begin](https://ai.google.dev/gemini-api/docs/quickstart#before_you_begin)
- [Install the Google GenAI SDK](https://ai.google.dev/gemini-api/docs/quickstart#install-gemini-library)
- [Make your first request](https://ai.google.dev/gemini-api/docs/quickstart#make-first-request)
- [What's next](https://ai.google.dev/gemini-api/docs/quickstart#what's-next)

This quickstart shows you how to install our [libraries](https://ai.google.dev/gemini-api/docs/libraries)
and make your first Gemini API request.

## Before you begin

Using the Gemini API requires an API key, you can create one for free to get started.

[Create a Gemini API Key](https://aistudio.google.com/app/apikey)

## Install the Google GenAI SDK

[Python](https://ai.google.dev/gemini-api/docs/quickstart#python)[JavaScript](https://ai.google.dev/gemini-api/docs/quickstart#javascript)[Go](https://ai.google.dev/gemini-api/docs/quickstart#go)[Java](https://ai.google.dev/gemini-api/docs/quickstart#java)[C#](https://ai.google.dev/gemini-api/docs/quickstart#c)[Apps Script](https://ai.google.dev/gemini-api/docs/quickstart#apps-script)More

Using [Python 3.9+](https://www.python.org/downloads/), install the
[`google-genai` package](https://pypi.org/project/google-genai/)
using the following
[pip command](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

Using [Node.js v18+](https://nodejs.org/en/download/package-manager),
install the
[Google Gen AI SDK for TypeScript and JavaScript](https://www.npmjs.com/package/@google/genai)
using the following
[npm command](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

Install
[google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai) in
your module directory using the [go get command](https://go.dev/doc/code):

```
go get google.golang.org/genai
```

If you're using Maven, you can install
[google-genai](https://github.com/googleapis/java-genai) by adding the
following to your dependencies:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

Install
[googleapis/go-genai](https://googleapis.github.io/dotnet-genai/) in
your module directory using the [dotnet add command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add)

```
dotnet add package Google.GenAI
```

1. To create a new Apps Script project, go to
[script.new](https://script.google.com/u/0/home/projects/create).
2. Click **Untitled project**.
3. Rename the Apps Script project **AI Studio** and click **Rename**.
4. Set your [API key](https://developers.google.com/apps-script/guides/properties#manage_script_properties_manually)
1. At the left, click **Project Settings**![The icon for project settings](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg).
2. Under **Script Properties** click **Add script property**.
3. For **Property**, enter the key name: `GEMINI_API_KEY`.
4. For **Value**, enter the value for the API key.
5. Click **Save script properties**.
5. Replace the `Code.gs` file contents with the following code:

## Make your first request

Here is an example that uses the
[`generateContent`](https://ai.google.dev/api/generate-content#method:-models.generatecontent) method
to send a request to the Gemini API using the Gemini 2.5 Flash model.

If you [set your API key](https://ai.google.dev/gemini-api/docs/api-key#set-api-env-var) as the
environment variable `GEMINI_API_KEY`, it will be picked up automatically by the
client when using the [Gemini API libraries](https://ai.google.dev/gemini-api/docs/libraries).
Otherwise you will need to [pass your API key](https://ai.google.dev/gemini-api/docs/api-key#provide-api-key-explicitly) as
an argument when initializing the client.

Note that all code samples in the Gemini API docs assume that you have set the
environment variable `GEMINI_API_KEY`.

[Python](https://ai.google.dev/gemini-api/docs/quickstart#python)[JavaScript](https://ai.google.dev/gemini-api/docs/quickstart#javascript)[Go](https://ai.google.dev/gemini-api/docs/quickstart#go)[Java](https://ai.google.dev/gemini-api/docs/quickstart#java)[C#](https://ai.google.dev/gemini-api/docs/quickstart#c)[Apps Script](https://ai.google.dev/gemini-api/docs/quickstart#apps-script)[REST](https://ai.google.dev/gemini-api/docs/quickstart#rest)More

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
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
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
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
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
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
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [\
      {\
        parts: [\
          { text: 'Explain how AI works in a few words' },\
        ],\
      },\
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
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

## What's next

Now that you made your first API request, you might want to explore the
following guides that show Gemini in action:

- [Text generation](https://ai.google.dev/gemini-api/docs/text-generation)
- [Image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Image understanding](https://ai.google.dev/gemini-api/docs/image-understanding)
- [Thinking](https://ai.google.dev/gemini-api/docs/thinking)
- [Function calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [Long context](https://ai.google.dev/gemini-api/docs/long-context)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings)

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-02-24 UTC."\],\[\],\[\]\]