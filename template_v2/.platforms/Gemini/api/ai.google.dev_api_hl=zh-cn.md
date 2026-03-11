[跳至主要内容](https://ai.google.dev/api?hl=zh-cn#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=zh-cn)](https://ai.google.dev/)

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

[获取 API 密钥](https://aistudio.google.com/apikey?hl=zh-cn) [实战宝典](https://github.com/google-gemini/cookbook) [社区](https://discuss.ai.google.dev/c/gemini-api/?hl=zh-cn)

[登录](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi%3Fhl%3Dzh-cn&prompt=select_account)

- 本页内容
- [主要端点](https://ai.google.dev/api?hl=zh-cn#primary-endpoints)
- [身份验证](https://ai.google.dev/api?hl=zh-cn#authentication)
- [内容生成](https://ai.google.dev/api?hl=zh-cn#content-generation)
  - [请求正文结构](https://ai.google.dev/api?hl=zh-cn#request-body-structure)
  - [响应正文结构](https://ai.google.dev/api?hl=zh-cn#response-body-structure)
- [请求示例](https://ai.google.dev/api?hl=zh-cn#request-examples)
  - [纯文字提示](https://ai.google.dev/api?hl=zh-cn#text-only-prompt)
  - [多模态提示（文本和图片）](https://ai.google.dev/api?hl=zh-cn#multimodal-prompt)
  - [多轮对话（聊天）](https://ai.google.dev/api?hl=zh-cn#multi-turn-conversations)
  - [要点总结](https://ai.google.dev/api?hl=zh-cn#key-takeaways)
- [响应示例](https://ai.google.dev/api?hl=zh-cn#response-examples)
  - [纯文本回答](https://ai.google.dev/api?hl=zh-cn#text-only-response)
- [Live API (BidiGenerateContent) WebSocket API](https://ai.google.dev/api?hl=zh-cn#live-api)
- [专业模型](https://ai.google.dev/api?hl=zh-cn#specialized-models)
- [平台 API](https://ai.google.dev/api?hl=zh-cn#platform-apis)
- [后续步骤](https://ai.google.dev/api?hl=zh-cn#whats-next)


Gemini 3.1 Flash-Lite 预览版现已推出。 [在 AI Studio 中试用](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=zh-cn)。




- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [API 参考](https://ai.google.dev/api?hl=zh-cn)



 发送反馈



# Gemini API reference

- 本页内容
- [主要端点](https://ai.google.dev/api?hl=zh-cn#primary-endpoints)
- [身份验证](https://ai.google.dev/api?hl=zh-cn#authentication)
- [内容生成](https://ai.google.dev/api?hl=zh-cn#content-generation)
  - [请求正文结构](https://ai.google.dev/api?hl=zh-cn#request-body-structure)
  - [响应正文结构](https://ai.google.dev/api?hl=zh-cn#response-body-structure)
- [请求示例](https://ai.google.dev/api?hl=zh-cn#request-examples)
  - [纯文字提示](https://ai.google.dev/api?hl=zh-cn#text-only-prompt)
  - [多模态提示（文本和图片）](https://ai.google.dev/api?hl=zh-cn#multimodal-prompt)
  - [多轮对话（聊天）](https://ai.google.dev/api?hl=zh-cn#multi-turn-conversations)
  - [要点总结](https://ai.google.dev/api?hl=zh-cn#key-takeaways)
- [响应示例](https://ai.google.dev/api?hl=zh-cn#response-examples)
  - [纯文本回答](https://ai.google.dev/api?hl=zh-cn#text-only-response)
- [Live API (BidiGenerateContent) WebSocket API](https://ai.google.dev/api?hl=zh-cn#live-api)
- [专业模型](https://ai.google.dev/api?hl=zh-cn#specialized-models)
- [平台 API](https://ai.google.dev/api?hl=zh-cn#platform-apis)
- [后续步骤](https://ai.google.dev/api?hl=zh-cn#whats-next)

此 API 参考文档介绍了可用于与 Gemini 模型互动的标准 API、流式 API 和实时 API。您可以在任何支持 HTTP 请求的环境中使用 REST API。如需了解如何开始发出第一个 API 调用，请参阅 [快速入门指南](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn)。如果您要查找特定语言的库和 SDK 的参考信息，请在左侧导航栏中的 **SDK 参考** 下找到相应语言的链接。

## 主要端点

Gemini API 围绕以下主要端点进行组织：

- **标准内容生成 ( [`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-cn#method:-models.generatecontent))**：一种标准 REST 端点，用于处理您的请求，并在单个软件包中返回模型的完整回答。此方法最适合非互动任务，您可以等待整个结果。
- **流式内容生成 ( [`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=zh-cn#method:-models.streamgeneratecontent))**：使用服务器发送的事件 (SSE) 在生成回答块时将其推送给您。这可为聊天机器人等应用提供更快、更具互动性的体验。
- **Live API ( [`BidiGenerateContent`](https://ai.google.dev/api/live?hl=zh-cn#send-messages))**：一种基于 WebSocket 的有状态 API，用于双向流式传输，专为实时对话使用情形而设计。
- **批量模式 ( [`batchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=zh-cn))**：用于提交批量 `generateContent` 请求的标准 REST 端点。
- **嵌入 ( [`embedContent`](https://ai.google.dev/api/embeddings?hl=zh-cn))**：一种标准 REST 端点，可根据输入 `Content` 生成文本嵌入向量。
- **Gen Media API**：用于通过我们的专用模型（例如用于生成图片的 [Imagen](https://ai.google.dev/api/models?hl=zh-cn#method:-models.predict) 和用于生成视频的 [Veo](https://ai.google.dev/api/models?hl=zh-cn#method:-models.predictlongrunning)）生成媒体的端点。
Gemini 还内置了这些功能，您可以使用 `generateContent` API 访问这些功能。
- **平台 API**：支持核心功能的实用程序端点，例如 [上传文件](https://ai.google.dev/api/files?hl=zh-cn) 和 [计算 token](https://ai.google.dev/api/tokens?hl=zh-cn)。

## 身份验证

对 Gemini API 的所有请求都必须包含带有 API 密钥的 `x-goog-api-key` 标头。您可以在 [Google AI Studio](https://aistudio.google.com/app/apikey?hl=zh-cn) 中点击几下即可创建一个。

以下示例请求在标头中包含 API 密钥：

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

如需了解如何使用 Gemini SDK 将密钥传递给 API，请参阅 [使用 Gemini API 密钥](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn) 指南。

## 内容生成

这是向模型发送提示的中心端点。有两个用于生成内容的端点，主要区别在于您接收响应的方式：

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-cn#method:-models.generatecontent) (REST)**：接收请求，并在模型完成整个生成过程后提供单个回答。
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=zh-cn#method:-models.streamgeneratecontent) (SSE)**：接收完全相同的请求，但模型会以流式传输方式返回生成的回答块。这可为互动式应用提供更好的用户体验，因为您可以立即显示部分结果。

### 请求正文结构

[请求正文](https://ai.google.dev/api/generate-content?hl=zh-cn#request-body) 是一个 JSON 对象，在标准模式和流式模式下 **完全相同**，由几个核心对象构建而成：

- [`Content`](https://ai.google.dev/api/caching?hl=zh-cn#Content) 对象：表示对话中的单个回合。
- [`Part`](https://ai.google.dev/api/caching?hl=zh-cn#Part) 对象：`Content` 回合中的一段数据（例如文本或图片）。
- `inline_data` ( [`Blob`](https://ai.google.dev/api/caching?hl=zh-cn#Blob))：用于存储原始媒体字节及其 MIME 类型的容器。

在最高层级，请求正文包含一个 `contents` 对象，该对象是一个 `Content` 对象列表，每个对象都表示对话中的一个轮次。在大多数情况下，对于基本文本生成，您将使用单个 `Content` 对象，但如果您想保留对话历史记录，可以使用多个 `Content` 对象。

以下示例展示了一个典型的 `generateContent` 请求正文：

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

### 响应正文结构

无论是流式模式还是标准模式， [响应正文](https://ai.google.dev/api/generate-content?hl=zh-cn#response-body) 都类似，但以下方面除外：

- 标准模式：响应正文包含一个 [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=zh-cn#v1beta.GenerateContentResponse) 实例。
- 流式传输模式：响应正文包含 [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=zh-cn#v1beta.GenerateContentResponse) 实例数据流。

从总体上讲，响应正文包含一个 `candidates` 对象，该对象是 `Candidate` 对象的列表。`Candidate` 对象包含一个 `Content` 对象，该对象具有模型返回的生成响应。

## 请求示例

以下示例展示了这些组件如何针对不同类型的请求协同工作。

### 纯文字提示

简单的文本提示由包含单个 `Content` 对象的 `contents` 数组组成。相应对象的 `parts` 数组又包含一个带有 `text` 字段的 `Part` 对象。

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

### 多模态提示（文本和图片）

如需在提示中同时提供文字和图片，`parts` 数组应包含两个 `Part` 对象：一个用于文字，另一个用于图片 `inline_data`。

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

### 多轮对话（聊天）

如需构建多回合对话，您可以使用多个 `Content` 对象定义 `contents` 数组。API 会将整个历史记录用作下一个回答的上下文。每个 `Content` 对象的 `role` 应在 `user` 和 `model` 之间交替。

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

### 要点总结

- `Content` 是信封：它是消息轮次的顶级容器，无论消息来自用户还是模型。
- `Part` 实现多模态：在单个 `Content` 对象中使用多个 `Part` 对象来组合不同类型的数据（文本、图片、视频 URI 等）。
- 选择数据方法：
  - 对于直接嵌入的小型媒体（例如大多数图片），请使用带有 `inline_data` 的 `Part`。
  - 对于较大文件或您想在多个请求中重复使用的文件，请使用 File API 上传文件，并通过 `file_data` 部分引用该文件。
- 管理对话历史记录：对于使用 REST API 的聊天应用，请通过为每个回合附加 `Content` 对象来构建 `contents` 数组，并在 `"user"` 和 `"model"` 角色之间交替。如果您使用的是 SDK，请参阅 SDK 文档，了解管理对话记录的推荐方式。

## 响应示例

以下示例展示了这些组件如何针对不同类型的请求协同工作。

### 纯文本回答

默认文本回答包含一个 `candidates` 数组，其中包含一个或多个 `content` 对象，这些对象包含模型的回答。

以下是 **标准** 回答的示例：

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

以下是一系列 **流式** 响应。每个响应都包含一个 `responseId`，用于将整个响应关联起来：

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

## Live API (BidiGenerateContent) WebSocket API

Live API 提供基于 WebSocket 的有状态 API，用于双向流式传输，以实现实时流式传输用例。您可以查看 [Live API 指南](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 和 [Live API 参考文档](https://ai.google.dev/api/live?hl=zh-cn)，了解更多详情。

## 专业模型

除了 Gemini 模型系列之外，Gemini API 还为 [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=zh-cn)、 [Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-cn) 和 [嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn) 模型等专用模型提供端点。您可以在“模型”部分下查看这些指南。

## 平台 API

其余端点可实现其他功能，以便与目前所述的主要端点搭配使用。如需了解详情，请查看“指南”部分中的 [批处理模式](https://ai.google.dev/gemini-api/docs/batch-mode?hl=zh-cn) 和 [文件 API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 主题。

## 后续步骤

如果您刚刚开始使用 Gemini API，请查看以下指南，这些指南将帮助您了解 Gemini API 编程模型：

- [Gemini API 快速入门](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn)
- [Gemini 模型指南](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn)

您可能还想查看功能指南，其中介绍了不同的 Gemini API 功能并提供了代码示例：

- [文本生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn)
- [上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)
- [嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)



 发送反馈



如未另行说明，那么本页面中的内容已根据 [知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/) 获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0) 获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-02-25。


需要向我们提供更多信息？






\[\[\["易于理解","easyToUnderstand","thumb-up"\],\["解决了我的问题","solvedMyProblem","thumb-up"\],\["其他","otherUp","thumb-up"\]\],\[\["没有我需要的信息","missingTheInformationINeed","thumb-down"\],\["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"\],\["内容需要更新","outOfDate","thumb-down"\],\["翻译问题","translationIssue","thumb-down"\],\["示例/代码问题","samplesCodeIssue","thumb-down"\],\["其他","otherDown","thumb-down"\]\],\["最后更新时间 (UTC)：2026-02-25。"\],\[\],\[\]\]