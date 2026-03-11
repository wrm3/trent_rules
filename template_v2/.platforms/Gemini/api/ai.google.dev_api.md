[Skip to main content](https://ai.google.dev/api#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

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

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi&prompt=select_account)

- On this page
- [Primary endpoints](https://ai.google.dev/api#primary-endpoints)
- [Authentication](https://ai.google.dev/api#authentication)
- [Content generation](https://ai.google.dev/api#content-generation)
  - [Request body structure](https://ai.google.dev/api#request-body-structure)
  - [Response body structure](https://ai.google.dev/api#response-body-structure)
- [Request examples](https://ai.google.dev/api#request-examples)
  - [Text-only prompt](https://ai.google.dev/api#text-only-prompt)
  - [Multimodal prompt (text and image)](https://ai.google.dev/api#multimodal-prompt)
  - [Multi-turn conversations (chat)](https://ai.google.dev/api#multi-turn-conversations)
  - [Key takeaways](https://ai.google.dev/api#key-takeaways)
- [Response examples](https://ai.google.dev/api#response-examples)
  - [Text-only response](https://ai.google.dev/api#text-only-response)
- [Live API (BidiGenerateContent) WebSockets API](https://ai.google.dev/api#live-api)
- [Specialized models](https://ai.google.dev/api#specialized-models)
- [Platform APIs](https://ai.google.dev/api#platform-apis)
- [What's next](https://ai.google.dev/api#whats-next)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [API reference](https://ai.google.dev/api)

Was this helpful?



 Send feedback



# Gemini API reference

- On this page
- [Primary endpoints](https://ai.google.dev/api#primary-endpoints)
- [Authentication](https://ai.google.dev/api#authentication)
- [Content generation](https://ai.google.dev/api#content-generation)
  - [Request body structure](https://ai.google.dev/api#request-body-structure)
  - [Response body structure](https://ai.google.dev/api#response-body-structure)
- [Request examples](https://ai.google.dev/api#request-examples)
  - [Text-only prompt](https://ai.google.dev/api#text-only-prompt)
  - [Multimodal prompt (text and image)](https://ai.google.dev/api#multimodal-prompt)
  - [Multi-turn conversations (chat)](https://ai.google.dev/api#multi-turn-conversations)
  - [Key takeaways](https://ai.google.dev/api#key-takeaways)
- [Response examples](https://ai.google.dev/api#response-examples)
  - [Text-only response](https://ai.google.dev/api#text-only-response)
- [Live API (BidiGenerateContent) WebSockets API](https://ai.google.dev/api#live-api)
- [Specialized models](https://ai.google.dev/api#specialized-models)
- [Platform APIs](https://ai.google.dev/api#platform-apis)
- [What's next](https://ai.google.dev/api#whats-next)

This API reference describes the standard, streaming, and real-time APIs you can
use to interact with the Gemini models. You can use the REST APIs in any
environment that supports HTTP requests. Refer to the
[Quickstart guide](https://ai.google.dev/gemini-api/docs/quickstart) for how to
get started with your first API call. If you're looking for the references for
our language-specific libraries and SDKs, go to the link for that language in
the left navigation under **SDK references**.

## Primary endpoints

The Gemini API is organized around the following major endpoints:

- **Standard content generation ( [`generateContent`](https://ai.google.dev/api/generate-content#method:-models.generatecontent)):**
A standard REST endpoint that processes your request and returns the model's
full response in a single package. This is best for non-interactive tasks
where you can wait for the entire result.
- **Streaming content generation ( [`streamGenerateContent`](https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent)):**
Uses Server-Sent Events (SSE) to push chunks of the response to you as they
are generated. This provides a faster, more interactive experience for
applications like chatbots.
- **Live API ( [`BidiGenerateContent`](https://ai.google.dev/api/live#send-messages)):** A stateful WebSocket-based
API for bi-directional streaming, designed for real-time conversational use
cases.
- **Batch mode ( [`batchGenerateContent`](https://ai.google.dev/api/batch-mode)):** A standard REST
endpoint for submitting batches of `generateContent` requests.
- **Embeddings ( [`embedContent`](https://ai.google.dev/api/embeddings)):** A standard REST endpoint
that generates a text embedding vector from the input `Content`.
- **Gen Media APIs:** Endpoints for generating media with our specialized
models such as [Imagen for image generation](https://ai.google.dev/api/models#method:-models.predict),
and [Veo for video generation](https://ai.google.dev/api/models#method:-models.predictlongrunning).
Gemini also has these capabilities built in which you can access using the
`generateContent` API.
- **Platform APIs:** Utility endpoints that support core capabilities such as
[uploading files](https://ai.google.dev/api/files), and [counting tokens](https://ai.google.dev/api/tokens).

## Authentication

All requests to the Gemini API must include a `x-goog-api-key` header with your
API key. Create one with a few clicks in [Google AI\\
Studio](https://aistudio.google.com/app/apikey).

The following is an example request with the API key included in the header:

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

For instructions on how to pass your key to the API using Gemini SDKs,
see the [Using Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key) guide.

## Content generation

This is the central endpoint for sending prompts to the model. There are two
endpoints for generating content, the key difference is how you receive the
response:

- **[`generateContent`](https://ai.google.dev/api/generate-content#method:-models.generatecontent)**
**(REST)**:
Receives a request and provides a
single response after the model has finished its entire generation.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent)**
**(SSE)**: Receives the exact same
request, but the model streams back chunks of the response as they are
generated. This provides a better user experience for interactive
applications as it lets you display partial results immediately.

### Request body structure

The [request body](https://ai.google.dev/api/generate-content#request-body) is a JSON object that is
**identical** for both standard and streaming modes and is built from a few core
objects:

- [`Content`](https://ai.google.dev/api/caching#Content) object: Represents a single turn in a
conversation.
- [`Part`](https://ai.google.dev/api/caching#Part) object: A piece of data within a `Content` turn
(like text or an image).
- `inline_data` ( [`Blob`](https://ai.google.dev/api/caching#Blob)): A container for raw media bytes
and their MIME type.

At the highest level, the request body contains a `contents` object, which is a
list of `Content` objects, each representing turns in conversation. In most
cases, for basic text generation, you will have a single `Content` object, but
if you'd like to maintain conversation history, you can use multiple `Content`
objects.

The following shows a typical `generateContent` request body:

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

### Response body structure

The [response body](https://ai.google.dev/api/generate-content#response-body) is similar for both
the streaming and standard modes except for the following:

- Standard mode: The response body contains an instance of
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content#v1beta.GenerateContentResponse).
- Streaming mode: The response body contains a stream of
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content#v1beta.GenerateContentResponse)
instances.

At a high level, the response body contains a `candidates` object, which is a
list of `Candidate` objects. The `Candidate` object contains a `Content`
object that has the generated response returned from the model.

## Request examples

The following examples show how these components come together for different
types of requests.

### Text-only prompt

A simple text prompt consists of a `contents` array with a single `Content`
object. That object's `parts` array, in turn, contains a single `Part` object
with a `text` field.

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

### Multimodal prompt (text and image)

To provide both text and an image in a prompt, the `parts` array should contain
two `Part` objects: one for the text, and one for the image `inline_data`.

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

### Multi-turn conversations (chat)

To build a conversation with multiple turns, you define the `contents` array
with multiple `Content` objects. The API will use this entire history as context
for the next response. The `role` for each `Content` object should alternate
between `user` and `model`.

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

### Key takeaways

- `Content` is the envelope: It's the top-level container for a message turn,
whether it's from the user or the model.
- `Part` enables multimodality: Use multiple `Part` objects within a single
`Content`
object to combine different types of data (text, image, video URI, etc.).
- Choose your data method:
  - For small, directly embedded media (like most images), use a `Part` with
    `inline_data`.
  - For larger files or files you want to reuse across requests, use the
    File API to upload the file and reference it with a `file_data` part.
- Manage conversation history: For chat applications using the REST API, build
the `contents` array by appending `Content` objects for each turn,
alternating between `"user"` and `"model"` roles. If you're using an SDK,
refer to the SDK documentation for the recommended way to manage
conversation history.

## Response examples

The following examples show how these components come together for different
types of requests.

### Text-only response

A default text response consists of a `candidates` array with one or more
`content` objects that contain the model's response.

The following is an example of a **standard** response:

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

The following is series of **streaming** responses. Each response contains a
`responseId` that ties the full response together:

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

Live API offers a stateful WebSocket based API for bi-directional streaming to
enable real-time streaming use cases. You can review
[Live API guide](https://ai.google.dev/gemini-api/docs/live) and the [Live API reference](https://ai.google.dev/api/live)
for more details.

## Specialized models

In addition to the Gemini family of models, Gemini API offers endpoints for
specialized models such as [Imagen](https://ai.google.dev/gemini-api/docs/imagen),
[Lyria](https://ai.google.dev/gemini-api/docs/music-generation) and
[embedding](https://ai.google.dev/gemini-api/docs/embeddings) models. You can check out
these guides under the Models section.

## Platform APIs

The rest of the endpoints enable additional capabilities to use with the main
endpoints described so far. Check out topics
[Batch mode](https://ai.google.dev/gemini-api/docs/batch-mode) and
[File API](https://ai.google.dev/gemini-api/docs/files) in the Guides section to learn more.

## What's next

If you're just getting started, check out the following guides, which will help
you understand the Gemini API programming model:

- [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [Gemini model guide](https://ai.google.dev/gemini-api/docs/models/gemini)

You might also want to check out the capabilities guides, which introduce different
Gemini API features and provide code examples:

- [Text generation](https://ai.google.dev/gemini-api/docs/text-generation)
- [Context caching](https://ai.google.dev/gemini-api/docs/caching)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings)

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-25 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-02-25 UTC."\],\[\],\[\]\]