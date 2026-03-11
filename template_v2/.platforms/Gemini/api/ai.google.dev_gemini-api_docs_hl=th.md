[ข้ามไปที่เนื้อหาหลัก](https://ai.google.dev/gemini-api/docs?hl=th#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=th)](https://ai.google.dev/)

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

[รับคีย์ API](https://aistudio.google.com/apikey?hl=th) [ตำราอาหาร](https://github.com/google-gemini/cookbook) [ชุมชน](https://discuss.ai.google.dev/c/gemini-api/?hl=th)

[ลงชื่อเข้าใช้](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dth&prompt=select_account)


ตอนนี้ Gemini 3.1 Flash-Lite (เวอร์ชันตัวอย่าง) พร้อมให้บริการแล้ว [ลองใช้ใน AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=th)

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

# Gemini API

เส้นทางที่เร็วที่สุดจากพรอมต์ไปสู่การผลิตด้วย Gemini, Veo, Nano Banana และอื่นๆ

[Python](https://ai.google.dev/gemini-api/docs?hl=th#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=th#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=th#go)[Java](https://ai.google.dev/gemini-api/docs?hl=th#java)[C#](https://ai.google.dev/gemini-api/docs?hl=th#c)[REST](https://ai.google.dev/gemini-api/docs?hl=th#rest)เพิ่มเติม

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

[เริ่มสร้าง](https://ai.google.dev/gemini-api/docs/quickstart?hl=th)

ทำตามคำแนะนำในการเริ่มต้นใช้งานอย่างรวดเร็วเพื่อรับคีย์ API และทำการเรียก API ครั้งแรกได้ในไม่กี่นาที

* * *

## พบกับโมเดล

[ดูทั้งหมด](https://ai.google.dev/gemini-api/docs/models?hl=th)

[auto\_awesome\\
Gemini 3.1 Pro\\
ใหม่\\
\\
โมเดลที่ชาญฉลาดที่สุดของเรา ซึ่งเป็นโมเดลที่ดีที่สุดในโลกสำหรับการทำความเข้าใจข้อมูลหลายรูปแบบ โดยทั้งหมดสร้างขึ้นบนพื้นฐานของการให้เหตุผลที่ล้ำสมัย](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) [spark\\
Gemini 3 Flash\\
ใหม่\\
\\
ประสิทธิภาพระดับแนวหน้าเทียบเท่าโมเดลขนาดใหญ่กว่าในราคาที่ถูกกว่า](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) [spark\\
Gemini 3.1 Flash-Lite\\
ใหม่\\
\\
โมเดลที่ใช้งานหนักและคำนึงถึงต้นทุนที่มีประสิทธิภาพและคุณภาพของซีรีส์ Gemini 3](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=th) [🍌\\
Nano Banana 2 และ Nano Banana Pro\\
\\
\\
โมเดลการสร้างและแก้ไขรูปภาพที่ล้ำสมัย](https://ai.google.dev/gemini-api/docs/image-generation?hl=th) [video\_library\\
Veo 3.1\\
\\
\\
โมเดลการสร้างวิดีโอสุดล้ำของเราพร้อมเสียงแบบเนทีฟ](https://ai.google.dev/gemini-api/docs/video?hl=th) [spark\\
Gemini Robotics\\
\\
\\
โมเดลภาษาภาพ (VLM) ที่นำความสามารถแบบเป็น Agent ของ Gemini มาใช้กับหุ่นยนต์และช่วยให้การให้เหตุผลขั้นสูงในโลกกายภาพเป็นไปได้](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th)

## สำรวจความสามารถ

[imagesmode\\
\\
การสร้างรูปภาพในตัว (Nano Banana)\\
\\
\\
สร้างและแก้ไขรูปภาพที่มีบริบทสูงได้โดยตรงด้วย Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=th) [article\\
\\
บริบทแบบยาว\\
\\
\\
ป้อนโทเค็นหลายล้านรายการลงในโมเดล Gemini และรับความเข้าใจจากรูปภาพ วิดีโอ และเอกสารที่ไม่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/long-context?hl=th) [code\\
\\
เอาต์พุตที่มีโครงสร้าง\\
\\
\\
จำกัดให้ Gemini ตอบกลับด้วย JSON ซึ่งเป็นรูปแบบข้อมูลที่มีโครงสร้างที่เหมาะสำหรับการประมวลผลอัตโนมัติ](https://ai.google.dev/gemini-api/docs/structured-output?hl=th) [functions\\
\\
การเรียกใช้ฟังก์ชัน\\
\\
\\
สร้างเวิร์กโฟลว์แบบเอเจนต์โดยเชื่อมต่อ Gemini กับ API และเครื่องมือภายนอก](https://ai.google.dev/gemini-api/docs/function-calling?hl=th) [videocam\\
\\
การสร้างวิดีโอด้วย Veo 3.1\\
\\
\\
สร้างเนื้อหาวิดีโอคุณภาพสูงจากพรอมต์ข้อความหรือรูปภาพด้วยโมเดลสุดล้ำของเรา](https://ai.google.dev/gemini-api/docs/video?hl=th) [android\_recorder\\
\\
เอเจนต์เสียงที่มี Live API\\
\\
\\
สร้างแอปพลิเคชันและเอเจนต์เสียงแบบเรียลไทม์ด้วย Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) [build\\
\\
เครื่องมือ\\
\\
\\
เชื่อมต่อ Gemini กับโลกภายนอกผ่านเครื่องมือในตัว เช่น Google Search, บริบท URL, Google Maps, การเรียกใช้โค้ด และการใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/tools?hl=th) [stacks\\
\\
การทำความเข้าใจเอกสาร\\
\\
\\
ประมวลผลไฟล์ PDF ได้สูงสุด 1,000 หน้าโดยมีความเข้าใจแบบมัลติโมดัลอย่างเต็มรูปแบบหรือไฟล์ประเภทอื่นๆ ที่เป็นข้อความ](https://ai.google.dev/gemini-api/docs/document-processing?hl=th) [cognition\_2\\
\\
กำลังคิด\\
\\
\\
ดูว่าความสามารถในการคิดช่วยปรับปรุงการให้เหตุผลสำหรับงานและเอเจนต์ที่ซับซ้อนได้อย่างไร](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

[Google AI Studio\\
\\
\\
ทดสอบพรอมต์ จัดการคีย์ API ตรวจสอบการใช้งาน และสร้างต้นแบบ](https://aistudio.google.com/?hl=th) [group\\
\\
ชุมชนนักพัฒนาแอป\\
\\
\\
ถามคำถามและค้นหาโซลูชันจากนักพัฒนาแอปคนอื่นๆ และวิศวกรของ Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=th) [menu\_book\\
\\
เอกสารอ้างอิง API\\
\\
\\
ดูข้อมูลโดยละเอียดเกี่ยวกับ Gemini API ได้ในเอกสารอ้างอิงอย่างเป็นทางการ](https://ai.google.dev/api?hl=th) [sensors\\
\\
สถานะ\\
\\
\\
ตรวจสอบสถานะของ Gemini API, Google AI Studio และบริการโมเดลของเรา](https://aistudio.google.com/status?hl=th)

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้ [ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้ [ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่ [นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-03-03 UTC




\[\[\["เข้าใจง่าย","easyToUnderstand","thumb-up"\],\["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"\],\["อื่นๆ","otherUp","thumb-up"\]\],\[\["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"\],\["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"\],\["ล้าสมัย","outOfDate","thumb-down"\],\["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"\],\["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"\],\["อื่นๆ","otherDown","thumb-down"\]\],\["อัปเดตล่าสุด 2026-03-03 UTC"\],\[\],\[\]\]