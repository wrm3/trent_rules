[跳至主要内容](https://ai.google.dev/gemini-api/docs?hl=zh-cn#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=zh-cn)](https://ai.google.dev/)

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

[获取 API 密钥](https://aistudio.google.com/apikey?hl=zh-cn) [实战宝典](https://github.com/google-gemini/cookbook) [社区](https://discuss.ai.google.dev/c/gemini-api/?hl=zh-cn)

[登录](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dzh-cn&prompt=select_account)


Gemini 3.1 Flash-Lite 预览版现已推出。 [在 AI Studio 中试用](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=zh-cn)。




- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

# Gemini API

借助 Gemini、Veo、Nano Banana 等工具，快速将提示转化为可供使用的内容。

[Python](https://ai.google.dev/gemini-api/docs?hl=zh-cn#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=zh-cn#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=zh-cn#go)[Java](https://ai.google.dev/gemini-api/docs?hl=zh-cn#java)[C#](https://ai.google.dev/gemini-api/docs?hl=zh-cn#c)[REST](https://ai.google.dev/gemini-api/docs?hl=zh-cn#rest)更多

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

[开始构建](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn)

按照我们的快速入门指南操作，您只需几分钟即可获取 API 密钥并发出第一个 API 调用。

* * *

## 认识这些模型

[查看全部](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)

[auto\_awesome\\
Gemini 3.1 Pro\\
新\\
\\
我们最智能的模型，也是全球领先的多模态理解模型，建立在先进的推理技术基础上。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) [spark\\
Gemini 3 Flash\\
新\\
\\
以更低的成本实现可与大型模型相媲美的 Frontier 级性能。](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) [spark\\
Gemini 3.1 Flash-Lite\\
新\\
\\
一款高体量、成本敏感型实用模型，具有 Gemini 3 系列的性能和质量。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-cn) [🍌\\
Nano Banana 2 和 Nano Banana Pro\\
\\
\\
先进的图片生成和编辑模型。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn) [video\_library\\
Veo 3.1\\
\\
\\
我们最先进的视频生成模型，支持原生音频。](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn) [spark\\
Gemini Robotics\\
\\
\\
一种视觉-语言模型 (VLM)，可将 Gemini 的智能体功能引入机器人技术，并在物理世界中实现高级推理。](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-cn)

## 探索功能

[imagesmode\\
\\
原生图片生成 (Nano Banana)\\
\\
\\
使用 Gemini 2.5 Flash Image 以原生方式生成和编辑高度情境化的图片。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn) [article\\
\\
长上下文\\
\\
\\
向 Gemini 模型输入数百万个 token，并从非结构化图片、视频和文档中获取理解。](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-cn) [code\\
\\
结构化输出\\
\\
\\
限制 Gemini 以 JSON（一种适合自动处理的结构化数据格式）进行回答。](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn) [functions\\
\\
函数调用\\
\\
\\
通过将 Gemini 连接到外部 API 和工具来构建智能体工作流。](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn) [videocam\\
\\
使用 Veo 3.1 生成视频\\
\\
\\
使用我们最先进的模型，根据文本或图片提示创作高品质视频内容。](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn) [android\_recorder\\
\\
使用 Live API 的语音代理\\
\\
\\
使用 Live API 构建实时语音应用和代理。](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) [build\\
\\
工具\\
\\
\\
通过 Google 搜索、网址上下文、Google 地图、代码执行和电脑使用等内置工具，将 Gemini 与世界连接起来。](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn) [stacks\\
\\
文档理解\\
\\
\\
处理最多 1,000 页的 PDF 文件，并具备全面的多模态理解能力，或处理其他基于文本的文件类型。](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn) [cognition\_2\\
\\
思考\\
\\
\\
了解思维能力如何提高复杂任务和代理的推理能力。](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)

[Google AI Studio\\
\\
\\
测试提示、管理 API 密钥、监控用量和构建原型。](https://aistudio.google.com/?hl=zh-cn) [group\\
\\
开发者社区\\
\\
\\
向其他开发者和 Google 工程师提问并寻求解决方案。](https://discuss.ai.google.dev/c/gemini-api/4?hl=zh-cn) [menu\_book\\
\\
API 参考文档\\
\\
\\
如需详细了解 Gemini API，请参阅官方参考文档。](https://ai.google.dev/api?hl=zh-cn) [sensors\\
\\
状态\\
\\
\\
查看 Gemini API、Google AI Studio 和我们的模型服务的状态。](https://aistudio.google.com/status?hl=zh-cn)

如未另行说明，那么本页面中的内容已根据 [知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/) 获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0) 获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-03-03。




\[\[\["易于理解","easyToUnderstand","thumb-up"\],\["解决了我的问题","solvedMyProblem","thumb-up"\],\["其他","otherUp","thumb-up"\]\],\[\["没有我需要的信息","missingTheInformationINeed","thumb-down"\],\["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"\],\["内容需要更新","outOfDate","thumb-down"\],\["翻译问题","translationIssue","thumb-down"\],\["示例/代码问题","samplesCodeIssue","thumb-down"\],\["其他","otherDown","thumb-down"\]\],\["最后更新时间 (UTC)：2026-03-03。"\],\[\],\[\]\]