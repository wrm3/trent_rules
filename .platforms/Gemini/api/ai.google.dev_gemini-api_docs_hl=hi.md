[सीधे मुख्य कॉन्टेंट पर जाएं](https://ai.google.dev/gemini-api/docs?hl=hi#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=hi)](https://ai.google.dev/)

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

[एपीआई पासकोड पाना](https://aistudio.google.com/apikey?hl=hi) [कुकबुक](https://github.com/google-gemini/cookbook) [कम्यूनिटी](https://discuss.ai.google.dev/c/gemini-api/?hl=hi)

[प्रवेश करें](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dhi&prompt=select_account)


Gemini 3.1 Flash-Lite की झलक अब उपलब्ध है. [इसे AI Studio में आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=hi).




- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

# Gemini API

Gemini, Veo, Nano Banana वगैरह की मदद से, प्रॉम्प्ट से लेकर प्रोडक्शन तक का सबसे तेज़ तरीका.

[Python](https://ai.google.dev/gemini-api/docs?hl=hi#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=hi#javascript)[ऐप पर जाएं](https://ai.google.dev/gemini-api/docs?hl=hi#%E0%A4%90%E0%A4%AA-%E0%A4%AA%E0%A4%B0-%E0%A4%9C%E0%A4%BE%E0%A4%8F%E0%A4%82)[Java](https://ai.google.dev/gemini-api/docs?hl=hi#java)[C#](https://ai.google.dev/gemini-api/docs?hl=hi#c)[REST](https://ai.google.dev/gemini-api/docs?hl=hi#rest)ज़्यादा

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

[बनाना शुरू करें](https://ai.google.dev/gemini-api/docs/quickstart?hl=hi)

एपीआई पासकोड पाने और कुछ ही मिनटों में अपना पहला एपीआई कॉल करने के लिए, हमारी क्विकस्टार्ट गाइड देखें.

* * *

## मॉडल के बारे में जानकारी

[सभी देखें](https://ai.google.dev/gemini-api/docs/models?hl=hi)

[auto\_awesome\\
Gemini 3.1 Pro\\
नया\\
\\
यह हमारा सबसे ऐडवांस मॉडल है. यह मल्टीमॉडल कॉन्टेंट को समझने के लिए, दुनिया का सबसे बेहतरीन मॉडल है. इसे बेहतरीन लॉजिक के साथ बनाया गया है.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) [spark\\
Gemini 3 Flash\\
नया\\
\\
यह फ़्रंटियर क्लास की परफ़ॉर्मेंस देता है. इसकी परफ़ॉर्मेंस, बड़े मॉडल के बराबर होती है, लेकिन इसकी लागत कम होती है.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) [spark\\
Gemini 3.1 Flash-Lite\\
नया\\
\\
यह मॉडल, Gemini 3 सीरीज़ की परफ़ॉर्मेंस और क्वालिटी के साथ, ज़्यादा वॉल्यूम वाले और कम लागत वाले काम के लिए उपलब्ध है.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=hi) [🍌\\
Nano Banana 2 और Nano Banana Pro\\
\\
\\
इमेज जनरेट करने और उनमें बदलाव करने वाले बेहतरीन मॉडल.](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) [video\_library\\
Veo 3.1\\
\\
\\
वीडियो जनरेट करने वाला हमारा बेहतरीन मॉडल, जिसमें ऑडियो जनरेट करने की सुविधा भी है.](https://ai.google.dev/gemini-api/docs/video?hl=hi) [spark\\
Gemini Robotics\\
\\
\\
यह विज़न-लैंग्वेज मॉडल (वीएलएम) है. यह रोबोटिक्स में Gemini की एजेंटिक क्षमताओं को शामिल करता है. साथ ही, यह फ़िज़िकल दुनिया में ऐडवांस लेवल की रीज़निंग को बेहतर बनाता है.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=hi)

## सुविधाओं के बारे में जानें

[imagesmode\\
\\
नेटिव इमेज जनरेशन (Nano Banana)\\
\\
\\
Gemini 2.5 Flash Image की मदद से, इमेज जनरेट करें और उनमें बदलाव करें. यह इमेज, कॉन्टेक्स्ट के हिसाब से सटीक होती हैं.](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) [article\\
\\
ज़्यादा कॉन्टेक्स्ट वाली विंडो\\
\\
\\
Gemini मॉडल में लाखों टोकन इनपुट करें. साथ ही, बिना किसी स्ट्रक्चर वाली इमेज, वीडियो, और दस्तावेज़ों को समझें.](https://ai.google.dev/gemini-api/docs/long-context?hl=hi) [code\\
\\
स्ट्रक्चर्ड आउटपुट\\
\\
\\
Gemini को सिर्फ़ JSON फ़ॉर्मैट में जवाब देने के लिए कहा गया है. यह स्ट्रक्चर्ड डेटा फ़ॉर्मैट, अपने-आप प्रोसेस होने के लिए सही है.](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) [functions\\
\\
फ़ंक्शन कॉल करने की सुविधा\\
\\
\\
Gemini को बाहरी एपीआई और टूल से कनेक्ट करके, एजेंटिक वर्कफ़्लो बनाएं.](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) [videocam\\
\\
Veo 3.1 की मदद से वीडियो जनरेट करना\\
\\
\\
टेक्स्ट या इमेज प्रॉम्प्ट से अच्छी क्वालिटी वाला वीडियो कॉन्टेंट जनरेट करें. इसके लिए, हमारे बेहतरीन मॉडल का इस्तेमाल करें.](https://ai.google.dev/gemini-api/docs/video?hl=hi) [android\_recorder\\
\\
Live API की सुविधा वाले वॉइस एजेंट\\
\\
\\
लाइव एपीआई की मदद से, रीयल-टाइम में काम करने वाले वॉइस ऐप्लिकेशन और एजेंट बनाएं.](https://ai.google.dev/gemini-api/docs/live?hl=hi) [build\\
\\
टूल\\
\\
\\
Gemini को दुनिया से कनेक्ट करने के लिए, Google Search, यूआरएल कॉन्टेक्स्ट, Google Maps, कोड एक्ज़ीक्यूशन, और कंप्यूटर इस्तेमाल करने जैसे बिल्ट-इन टूल का इस्तेमाल करें.](https://ai.google.dev/gemini-api/docs/tools?hl=hi) [stacks\\
\\
दस्तावेज़ को समझना\\
\\
\\
मल्टीमॉडल की पूरी जानकारी या टेक्स्ट पर आधारित अन्य फ़ाइल टाइप के साथ, 1,000 पेजों तक की PDF फ़ाइलों को प्रोसेस करें.](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi) [cognition\_2\\
\\
सूझ-बूझ वाला मॉडल\\
\\
\\
जानें कि सोचने की क्षमता, मुश्किल कामों और एजेंट के लिए तर्क को कैसे बेहतर बनाती है.](https://ai.google.dev/gemini-api/docs/thinking?hl=hi)

[Google AI Studio\\
\\
\\
प्रॉम्प्ट की जांच करें, एपीआई कुंजियां मैनेज करें, इस्तेमाल को मॉनिटर करें, और प्रोटोटाइप बनाएं.](https://aistudio.google.com/?hl=hi) [group\\
\\
डेवलपर कम्यूनिटी\\
\\
\\
अन्य डेवलपर और Google इंजीनियर से सवाल पूछें और समाधान पाएं.](https://discuss.ai.google.dev/c/gemini-api/4?hl=hi) [menu\_book\\
\\
एपीआई का संदर्भ\\
\\
\\
आधिकारिक रेफ़रंस दस्तावेज़ में, Gemini API के बारे में ज़्यादा जानकारी पाएं.](https://ai.google.dev/api?hl=hi) [sensors\\
\\
स्थिति\\
\\
\\
Gemini API, Google AI Studio, और हमारी मॉडल सेवाओं की स्थिति देखें.](https://aistudio.google.com/status?hl=hi)

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-03-03 (UTC) को अपडेट किया गया.




\[\[\["समझने में आसान है","easyToUnderstand","thumb-up"\],\["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"\],\["अन्य","otherUp","thumb-up"\]\],\[\["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"\],\["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"\],\["पुराना","outOfDate","thumb-down"\],\["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"\],\["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"\],\["अन्य","otherDown","thumb-down"\]\],\["आखिरी बार 2026-03-03 (UTC) को अपडेट किया गया."\],\[\],\[\]\]