[Skip to main content](https://ai.google.dev/gemini-api/docs/libraries#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/libraries)
- [Deutsch](https://ai.google.dev/gemini-api/docs/libraries?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/libraries?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/libraries?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/libraries?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/libraries?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/libraries?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/libraries?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/libraries?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/libraries?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/libraries?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/libraries?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/libraries?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/libraries?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/libraries?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/libraries?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/libraries?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Flibraries&prompt=select_account)

- On this page
- [Language support and installation](https://ai.google.dev/gemini-api/docs/libraries#install)
- [General availability](https://ai.google.dev/gemini-api/docs/libraries#new-libraries)
- [Legacy libraries and migration](https://ai.google.dev/gemini-api/docs/libraries#previous-sdks)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Gemini API libraries

- On this page
- [Language support and installation](https://ai.google.dev/gemini-api/docs/libraries#install)
- [General availability](https://ai.google.dev/gemini-api/docs/libraries#new-libraries)
- [Legacy libraries and migration](https://ai.google.dev/gemini-api/docs/libraries#previous-sdks)

When building with the Gemini API, we recommend using the **Google GenAI SDK**.
These are the official, production-ready libraries that we develop and maintain
for the most popular languages. They are in [General Availability](https://ai.google.dev/gemini-api/docs/libraries#new-libraries) and used in all our official
documentation and examples.

If you're new to the Gemini API, follow our [quickstart guide](https://ai.google.dev/gemini-api/docs/quickstart) to get started.

## Language support and installation

The Google GenAI SDK is available for the Python, JavaScript/TypeScript, Go and
Java languages. You can install each language's library using package managers,
or visit their GitHub repos for further engagement:

[Python](https://ai.google.dev/gemini-api/docs/libraries#python)[JavaScript](https://ai.google.dev/gemini-api/docs/libraries#javascript)[Go](https://ai.google.dev/gemini-api/docs/libraries#go)[Java](https://ai.google.dev/gemini-api/docs/libraries#java)[C#](https://ai.google.dev/gemini-api/docs/libraries#c)More

- Library: [`google-genai`](https://pypi.org/project/google-genai)

- GitHub Repository: [googleapis/python-genai](https://github.com/googleapis/python-genai)

- Installation: `pip install google-genai`


- Library: [`@google/genai`](https://www.npmjs.com/package/@google/genai)

- GitHub Repository: [googleapis/js-genai](https://github.com/googleapis/js-genai)

- Installation: `npm install @google/genai`


- Library: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)

- GitHub Repository: [googleapis/go-genai](https://github.com/googleapis/go-genai)

- Installation: `go get google.golang.org/genai`


- Library: `google-genai`

- GitHub Repository: [googleapis/java-genai](https://github.com/googleapis/java-genai)

- Installation: If you're using Maven, add the following to your dependencies:


```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

- Library: `Google.GenAI`

- GitHub Repository: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)

- Installation: `dotnet add package Google.GenAI`


## General availability

As of May 2025, the Google GenAI SDK has reached General Availability (GA) across
all supported platforms and are the recommended libraries to access the Gemini API.
They are stable, fully supported for production use, and are actively maintained.
They provide access to the latest features, and offer the best performance working
with Gemini.

If you're using one of our legacy libraries,
we strongly recommend you migrate so that you can access the latest features and
get the best performance working with Gemini. Review the [legacy libraries](https://ai.google.dev/gemini-api/docs/libraries#previous-sdks) section for more information.

## Legacy libraries and migration

If you are using one of our legacy libraries, we recommend that you
[migrate to the new libraries](https://ai.google.dev/gemini-api/docs/migrate).

The legacy libraries don't provide access to recent features (such as
[Live API](https://ai.google.dev/gemini-api/docs/live) and [Veo](https://ai.google.dev/gemini-api/docs/video)) and are
deprecated as of November 30th, 2025.

Each legacy library's support status varies, detailed in the following table:

| Language | Legacy library | Support status | Recommended library |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Not actively maintained | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Not actively maintained | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Not actively maintained | `google.golang.org/genai` |
| **Dart and Flutter** | `google_generative_ai` | Not actively maintained | Use trusted community or third party libraries, like [firebase\_ai](https://pub.dev/packages/firebase_ai), or access using REST API |
| **Swift** | `generative-ai-swift` | Not actively maintained | Use [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic) |
| **Android** | `generative-ai-android` | Not actively maintained | Use [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic) |

**Note for Java developers:** There was no legacy Google-provided Java SDK for
the Gemini API, so no migration from a previous Google library is required. You
can start directly with the new library in the
[Language support and installation](https://ai.google.dev/gemini-api/docs/libraries#install) section.

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-02-24 UTC."\],\[\],\[\]\]