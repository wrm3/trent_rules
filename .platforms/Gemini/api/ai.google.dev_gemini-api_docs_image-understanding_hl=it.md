[Passa ai contenuti principali](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=it)](https://ai.google.dev/)

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

[Recupera chiave API](https://aistudio.google.com/apikey?hl=it) [Libro di ricette](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=it)

[Accedi](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dit&prompt=select_account)

- Su questa pagina
- [Invio di immagini a Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#image-input)
  - [Trasferimento dei dati delle immagini in linea](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#inline-image)
  - [Caricamento di immagini utilizzando l'API File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#upload-image)
- [Prompt con più immagini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#multiple-images)
- [Rilevamento di oggetti](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#object-detection)
- [Segmentazione](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#segmentation)
- [Formati di immagine supportati](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#supported-formats)
- [Funzionalità](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#capabilities)
- [Limitazioni e informazioni tecniche chiave](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#technical-details-image)
  - [Limite di file](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#file_limit)
  - [Calcolo dei token](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#token_calculation)
  - [Risoluzione dei contenuti multimediali](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#media_resolution)
- [Suggerimenti e best practice](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#tips-best-practices)
- [Passaggi successivi](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#whats-next)


L'anteprima di Gemini 3.1 Flash-Lite è ora disponibile. [Provalo in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=it).




- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Questa pagina è stata utile?



 Invia feedback



# Comprensione delle immagini

- Su questa pagina
- [Invio di immagini a Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#image-input)
  - [Trasferimento dei dati delle immagini in linea](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#inline-image)
  - [Caricamento di immagini utilizzando l'API File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#upload-image)
- [Prompt con più immagini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#multiple-images)
- [Rilevamento di oggetti](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#object-detection)
- [Segmentazione](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#segmentation)
- [Formati di immagine supportati](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#supported-formats)
- [Funzionalità](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#capabilities)
- [Limitazioni e informazioni tecniche chiave](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#technical-details-image)
  - [Limite di file](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#file_limit)
  - [Calcolo dei token](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#token_calculation)
  - [Risoluzione dei contenuti multimediali](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#media_resolution)
- [Suggerimenti e best practice](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#tips-best-practices)
- [Passaggi successivi](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#whats-next)

I modelli Gemini sono progettati per essere multimodali fin dalla base, consentendo un'ampia gamma di attività di elaborazione delle immagini e visione artificiale, tra cui, a titolo esemplificativo, la didascalia, la classificazione e la risposta a domande visive, senza dover addestrare modelli di ML specializzati.

Oltre alle funzionalità multimodali generali, i modelli Gemini offrono
**maggiore precisione** per casi d'uso specifici come il [rilevamento di oggetti](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#object-detection) e la [segmentazione](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#segmentation), grazie a un
addestramento aggiuntivo.

## Invio di immagini a Gemini

Puoi fornire immagini come input a Gemini utilizzando due metodi:

- [Trasmissione di dati di immagini in linea](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#inline-image): ideale per file più piccoli (dimensioni totali della richiesta inferiori a 20 MB, inclusi i prompt).
- [Caricamento di immagini tramite l'API File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#upload-image): consigliato per file di grandi dimensioni o per
riutilizzare le immagini in più richieste.

### Trasferimento dei dati delle immagini in linea

Puoi trasmettere i dati delle immagini in linea nella
richiesta a `generateContent`. Puoi fornire i dati delle immagini come stringhe con codifica Base64 o leggendo direttamente i file locali (a seconda della lingua).

L'esempio seguente mostra come leggere un'immagine da un file locale e passarla
all'API `generateContent` per l'elaborazione.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#rest)Altro

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

Puoi anche recuperare un'immagine da un URL, convertirla in byte e passarla a
`generateContent` come mostrato negli esempi seguenti.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#rest)Altro

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

### Caricamento di immagini utilizzando l'API File

Per file di grandi dimensioni o per poter utilizzare ripetutamente lo stesso file immagine, utilizza l'API Files. Il seguente codice carica un file immagine e poi lo utilizza in una
chiamata a `generateContent`. Per ulteriori informazioni ed esempi, consulta la [guida all'API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#rest)Altro

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

## Prompt con più immagini

Puoi fornire più immagini in un singolo prompt includendo più oggetti
`Part` immagine nell'array `contents`. Questi possono essere un mix di dati in linea
(file locali o URL) e riferimenti all'API File.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#rest)Altro

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

## Rilevamento di oggetti

I modelli vengono addestrati per rilevare gli oggetti in un'immagine e ottenere le coordinate del riquadro di delimitazione. Le coordinate, relative alle dimensioni dell'immagine, vengono scalate a \[0, 1000\]. Devi ridurre la scala di queste coordinate in base
alle dimensioni originali dell'immagine.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#python)Altro

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

Per altri esempi, consulta i seguenti notebook nel [cookbook di Gemini](https://github.com/google-gemini/cookbook):

- [Notebook per la comprensione spaziale 2D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=it)
- [Notebook sperimentale per la navigazione 3D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=it)

## Segmentazione

A partire da Gemini 2.5, i modelli non solo rilevano gli elementi, ma li segmentano
e forniscono le relative maschere di contorno.

Il modello prevede un elenco JSON, in cui ogni elemento rappresenta una maschera di segmentazione.
Ogni elemento ha un riquadro di selezione ("`box_2d`") nel formato `[y0, x0, y1, x1]` con
coordinate normalizzate comprese tra 0 e 1000, un'etichetta ("`label`") che identifica
l'oggetto e infine la maschera di segmentazione all'interno del riquadro di selezione, come PNG codificato in base64
che è una mappa di probabilità con valori compresi tra 0 e 255.
La maschera deve essere ridimensionata in modo che corrisponda alle dimensioni del riquadro di selezione, quindi
binarizzata alla soglia di confidenza (127 per il punto medio).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#python)Altro

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

Per un esempio più dettagliato, consulta l' [esempio di segmentazione](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=it#scrollTo=WQJTJ8wdGOKx) nella guida al cookbook.

![Un tavolo con cupcake, con gli oggetti in legno e vetro evidenziati](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=it)Un esempio di output di segmentazione con oggetti e maschere di segmentazione

## Formati di immagine supportati

Gemini supporta i seguenti tipi MIME di formati di immagine:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

Per scoprire altri metodi di input dei file, consulta la guida
[Metodi di input dei file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it).

## Funzionalità

Tutte le versioni del modello Gemini sono multimodali e possono essere utilizzate in un'ampia gamma di
attività di elaborazione delle immagini e visione artificiale, tra cui, a titolo esemplificativo, la generazione di didascalie per immagini,
domande e risposte visive, classificazione delle immagini, rilevamento e segmentazione degli oggetti.

Gemini può ridurre la necessità di utilizzare modelli di ML specializzati a seconda dei requisiti di qualità e prestazioni.

Le versioni più recenti dei modelli sono addestrate in modo specifico per migliorare l'accuratezza di attività specializzate, oltre alle funzionalità generiche, come il [rilevamento degli oggetti](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#object-detection) e la [segmentazione](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#segmentation) avanzati.

## Limitazioni e informazioni tecniche chiave

### Limite di file

I modelli Gemini supportano un massimo di 3600 file immagine per richiesta.

### Calcolo dei token

- 258 token se entrambe le dimensioni sono <= 384 pixel.
Le immagini più grandi vengono suddivise in riquadri di 768 x 768 pixel, ognuno dei quali costa 258 token.

Una formula approssimativa per calcolare il numero di riquadri è la seguente:

- Calcola la dimensione dell'unità di ritaglio che è approssimativamente: floor(min(width, height) / 1.5).
- Dividi ogni dimensione per la dimensione dell'unità di ritaglio e moltiplica i risultati per ottenere il
numero di riquadri.

Ad esempio, un'immagine di dimensioni 960 x 540 avrebbe una dimensione dell'unità di ritaglio
di 360. Dividi ogni dimensione per 360 e il numero di riquadri è 3 \* 2 = 6.

### Risoluzione dei contenuti multimediali

Gemini 3 introduce un controllo granulare sull'elaborazione della visione multimodale con il parametro
`media_resolution`. Il parametro `media_resolution` determina il
**numero massimo di token allocati per ogni immagine di input o frame video.**
Risoluzioni più elevate migliorano la capacità del modello di
leggere testi piccoli o identificare piccoli dettagli, ma aumentano l'utilizzo di token e la latenza.

Per maggiori dettagli sul parametro e su come può influire sui calcoli dei token,
consulta la guida alla [risoluzione dei contenuti multimediali](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it).

## Suggerimenti e best practice

- Verifica che le immagini siano ruotate correttamente.
- Utilizza immagini chiare e non sfocate.
- Quando utilizzi una singola immagine con testo, posiziona il prompt di testo _dopo_ la parte dell'immagine nell'array `contents`.

## Passaggi successivi

Questa guida mostra come caricare file immagine e generare output di testo da input immagine. Per saperne di più, consulta le seguenti risorse:

- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=it): scopri di più sul caricamento e sulla gestione dei file da utilizzare con Gemini.
- [Istruzioni di sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#system-instructions):
le istruzioni di sistema ti consentono di orientare il comportamento del modello in base alle tue esigenze e ai tuoi casi d'uso specifici.
- [Strategie di prompt dei file](https://ai.google.dev/gemini-api/docs/files?hl=it#prompt-guide): l'API
Gemini supporta i prompt con dati di testo, immagine, audio e video, noti anche come prompt multimodali.
- [Linee guida per la sicurezza](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=it): a volte i modelli di AI generativa producono output inaspettati, ad esempio output imprecisi, distorti o offensivi. Il post-processing e la valutazione umana sono essenziali per
limitare il rischio di danni derivanti da questi output.

Questa pagina è stata utile?



 Invia feedback



Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-02-19 UTC.


Vuoi dirci altro?






\[\[\["Facile da capire","easyToUnderstand","thumb-up"\],\["Il problema è stato risolto","solvedMyProblem","thumb-up"\],\["Altra","otherUp","thumb-up"\]\],\[\["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"\],\["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"\],\["Obsoleti","outOfDate","thumb-down"\],\["Problema di traduzione","translationIssue","thumb-down"\],\["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"\],\["Altra","otherDown","thumb-down"\]\],\["Ultimo aggiornamento 2026-02-19 UTC."\],\[\],\[\]\]