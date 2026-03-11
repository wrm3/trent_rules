[التخطّي إلى المحتوى الرئيسي](https://ai.google.dev/gemini-api/docs?hl=ar#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=ar)](https://ai.google.dev/)

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

[الحصول على مفتاح واجهة برمجة التطبيقات](https://aistudio.google.com/apikey?hl=ar) [كتاب الطبخ](https://github.com/google-gemini/cookbook) [منتدى](https://discuss.ai.google.dev/c/gemini-api/?hl=ar)

[تسجيل الدخول](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dar&prompt=select_account)


أصبحت الآن معاينة Gemini 3.1 Flash-Lite متاحة. [تجربة الميزة في AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=ar)

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

# Gemini API

أسرع طريقة للانتقال من الطلب إلى الإنتاج باستخدام Gemini وVeo وNano Banana وغير ذلك

[Python](https://ai.google.dev/gemini-api/docs?hl=ar#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=ar#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=ar#go)[جافا](https://ai.google.dev/gemini-api/docs?hl=ar#%D8%AC%D8%A7%D9%81%D8%A7)[#C](https://ai.google.dev/gemini-api/docs?hl=ar#c)[REST](https://ai.google.dev/gemini-api/docs?hl=ar#rest)المزيد

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

[بدء التركيب](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar)

اتّبِع دليل البدء السريع للحصول على مفتاح واجهة برمجة تطبيقات وإجراء طلبك الأول لواجهة برمجة التطبيقات في دقائق.

* * *

## التعرّف على النماذج

[عرض الكل](https://ai.google.dev/gemini-api/docs/models?hl=ar)

[auto\_awesome\\
‫Gemini 3.1 Pro\\
جديد\\
\\
نموذجنا الأكثر ذكاءً، وهو الأفضل في العالم لفهم المحتوى المتعدد الوسائط، وكل ذلك استنادًا إلى إمكانات استدلالية متطوّرة.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) [spark\\
‫Gemini 3 Flash\\
جديد\\
\\
أداء فائق يضاهي النماذج الأكبر حجمًا بجزء بسيط من التكلفة](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) [spark\\
Gemini 3.1 Flash-Lite\\
جديد\\
\\
نموذج قوي وفعّال من حيث التكلفة ومناسب للأحجام الكبيرة، ويقدّم الأداء والجودة نفسها التي تقدّمها سلسلة Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ar) [🍌\\
‫Nano Banana 2 وNano Banana Pro\\
\\
\\
نماذج متطوّرة لإنشاء الصور وتعديلها](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) [video\_library\\
‫Veo 3.1\\
\\
\\
نقدّم لك نموذجنا الأحدث المصمَّم لإنشاء الفيديوهات، والذي يتضمّن إنشاء صوت أصلي.](https://ai.google.dev/gemini-api/docs/video?hl=ar) [spark\\
Gemini Robotics\\
\\
\\
هو نموذج للرؤية واللغة (VLM) يتيح استخدام إمكانات Gemini المستندة إلى الذكاء الاصطناعي الوكيل في مجال الروبوتات، كما يتيح الاستدلال المتقدّم في العالم المادي.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ar)

## استكشاف الإمكانيات

[imagesmode\\
\\
أداة إنشاء الصور الأصلية (Nano Banana)\\
\\
\\
يمكنك إنشاء صور عالية الدقة وتعديلها بشكلٍ مباشر باستخدام Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) [article\\
\\
سياق طويل\\
\\
\\
إدخال ملايين الرموز المميزة إلى نماذج Gemini واستخلاص المعلومات من الصور والفيديوهات والمستندات غير المنظَّمة](https://ai.google.dev/gemini-api/docs/long-context?hl=ar) [code\\
\\
المُخرجات المنظَّمة\\
\\
\\
يمكنك حصر ردود Gemini على تنسيق JSON، وهو تنسيق بيانات منظَّمة مناسب للمعالجة الآلية.](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) [functions\\
\\
استدعاء الدالة\\
\\
\\
يمكنك إنشاء مهام مبرمَجة من خلال ربط Gemini بواجهات برمجة التطبيقات والأدوات الخارجية.](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) [videocam\\
\\
إنشاء الفيديوهات باستخدام Veo 3.1\\
\\
\\
يمكنك إنشاء محتوى فيديو عالي الجودة من طلبات نصية أو طلبات صور باستخدام نموذجنا الأحدث.](https://ai.google.dev/gemini-api/docs/video?hl=ar) [android\_recorder\\
\\
وكلاء صوت مزوّدون بواجهة برمجة تطبيقات Live API\\
\\
\\
يمكنك إنشاء تطبيقات ووكلاء صوتيين في الوقت الفعلي باستخدام Live API.](https://ai.google.dev/gemini-api/docs/live?hl=ar) [build\\
\\
الأدوات\\
\\
\\
يمكنك ربط Gemini بالعالم من خلال أدوات مدمجة، مثل "بحث Google" و"سياق عنوان URL" و"خرائط Google" و"تنفيذ الرموز البرمجية" و"استخدام الكمبيوتر".](https://ai.google.dev/gemini-api/docs/tools?hl=ar) [stacks\\
\\
فهم المستندات\\
\\
\\
معالجة ما يصل إلى 1,000 صفحة من ملفات PDF مع فهم كامل للوسائط المتعددة أو أنواع الملفات الأخرى المستندة إلى النصوص](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar) [cognition\_2\\
\\
جارٍ التفكير\\
\\
\\
استكشاف كيف تحسّن إمكانات التفكير عملية الاستدلال في المهام المعقّدة والوكلاء](https://ai.google.dev/gemini-api/docs/thinking?hl=ar)

[Google AI Studio\\
\\
\\
اختبار الطلبات وإدارة مفاتيح واجهة برمجة التطبيقات وتتبُّع الاستخدام وإنشاء نماذج أوّلية](https://aistudio.google.com/?hl=ar) [group\\
\\
منتدى المطوّرين\\
\\
\\
طرح الأسئلة والعثور على حلول من مطوّرين آخرين ومهندسي Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar) [menu\_book\\
\\
مرجع واجهة برمجة تطبيقات\\
\\
\\
يمكنك العثور على معلومات تفصيلية حول Gemini API في المستندات المرجعية الرسمية.](https://ai.google.dev/api?hl=ar) [sensors\\
\\
الحالة\\
\\
\\
التحقّق من حالة Gemini API وGoogle AI Studio وخدمات النماذج](https://aistudio.google.com/status?hl=ar)

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-03-03 (حسب التوقيت العالمي المتفَّق عليه)




\[\[\["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"\],\["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"\],\["غير ذلك","otherUp","thumb-up"\]\],\[\["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"\],\["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"\],\["المحتوى قديم.","outOfDate","thumb-down"\],\["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"\],\["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"\],\["غير ذلك","otherDown","thumb-down"\]\],\["تاريخ التعديل الأخير: 2026-03-03 (حسب التوقيت العالمي المتفَّق عليه)"\],\[\],\[\]\]