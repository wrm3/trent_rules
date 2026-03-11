[Przejdź do głównej treści](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=pl)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/image-understanding)
- [Deutsch](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/image-understanding?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/image-understanding?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/image-understanding?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko)

[Pobierz klucz interfejsu API](https://aistudio.google.com/apikey?hl=pl) [Książka kucharska](https://github.com/google-gemini/cookbook) [Społeczność](https://discuss.ai.google.dev/c/gemini-api/?hl=pl)

[Zaloguj się](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dpl&prompt=select_account)

- Na tej stronie
- [Przekazywanie obrazów do Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#image-input)
  - [Przekazywanie danych obrazu w tekście](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#inline-image)
  - [Przesyłanie obrazów za pomocą interfejsu File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#upload-image)
- [Prompty z wieloma obrazami](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#multiple-images)
- [Wykrywanie obiektów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#object-detection)
- [Podział na segmenty](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#segmentation)
- [Obsługiwane formaty obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#supported-formats)
- [Uprawnienia](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#capabilities)
- [Ograniczenia i najważniejsze informacje techniczne](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#technical-details-image)
  - [Limit plików](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#file_limit)
  - [Obliczanie tokenów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#token_calculation)
  - [Rozdzielczość multimediów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#media_resolution)
- [Porady i sprawdzone metody](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#tips-best-practices)
- [Co dalej?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#whats-next)


Wersja testowa Gemini 3.1 Flash-Lite jest już dostępna. [Wypróbuj w AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=pl)

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Czy te wskazówki były pomocne?



 Prześlij opinię



# Interpretacja obrazu

- Na tej stronie
- [Przekazywanie obrazów do Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#image-input)
  - [Przekazywanie danych obrazu w tekście](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#inline-image)
  - [Przesyłanie obrazów za pomocą interfejsu File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#upload-image)
- [Prompty z wieloma obrazami](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#multiple-images)
- [Wykrywanie obiektów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#object-detection)
- [Podział na segmenty](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#segmentation)
- [Obsługiwane formaty obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#supported-formats)
- [Uprawnienia](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#capabilities)
- [Ograniczenia i najważniejsze informacje techniczne](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#technical-details-image)
  - [Limit plików](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#file_limit)
  - [Obliczanie tokenów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#token_calculation)
  - [Rozdzielczość multimediów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#media_resolution)
- [Porady i sprawdzone metody](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#tips-best-practices)
- [Co dalej?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#whats-next)

Modele Gemini są od podstaw tworzone z myślą o multimodalności, co umożliwia wykonywanie wielu zadań związanych z przetwarzaniem obrazów i widzeniem komputerowym, w tym tworzenie podpisów do obrazów, klasyfikowanie obrazów i odpowiadanie na pytania dotyczące obrazów, bez konieczności trenowania specjalistycznych modeli uczenia maszynowego.

Oprócz ogólnych możliwości multimodalnych modele Gemini oferują **większą dokładność** w przypadku konkretnych zastosowań, takich jak [wykrywanie obiektów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#object-detection) i [segmentacja](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#segmentation), dzięki dodatkowemu trenowaniu.

## Przekazywanie obrazów do Gemini

Obrazy możesz przekazywać do Gemini na 2 sposoby:

- [Przekazywanie danych obrazu w formie inline:](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#inline-image) idealne rozwiązanie w przypadku mniejszych plików (łączny rozmiar żądania, w tym promptów, jest mniejszy niż 20 MB).
- [Przesyłanie obrazów za pomocą interfejsu File API:](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#upload-image) zalecane w przypadku większych plików lub ponownego wykorzystywania obrazów w wielu żądaniach.

### Przekazywanie danych obrazu w tekście

Możesz przekazywać dane obrazu w treści żądania do `generateContent`. Dane obrazu możesz podać jako ciągi tekstowe z kodowaniem Base64 lub wczytując bezpośrednio pliki lokalne (w zależności od języka).

Poniższy przykład pokazuje, jak odczytać obraz z pliku lokalnego i przekazać go do interfejsu `generateContent` API w celu przetworzenia.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#rest)Więcej

```
  from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[\
      types.Part.from_bytes(\
        data=image_bytes,\
        mime_type='image/jpeg',\
      ),\
      'Caption this image.'\
    ]
  )

  print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const contents = [\
  {\
    inlineData: {\
      mimeType: "image/jpeg",\
      data: base64ImageFile,\
    },\
  },\
  { text: "Caption this image." },\
];

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: contents,
});
console.log(response.text);
```

```
bytes, _ := os.ReadFile("path/to/small-sample.jpg")

parts := []*genai.Part{
  genai.NewPartFromBytes(bytes, "image/jpeg"),
  genai.NewPartFromText("Caption this image."),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3-flash-preview",
  contents,
  nil,
)

fmt.Println(result.Text())
```

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
B64FLAGS="--input"
else
B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{\
    "parts":[\
        {\
            "inline_data": {\
            "mime_type":"image/jpeg",\
            "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"\
            }\
        },\
        {"text": "Caption this image."},\
    ]\
    }]
}' 2> /dev/null
```

Możesz też pobrać obraz z adresu URL, przekonwertować go na bajty i przekazać do `generateContent`, jak pokazano w przykładach poniżej.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#rest)Więcej

```
from google import genai
from google.genai import types

import requests

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["What is this image?", image],
)

print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const ai = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";

  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [\
    {\
      inlineData: {\
        mimeType: 'image/jpeg',\
        data: base64ImageData,\
      },\
    },\
    { text: "Caption this image." }\
  ],
  });
  console.log(result.text);
}

main();
```

```
package main

import (
  "context"
  "fmt"
  "os"
  "io"
  "net/http"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Download the image.
  imageResp, _ := http.Get("https://goo.gle/instrument-img")

  imageBytes, _ := io.ReadAll(imageResp.Body)

  parts := []*genai.Part{
    genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    genai.NewPartFromText("Caption this image."),
  }

  contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3-flash-preview",
    contents,
    nil,
  )

  fmt.Println(result.Text())
}
```

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
            {\
              "inline_data": {\
                "mime_type":"'"$MIME_TYPE"'",\
                "data": "'"$IMAGE_B64"'"\
              }\
            },\
            {"text": "Caption this image."}\
        ]\
      }]
    }' 2> /dev/null
```

### Przesyłanie obrazów za pomocą interfejsu File API

W przypadku dużych plików lub jeśli chcesz wielokrotnie używać tego samego pliku obrazu, użyj interfejsu Files API. Poniższy kod przesyła plik obrazu, a następnie używa go w wywołaniu funkcji `generateContent`. Więcej informacji i przykłady znajdziesz w [przewodniku po interfejsie Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#rest)Więcej

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[my_file, "Caption this image."],
)

print(response.text)
```

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([\
      createPartFromUri(myfile.uri, myfile.mimeType),\
      "Caption this image.",\
    ]),
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
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.jpg", nil)

  parts := []*genai.Part{
      genai.NewPartFromText("Caption this image."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

```
IMAGE_PATH="path/to/sample.jpg"
MIME_TYPE=$(file -b --mime-type "${IMAGE_PATH}")
NUM_BYTES=$(wc -c < "${IMAGE_PATH}")
DISPLAY_NAME=IMAGE

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},\
          {"text": "Caption this image."}]\
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Prompty z wieloma obrazami

W jednym promcie możesz podać wiele obrazów, umieszczając w tablicy `contents` wiele obiektów image`Part`. Mogą to być dane wbudowane (lokalne pliki lub adresy URL) i odwołania do interfejsu File API.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#rest)Więcej

```
from google import genai
from google.genai import types

client = genai.Client()

# Upload the first image
image1_path = "path/to/image1.jpg"
uploaded_file = client.files.upload(file=image1_path)

# Prepare the second image as inline data
image2_path = "path/to/image2.png"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

# Create the prompt with text and multiple images
response = client.models.generate_content(

    model="gemini-3-flash-preview",
    contents=[\
        "What is different between these two images?",\
        uploaded_file,  # Use the uploaded file reference\
        types.Part.from_bytes(\
            data=img2_bytes,\
            mime_type='image/png'\
        )\
    ]
)

print(response.text)
```

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
  // Upload the first image
  const image1_path = "path/to/image1.jpg";
  const uploadedFile = await ai.files.upload({
    file: image1_path,
    config: { mimeType: "image/jpeg" },
  });

  // Prepare the second image as inline data
  const image2_path = "path/to/image2.png";
  const base64Image2File = fs.readFileSync(image2_path, {
    encoding: "base64",
  });

  // Create the prompt with text and multiple images

  const response = await ai.models.generateContent({

    model: "gemini-3-flash-preview",
    contents: createUserContent([\
      "What is different between these two images?",\
      createPartFromUri(uploadedFile.uri, uploadedFile.mimeType),\
      {\
        inlineData: {\
          mimeType: "image/png",\
          data: base64Image2File,\
        },\
      },\
    ]),
  });
  console.log(response.text);
}

await main();
```

```
// Upload the first image
image1Path := "path/to/image1.jpg"
uploadedFile, _ := client.Files.UploadFromPath(ctx, image1Path, nil)

// Prepare the second image as inline data
image2Path := "path/to/image2.jpeg"
imgBytes, _ := os.ReadFile(image2Path)

parts := []*genai.Part{
  genai.NewPartFromText("What is different between these two images?"),
  genai.NewPartFromBytes(imgBytes, "image/jpeg"),
  genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3-flash-preview",
  contents,
  nil,
)

fmt.Println(result.Text())
```

```
# Upload the first image
IMAGE1_PATH="path/to/image1.jpg"
MIME1_TYPE=$(file -b --mime-type "${IMAGE1_PATH}")
NUM1_BYTES=$(wc -c < "${IMAGE1_PATH}")
DISPLAY_NAME1=IMAGE1

tmp_header_file1=upload-header1.tmp

curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header1.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME1_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME1}'}}" 2> /dev/null

upload_url1=$(grep -i "x-goog-upload-url: " "${tmp_header_file1}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file1}"

curl "${upload_url1}" \
  -H "Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE1_PATH}" 2> /dev/null > file_info1.json

file1_uri=$(jq ".file.uri" file_info1.json)
echo file1_uri=$file1_uri

# Prepare the second image (inline)
IMAGE2_PATH="path/to/image2.png"
MIME2_TYPE=$(file -b --mime-type "${IMAGE2_PATH}")

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi
IMAGE2_BASE64=$(base64 $B64FLAGS $IMAGE2_PATH)

# Now generate content using both images
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"text": "What is different between these two images?"},\
          {"file_data":{"mime_type": "'"${MIME1_TYPE}"'", "file_uri": '$file1_uri'}},\
          {\
            "inline_data": {\
              "mime_type":"'"${MIME2_TYPE}"'",\
              "data": "'"$IMAGE2_BASE64"'"\
            }\
          }\
        ]\
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Wykrywanie obiektów

Modele są trenowane pod kątem wykrywania obiektów na obrazie i uzyskiwania współrzędnych ich ramek ograniczających. Współrzędne są skalowane do zakresu \[0, 1000\] względem wymiarów obrazu. Musisz przeskalować te współrzędne na podstawie oryginalnego rozmiaru obrazu.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#python)Więcej

```
from google import genai
from google.genai import types
from PIL import Image
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open("/path/to/image.png")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-3-flash-preview",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

print("Image size: ", width, height)
print("Bounding boxes:", converted_bounding_boxes)
```

Więcej przykładów znajdziesz w tych notatnikach w [zbiorze Cookbook Gemini](https://github.com/google-gemini/cookbook):

- [Notatnik dotyczący przestrzennego rozumienia 2D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=pl)
- [Eksperymentalny notatnik do wskazywania 3D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=pl)

## Podział na segmenty

Począwszy od Gemini 2.5, modele nie tylko wykrywają obiekty, ale także je segmentują i dostarczają ich maski konturowe.

Model prognozuje listę JSON, w której każdy element reprezentuje maskę segmentacji.
Każdy element ma ramkę ograniczającą („`box_2d`”) w formacie `[y0, x0, y1, x1]` ze znormalizowanymi współrzędnymi z przedziału od 0 do 1000, etykietę („`label`”) identyfikującą obiekt oraz maskę segmentacji w ramce ograniczającej w formacie base64 zakodowanego pliku PNG, który jest mapą prawdopodobieństwa z wartościami z przedziału od 0 do 255.
Maskę należy dopasować do wymiarów ramki ograniczającej, a następnie poddać binaryzacji przy użyciu progu ufności (127 w przypadku punktu środkowego).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#python)Więcej

````
from google import genai
from google.genai import types
from PIL import Image, ImageDraw
import io
import base64
import json
import numpy as np
import os

client = genai.Client()

def parse_json(json_output: str):
  # Parsing out the markdown fencing
  lines = json_output.splitlines()
  for i, line in enumerate(lines):
    if line == "```json":
      json_output = "\n".join(lines[i+1:])  # Remove everything before "```json"
      output = json_output.split("```")[0]  # Remove everything after the closing "```"
      break  # Exit the loop once "```json" is found
  return json_output

def extract_segmentation_masks(image_path: str, output_dir: str = "segmentation_outputs"):
  # Load and resize image
  im = Image.open(image_path)
  im.thumbnail([1024, 1024], Image.Resampling.LANCZOS)

  prompt = """
  Give the segmentation masks for the wooden and glass items.
  Output a JSON list of segmentation masks where each entry contains the 2D
  bounding box in the key "box_2d", the segmentation mask in key "mask", and
  the text label in the key "label". Use descriptive labels.
  """

  config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0) # set thinking_budget to 0 for better results in object detection
  )

  response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt, im], # Pillow images can be directly passed as inputs (which will be converted by the SDK)
    config=config
  )

  # Parse JSON response
  items = json.loads(parse_json(response.text))

  # Create output directory
  os.makedirs(output_dir, exist_ok=True)

  # Process each mask
  for i, item in enumerate(items):
      # Get bounding box coordinates
      box = item["box_2d"]
      y0 = int(box[0] / 1000 * im.size[1])
      x0 = int(box[1] / 1000 * im.size[0])
      y1 = int(box[2] / 1000 * im.size[1])
      x1 = int(box[3] / 1000 * im.size[0])

      # Skip invalid boxes
      if y0 >= y1 or x0 >= x1:
          continue

      # Process mask
      png_str = item["mask"]
      if not png_str.startswith("data:image/png;base64,"):
          continue

      # Remove prefix
      png_str = png_str.removeprefix("data:image/png;base64,")
      mask_data = base64.b64decode(png_str)
      mask = Image.open(io.BytesIO(mask_data))

      # Resize mask to match bounding box
      mask = mask.resize((x1 - x0, y1 - y0), Image.Resampling.BILINEAR)

      # Convert mask to numpy array for processing
      mask_array = np.array(mask)

      # Create overlay for this mask
      overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
      overlay_draw = ImageDraw.Draw(overlay)

      # Create overlay for the mask
      color = (255, 255, 255, 200)
      for y in range(y0, y1):
          for x in range(x0, x1):
              if mask_array[y - y0, x - x0] > 128:  # Threshold for mask
                  overlay_draw.point((x, y), fill=color)

      # Save individual mask and its overlay
      mask_filename = f"{item['label']}_{i}_mask.png"
      overlay_filename = f"{item['label']}_{i}_overlay.png"

      mask.save(os.path.join(output_dir, mask_filename))

      # Create and save overlay
      composite = Image.alpha_composite(im.convert('RGBA'), overlay)
      composite.save(os.path.join(output_dir, overlay_filename))
      print(f"Saved mask and overlay for {item['label']} to {output_dir}")

# Example usage
if __name__ == "__main__":
  extract_segmentation_masks("path/to/image.png")
````

Bardziej szczegółowy przykład znajdziesz w [przykładzie segmentacji](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=pl#scrollTo=WQJTJ8wdGOKx) w przewodniku.

![Stół z babeczkami, na którym wyróżniono drewniane i szklane przedmioty](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=pl)Przykładowe dane wyjściowe segmentacji z obiektami i maskami segmentacji

## Obsługiwane formaty obrazów

Gemini obsługuje te typy MIME formatów obrazów:

- PNG – `image/png`
- JPEG – `image/jpeg`
- WEBP - `image/webp`
- HEIC – `image/heic`
- HEIF – `image/heif`

Więcej informacji o innych metodach wprowadzania plików znajdziesz w przewodniku [Metody wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

## Uprawnienia

Wszystkie wersje modelu Gemini są wielomodalne i mogą być wykorzystywane w szerokim zakresie zadań związanych z przetwarzaniem obrazów i rozpoznawaniem obrazów, w tym m.in. do tworzenia podpisów do obrazów, odpowiadania na pytania dotyczące obrazów, klasyfikowania obrazów, wykrywania obiektów i segmentacji.

W zależności od wymagań dotyczących jakości i skuteczności Gemini może zmniejszyć potrzebę korzystania ze specjalistycznych modeli uczenia maszynowego.

Najnowsze wersje modeli są specjalnie trenowane, aby zwiększać dokładność wykonywania specjalistycznych zadań oprócz ogólnych funkcji, takich jak ulepszone [wykrywanie obiektów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#object-detection) i [segmentacja](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl#segmentation).

## Ograniczenia i najważniejsze informacje techniczne

### Limit plików

Modele Gemini obsługują maksymalnie 3600 plików obrazów na żądanie.

### Obliczanie tokenów

- 258 tokenów, jeśli oba wymiary są mniejsze lub równe 384 pikselom.
Większe obrazy są dzielone na kafelki o rozmiarze 768 x 768 pikseli, z których każdy kosztuje 258 tokenów.

Przybliżony wzór na obliczenie liczby płytek jest następujący:

- Oblicz rozmiar jednostki przycięcia, który wynosi w przybliżeniu: floor(min(szerokość, wysokość) / 1,5).
- Podziel każdy wymiar przez rozmiar jednostki przycinania i pomnóż przez siebie, aby uzyskać liczbę kafelków.

Na przykład w przypadku obrazu o wymiarach 960 x 540 jednostka przycięcia będzie miała rozmiar 360. Podziel każdy wymiar przez 360, a liczba kafelków wyniesie 3 × 2 = 6.

### Rozdzielczość multimediów

Gemini 3 wprowadza szczegółową kontrolę nad multimodalnym przetwarzaniem obrazu za pomocą parametru `media_resolution`. Parametr `media_resolution` określa **maksymalną liczbę tokenów przypisanych do każdego obrazu wejściowego lub klatki filmu**.
Wyższe rozdzielczości zwiększają zdolność modelu do odczytywania drobnego tekstu lub rozpoznawania małych szczegółów, ale zwiększają zużycie tokenów i opóźnienie.

Więcej informacji o tym parametrze i jego wpływie na obliczenia tokenów znajdziesz w przewodniku [rozdzielczość multimediów](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl).

## Porady i sprawdzone metody

- Sprawdź, czy obrazy są prawidłowo obrócone.
- Używaj wyraźnych, nierozmytych obrazów.
- Jeśli używasz pojedynczego obrazu z tekstem, umieść prompt tekstowy _po_ części obrazu w tablicy `contents`.

## Co dalej?

Z tego przewodnika dowiesz się, jak przesyłać pliki graficzne i generować dane wyjściowe w postaci tekstu na podstawie danych wejściowych w postaci obrazów. Więcej informacji znajdziesz w tych materiałach:

- [Interfejs Files API:](https://ai.google.dev/gemini-api/docs/files?hl=pl) dowiedz się więcej o przesyłaniu plików i zarządzaniu nimi na potrzeby Gemini.
- [Instrukcje systemowe:](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions)
instrukcje systemowe pozwalają sterować zachowaniem modelu na podstawie konkretnych potrzeb i przypadków użycia.
- [Strategie promptowania plików:](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide) interfejs Gemini API obsługuje promptowanie za pomocą danych tekstowych, obrazów, dźwięku i wideo, czyli promptowanie multimodalne.
- [Wskazówki dotyczące bezpieczeństwa:](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl) modele generatywnej AI czasami tworzą nieoczekiwane wyniki, np. niedokładne, stronnicze lub obraźliwe. Przetwarzanie końcowe i ocena przez weryfikatora są niezbędne, aby ograniczyć ryzyko szkód wynikających z takich danych wyjściowych.

Czy te wskazówki były pomocne?



 Prześlij opinię



O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-02-19 UTC.


Chcesz przekazać coś jeszcze?






\[\[\["Łatwo zrozumieć","easyToUnderstand","thumb-up"\],\["Rozwiązało to mój problem","solvedMyProblem","thumb-up"\],\["Inne","otherUp","thumb-up"\]\],\[\["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"\],\["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"\],\["Nieaktualne treści","outOfDate","thumb-down"\],\["Problem z tłumaczeniem","translationIssue","thumb-down"\],\["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"\],\["Inne","otherDown","thumb-down"\]\],\["Ostatnia aktualizacja: 2026-02-19 UTC."\],\[\],\[\]\]