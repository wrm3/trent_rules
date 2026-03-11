[Ir al contenido principal](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=es-419)](https://ai.google.dev/)

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

[Cómo obtener una clave de API](https://aistudio.google.com/apikey?hl=es-419) [Guía de soluciones](https://github.com/google-gemini/cookbook) [Comunidad](https://discuss.ai.google.dev/c/gemini-api/?hl=es-419)

[Acceder](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Des-419&prompt=select_account)

- En esta página
- [Cómo pasar imágenes a Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#image-input)
  - [Cómo pasar datos de imágenes intercaladas](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#inline-image)
  - [Cómo subir imágenes con la API de File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#upload-image)
- [Instrucciones con varias imágenes](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#multiple-images)
- [Detección de objetos](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#object-detection)
- [Segmentación](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#segmentation)
- [Formatos de imagen compatibles](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#supported-formats)
- [Funciones](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#capabilities)
- [Limitaciones e información técnica clave](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#technical-details-image)
  - [Límite de archivos](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#file_limit)
  - [Cálculo de tokens](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#token_calculation)
  - [Resolución de medios](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#media_resolution)
- [Sugerencias y prácticas recomendadas](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#tips-best-practices)
- [¿Qué sigue?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#whats-next)


Ya está disponible la versión preliminar de Gemini 3.1 Flash-Lite. [Pruébalo en AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=es-419).




- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

¿Te resultó útil?



 Enviar comentarios



# Comprensión de imágenes

- En esta página
- [Cómo pasar imágenes a Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#image-input)
  - [Cómo pasar datos de imágenes intercaladas](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#inline-image)
  - [Cómo subir imágenes con la API de File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#upload-image)
- [Instrucciones con varias imágenes](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#multiple-images)
- [Detección de objetos](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#object-detection)
- [Segmentación](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#segmentation)
- [Formatos de imagen compatibles](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#supported-formats)
- [Funciones](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#capabilities)
- [Limitaciones e información técnica clave](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#technical-details-image)
  - [Límite de archivos](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#file_limit)
  - [Cálculo de tokens](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#token_calculation)
  - [Resolución de medios](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#media_resolution)
- [Sugerencias y prácticas recomendadas](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#tips-best-practices)
- [¿Qué sigue?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#whats-next)

Los modelos de Gemini se desarrollaron desde cero para ser multimodales, lo que permite realizar una amplia variedad de tareas de procesamiento de imágenes y visión artificial, como la creación de leyendas de imágenes, la clasificación y la búsqueda de respuestas visuales, sin necesidad de entrenar modelos de AA especializados.

Además de sus capacidades multimodales generales, los modelos de Gemini ofrecen una **mayor precisión** para casos de uso específicos, como la [detección de objetos](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#object-detection) y la [segmentación](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#segmentation), a través de entrenamiento adicional.

## Cómo pasar imágenes a Gemini

Puedes proporcionar imágenes como entrada a Gemini de dos maneras:

- [Paso de datos de imágenes intercaladas](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#inline-image): Es ideal para archivos más pequeños (tamaño total de la solicitud inferior a 20 MB, incluidas las instrucciones).
- [Cómo subir imágenes con la API de File](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#upload-image): Se recomienda para archivos más grandes o para reutilizar imágenes en varias solicitudes.

### Cómo pasar datos de imágenes intercaladas

Puedes pasar datos de imágenes intercaladas en la solicitud a `generateContent`. Puedes proporcionar datos de imagen como cadenas codificadas en Base64 o leyendo archivos locales directamente (según el lenguaje).

En el siguiente ejemplo, se muestra cómo leer una imagen de un archivo local y pasarla a la API de `generateContent` para su procesamiento.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#rest)Más

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

También puedes recuperar una imagen de una URL, convertirla en bytes y pasarla a `generateContent`, como se muestra en los siguientes ejemplos.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#rest)Más

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

### Cómo subir imágenes con la API de File

Para archivos grandes o para poder usar el mismo archivo de imagen varias veces, usa la API de Files. El siguiente código sube un archivo de imagen y, luego, lo usa en una llamada a `generateContent`. Consulta la [guía de la API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419) para obtener más información y ejemplos.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#rest)Más

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

## Instrucciones con varias imágenes

Puedes proporcionar varias imágenes en una sola instrucción incluyendo varios objetos `Part` de imagen en el array `contents`. Pueden ser una combinación de datos intercalados (archivos locales o URLs) y referencias a la API de File.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#rest)Más

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

## Detección de objetos

Los modelos se entrenan para detectar objetos en una imagen y obtener las coordenadas de sus cuadros delimitadores. Las coordenadas, relativas a las dimensiones de la imagen, se ajustan a una escala de \[0, 1000\]. Debes ajustar estas coordenadas según el tamaño de tu imagen original.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#python)Más

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

Para obtener más ejemplos, consulta los siguientes notebooks en la [guía de soluciones de Gemini](https://github.com/google-gemini/cookbook):

- [Notebook de comprensión espacial 2D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=es-419)
- [Notebook experimental de apuntado en 3D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=es-419)

## Segmentación

A partir de Gemini 2.5, los modelos no solo detectan elementos, sino que también los segmentan y proporcionan sus máscaras de contorno.

El modelo predice una lista JSON, en la que cada elemento representa una máscara de segmentación.
Cada elemento tiene un cuadro de límite (“`box_2d`”) en el formato `[y0, x0, y1, x1]` con coordenadas normalizadas entre 0 y 1,000, una etiqueta (“`label`”) que identifica el objeto y, por último, la máscara de segmentación dentro del cuadro de límite, como un PNG codificado en base64 que es un mapa de probabilidad con valores entre 0 y 255.
La máscara debe cambiar de tamaño para que coincida con las dimensiones del cuadro delimitador y, luego, se debe binarizar en el umbral de confianza (127 para el punto medio).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#python)Más

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

Consulta el [ejemplo de segmentación](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=es-419#scrollTo=WQJTJ8wdGOKx) en la guía de recetas para ver un ejemplo más detallado.

![Una mesa con cupcakes, con los objetos de madera y vidrio destacados](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=es-419)Un ejemplo de resultado de segmentación con objetos y máscaras de segmentación

## Formatos de imagen compatibles

Gemini admite los siguientes tipos de MIME de formato de imagen:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC: `image/heic`
- HEIF - `image/heif`

Para obtener información sobre otros métodos de entrada de archivos, consulta la guía [Métodos de entrada de archivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419).

## Funciones

Todas las versiones del modelo de Gemini son multimodales y se pueden utilizar en una amplia variedad de tareas de procesamiento de imágenes y visión artificial, como subtitulado de imágenes, búsqueda de respuestas visuales, clasificación de imágenes, detección de objetos y segmentación.

Gemini puede reducir la necesidad de usar modelos de AA especializados según tus requisitos de calidad y rendimiento.

Las versiones de modelos más recientes se entrenan específicamente para mejorar la precisión de las tareas especializadas, además de las capacidades genéricas, como la [detección](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#object-detection) y la [segmentación](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#segmentation) de objetos mejoradas.

## Limitaciones e información técnica clave

### Límite de archivos

Los modelos de Gemini admiten un máximo de 3,600 archivos de imagen por solicitud.

### Cálculo de tokens

- 258 tokens si ambas dimensiones son <= 384 píxeles
Las imágenes más grandes se dividen en mosaicos de 768 x 768 píxeles, y cada uno cuesta 258 tokens.

Una fórmula aproximada para calcular la cantidad de mosaicos es la siguiente:

- Calcula el tamaño de la unidad de recorte, que es aproximadamente floor(min(ancho, alto) / 1.5).
- Divide cada dimensión por el tamaño de la unidad de recorte y multiplícalas para obtener la cantidad de mosaicos.

Por ejemplo, una imagen de 960 x 540 tendría un tamaño de unidad de recorte de 360. Divide cada dimensión por 360, y la cantidad de mosaicos es 3 \* 2 = 6.

### Resolución de medios

Gemini 3 introduce un control detallado sobre el procesamiento de la visión multimodal con el parámetro `media_resolution`. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.**
Las resoluciones más altas mejoran la capacidad del modelo para leer texto pequeño o identificar detalles, pero aumentan el uso de tokens y la latencia.

Para obtener más detalles sobre el parámetro y cómo puede afectar los cálculos de tokens, consulta la guía de [resolución de medios](https://ai.google.dev/gemini-api/docs/media-resolution?hl=es-419).

## Sugerencias y prácticas recomendadas

- Verifica que las imágenes se roten correctamente.
- Usa imágenes claras y no borrosas.
- Cuando uses una sola imagen con texto, coloca la instrucción de texto _después_ de la parte de la imagen en el array `contents`.

## ¿Qué sigue?

En esta guía, se muestra cómo subir archivos de imagen y generar resultados de texto a partir de entradas de imágenes. Para obtener más información, consulta los siguientes recursos:

- [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419): Obtén más información para subir y administrar archivos para usarlos con Gemini.
- [Instrucciones del sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#system-instructions):
Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus necesidades y casos de uso específicos.
- [Estrategias de instrucciones con archivos](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide): La API de Gemini admite instrucciones con datos de texto, imagen, audio y video, también conocidas como instrucciones multimodales.
- [Orientación sobre seguridad](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=es-419): A veces, los modelos de IA generativa producen resultados inesperados, como resultados inexactos, sesgados u ofensivos. El procesamiento posterior y la evaluación humana son fundamentales para limitar el riesgo de daño que pueden causar estos resultados.

¿Te resultó útil?



 Enviar comentarios



Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-02-19 (UTC)


¿Quieres brindar más información?






\[\[\["Fácil de comprender","easyToUnderstand","thumb-up"\],\["Resolvió mi problema","solvedMyProblem","thumb-up"\],\["Otro","otherUp","thumb-up"\]\],\[\["Falta la información que necesito","missingTheInformationINeed","thumb-down"\],\["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"\],\["Desactualizado","outOfDate","thumb-down"\],\["Problema de traducción","translationIssue","thumb-down"\],\["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"\],\["Otro","otherDown","thumb-down"\]\],\["Última actualización: 2026-02-19 (UTC)"\],\[\],\[\]\]