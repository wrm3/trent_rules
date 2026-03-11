[メイン コンテンツにスキップ](https://ai.google.dev/gemini-api/docs?hl=ja#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=ja)](https://ai.google.dev/)

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

[API キーを取得する](https://aistudio.google.com/apikey?hl=ja) [クックブック](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=ja)

[ログイン](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dja&prompt=select_account)


Gemini 3.1 Flash-Lite プレビュー版が利用可能になりました。 [AI Studio でお試しください](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=ja)。




- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

# Gemini API

Gemini、Veo、Nano Banana などを活用して、プロンプトから本番環境への移行を最短経路で実現できます。

[Python](https://ai.google.dev/gemini-api/docs?hl=ja#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=ja#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=ja#go)[Java](https://ai.google.dev/gemini-api/docs?hl=ja#java)[C#](https://ai.google.dev/gemini-api/docs?hl=ja#c)[REST](https://ai.google.dev/gemini-api/docs?hl=ja#rest)もっと見る

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

[構築を開始する](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja)

クイックスタート ガイドに沿って、API キーを取得し、最初の API 呼び出しを数分で行います。

* * *

## 各モデルについて

[すべて表示](https://ai.google.dev/gemini-api/docs/models?hl=ja)

[auto\_awesome\\
Gemini 3.1 Pro\\
新機能\\
\\
最先端の推論に基づいて構築された、Google の最もインテリジェントなモデルであり、マルチモーダル理解において世界最高水準のモデルです。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) [spark\\
Gemini 3 Flash\\
新モデル\\
\\
大規模モデルに匹敵するパフォーマンスを、わずかな費用で実現します。](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) [spark\\
Gemini 3.1 Flash-Lite\\
新モデル\\
\\
Gemini 3 シリーズのパフォーマンスと品質を備えた、大量のコスト重視のワークホース モデル。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ja) [🍌\\
Nano Banana 2 と Nano Banana Pro\\
\\
\\
最先端の画像生成および編集モデル。](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja) [video\_library\\
Veo 3.1\\
\\
\\
最先端の動画生成モデル（ネイティブ音声付き）。](https://ai.google.dev/gemini-api/docs/video?hl=ja) [spark\\
Gemini Robotics\\
\\
\\
Gemini のエージェント機能をロボット工学に導入し、物理世界での高度な推論を可能にする視覚言語モデル（VLM）。](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ja)

## 機能を確認する

[imagesmode\\
\\
ネイティブ画像生成（Nano Banana）\\
\\
\\
Gemini 2.5 Flash Image を使用して、コンテキストを高度に認識した画像をネイティブに生成、編集できます。](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja) [article\\
\\
長いコンテキスト\\
\\
\\
Gemini モデルに数百万個のトークンを入力し、非構造化画像、動画、ドキュメントから理解を導き出します。](https://ai.google.dev/gemini-api/docs/long-context?hl=ja) [code\\
\\
構造化出力\\
\\
Gemini が JSON（自動処理に適した構造化データ形式）で応答するように制約します。](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja) [functions\\
\\
関数呼び出し\\
\\
\\
Gemini を外部の API やツールに接続して、エージェント ワークフローを構築します。](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja) [videocam\\
\\
Veo 3.1 による動画生成\\
\\
\\
Google の最先端のモデルを使用して、テキストや画像のプロンプトから高品質の動画コンテンツを作成できます。](https://ai.google.dev/gemini-api/docs/video?hl=ja) [android\_recorder\\
\\
Live API を使用した音声エージェント\\
\\
\\
Live API を使用して、リアルタイム音声アプリケーションとエージェントを構築します。](https://ai.google.dev/gemini-api/docs/live?hl=ja) [build\\
\\
ツール\\
\\
\\
Google 検索、URL コンテキスト、Google マップ、コード実行、コンピュータの使用などの組み込みツールを使用して、Gemini を世界に接続します。](https://ai.google.dev/gemini-api/docs/tools?hl=ja) [stacks\\
\\
ドキュメントの理解\\
\\
\\
最大 1,000 ページの PDF ファイルや、その他のテキストベースのファイル形式を、マルチモーダルで完全に理解して処理します。](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja) [cognition\_2\\
\\
思考\\
\\
思考能力が複雑なタスクやエージェントの推論をどのように改善するかについて説明します。](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)

[Google AI Studio\\
\\
\\
プロンプトのテスト、API キーの管理、使用状況のモニタリング、プロトタイプの作成を行います。](https://aistudio.google.com/?hl=ja) [group\\
\\
デベロッパー コミュニティ\\
\\
\\
他のデベロッパーや Google のエンジニアに質問して、解決策を見つけます。](https://discuss.ai.google.dev/c/gemini-api/4?hl=ja) [menu\_book\\
\\
API リファレンス\\
\\
\\
Gemini API の詳細については、公式リファレンス ドキュメントをご覧ください。](https://ai.google.dev/api?hl=ja) [sensors\\
\\
ステータス\\
\\
Gemini API、Google AI Studio、モデルサービスのステータスを確認します。](https://aistudio.google.com/status?hl=ja)

特に記載のない限り、このページのコンテンツは [クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/) により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0) により使用許諾されます。詳しくは、 [Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja) をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-03-03 UTC。




\[\[\["わかりやすい","easyToUnderstand","thumb-up"\],\["問題の解決に役立った","solvedMyProblem","thumb-up"\],\["その他","otherUp","thumb-up"\]\],\[\["必要な情報がない","missingTheInformationINeed","thumb-down"\],\["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"\],\["最新ではない","outOfDate","thumb-down"\],\["翻訳に関する問題","translationIssue","thumb-down"\],\["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"\],\["その他","otherDown","thumb-down"\]\],\["最終更新日 2026-03-03 UTC。"\],\[\],\[\]\]