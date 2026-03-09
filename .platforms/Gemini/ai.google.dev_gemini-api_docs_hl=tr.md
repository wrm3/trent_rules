[Ana içeriğe atla](https://ai.google.dev/gemini-api/docs?hl=tr#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=tr)](https://ai.google.dev/)

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

[API anahtarı alma](https://aistudio.google.com/apikey?hl=tr) [Tarif Defteri](https://github.com/google-gemini/cookbook) [Topluluk](https://discuss.ai.google.dev/c/gemini-api/?hl=tr)

[Oturum aç](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dtr&prompt=select_account)


Gemini 3.1 Flash-Lite önizlemesi kullanıma sunuldu. [AI Studio'da deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=tr).




- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

# Gemini API'yi kullanarak uygulamalarınıza entegre edin.

Gemini, Veo, Nano Banana ve diğer araçlarla istemden üretime en hızlı geçiş.

[Python](https://ai.google.dev/gemini-api/docs?hl=tr#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=tr#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=tr#go)[Java](https://ai.google.dev/gemini-api/docs?hl=tr#java)[C#](https://ai.google.dev/gemini-api/docs?hl=tr#c)[REST](https://ai.google.dev/gemini-api/docs?hl=tr#rest)Daha fazla

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

[Oluşturmaya başlama](https://ai.google.dev/gemini-api/docs/quickstart?hl=tr)

API anahtarı almak ve ilk API çağrınızı dakikalar içinde yapmak için Hızlı Başlangıç kılavuzumuzu inceleyin.

* * *

## Modellerle tanışın

[Tümünü görüntüleyin](https://ai.google.dev/gemini-api/docs/models?hl=tr)

[auto\_awesome\\
Gemini 3.1 Pro\\
Yeni\\
\\
En akıllı modelimiz, en son teknoloji ürünü akıl yürütme üzerine inşa edilmiş olup çok formatlı anlama konusunda dünyanın en iyisidir.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) [spark\\
Gemini 3 Flash\\
Yeni\\
\\
Maliyetinin çok daha düşük olmasına rağmen daha büyük modellerle yarışan Frontier sınıfı performans.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) [spark\\
Gemini 3.1 Flash-Lite\\
Yeni\\
\\
Gemini 3 serisinin performans ve kalitesine sahip, yüksek hacimli ve maliyet açısından hassas iş yükleri için ideal model.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=tr) [🍌\\
Nano Banana 2 ve Nano Banana Pro\\
\\
\\
Son teknoloji ürünü görüntü üretme ve düzenleme modelleri.](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) [video\_library\\
Veo 3.1\\
\\
\\
Doğal ses özelliğine sahip, son teknoloji ürünü video üretim modelimiz.](https://ai.google.dev/gemini-api/docs/video?hl=tr) [spark\\
Gemini Robotics\\
\\
\\
Gemini'ın aracı özelliklerini robotik alanına taşıyan ve fiziksel dünyada gelişmiş akıl yürütme imkanı sunan bir görüntü-dil modeli (VLM).](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr)

## Özellikleri keşfedin

[imagesmode\\
\\
Yerel Görüntü Üretme (Nano Banana)\\
\\
\\
Gemini 2.5 Flash Image ile bağlamı yüksek görüntüler oluşturun ve düzenleyin.](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) [article\\
\\
Uzun Bağlam\\
\\
\\
Gemini modellerine milyonlarca jeton girin ve yapılandırılmamış resimler, videolar ve dokümanlardan bilgi edinin.](https://ai.google.dev/gemini-api/docs/long-context?hl=tr) [code\\
\\
Yapılandırılmış Çıkışlar\\
\\
\\
Gemini'ın, otomatik işleme için uygun bir yapılandırılmış veri biçimi olan JSON ile yanıt vermesini sağlayın.](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) [functions\\
\\
İşlev Çağırma\\
\\
\\
Gemini'ı harici API'lere ve araçlara bağlayarak etkili iş akışları oluşturun.](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) [videocam\\
\\
Veo 3.1 ile video üretimi\\
\\
\\
Son teknolojiyle geliştirilen modelimizle metin veya resim istemlerinden yüksek kaliteli video içerikleri oluşturun.](https://ai.google.dev/gemini-api/docs/video?hl=tr) [android\_recorder\\
\\
Live API ile Sesli Aracıları\\
\\
\\
Live API ile gerçek zamanlı ses uygulamaları ve aracıları oluşturun.](https://ai.google.dev/gemini-api/docs/live?hl=tr) [build\\
\\
Araçlar\\
\\
\\
Google Arama, URL Bağlamı, Google Haritalar, Kod Yürütme ve Bilgisayar Kullanımı gibi yerleşik araçlarla Gemini'ı dünyaya bağlayın.](https://ai.google.dev/gemini-api/docs/tools?hl=tr) [stacks\\
\\
Belge Anlama\\
\\
\\
Tam çok formatlı anlayışla veya diğer metin tabanlı dosya türleriyle 1.000 sayfaya kadar PDF dosyası işleyin.](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr) [cognition\_2\\
\\
Düşünen\\
\\
\\
Düşünme yeteneklerinin karmaşık görevler ve aracılar için akıl yürütmeyi nasıl iyileştirdiğini keşfedin.](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)

[Google AI Studio\\
\\
\\
İstemleri test edin, API anahtarlarınızı yönetin, kullanımı izleyin ve prototipler oluşturun.](https://aistudio.google.com/?hl=tr) [group\\
\\
Geliştirici Topluluğu\\
\\
\\
Diğer geliştiricilere ve Google mühendislerine soru sorabilir, çözümler bulabilirsiniz.](https://discuss.ai.google.dev/c/gemini-api/4?hl=tr) [menu\_book\\
\\
API Referansı\\
\\
\\
Gemini API hakkında ayrıntılı bilgiyi resmi referans belgelerinde bulabilirsiniz.](https://ai.google.dev/api?hl=tr) [sensors\\
\\
Durum\\
\\
\\
Gemini API, Google AI Studio ve model hizmetlerimizin durumunu kontrol edin.](https://aistudio.google.com/status?hl=tr)

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-03-03 UTC.




\[\[\["Anlaması kolay","easyToUnderstand","thumb-up"\],\["Sorunumu çözdü","solvedMyProblem","thumb-up"\],\["Diğer","otherUp","thumb-up"\]\],\[\["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"\],\["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"\],\["Güncel değil","outOfDate","thumb-down"\],\["Çeviri sorunu","translationIssue","thumb-down"\],\["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"\],\["Diğer","otherDown","thumb-down"\]\],\["Son güncelleme tarihi: 2026-03-03 UTC."\],\[\],\[\]\]