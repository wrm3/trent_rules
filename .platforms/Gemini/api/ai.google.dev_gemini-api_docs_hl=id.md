[Langsung ke konten utama](https://ai.google.dev/gemini-api/docs?hl=id#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=id)](https://ai.google.dev/)

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

[Mendapatkan kunci API](https://aistudio.google.com/apikey?hl=id) [Cookbook](https://github.com/google-gemini/cookbook) [Komunitas](https://discuss.ai.google.dev/c/gemini-api/?hl=id)

[Masuk](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Did&prompt=select_account)


Pratinjau Gemini 3.1 Flash-Lite kini tersedia. [Coba di AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=id).




- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

# Gemini API

Jalur tercepat dari perintah hingga produksi dengan Gemini, Veo, Nano Banana, dan lainnya.

[Python](https://ai.google.dev/gemini-api/docs?hl=id#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=id#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=id#go)[Java](https://ai.google.dev/gemini-api/docs?hl=id#java)[C#](https://ai.google.dev/gemini-api/docs?hl=id#c)[REST](https://ai.google.dev/gemini-api/docs?hl=id#rest)Lainnya

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

[Mulai membangun](https://ai.google.dev/gemini-api/docs/quickstart?hl=id)

Ikuti Panduan memulai kami untuk mendapatkan kunci API dan melakukan panggilan API pertama Anda dalam hitungan menit.

* * *

## Perkenalkan model kami

[Lihat semua](https://ai.google.dev/gemini-api/docs/models?hl=id)

[auto\_awesome\\
Gemini 3.1 Pro\\
Baru\\
\\
Model tercerdas kami, yang terbaik di dunia untuk pemahaman multimodal, semuanya dibangun berdasarkan penalaran canggih.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) [spark\\
Gemini 3 Flash\\
Baru\\
\\
Performa kelas terdepan yang menyaingi model yang lebih besar dengan sebagian kecil biaya.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) [spark\\
Gemini 3.1 Flash-Lite\\
Baru\\
\\
Model andalan yang menangani volume tinggi dan sensitif terhadap biaya dengan performa dan kualitas seri Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=id) [🍌\\
Nano Banana 2 dan Nano Banana Pro\\
\\
\\
Model pengeditan dan pembuatan gambar tercanggih.](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) [video\_library\\
Veo 3.1\\
\\
\\
Model pembuatan video tercanggih kami, dengan audio native.](https://ai.google.dev/gemini-api/docs/video?hl=id) [spark\\
Gemini Robotics\\
\\
\\
Model bahasa-penglihatan (VLM) yang menghadirkan kemampuan agentic Gemini ke robotika dan memungkinkan penalaran tingkat lanjut di dunia fisik.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=id)

## Ketahui Kemampuannya

[imagesmode\\
\\
Pembuatan Gambar Native (Nano Banana)\\
\\
\\
Buat dan edit gambar yang sangat kontekstual secara native dengan Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) [article\\
\\
Konteks Panjang\\
\\
\\
Masukkan jutaan token ke model Gemini dan dapatkan pemahaman dari gambar, video, dan dokumen yang tidak terstruktur.](https://ai.google.dev/gemini-api/docs/long-context?hl=id) [code\\
\\
Output Terstruktur\\
\\
\\
Batasi Gemini untuk merespons dengan JSON, format data terstruktur yang cocok untuk pemrosesan otomatis.](https://ai.google.dev/gemini-api/docs/structured-output?hl=id) [functions\\
\\
Pemanggilan Fungsi\\
\\
\\
Bangun alur kerja agentic dengan menghubungkan Gemini ke API dan alat eksternal.](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) [videocam\\
\\
Pembuatan Video dengan Veo 3.1\\
\\
\\
Buat konten video berkualitas tinggi dari perintah teks atau gambar dengan model tercanggih kami.](https://ai.google.dev/gemini-api/docs/video?hl=id) [android\_recorder\\
\\
Agen Suara dengan Live API\\
\\
\\
Bangun aplikasi dan agen suara real-time dengan Live API.](https://ai.google.dev/gemini-api/docs/live?hl=id) [build\\
\\
Alat\\
\\
\\
Hubungkan Gemini dengan dunia melalui alat bawaan seperti Google Penelusuran, Konteks URL, Google Maps, Eksekusi Kode, dan Penggunaan Komputer.](https://ai.google.dev/gemini-api/docs/tools?hl=id) [stacks\\
\\
Document Understanding\\
\\
\\
Memproses hingga 1.000 halaman file PDF dengan pemahaman multimodal penuh atau jenis file berbasis teks lainnya.](https://ai.google.dev/gemini-api/docs/document-processing?hl=id) [cognition\_2\\
\\
Penalaran\\
\\
\\
Pelajari cara kemampuan berpikir meningkatkan penalaran untuk tugas dan agen yang kompleks.](https://ai.google.dev/gemini-api/docs/thinking?hl=id)

[Google AI Studio\\
\\
\\
Uji perintah, kelola kunci API, pantau penggunaan, dan buat prototipe.](https://aistudio.google.com/?hl=id) [group\\
\\
Komunitas Developer\\
\\
\\
Ajukan pertanyaan dan temukan solusi dari developer lain dan engineer Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=id) [menu\_book\\
\\
Referensi API\\
\\
\\
Temukan informasi mendetail tentang Gemini API dalam dokumentasi referensi resmi.](https://ai.google.dev/api?hl=id) [sensors\\
\\
Status\\
\\
\\
Periksa status Gemini API, Google AI Studio, dan layanan model kami.](https://aistudio.google.com/status?hl=id)

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-03-03 UTC.




\[\[\["Mudah dipahami","easyToUnderstand","thumb-up"\],\["Memecahkan masalah saya","solvedMyProblem","thumb-up"\],\["Lainnya","otherUp","thumb-up"\]\],\[\["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"\],\["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"\],\["Sudah usang","outOfDate","thumb-down"\],\["Masalah terjemahan","translationIssue","thumb-down"\],\["Masalah kode / contoh","samplesCodeIssue","thumb-down"\],\["Lainnya","otherDown","thumb-down"\]\],\["Terakhir diperbarui pada 2026-03-03 UTC."\],\[\],\[\]\]