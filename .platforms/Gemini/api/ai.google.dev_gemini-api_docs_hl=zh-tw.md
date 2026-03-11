[跳至主要內容](https://ai.google.dev/gemini-api/docs?hl=zh-tw#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=zh-tw)](https://ai.google.dev/)

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

[取得 API 金鑰](https://aistudio.google.com/apikey?hl=zh-tw) [教戰手冊](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=zh-tw)

[登入](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dzh-tw&prompt=select_account)


Gemini 3.1 Flash-Lite 預先發布版現已推出。 [在 AI Studio 中試用](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=zh-tw)。




- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

# Gemini API

透過 Gemini、Veo、Nano Banana 等工具，從提示到製作完成，以最快速度完成工作。

[Python](https://ai.google.dev/gemini-api/docs?hl=zh-tw#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=zh-tw#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=zh-tw#go)[Java](https://ai.google.dev/gemini-api/docs?hl=zh-tw#java)[C#](https://ai.google.dev/gemini-api/docs?hl=zh-tw#c)[REST](https://ai.google.dev/gemini-api/docs?hl=zh-tw#rest)更多選項

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

[開始建構](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-tw)

按照快速入門指南操作，幾分鐘內即可取得 API 金鑰並發出第一個 API 呼叫。

* * *

## 認識各個模型

[查看全部](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)

[auto\_awesome\\
Gemini 3.1 Pro\\
新推出\\
\\
這是 Google 最聰明的模型，也是全球最出色的多模態理解模型，一切都建立在最先進的推論技術基礎。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) [spark\\
Gemini 3 Flash\\
新推出\\
\\
以一小部分的成本，達到與大型模型匹敵的頂尖效能。](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) [spark\\
Gemini 3.1 Flash-Lite\\
新\\
\\
這款模型適用於高資料量且預算有限的工作，效能和品質與 Gemini 3 系列模型不相上下。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-tw) [🍌\\
Nano Banana 2 和 Nano Banana Pro\\
\\
\\
最先進的圖像生成及編輯模型。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) [video\_library\\
Veo 3.1\\
\\
\\
Google 最先進的影片生成模型，支援原生音訊。](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw) [spark\\
Gemini Robotics\\
\\
\\
這項技術是視覺語言模型 (VLM)，可將 Gemini 的代理功能帶入機器人領域，並在實體世界中進行進階推理。](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-tw)

## 探索各種功能

[imagesmode\\
\\
原生圖像生成功能 (Nano Banana)\\
\\
\\
使用 Gemini 2.5 Flash Image 生成及編輯高度符合情境的圖片。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) [article\\
\\
長篇脈絡資訊\\
\\
\\
將數百萬個權杖輸入 Gemini 模型，從非結構化圖片、影片和文件中取得資訊。](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw) [code\\
\\
結構化輸出內容\\
\\
\\
限制 Gemini 只能以 JSON 回覆，這是一種適合自動處理的結構化資料格式。](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw) [functions\\
\\
函式呼叫\\
\\
\\
將 Gemini 連結至外部 API 和工具，建構代理工作流程。](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw) [videocam\\
\\
使用 Veo 3.1 生成影片\\
\\
\\
使用最先進的模型，根據文字或圖片提示生成高品質影片內容。](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw) [android\_recorder\\
\\
使用 Live API 的語音代理程式\\
\\
\\
使用 Live API 建構即時語音應用程式和代理程式。](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw) [build\\
\\
工具\\
\\
\\
透過 Google 搜尋、網址內容、Google 地圖、程式碼執行和電腦使用等內建工具，讓 Gemini 連結到世界。](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw) [stacks\\
\\
文件解讀\\
\\
\\
處理最多 1000 頁的 PDF 檔案，並充分理解多模態內容或其他文字型檔案。](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw) [cognition\_2\\
\\
思考\\
\\
\\
瞭解思考能力如何提升複雜工作和代理程式的推理能力。](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)

[Google AI Studio\\
\\
\\
測試提示、管理 API 金鑰、監控用量及建構原型。](https://aistudio.google.com/?hl=zh-tw) [group\\
\\
開發人員社群\\
\\
\\
向其他開發人員和 Google 工程師提問，並尋求解決方案。](https://discuss.ai.google.dev/c/gemini-api/4?hl=zh-tw) [menu\_book\\
\\
API 參考資料\\
\\
\\
如要進一步瞭解 Gemini API，請參閱官方參考說明文件。](https://ai.google.dev/api?hl=zh-tw) [sensors\\
\\
狀態\\
\\
\\
查看 Gemini API、Google AI Studio 和模型服務的狀態。](https://aistudio.google.com/status?hl=zh-tw)

除非另有註明，否則本頁面中的內容是採用 [創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為 [阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《 [Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-03-03 (世界標準時間)。




\[\[\["容易理解","easyToUnderstand","thumb-up"\],\["確實解決了我的問題","solvedMyProblem","thumb-up"\],\["其他","otherUp","thumb-up"\]\],\[\["缺少我需要的資訊","missingTheInformationINeed","thumb-down"\],\["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"\],\["過時","outOfDate","thumb-down"\],\["翻譯問題","translationIssue","thumb-down"\],\["示例/程式碼問題","samplesCodeIssue","thumb-down"\],\["其他","otherDown","thumb-down"\]\],\["上次更新時間：2026-03-03 (世界標準時間)。"\],\[\],\[\]\]