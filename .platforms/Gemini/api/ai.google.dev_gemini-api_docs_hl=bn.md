[সরাসরি আসল কন্টেন্টে যান](https://ai.google.dev/gemini-api/docs?hl=bn#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=bn)](https://ai.google.dev/)

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

[API কী পান](https://aistudio.google.com/apikey?hl=bn) [রান্নার বই](https://github.com/google-gemini/cookbook) [কমিউনিটি](https://discuss.ai.google.dev/c/gemini-api/?hl=bn)

[সাইন-ইন করুন](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dbn&prompt=select_account)

জেমিনি ৩.১ ফ্ল্যাশ-লাইট প্রিভিউ এখন উপলব্ধ। [এটি এআই স্টুডিওতে চেষ্টা করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=bn) ।


![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

এই পৃষ্ঠাটি [Cloud Translation API](https://cloud.google.com/translate/?hl=bn) অনুবাদ করেছে।


Switch to English


- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [ডক্স](https://ai.google.dev/gemini-api/docs?hl=bn)

# জেমিনি এপিআই

জেমিনি, ভিও, ন্যানো ব্যানানা এবং আরও অনেক কিছুর মাধ্যমে প্রম্পট থেকে প্রোডাকশনের দ্রুততম পথ।

[পাইথন](https://ai.google.dev/gemini-api/docs?hl=bn#%E0%A6%AA%E0%A6%BE%E0%A6%87%E0%A6%A5%E0%A6%A8)[জাভাস্ক্রিপ্ট](https://ai.google.dev/gemini-api/docs?hl=bn#%E0%A6%9C%E0%A6%BE%E0%A6%AD%E0%A6%BE%E0%A6%B8%E0%A7%8D%E0%A6%95%E0%A7%8D%E0%A6%B0%E0%A6%BF%E0%A6%AA%E0%A7%8D%E0%A6%9F)[যাও](https://ai.google.dev/gemini-api/docs?hl=bn#%E0%A6%AF%E0%A6%BE%E0%A6%93)[জাভা](https://ai.google.dev/gemini-api/docs?hl=bn#%E0%A6%9C%E0%A6%BE%E0%A6%AD%E0%A6%BE)[সি#](https://ai.google.dev/gemini-api/docs?hl=bn#%E0%A6%B8%E0%A6%BF)[বিশ্রাম](https://ai.google.dev/gemini-api/docs?hl=bn#%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%AE)আরও দেখুন

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

[নির্মাণ শুরু করুন](https://ai.google.dev/gemini-api/docs/quickstart?hl=bn)

একটি API কী পেতে এবং কয়েক মিনিটের মধ্যে আপনার প্রথম API কল করতে আমাদের কুইকস্টার্ট নির্দেশিকা অনুসরণ করুন।

* * *

## মডেলদের সাথে পরিচিত হোন

[সবগুলো দেখুন](https://ai.google.dev/gemini-api/docs/models?hl=bn)

auto\_awesome জেমিনি ৩.১ প্রো নতুন

আমাদের সবচেয়ে বুদ্ধিমান মডেল, বহুমুখী বোঝাপড়ার জন্য বিশ্বের সেরা, সবই অত্যাধুনিক যুক্তির উপর নির্মিত।

spark জেমিনি 3 ফ্ল্যাশ নতুন

খরচের একটি ভগ্নাংশে বৃহত্তর মডেলগুলির সাথে প্রতিযোগিতা করে ফ্রন্টিয়ার-ক্লাস পারফরম্যান্স।

spark জেমিনি 3.1 ফ্ল্যাশ-লাইট নতুন

জেমিনি ৩ সিরিজের পারফরম্যান্স এবং গুণমান সহ উচ্চ-ভলিউম, খরচ-সংবেদনশীল ওয়ার্কহর্স মডেল।

🍌 ন্যানো ব্যানানা ২ এবং ন্যানো ব্যানানা প্রো

অত্যাধুনিক ছবি তৈরি এবং সম্পাদনা মডেল।

video\_library ভিও ৩.১

আমাদের অত্যাধুনিক ভিডিও জেনারেশন মডেল, নেটিভ অডিও সহ।

spark জেমিনি রোবোটিক্স

একটি দৃষ্টি-ভাষা মডেল (VLM) যা জেমিনির এজেন্টিক ক্ষমতাকে রোবোটিক্সে নিয়ে আসে এবং ভৌত জগতে উন্নত যুক্তি সক্ষম করে।

## সক্ষমতা অন্বেষণ করুন

imagesmode

নেটিভ ইমেজ জেনারেশন (ন্যানো কলা)

জেমিনি ২.৫ ফ্ল্যাশ ইমেজের সাহায্যে অত্যন্ত প্রাসঙ্গিক ছবি তৈরি এবং সম্পাদনা করুন।

article

দীর্ঘ প্রসঙ্গ

জেমিনি মডেলগুলিতে লক্ষ লক্ষ টোকেন ইনপুট করুন এবং অসংগঠিত ছবি, ভিডিও এবং নথি থেকে বোধগম্যতা অর্জন করুন।

code

স্ট্রাকচার্ড আউটপুট

জেমিনিকে JSON ব্যবহার করে প্রতিক্রিয়া জানাতে বাধ্য করুন, যা স্বয়ংক্রিয় প্রক্রিয়াকরণের জন্য উপযুক্ত একটি স্ট্রাকচার্ড ডেটা ফর্ম্যাট।

functions

ফাংশন কলিং

জেমিনিকে বহিরাগত API এবং সরঞ্জামগুলির সাথে সংযুক্ত করে এজেন্টিক ওয়ার্কফ্লো তৈরি করুন।

videocam

ভিও ৩.১ এর মাধ্যমে ভিডিও জেনারেশন

আমাদের অত্যাধুনিক মডেলের সাহায্যে টেক্সট বা ইমেজ প্রম্পট থেকে উচ্চমানের ভিডিও কন্টেন্ট তৈরি করুন।

android\_recorder

লাইভ এপিআই সহ ভয়েস এজেন্ট

লাইভ API ব্যবহার করে রিয়েল-টাইম ভয়েস অ্যাপ্লিকেশন এবং এজেন্ট তৈরি করুন।

build

যন্ত্র

গুগল সার্চ, ইউআরএল কনটেক্সট, গুগল ম্যাপস, কোড এক্সিকিউশন এবং কম্পিউটার ব্যবহারের মতো অন্তর্নির্মিত সরঞ্জামগুলির মাধ্যমে জেমিনিকে বিশ্বের সাথে সংযুক্ত করুন।

stacks

ডকুমেন্ট বোঝাপড়া

সম্পূর্ণ মাল্টিমোডাল বোঝাপড়া বা অন্যান্য টেক্সট-ভিত্তিক ফাইল প্রকার সহ 1000 পৃষ্ঠা পর্যন্ত পিডিএফ ফাইল প্রক্রিয়া করুন।

cognition\_2

ভাবছি

জটিল কাজ এবং এজেন্টদের জন্য চিন্তা করার ক্ষমতা কীভাবে যুক্তি উন্নত করে তা অন্বেষণ করুন।

গুগল এআই স্টুডিও

প্রম্পট পরীক্ষা করুন, আপনার API কী পরিচালনা করুন, ব্যবহার পর্যবেক্ষণ করুন এবং প্রোটোটাইপ তৈরি করুন।

group

ডেভেলপার কমিউনিটি

অন্যান্য ডেভেলপার এবং গুগল ইঞ্জিনিয়ারদের কাছ থেকে প্রশ্ন জিজ্ঞাসা করুন এবং সমাধান খুঁজুন।

menu\_book

API রেফারেন্স

জেমিনি এপিআই সম্পর্কে বিস্তারিত তথ্য অফিসিয়াল রেফারেন্স ডকুমেন্টেশনে পাবেন।

sensors

অবস্থা

জেমিনি এপিআই, গুগল এআই স্টুডিও এবং আমাদের মডেল পরিষেবাগুলির স্থিতি পরীক্ষা করুন।

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-03-03 UTC-তে শেষবার আপডেট করা হয়েছে।




\[\[\["সহজে বোঝা যায়","easyToUnderstand","thumb-up"\],\["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"\],\["অন্যান্য","otherUp","thumb-up"\]\],\[\["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"\],\["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"\],\["পুরনো","outOfDate","thumb-down"\],\["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"\],\["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"\],\["অন্যান্য","otherDown","thumb-down"\]\],\["2026-03-03 UTC-তে শেষবার আপডেট করা হয়েছে।"\],\[\],\[\]\]