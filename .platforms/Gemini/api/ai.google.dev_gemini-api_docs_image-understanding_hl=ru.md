[Перейти к основному контенту](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=ru)](https://ai.google.dev/)

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

[Как получить ключ API](https://aistudio.google.com/apikey?hl=ru) [Кулинарная книга](https://github.com/google-gemini/cookbook) [Сообщество](https://discuss.ai.google.dev/c/gemini-api/?hl=ru)

[Войти](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dru&prompt=select_account)

- Содержание
- [Передача изображений Близнецам](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#image-input)
  - [Передача встроенных данных изображения](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#inline-image)
  - [Загрузка изображений с помощью File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#upload-image)
- [Подсказка с несколькими изображениями](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#multiple-images)
- [Обнаружение объектов](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#object-detection)
- [Сегментация](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#segmentation)
- [Поддерживаемые форматы изображений](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#supported-formats)
- [Возможности](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#capabilities)
- [Ограничения и ключевая техническая информация](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#technical-details-image)
  - [ограничение на количество файлов](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#file_limit)
  - [Расчет токенов](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#token_calculation)
  - [Разрешение СМИ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#media_resolution)
- [Советы и лучшие практики](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#tips-best-practices)
- [Что дальше?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#whats-next)

Предварительная версия Gemini 3.1 Flash-Lite теперь доступна. [Попробуйте её в AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=ru) .


![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Эта страница переведена с помощью [Cloud Translation API](https://cloud.google.com/translate/?hl=ru).


Switch to English


- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Эта информация оказалась полезной?



 Отправить отзыв



# Понимание изображения

- Содержание
- [Передача изображений Близнецам](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#image-input)
  - [Передача встроенных данных изображения](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#inline-image)
  - [Загрузка изображений с помощью File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#upload-image)
- [Подсказка с несколькими изображениями](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#multiple-images)
- [Обнаружение объектов](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#object-detection)
- [Сегментация](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#segmentation)
- [Поддерживаемые форматы изображений](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#supported-formats)
- [Возможности](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#capabilities)
- [Ограничения и ключевая техническая информация](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#technical-details-image)
  - [ограничение на количество файлов](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#file_limit)
  - [Расчет токенов](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#token_calculation)
  - [Разрешение СМИ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#media_resolution)
- [Советы и лучшие практики](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#tips-best-practices)
- [Что дальше?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#whats-next)

Модели Gemini изначально созданы для мультимодального анализа, что открывает широкий спектр возможностей для обработки изображений и компьютерного зрения, включая, помимо прочего, создание подписей к изображениям, классификацию и ответы на визуальные вопросы, без необходимости обучения специализированных моделей машинного обучения.

В дополнение к своим общим мультимодальным возможностям, модели Gemini обеспечивают **повышенную точность** для конкретных сценариев использования, таких как [обнаружение](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#object-detection) и [сегментация](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#segmentation) объектов, за счет дополнительного обучения.

## Передача изображений Близнецам

В Gemini можно передавать изображения двумя способами:

- [Передача встроенных данных изображения](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#inline-image) : идеально подходит для небольших файлов (общий размер запроса менее 20 МБ, включая подсказки).
- [Загрузка изображений с помощью File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#upload-image) : рекомендуется для больших файлов или для повторного использования изображений в нескольких запросах.

### Передача встроенных данных изображения

В запросе к функции `generateContent` можно передавать встроенные данные изображения. Данные изображения можно предоставить в виде строк, закодированных в Base64, или путем прямого чтения локальных файлов (в зависимости от языка).

В следующем примере показано, как прочитать изображение из локального файла и передать его в API `generateContent` для обработки.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#javascript)[Идти](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%B8%D0%B4%D1%82%D0%B8)[ОТДЫХ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%BE%D1%82%D0%B4%D1%8B%D1%85)Ещё

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

Также можно получить изображение по URL-адресу, преобразовать его в байты и передать в функцию `generateContent` как показано в следующих примерах.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#javascript)[Идти](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%B8%D0%B4%D1%82%D0%B8)[ОТДЫХ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%BE%D1%82%D0%B4%D1%8B%D1%85)Ещё

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

### Загрузка изображений с помощью File API

Для больших файлов или для возможности многократного использования одного и того же файла изображения используйте API файлов. Приведенный ниже код загружает файл изображения, а затем использует его в вызове функции `generateContent` . Дополнительную информацию и примеры см. [в руководстве по API файлов](https://ai.google.dev/gemini-api/docs/files?hl=ru) .

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#javascript)[Идти](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%B8%D0%B4%D1%82%D0%B8)[ОТДЫХ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%BE%D1%82%D0%B4%D1%8B%D1%85)Ещё

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

## Подсказка с несколькими изображениями

В одном запросе можно указать несколько изображений, включив несколько объектов `Part` в массив `contents` . Это могут быть как встроенные данные (локальные файлы или URL-адреса), так и ссылки на File API.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#javascript)[Идти](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%B8%D0%B4%D1%82%D0%B8)[ОТДЫХ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#%D0%BE%D1%82%D0%B4%D1%8B%D1%85)Ещё

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

## Обнаружение объектов

Модели обучаются обнаруживать объекты на изображении и получать координаты их ограничивающих рамок. Эти координаты, относительно размеров изображения, масштабируются в диапазоне \[0, 1000\]. Вам необходимо уменьшить масштаб этих координат в соответствии с исходным размером изображения.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#python)Ещё

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

Дополнительные примеры можно найти в следующих блокнотах из [«Gemini Cookbook»](https://github.com/google-gemini/cookbook) :

- [Тетрадь для запоминания пространственного восприятия в 2D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=ru)
- [Экспериментальный блокнот для 3D-указания](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=ru)

## Сегментация

Начиная с версии Gemini 2.5, модели не только распознают объекты, но и сегментируют их, а также предоставляют маски контуров.

Модель предсказывает список в формате JSON, где каждый элемент представляет собой маску сегментации. Каждый элемент имеет ограничивающий прямоугольник (" `box_2d` ") в формате `[y0, x0, y1, x1]` с нормализованными координатами от 0 до 1000, метку (" `label` "), идентифицирующую объект, и, наконец, маску сегментации внутри ограничивающего прямоугольника в формате PNG, закодированном в base64, представляющем собой карту вероятностей со значениями от 0 до 255. Маску необходимо изменить в размере, чтобы она соответствовала размерам ограничивающего прямоугольника, а затем бинаризировать с заданным порогом достоверности (127 для середины).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#python)Ещё

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

Для более подробного примера см. [раздел «Сегментация»](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=ru#scrollTo=WQJTJ8wdGOKx) в руководстве пользователя.

![Столик с кексами, на котором эффектно смотрятся деревянные и стеклянные предметы.](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=ru) Пример результатов сегментации с объектами и масками сегментации.

## Поддерживаемые форматы изображений

Gemini поддерживает следующие MIME-типы форматов изображений:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

Чтобы узнать о других методах ввода файлов, см. руководство [по методам ввода файлов](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ru) .

## Возможности

Все версии модели Gemini являются мультимодальными и могут использоваться в широком спектре задач обработки изображений и компьютерного зрения, включая, помимо прочего, создание подписей к изображениям, визуальные вопросы и ответы, классификацию изображений, обнаружение и сегментацию объектов.

Gemini может снизить потребность в использовании специализированных моделей машинного обучения в зависимости от ваших требований к качеству и производительности.

В последних версиях модели специально разработаны алгоритмы для повышения точности выполнения специализированных задач в дополнение к общим возможностям, таким как улучшенное [обнаружение](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#object-detection) и [сегментация](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ru#segmentation) объектов.

## Ограничения и ключевая техническая информация

### ограничение на количество файлов

Модели Gemini поддерживают максимум 3600 файлов изображений за один запрос.

### Расчет токенов

- 258 токенов, если оба размера <= 384 пикселя. Изображения большего размера разбиваются на фрагменты размером 768x768 пикселей, каждый из которых стоит 258 токенов.

Примерная формула для расчета количества плиток выглядит следующим образом:

- Рассчитайте приблизительный размер единицы урожая: floor(min(ширина, высота) / 1,5).
- Разделите каждое измерение на размер единицы урожая и перемножьте полученные значения, чтобы получить количество плиток.

Например, для изображения размером 960x540 размер ячейки кадрирования составит 360. Разделив каждое измерение на 360, получим количество ячеек 3 \* 2 = 6.

### Разрешение СМИ

Gemini 3 обеспечивает детальный контроль над обработкой мультимодального зрения с помощью параметра `media_resolution` . Параметр `media_resolution` определяет **максимальное количество токенов, выделяемых на каждое входное изображение или видеокадр.** Более высокое разрешение улучшает способность модели считывать мелкий текст или идентифицировать мелкие детали, но увеличивает использование токенов и задержку.

Для получения более подробной информации о параметре и о том, как он может влиять на вычисления токенов, см. руководство [по разрешению медиаконтента](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ru) .

## Советы и лучшие практики

- Убедитесь, что изображения правильно повернуты.
- Используйте четкие, неразмытые изображения.
- При использовании одного изображения с текстом, поместите текстовый запрос _после_ части с изображением в массиве `contents` .

## Что дальше?

В этом руководстве показано, как загружать файлы изображений и создавать текстовые выходные данные на основе изображений. Для получения дополнительной информации см. следующие ресурсы:

- [API для работы с файлами](https://ai.google.dev/gemini-api/docs/files?hl=ru) : Узнайте больше о загрузке и управлении файлами для использования с Gemini.
- [Системные инструкции](https://ai.google.dev/gemini-api/docs/text-generation?hl=ru#system-instructions) : Системные инструкции позволяют управлять поведением модели в соответствии с вашими конкретными потребностями и сценариями использования.
- [Стратегии запроса файлов](https://ai.google.dev/gemini-api/docs/files?hl=ru#prompt-guide) : API Gemini поддерживает запрос файлов с использованием текста, изображений, аудио и видеоданных, также известный как мультимодальный запрос.
- [Рекомендации по безопасности](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ru) : Иногда модели генеративного ИИ выдают неожиданные результаты, например, неточные, предвзятые или оскорбительные. Постобработка и оценка человеком необходимы для минимизации риска причинения вреда от таких результатов.

Эта информация оказалась полезной?



 Отправить отзыв



Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-02-19 UTC.


Хотите рассказать подробнее?






\[\[\["Прост для понимания","easyToUnderstand","thumb-up"\],\["Помог мне решить мою проблему","solvedMyProblem","thumb-up"\],\["Другое","otherUp","thumb-up"\]\],\[\["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"\],\["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"\],\["Устарел","outOfDate","thumb-down"\],\["Проблема с переводом текста","translationIssue","thumb-down"\],\["Проблемы образцов/кода","samplesCodeIssue","thumb-down"\],\["Другое","otherDown","thumb-down"\]\],\["Последнее обновление: 2026-02-19 UTC."\],\[\],\[\]\]