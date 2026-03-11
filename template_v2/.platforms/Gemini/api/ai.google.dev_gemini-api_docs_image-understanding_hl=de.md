[Zum Hauptinhalt springen](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=de)](https://ai.google.dev/)

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

[API-Schlüssel abrufen](https://aistudio.google.com/apikey?hl=de) [Kochbuch](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=de)

[Anmelden](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dde&prompt=select_account)

- Auf dieser Seite
- [Bilder an Gemini übergeben](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#image-input)
  - [Inline-Bilddaten übergeben](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#inline-image)
  - [Bilder mit der File API hochladen](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#upload-image)
- [Prompts mit mehreren Bildern](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#multiple-images)
- [Objekterkennung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#object-detection)
- [Segmentierung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#segmentation)
- [Unterstützte Bildformate](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#supported-formats)
- [Leistungsspektrum](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#capabilities)
- [Einschränkungen und wichtige technische Informationen](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#technical-details-image)
  - [Dateilimit](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#file_limit)
  - [Tokenberechnung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#token_calculation)
  - [Auflösung von Medien](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#media_resolution)
- [Tipps und Best Practices](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#tips-best-practices)
- [Nächste Schritte](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#whats-next)


Gemini 3.1 Flash-Lite ist jetzt als Vorabversion verfügbar. [In AI Studio ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=de)

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

War das hilfreich?



 Feedback geben



# Bildverständnis

- Auf dieser Seite
- [Bilder an Gemini übergeben](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#image-input)
  - [Inline-Bilddaten übergeben](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#inline-image)
  - [Bilder mit der File API hochladen](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#upload-image)
- [Prompts mit mehreren Bildern](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#multiple-images)
- [Objekterkennung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#object-detection)
- [Segmentierung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#segmentation)
- [Unterstützte Bildformate](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#supported-formats)
- [Leistungsspektrum](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#capabilities)
- [Einschränkungen und wichtige technische Informationen](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#technical-details-image)
  - [Dateilimit](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#file_limit)
  - [Tokenberechnung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#token_calculation)
  - [Auflösung von Medien](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#media_resolution)
- [Tipps und Best Practices](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#tips-best-practices)
- [Nächste Schritte](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#whats-next)

Gemini-Modelle sind von Grund auf multimodal konzipiert und ermöglichen eine Vielzahl von Aufgaben im Bereich Bildverarbeitung und Computer Vision, darunter Bilduntertitelung, ‑klassifizierung und Visual Question Answering, ohne dass spezielle ML-Modelle trainiert werden müssen.

Zusätzlich zu ihren allgemeinen multimodalen Funktionen bieten Gemini-Modelle durch zusätzliches Training eine **höhere Genauigkeit** für bestimmte Anwendungsfälle wie [Objekterkennung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#object-detection) und [Segmentierung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#segmentation).

## Bilder an Gemini übergeben

Sie haben zwei Möglichkeiten, Bilder als Eingabe für Gemini bereitzustellen:

- [Inline-Bilddaten übergeben](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#inline-image): Ideal für kleinere Dateien (Gesamtanfragegröße unter 20 MB, einschließlich Prompts).
- [Bilder mit der File API hochladen](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#upload-image): Empfohlen für größere Dateien oder wenn Bilder in mehreren Anfragen wiederverwendet werden sollen.

### Inline-Bilddaten übergeben

Sie können Inline-Bilddaten im Request an `generateContent` übergeben. Sie können Bilddaten als Base64-codierte Strings bereitstellen oder lokale Dateien direkt lesen (je nach Sprache).

Im folgenden Beispiel wird gezeigt, wie ein Bild aus einer lokalen Datei gelesen und zur Verarbeitung an die `generateContent` API übergeben wird.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#rest)Mehr

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

Sie können auch ein Bild von einer URL abrufen, es in Byte konvertieren und an `generateContent` übergeben, wie in den folgenden Beispielen gezeigt.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#rest)Mehr

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

### Bilder mit der File API hochladen

Verwenden Sie für große Dateien oder um dieselbe Bilddatei wiederholt verwenden zu können, die Files API. Mit dem folgenden Code wird eine Bilddatei hochgeladen und dann in einem Aufruf von `generateContent` verwendet. Weitere Informationen und Beispiele finden Sie im [Leitfaden zur Files API](https://ai.google.dev/gemini-api/docs/files?hl=de).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#rest)Mehr

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

## Prompts mit mehreren Bildern

Sie können in einem einzelnen Prompt mehrere Bilder angeben, indem Sie mehrere `Part`-Objekte für Bilder in das `contents`-Array einfügen. Dabei kann es sich um eine Mischung aus Inlinedaten (lokale Dateien oder URLs) und File API-Verweisen handeln.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#rest)Mehr

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

## Objekterkennung

Modelle werden trainiert, um Objekte in einem Bild zu erkennen und die Koordinaten ihrer Begrenzungsrahmen abzurufen. Die Koordinaten werden im Verhältnis zu den Bilddimensionen auf \[0, 1000\] skaliert. Sie müssen diese Koordinaten anhand der Originalbildgröße herunterskalieren.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#python)Mehr

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

Weitere Beispiele finden Sie in den folgenden Notebooks im [Gemini Cookbook](https://github.com/google-gemini/cookbook):

- [Notebook zum räumlichen 2D-Verständnis](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=de)
- [Experimentelles 3D-Zeiger-Notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=de)

## Segmentierung

Ab Gemini 2.5 können Modelle Elemente nicht nur erkennen, sondern auch segmentieren und ihre Konturmasken bereitstellen.

Das Modell sagt eine JSON-Liste voraus, wobei jedes Element eine Segmentierungsmaske darstellt.
Jedes Element hat einen Begrenzungsrahmen („`box_2d`“) im Format `[y0, x0, y1, x1]` mit normalisierten Koordinaten zwischen 0 und 1000, ein Label („`label`“), das das Objekt identifiziert, und schließlich die Segmentierungsmaske innerhalb des Begrenzungsrahmens als Base64-codiertes PNG, das eine Wahrscheinlichkeitskarte mit Werten zwischen 0 und 255 ist.
Die Maske muss an die Abmessungen des umgebenden Rechtecks angepasst und dann mit Ihrem Konfidenzwert (127 für den Mittelpunkt) binarisiert werden.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#python)Mehr

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

Ein detaillierteres Beispiel finden Sie im [Segmentierungsbeispiel](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=de#scrollTo=WQJTJ8wdGOKx) im Cookbook-Leitfaden.

![Ein Tisch mit Cupcakes, auf dem die Holz- und Glasobjekte hervorgehoben sind](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=de)Beispiel für eine Segmentierungsausgabe mit Objekten und Segmentierungsmasken

## Unterstützte Bildformate

Gemini unterstützt die folgenden MIME-Typen für Bildformate:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC – `image/heic`
- HEIF - `image/heif`

Informationen zu anderen Methoden für die Dateieingabe finden Sie im Leitfaden [Methoden für die Dateieingabe](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de).

## Leistungsspektrum

Alle Gemini-Modellversionen sind multimodal und können für eine Vielzahl von Bildverarbeitungs- und Computer Vision-Aufgaben verwendet werden, darunter Bildunterschriftung, visuelle Frage- und Antwortaufgaben, Bildklassifizierung, Objekterkennung und Segmentierung.

Je nach Ihren Qualitäts- und Leistungsanforderungen kann Gemini die Notwendigkeit reduzieren, spezielle ML-Modelle zu verwenden.

Die neuesten Modellversionen werden speziell trainiert, um die Genauigkeit von spezialisierten Aufgaben zusätzlich zu generischen Funktionen wie verbesserter [Objekterkennung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#object-detection) und [Segmentierung](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de#segmentation) zu verbessern.

## Einschränkungen und wichtige technische Informationen

### Dateilimit

Gemini-Modelle unterstützen maximal 3.600 Bilddateien pro Anfrage.

### Tokenberechnung

- 258 Tokens, wenn beide Dimensionen kleiner oder gleich 384 Pixel sind.
Größere Bilder werden in Kacheln mit 768 × 768 Pixeln aufgeteilt, die jeweils 258 Tokens kosten.

Eine ungefähre Formel zur Berechnung der Anzahl der Kacheln lautet so:

- Berechne die Größe der Zuschneideeinheit, die ungefähr so aussieht: floor(min(width, height) / 1,5).
- Teilen Sie jede Dimension durch die Größe der Zuschneideeinheit und multiplizieren Sie die Ergebnisse, um die Anzahl der Kacheln zu erhalten.

Ein Bild mit den Abmessungen 960 × 540 hätte beispielsweise eine Zuschneideeinheit von 360. Teilen Sie jede Dimension durch 360. Die Anzahl der Kacheln beträgt 3 × 2 = 6.

### Auflösung von Medien

Mit Gemini 3 wird die multimodale Bildverarbeitung durch den Parameter `media_resolution` detaillierter gesteuert. Der Parameter `media_resolution` bestimmt die **maximale Anzahl von Tokens, die pro Eingabebild oder Videoframes zugewiesen werden**.
Höhere Auflösungen verbessern die Fähigkeit des Modells, feinen Text zu lesen oder kleine Details zu erkennen, erhöhen aber die Token-Nutzung und die Latenz.

Weitere Informationen zum Parameter und dazu, wie er sich auf die Tokenberechnung auswirken kann, finden Sie im [Leitfaden zur Media-Auflösung](https://ai.google.dev/gemini-api/docs/media-resolution?hl=de).

## Tipps und Best Practices

- Prüfen Sie, ob die Bilder richtig gedreht sind.
- Verwenden Sie klare, nicht verschwommene Bilder.
- Wenn Sie ein einzelnes Bild mit Text verwenden, platzieren Sie den Text-Prompt _nach_ dem Bildteil im `contents`-Array.

## Nächste Schritte

In diesem Leitfaden erfahren Sie, wie Sie Bilddateien hochladen und Textausgaben aus Bildeingaben generieren. Weitere Informationen finden Sie in den folgenden Ressourcen:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de): Hier finden Sie weitere Informationen zum Hochladen und Verwalten von Dateien für die Verwendung mit Gemini.
- [Systemanweisungen](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#system-instructions): Mit Systemanweisungen können Sie das Verhalten des Modells entsprechend Ihren spezifischen Anforderungen und Anwendungsfällen steuern.
- [Strategien für Dateiprompts](https://ai.google.dev/gemini-api/docs/files?hl=de#prompt-guide): Die Gemini API unterstützt Prompts mit Text-, Bild-, Audio- und Videodaten, auch als multimodale Prompts bezeichnet.
- [Sicherheitshinweise](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=de): Generative KI-Modelle können manchmal unerwartete Ausgaben liefern, z. B. ungenaue, voreingenommene oder anstößige Ausgaben. Die Nachbearbeitung und menschliche Bewertung sind unerlässlich, um das Risiko von Schäden durch solche Ausgaben zu begrenzen.

War das hilfreich?



 Feedback geben



Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-02-19 (UTC).


Haben Sie Feedback für uns?






\[\[\["Leicht verständlich","easyToUnderstand","thumb-up"\],\["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"\],\["Sonstiges","otherUp","thumb-up"\]\],\[\["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"\],\["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"\],\["Nicht mehr aktuell","outOfDate","thumb-down"\],\["Problem mit der Übersetzung","translationIssue","thumb-down"\],\["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"\],\["Sonstiges","otherDown","thumb-down"\]\],\["Zuletzt aktualisiert: 2026-02-19 (UTC)."\],\[\],\[\]\]