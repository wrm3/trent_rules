[Kapërce te përmbajtja kryesore](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=sq)](https://ai.google.dev/)

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

[Merr çelësin API](https://aistudio.google.com/apikey?hl=sq) [Libër gatimi](https://github.com/google-gemini/cookbook) [Komuniteti](https://discuss.ai.google.dev/c/gemini-api/?hl=sq)

[Identifikohu](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dsq&prompt=select_account)

- Në këtë faqe
- [Kalimi i imazheve te Binjakët](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#image-input)
  - [Duke kaluar të dhënat e imazhit në linjë](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#inline-image)
  - [Ngarkimi i imazheve duke përdorur API-n e Skedarëve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#upload-image)
- [Nxitje me imazhe të shumta](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#multiple-images)
- [Zbulimi i objekteve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#object-detection)
- [Segmentimi](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#segmentation)
- [Formatet e imazheve të mbështetura](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#supported-formats)
- [Aftësitë](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#capabilities)
- [Kufizimet dhe informacionet kryesore teknike](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#technical-details-image)
  - [Limiti i skedarëve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#file_limit)
  - [Llogaritja e tokenëve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#token_calculation)
  - [Rezolucioni i medias](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#media_resolution)
- [Këshilla dhe praktikat më të mira](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#tips-best-practices)
- [Çfarë vjen më pas](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#whats-next)

Pamja paraprake e Gemini 3.1 Flash-Lite është tani e disponueshme. [Provojeni në AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=sq) .


![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Kjo faqe është përkthyer nga [Cloud Translation API](https://cloud.google.com/translate/?hl=sq).


Switch to English


- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet, Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Ishte e dobishme?



 Dërgo komente



# Kuptimi i imazhit

- Në këtë faqe
- [Kalimi i imazheve te Binjakët](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#image-input)
  - [Duke kaluar të dhënat e imazhit në linjë](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#inline-image)
  - [Ngarkimi i imazheve duke përdorur API-n e Skedarëve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#upload-image)
- [Nxitje me imazhe të shumta](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#multiple-images)
- [Zbulimi i objekteve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#object-detection)
- [Segmentimi](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#segmentation)
- [Formatet e imazheve të mbështetura](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#supported-formats)
- [Aftësitë](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#capabilities)
- [Kufizimet dhe informacionet kryesore teknike](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#technical-details-image)
  - [Limiti i skedarëve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#file_limit)
  - [Llogaritja e tokenëve](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#token_calculation)
  - [Rezolucioni i medias](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#media_resolution)
- [Këshilla dhe praktikat më të mira](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#tips-best-practices)
- [Çfarë vjen më pas](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#whats-next)

Modelet Gemini janë ndërtuar për të qenë multimodale që nga themelet, duke zhbllokuar një gamë të gjerë detyrash të përpunimit të imazheve dhe vizionit kompjuterik, duke përfshirë, por pa u kufizuar në, mbishkrimin e imazheve, klasifikimin dhe përgjigjen e pyetjeve vizuale pa pasur nevojë të trajnohen modele të specializuara të ML.

Përveç aftësive të tyre të përgjithshme multimodale, modelet Gemini ofrojnë **saktësi të përmirësuar** për raste specifike përdorimi si [zbulimi](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#object-detection) dhe [segmentimi i](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#segmentation) objekteve, përmes trajnimit shtesë.

## Kalimi i imazheve te Binjakët

Ju mund të jepni imazhe si të dhëna për Gemini duke përdorur dy metoda:

- [Kalimi i të dhënave të imazhit në linjë](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#inline-image) : Ideale për skedarë më të vegjël (madhësia totale e kërkesës më pak se 20MB, duke përfshirë kërkesat).
- [Ngarkimi i imazheve duke përdorur File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#upload-image) : Rekomandohet për skedarë më të mëdhenj ose për ripërdorimin e imazheve në kërkesa të shumëfishta.

### Duke kaluar të dhënat e imazhit në linjë

Mund të kaloni të dhëna të imazhit brenda rreshtit në kërkesën për `generateContent` . Mund të jepni të dhëna të imazhit si vargje të koduara Base64 ose duke lexuar skedarë lokalë direkt (në varësi të gjuhës).

Shembulli i mëposhtëm tregon se si të lexohet një imazh nga një skedar lokal dhe t'ia kalohet API-t `generateContent` për përpunim.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#pushtim)Më shumë

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

Gjithashtu mund të merrni një imazh nga një URL, ta konvertoni atë në bajt dhe ta kaloni te `generateContent` siç tregohet në shembujt e mëposhtëm.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#pushtim)Më shumë

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

### Ngarkimi i imazheve duke përdorur API-n e Skedarëve

Për skedarë të mëdhenj ose për të qenë në gjendje të përdorni të njëjtin skedar imazhi në mënyrë të përsëritur, përdorni Files API. Kodi i mëposhtëm ngarkon një skedar imazhi dhe më pas e përdor skedarin në një thirrje për `generateContent` . Shihni [udhëzuesin e Files API](https://ai.google.dev/gemini-api/docs/files?hl=sq) për më shumë informacion dhe shembuj.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#pushtim)Më shumë

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

## Nxitje me imazhe të shumta

Mund të ofroni imazhe të shumëfishta në një kërkesë të vetme duke përfshirë objekte të shumëfishta `Part` së Imazhit në vargun e `contents` . Këto mund të jenë një përzierje e të dhënave të integruara (skedarë lokalë ose URL) dhe referencave të API-t të Skedarëve.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#pushtim)Më shumë

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

## Zbulimi i objekteve

Modelet janë të trajnuara për të zbuluar objektet në një imazh dhe për të marrë koordinatat e tyre të kutisë kufizuese. Koordinatat, në lidhje me dimensionet e imazhit, shkallëzohen në \[0, 1000\]. Ju duhet t'i hiqni shkallën këtyre koordinatave bazuar në madhësinë origjinale të imazhit tuaj.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#python)Më shumë

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

Për më shumë shembuj, shikoni fletoret e mëposhtme në [Librin e Gatimit Gemini](https://github.com/google-gemini/cookbook) :

- [Fletore për të kuptuarit hapësinor 2D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=sq)
- [Fletore eksperimentale me drejtim 3D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=sq)

## Segmentimi

Duke filluar me Gemini 2.5, modelet jo vetëm që zbulojnë artikujt, por edhe i segmentojnë ato dhe ofrojnë maskat e tyre të konturit.

Modeli parashikon një listë JSON, ku çdo artikull përfaqëson një maskë segmentimi. Çdo artikull ka një kuti kufizuese (" `box_2d` ") në formatin `[y0, x0, y1, x1]` me koordinata të normalizuara midis 0 dhe 1000, një etiketë (" `label` ") që identifikon objektin dhe së fundmi maskën e segmentimit brenda kutisë kufizuese, si png e koduar me bazë 64 që është një hartë probabiliteti me vlera midis 0 dhe 255. Maska duhet të ridimensionohet që të përputhet me dimensionet e kutisë kufizuese, pastaj të binarizohet në pragun tuaj të besimit (127 për pikën e mesit).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#python)Më shumë

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

Shikoni [shembullin e segmentimit](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=sq#scrollTo=WQJTJ8wdGOKx) në udhëzuesin e librit të gatimit për një shembull më të detajuar.

![Një tavolinë me kekë të vegjël, me objektet prej druri dhe qelqi të theksuara](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=sq) Një shembull i një rezultati segmentimi me objekte dhe maska ​​segmentimi

## Formatet e imazheve të mbështetura

Gemini mbështet llojet e mëposhtme MIME të formateve të imazhit:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

Për të mësuar rreth metodave të tjera të futjes së skedarëve, shihni udhëzuesin e [metodave të futjes së skedarëve](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=sq) .

## Aftësitë

Të gjitha versionet e modelit Gemini janë multimodale dhe mund të përdoren në një gamë të gjerë të detyrave të përpunimit të imazheve dhe vizionit kompjuterik, duke përfshirë, por pa u kufizuar në, mbishkrimin e imazheve, pyetjet dhe përgjigjet vizuale, klasifikimin e imazheve, zbulimin dhe segmentimin e objekteve.

Gemini mund të zvogëlojë nevojën për të përdorur modele të specializuara të ML në varësi të kërkesave tuaja të cilësisë dhe performancës.

Versionet më të fundit të modelit janë trajnuar posaçërisht për të përmirësuar saktësinë e detyrave të specializuara, përveç aftësive gjenerike, si [zbulimi](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#object-detection) dhe [segmentimi](https://ai.google.dev/gemini-api/docs/image-understanding?hl=sq#segmentation) i përmirësuar i objekteve.

## Kufizimet dhe informacionet kryesore teknike

### Limiti i skedarëve

Modelet Gemini mbështesin një maksimum prej 3,600 skedarësh imazhesh për kërkesë.

### Llogaritja e tokenëve

- 258 tokena nëse të dy dimensionet janë <= 384 piksel. Imazhet më të mëdha ndahen në pllaka me 768x768 piksel, secila me 258 tokena.

Një formulë e përafërt për llogaritjen e numrit të pllakave është si më poshtë:

- Llogarit madhësinë e njësisë së të korrave e cila është afërsisht: dyshemeja (min(gjerësia, lartësia) / 1.5).
- Pjesëtoni çdo dimension me madhësinë e njësisë së prerjes dhe shumëzojeni së bashku për të marrë numrin e pllakave.

Për shembull, për një imazh me dimensione 960x540, madhësia e njësisë së prerjes do të jetë 360. Pjesëtoni çdo dimension me 360 ​​dhe numri i pllakave është 3 \* 2 = 6.

### Rezolucioni i medias

Gemini 3 prezanton kontroll të detajuar mbi përpunimin e vizionit multimodal me parametrin `media_resolution` . Parametri `media_resolution` përcakton **numrin maksimal të tokenëve të alokuar për imazh hyrës ose kornizë video.** Rezolucionet më të larta përmirësojnë aftësinë e modelit për të lexuar tekst të imët ose për të identifikuar detaje të vogla, por rrisin përdorimin e tokenëve dhe vonesën.

Për më shumë detaje rreth parametrit dhe se si mund të ndikojë në llogaritjet e tokenëve, shihni udhëzuesin e [rezolucionit të medias](https://ai.google.dev/gemini-api/docs/media-resolution?hl=sq) .

## Këshilla dhe praktikat më të mira

- Verifikoni që imazhet janë rrotulluar saktë.
- Përdorni imazhe të qarta, jo të turbullta.
- Kur përdorni një imazh të vetëm me tekst, vendosni njoftimin e tekstit _pas_ pjesës së imazhit në vargun e `contents` .

## Çfarë vjen më pas

Ky udhëzues ju tregon se si të ngarkoni skedarë imazhesh dhe të gjeneroni rezultate teksti nga të dhënat e futura të imazheve. Për të mësuar më shumë, shihni burimet e mëposhtme:

- [API-t e skedarëve](https://ai.google.dev/gemini-api/docs/files?hl=sq) : Mësoni më shumë rreth ngarkimit dhe menaxhimit të skedarëve për përdorim me Gemini.
- [Udhëzimet e sistemit](https://ai.google.dev/gemini-api/docs/text-generation?hl=sq#system-instructions) : Udhëzimet e sistemit ju lejojnë të drejtoni sjelljen e modelit bazuar në nevojat dhe rastet tuaja specifike të përdorimit.
- [Strategjitë e nxitjes së skedarëve](https://ai.google.dev/gemini-api/docs/files?hl=sq#prompt-guide) : API Gemini mbështet nxitjen me të dhëna teksti, imazhi, audio dhe video, të njohura edhe si nxitje multimodale.
- [Udhëzime për sigurinë](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=sq) : Ndonjëherë modelet gjeneruese të IA-së prodhojnë rezultate të papritura, të tilla si rezultate që janë të pasakta, të anshme ose fyese. Përpunimi pasues dhe vlerësimi njerëzor janë thelbësorë për të kufizuar rrezikun e dëmtimit nga rezultate të tilla.

Ishte e dobishme?



 Dërgo komente



Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-02-19 UTC.


Duhet të na tregosh më shumë?






\[\[\["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"\],\["E zgjidhi problemin tim","solvedMyProblem","thumb-up"\],\["Tjetër","otherUp","thumb-up"\]\],\[\["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"\],\["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"\],\["E papërditësuar","outOfDate","thumb-down"\],\["Problem përkthimi","translationIssue","thumb-down"\],\["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"\],\["Tjetër","otherDown","thumb-down"\]\],\["Përditësimi i fundit: 2026-02-19 UTC."\],\[\],\[\]\]