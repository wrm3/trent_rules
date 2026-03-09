[기본 콘텐츠로 건너뛰기](https://ai.google.dev/gemini-api/docs?hl=ko#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=ko)](https://ai.google.dev/)

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

[API 키 가져오기](https://aistudio.google.com/apikey?hl=ko) [설명서](https://github.com/google-gemini/cookbook) [커뮤니티](https://discuss.ai.google.dev/c/gemini-api/?hl=ko)

[로그인](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dko&prompt=select_account)


이제 Gemini 3.1 Flash-Lite 프리뷰를 사용할 수 있습니다. [AI Studio에서 사용해 보세요](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=ko).




- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

# Gemini API

Gemini, Veo, Nano Banana 등을 사용해 프롬프트에서 프로덕션까지 가장 빠르게 도달할 수 있는 경로를 제공합니다.

[Python](https://ai.google.dev/gemini-api/docs?hl=ko#python)[자바스크립트](https://ai.google.dev/gemini-api/docs?hl=ko#%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8)[Go](https://ai.google.dev/gemini-api/docs?hl=ko#go)[Java](https://ai.google.dev/gemini-api/docs?hl=ko#java)[C#](https://ai.google.dev/gemini-api/docs?hl=ko#c)[REST](https://ai.google.dev/gemini-api/docs?hl=ko#rest)더보기

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

[레고 시작하기](https://ai.google.dev/gemini-api/docs/quickstart?hl=ko)

빠른 시작 가이드에 따라 API 키를 가져오고 몇 분 만에 첫 번째 API 호출을 실행하세요.

* * *

## 모델 살펴보기

[모두 보기](https://ai.google.dev/gemini-api/docs/models?hl=ko)

[auto\_awesome\\
Gemini 3.1 Pro\\
신규\\
\\
최첨단 추론을 기반으로 빌드된 Google의 가장 지능적인 모델로, 멀티모달 이해 능력이 세계 최고 수준입니다.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ko) [spark\\
Gemini 3 Flash\\
신규\\
\\
비용은 훨씬 적지만 더 큰 모델에 필적하는 Frontier급 성능](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ko) [spark\\
Gemini 3.1 Flash-Lite\\
신규\\
\\
Gemini 3 시리즈의 성능과 품질을 갖춘 비용에 민감한 대량의 워크호스 모델입니다.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ko) [🍌\\
Nano Banana 2 및 Nano Banana Pro\\
\\
\\
최첨단 이미지 생성 및 편집 모델](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko) [video\_library\\
Veo 3.1\\
\\
\\
네이티브 오디오를 지원하는 최첨단 동영상 생성 모델입니다.](https://ai.google.dev/gemini-api/docs/video?hl=ko) [spark\\
Gemini Robotics\\
\\
\\
Gemini의 에이전트 기능을 로봇 공학에 적용하고 실제 환경에서 고급 추론을 지원하는 비전 언어 모델 (VLM)입니다.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ko)

## 기능 살펴보기

[imagesmode\\
\\
네이티브 이미지 생성 (Nano Banana)\\
\\
\\
Gemini 2.5 Flash Image를 사용하여 컨텍스트가 풍부한 이미지를 기본적으로 생성하고 편집하세요.](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko) [article\\
\\
긴 컨텍스트\\
\\
\\
Gemini 모델에 수백만 개의 토큰을 입력하고 비구조화된 이미지, 동영상, 문서에서 이해를 도출하세요.](https://ai.google.dev/gemini-api/docs/long-context?hl=ko) [code\\
\\
구조화된 출력\\
\\
\\
Gemini가 자동 처리에 적합한 구조화된 데이터 형식인 JSON으로 응답하도록 제한합니다.](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko) [functions\\
\\
함수 호출\\
\\
\\
Gemini를 외부 API 및 도구에 연결하여 에이전트형 워크플로를 빌드합니다.](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko) [videocam\\
\\
Veo 3.1을 사용한 동영상 생성\\
\\
\\
최첨단 모델을 사용하여 텍스트 또는 이미지 프롬프트에서 고품질 동영상 콘텐츠를 만드세요.](https://ai.google.dev/gemini-api/docs/video?hl=ko) [android\_recorder\\
\\
Live API를 사용하는 음성 에이전트\\
\\
\\
Live API를 사용하여 실시간 음성 애플리케이션과 에이전트를 빌드하세요.](https://ai.google.dev/gemini-api/docs/live?hl=ko) [build\\
\\
도구\\
\\
\\
Google 검색, URL 컨텍스트, Google 지도, 코드 실행, 컴퓨터 사용과 같은 기본 제공 도구를 통해 Gemini를 세상에 연결하세요.](https://ai.google.dev/gemini-api/docs/tools?hl=ko) [stacks\\
\\
문서 이해\\
\\
\\
최대 1,000페이지의 PDF 파일(멀티모달 이해 기능 지원) 또는 기타 텍스트 기반 파일 형식을 처리합니다.](https://ai.google.dev/gemini-api/docs/document-processing?hl=ko) [cognition\_2\\
\\
사고 모델\\
\\
\\
사고 능력이 복잡한 작업과 에이전트의 추론을 어떻게 개선하는지 알아봅니다.](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)

[Google AI Studio\\
\\
\\
프롬프트를 테스트하고, API 키를 관리하고, 사용량을 모니터링하고, 프로토타입을 빌드하세요.](https://aistudio.google.com/?hl=ko) [group\\
\\
개발자 커뮤니티\\
\\
\\
다른 개발자 및 Google 엔지니어에게 질문하고 솔루션을 찾아보세요.](https://discuss.ai.google.dev/c/gemini-api/4?hl=ko) [menu\_book\\
\\
API 참조\\
\\
\\
공식 참조 문서에서 Gemini API에 관한 자세한 정보를 확인하세요.](https://ai.google.dev/api?hl=ko) [sensors\\
\\
상태\\
\\
\\
Gemini API, Google AI Studio, 모델 서비스의 상태를 확인하세요.](https://aistudio.google.com/status?hl=ko)

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/) 에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0) 에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko) 을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-03-03(UTC)




\[\[\["이해하기 쉬움","easyToUnderstand","thumb-up"\],\["문제가 해결됨","solvedMyProblem","thumb-up"\],\["기타","otherUp","thumb-up"\]\],\[\["필요한 정보가 없음","missingTheInformationINeed","thumb-down"\],\["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"\],\["오래됨","outOfDate","thumb-down"\],\["번역 문제","translationIssue","thumb-down"\],\["샘플/코드 문제","samplesCodeIssue","thumb-down"\],\["기타","otherDown","thumb-down"\]\],\["최종 업데이트: 2026-03-03(UTC)"\],\[\],\[\]\]