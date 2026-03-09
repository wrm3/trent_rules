[Passer au contenu principal](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=fr)](https://ai.google.dev/)

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

[Obtenir une clé API](https://aistudio.google.com/apikey?hl=fr) [Liste de recettes](https://github.com/google-gemini/cookbook) [Communauté](https://discuss.ai.google.dev/c/gemini-api/?hl=fr)

[Connexion](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dfr&prompt=select_account)

- Sur cette page
- [Transmettre des images à Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#image-input)
  - [Transmettre des données d'image intégrées](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#inline-image)
  - [Importer des images à l'aide de l'API File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#upload-image)
- [Créer des requêtes avec plusieurs images](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#multiple-images)
- [Détection d'objets](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#object-detection)
- [Segmentation](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#segmentation)
- [Formats d'image compatibles](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#supported-formats)
- [Capacités](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#capabilities)
- [Limites et informations techniques clés](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#technical-details-image)
  - [Limite de fichiers](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#file_limit)
  - [Calcul des jetons](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#token_calculation)
  - [Résolution du contenu multimédia](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#media_resolution)
- [Conseils et bonnes pratiques](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#tips-best-practices)
- [Étape suivante](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#whats-next)


La version Preview de Gemini 3.1 Flash-Lite est désormais disponible. [Essayez-le dans AI Studio.](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=fr)

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Ce contenu vous a-t-il été utile ?



 Envoyer des commentaires



# Compréhension des images

- Sur cette page
- [Transmettre des images à Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#image-input)
  - [Transmettre des données d'image intégrées](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#inline-image)
  - [Importer des images à l'aide de l'API File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#upload-image)
- [Créer des requêtes avec plusieurs images](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#multiple-images)
- [Détection d'objets](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#object-detection)
- [Segmentation](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#segmentation)
- [Formats d'image compatibles](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#supported-formats)
- [Capacités](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#capabilities)
- [Limites et informations techniques clés](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#technical-details-image)
  - [Limite de fichiers](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#file_limit)
  - [Calcul des jetons](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#token_calculation)
  - [Résolution du contenu multimédia](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#media_resolution)
- [Conseils et bonnes pratiques](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#tips-best-practices)
- [Étape suivante](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#whats-next)

Les modèles Gemini sont conçus pour être multimodaux dès le départ, ce qui permet d'effectuer un large éventail de tâches de traitement d'images et de vision par ordinateur, y compris, mais sans s'y limiter, la création de légendes d'images, la classification et les systèmes de questions-réponses visuelles, sans avoir à entraîner des modèles de ML spécialisés.

En plus de leurs capacités multimodales générales, les modèles Gemini offrent une **précision améliorée** pour des cas d'utilisation spécifiques tels que la [détection d'objets](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#object-detection) et la [segmentation](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#segmentation), grâce à un entraînement supplémentaire.

## Transmettre des images à Gemini

Vous pouvez fournir des images en entrée à Gemini de deux manières :

- [Transmettre des données d'image intégrées](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#inline-image) : idéal pour les fichiers plus petits (taille totale de la requête inférieure à 20 Mo, y compris les requêtes).
- [Importer des images à l'aide de l'API File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#upload-image) : recommandé pour les fichiers volumineux ou pour réutiliser des images dans plusieurs requêtes.

### Transmettre des données d'image intégrées

Vous pouvez transmettre des données d'image intégrées dans la requête à `generateContent`. Vous pouvez fournir des données d'image sous forme de chaînes encodées en base64 ou en lisant directement les fichiers locaux (selon la langue).

L'exemple suivant montre comment lire une image à partir d'un fichier local et la transmettre à l'API `generateContent` pour traitement.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#rest)Plus

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

Vous pouvez également extraire une image à partir d'une URL, la convertir en octets et la transmettre à `generateContent`, comme illustré dans les exemples suivants.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#rest)Plus

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

### Importer des images à l'aide de l'API File

Pour les fichiers volumineux ou pour pouvoir utiliser le même fichier image à plusieurs reprises, utilisez l'API Files. Le code suivant importe un fichier image, puis l'utilise dans un appel à `generateContent`. Pour en savoir plus et obtenir des exemples, consultez le [guide de l'API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#rest)Plus

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

## Créer des requêtes avec plusieurs images

Vous pouvez fournir plusieurs images dans une même requête en incluant plusieurs objets `Part` dans le tableau `contents`. Il peut s'agir d'un mélange de données intégrées (fichiers locaux ou URL) et de références à l'API File.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#rest)Plus

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

## Détection d'objets

Les modèles sont entraînés à détecter des objets dans une image et à obtenir les coordonnées de leur cadre de délimitation. Les coordonnées, par rapport aux dimensions de l'image, sont mises à l'échelle de 0 à 1 000. Vous devez redimensionner ces coordonnées en fonction de la taille de votre image d'origine.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#python)Plus

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

Pour obtenir d'autres exemples, consultez les notebooks suivants dans le [Gemini Cookbook](https://github.com/google-gemini/cookbook) :

- [Notebook sur la compréhension spatiale 2D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=fr)
- [Notebook expérimental de pointage 3D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=fr)

## Segmentation

À partir de Gemini 2.5, les modèles détectent les éléments, mais les segmentent également et fournissent leurs masques de contour.

Le modèle prédit une liste JSON, où chaque élément représente un masque de segmentation.
Chaque élément possède un cadre de délimitation ("`box_2d`") au format `[y0, x0, y1, x1]` avec des coordonnées normalisées comprises entre 0 et 1 000, un libellé ("`label`") qui identifie l'objet et enfin le masque de segmentation à l'intérieur du cadre de délimitation, sous forme de fichier PNG encodé en base64 qui est une carte de probabilité avec des valeurs comprises entre 0 et 255.
Le masque doit être redimensionné pour correspondre aux dimensions du cadre de délimitation, puis binarisé à votre seuil de confiance (127 pour le point médian).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#python)Plus

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

Pour obtenir un exemple plus détaillé, consultez l' [exemple de segmentation](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=fr#scrollTo=WQJTJ8wdGOKx) dans le guide du cookbook.

![Table avec des cupcakes, avec les objets en bois et en verre mis en évidence](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=fr)Exemple de résultat de segmentation avec des objets et des masques de segmentation

## Formats d'image compatibles

Gemini est compatible avec les types MIME suivants pour les formats d'image :

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC : `image/heic`
- HEIF - `image/heif`

Pour en savoir plus sur les autres méthodes de saisie de fichiers, consultez le guide [Méthodes de saisie de fichiers](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fr).

## Capacités

Toutes les versions du modèle Gemini sont multimodales et peuvent être utilisées dans un large éventail de tâches de traitement d'images et de vision par ordinateur, y compris, mais sans s'y limiter, le sous-titrage d'images, les questions et réponses visuelles, la classification d'images, la détection d'objets et la segmentation.

Gemini peut réduire la nécessité d'utiliser des modèles de ML spécialisés en fonction de vos exigences en termes de qualité et de performances.

Les dernières versions des modèles sont spécifiquement entraînées pour améliorer la précision des tâches spécialisées en plus des capacités génériques, comme la [détection](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#object-detection) et la [segmentation](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fr#segmentation) d'objets améliorées.

## Limites et informations techniques clés

### Limite de fichiers

Les modèles Gemini acceptent un maximum de 3 600 fichiers image par requête.

### Calcul des jetons

- 258 jetons si les deux dimensions sont inférieures ou égales à 384 pixels.
Les images plus grandes sont divisées en vignettes de 768 x 768 pixels, chacune coûtant 258 jetons.

Voici une formule approximative pour calculer le nombre de tuiles :

- Calculez la taille de l'unité de recadrage, qui est approximativement égale à : floor(min(width, height) / 1.5).
- Divisez chaque dimension par la taille de l'unité de recadrage, puis multipliez les résultats pour obtenir le nombre de tuiles.

Par exemple, pour une image de dimensions 960 x 540, la taille de l'unité de recadrage serait de 360. Divisez chaque dimension par 360. Le nombre de tuiles est alors de 3 \* 2 = 6.

### Résolution du contenu multimédia

Gemini 3 introduit un contrôle précis sur le traitement de la vision multimodale avec le paramètre `media_resolution`. Le paramètre `media_resolution` détermine le **nombre maximal de jetons alloués par image ou frame vidéo en entrée**.
Les résolutions plus élevées améliorent la capacité du modèle à lire du texte fin ou à identifier de petits détails, mais augmentent l'utilisation de jetons et la latence.

Pour en savoir plus sur le paramètre et son impact sur le calcul des jetons, consultez le guide sur la [résolution du contenu multimédia](https://ai.google.dev/gemini-api/docs/media-resolution?hl=fr).

## Conseils et bonnes pratiques

- Vérifiez que les images sont correctement orientées.
- Utilisez des images claires et non floues.
- Lorsque vous utilisez une seule image avec du texte, placez le prompt textuel _après_ la partie image dans le tableau `contents`.

## Étape suivante

Ce guide vous explique comment importer des fichiers image et générer des sorties de texte à partir d'entrées d'image. Pour en savoir plus, consultez les ressources suivantes :

- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) : découvrez comment importer et gérer des fichiers à utiliser avec Gemini.
- [Instructions système](https://ai.google.dev/gemini-api/docs/text-generation?hl=fr#system-instructions) : elles vous permettent d'orienter le comportement du modèle en fonction de vos besoins et de vos cas d'utilisation spécifiques.
- [Stratégies d'incitation pour les fichiers](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide) : l'API Gemini est compatible avec les incitations utilisant des données textuelles, d'image, audio et vidéo, également appelées incitations multimodales.
- [Consignes de sécurité](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=fr) : les modèles d'IA générative produisent parfois des résultats inattendus, par exemple inexacts, biaisés ou choquants. Le post-traitement et l'évaluation humaine sont essentiels pour limiter le risque de préjudice lié à ces résultats.

Ce contenu vous a-t-il été utile ?



 Envoyer des commentaires



Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/02/19 (UTC).


Voulez-vous nous donner plus d'informations ?






\[\[\["Facile à comprendre","easyToUnderstand","thumb-up"\],\["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"\],\["Autre","otherUp","thumb-up"\]\],\[\["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"\],\["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"\],\["Obsolète","outOfDate","thumb-down"\],\["Problème de traduction","translationIssue","thumb-down"\],\["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"\],\["Autre","otherDown","thumb-down"\]\],\["Dernière mise à jour le 2026/02/19 (UTC)."\],\[\],\[\]\]