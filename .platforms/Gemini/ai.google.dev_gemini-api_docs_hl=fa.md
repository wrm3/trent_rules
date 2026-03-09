[رد شدن و رفتن به محتوای اصلی](https://ai.google.dev/gemini-api/docs?hl=fa#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=fa)](https://ai.google.dev/)

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

[کلید API را دریافت کنید](https://aistudio.google.com/apikey?hl=fa) [کتاب آشپزی](https://github.com/google-gemini/cookbook) [انجمن](https://discuss.ai.google.dev/c/gemini-api/?hl=fa)

[ورود به برنامه](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dfa&prompt=select_account)

پیش‌نمایش Gemini 3.1 Flash-Lite اکنون در دسترس است. [آن را در AI Studio امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=fa) .


![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

این صفحه به‌وسیله [‏Cloud Translation API‏](https://cloud.google.com/translate/?hl=fa) ترجمه شده است.


Switch to English


- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [اسناد](https://ai.google.dev/gemini-api/docs?hl=fa)

# رابط برنامه‌نویسی کاربردی Gemini

سریع‌ترین مسیر از سفارش تا تولید با Gemini، Veo، Nano Banana و موارد دیگر.

[پایتون](https://ai.google.dev/gemini-api/docs?hl=fa#%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86)[جاوا اسکریپت](https://ai.google.dev/gemini-api/docs?hl=fa#%D8%AC%D8%A7%D9%88%D8%A7-%D8%A7%D8%B3%DA%A9%D8%B1%DB%8C%D9%BE%D8%AA)[برو](https://ai.google.dev/gemini-api/docs?hl=fa#%D8%A8%D8%B1%D9%88)[جاوا](https://ai.google.dev/gemini-api/docs?hl=fa#%D8%AC%D8%A7%D9%88%D8%A7)[سی شارپ](https://ai.google.dev/gemini-api/docs?hl=fa#%D8%B3%DB%8C-%D8%B4%D8%A7%D8%B1%D9%BE)[استراحت](https://ai.google.dev/gemini-api/docs?hl=fa#%D8%A7%D8%B3%D8%AA%D8%B1%D8%A7%D8%AD%D8%AA)بیشتر

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

[شروع به ساختن کنید](https://ai.google.dev/gemini-api/docs/quickstart?hl=fa)

برای دریافت کلید API و برقراری اولین فراخوانی API خود در عرض چند دقیقه، راهنمای شروع سریع ما را دنبال کنید.

* * *

## با مدل‌ها آشنا شوید

[مشاهده همه](https://ai.google.dev/gemini-api/docs/models?hl=fa)

auto\_awesome جمینی ۳.۱ پرو جدید

هوشمندترین مدل ما، بهترین مدل در جهان برای درک چندوجهی، که همگی بر اساس استدلال پیشرفته ساخته شده‌اند.

spark Gemini 3 فلش جدید

عملکردی در سطح کلاس Frontier که با کسری از قیمت، مدل‌های بزرگ‌تر را به رقابت می‌خواند.

spark جمینی ۳.۱ فلش-لایت جدید

مدلی کارآمد، مقرون‌به‌صرفه و با حجم تولید بالا، با عملکرد و کیفیت سری Gemini 3.

🍌 نانو موز ۲ و نانو موز پرو

مدل‌های پیشرفته تولید و ویرایش تصویر.

video\_library وئو ۳.۱

مدل تولید ویدیوی پیشرفته ما، با صدای بومی.

spark رباتیک جمینی

یک مدل زبان بینایی (VLM) که قابلیت‌های عامل‌محور Gemini را به رباتیک می‌آورد و استدلال پیشرفته در دنیای فیزیکی را امکان‌پذیر می‌کند.

## بررسی قابلیت‌ها

imagesmode

تولید تصویر بومی (نانو موز)

با استفاده از Gemini 2.5 Flash Image، تصاویر بسیار متنی را به صورت بومی تولید و ویرایش کنید.

article

متن طولانی

میلیون‌ها توکن را به مدل‌های Gemini وارد کنید و از تصاویر، ویدیوها و اسناد بدون ساختار، درک لازم را به دست آورید.

code

خروجی‌های ساختاریافته

Gemini را مجبور کنید تا با JSON پاسخ دهد، یک فرمت داده ساختار یافته مناسب برای پردازش خودکار.

functions

فراخوانی تابع

با اتصال Gemini به APIها و ابزارهای خارجی، گردش‌های کاری عامل‌محور بسازید.

videocam

تولید ویدیو با Veo 3.1

با استفاده از مدل پیشرفته ما، محتوای ویدیویی با کیفیت بالا از متن یا تصویر ایجاد کنید.

android\_recorder

عامل‌های صوتی با API زنده

با استفاده از Live API، اپلیکیشن‌ها و عامل‌های صوتی بلادرنگ بسازید.

build

ابزارها

Gemini را از طریق ابزارهای داخلی مانند جستجوی گوگل، متن URL، نقشه‌های گوگل، اجرای کد و استفاده از رایانه به جهان متصل کنید.

stacks

درک سند

پردازش تا ۱۰۰۰ صفحه فایل PDF با درک کامل چندوجهی یا سایر انواع فایل‌های مبتنی بر متن.

cognition\_2

تفکر

بررسی کنید که چگونه قابلیت‌های تفکر، استدلال برای وظایف و عامل‌های پیچیده را بهبود می‌بخشد.

استودیوی هوش مصنوعی گوگل

اعلان‌ها را آزمایش کنید، کلیدهای API خود را مدیریت کنید، میزان استفاده را زیر نظر داشته باشید و نمونه‌های اولیه بسازید.

group

جامعه توسعه‌دهندگان

از دیگر توسعه‌دهندگان و مهندسان گوگل سوال بپرسید و راه‌حل پیدا کنید.

menu\_book

مرجع API

اطلاعات دقیق در مورد API مربوط به Gemini را در مستندات مرجع رسمی بیابید.

sensors

وضعیت

وضعیت Gemini API، Google AI Studio و سرویس‌های مدل ما را بررسی کنید.

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-03-03 به‌وقت ساعت هماهنگ جهانی.




\[\[\["درک آسان","easyToUnderstand","thumb-up"\],\["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"\],\["غیره","otherUp","thumb-up"\]\],\[\["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"\],\["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"\],\["قدیمی","outOfDate","thumb-down"\],\["مشکل ترجمه","translationIssue","thumb-down"\],\["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"\],\["غیره","otherDown","thumb-down"\]\],\["تاریخ آخرین به‌روزرسانی 2026-03-03 به‌وقت ساعت هماهنگ جهانی."\],\[\],\[\]\]