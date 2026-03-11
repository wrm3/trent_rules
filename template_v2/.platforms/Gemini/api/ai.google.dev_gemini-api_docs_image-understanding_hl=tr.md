[Ana içeriğe atla](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=tr)](https://ai.google.dev/)

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

[API anahtarı alma](https://aistudio.google.com/apikey?hl=tr) [Tarif Defteri](https://github.com/google-gemini/cookbook) [Topluluk](https://discuss.ai.google.dev/c/gemini-api/?hl=tr)

[Oturum aç](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dtr&prompt=select_account)

- Bu sayfada
- [Gemini'a görüntü aktarma](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#image-input)
  - [Satır içi resim verilerini iletme](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#inline-image)
  - [File API'yi kullanarak resim yükleme](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#upload-image)
- [Birden fazla resimle istem oluşturma](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#multiple-images)
- [Nesne algılama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#object-detection)
- [Segmentasyon](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#segmentation)
- [Desteklenen görsel biçimleri](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#supported-formats)
- [Özellikler](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#capabilities)
- [Sınırlamalar ve temel teknik bilgiler](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#technical-details-image)
  - [Dosya sınırı](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#file_limit)
  - [Jeton hesaplama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#token_calculation)
  - [Medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#media_resolution)
- [İpuçları ve en iyi uygulamalar](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#tips-best-practices)
- [Sırada ne var?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#whats-next)


Gemini 3.1 Flash-Lite önizlemesi kullanıma sunuldu. [AI Studio'da deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=tr).




- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Bu size yardımcı oldu mu?



 Geri bildirim gönderin



# Görüntü anlama

- Bu sayfada
- [Gemini'a görüntü aktarma](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#image-input)
  - [Satır içi resim verilerini iletme](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#inline-image)
  - [File API'yi kullanarak resim yükleme](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#upload-image)
- [Birden fazla resimle istem oluşturma](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#multiple-images)
- [Nesne algılama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#object-detection)
- [Segmentasyon](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#segmentation)
- [Desteklenen görsel biçimleri](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#supported-formats)
- [Özellikler](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#capabilities)
- [Sınırlamalar ve temel teknik bilgiler](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#technical-details-image)
  - [Dosya sınırı](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#file_limit)
  - [Jeton hesaplama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#token_calculation)
  - [Medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#media_resolution)
- [İpuçları ve en iyi uygulamalar](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#tips-best-practices)
- [Sırada ne var?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#whats-next)

Gemini modelleri baştan sona çok formatlı olacak şekilde tasarlandığından, özel makine öğrenimi modelleri eğitmenize gerek kalmadan görüntü açıklaması, sınıflandırma ve görsel soru yanıtlama gibi çok çeşitli görüntü işleme ve bilgisayarla görme görevlerini yerine getirebilirsiniz.

Gemini modelleri, genel çok formatlı özelliklerinin yanı sıra ek eğitim sayesinde [nesne algılama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#object-detection) ve [segmentasyon](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#segmentation) gibi belirli kullanım alanlarında **daha yüksek doğruluk** sunar.

## Gemini'a görüntü aktarma

Gemini'a giriş olarak resim sağlamak için iki yöntem kullanabilirsiniz:

- [Satır içi resim verilerini iletme](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#inline-image): Daha küçük dosyalar için idealdir (istemler dahil olmak üzere toplam istek boyutu 20 MB'tan az olmalıdır).
- [File API'yi kullanarak resim yükleme](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#upload-image): Daha büyük dosyalar veya resimleri birden fazla istekte yeniden kullanmak için önerilir.

### Satır içi resim verilerini iletme

Satır içi resim verilerini `generateContent` isteğinde iletebilirsiniz. Görüntü verilerini Base64 kodlu dizeler olarak veya doğrudan yerel dosyaları okuyarak (dile bağlı olarak) sağlayabilirsiniz.

Aşağıdaki örnekte, yerel bir dosyadan nasıl resim okunacağı ve işlenmesi için `generateContent` API'ye nasıl iletileceği gösterilmektedir.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#rest)Daha fazla

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

Ayrıca bir URL'den resim getirebilir, bunu baytlara dönüştürebilir ve aşağıdaki örneklerde gösterildiği gibi `generateContent`'ye iletebilirsiniz.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#rest)Daha fazla

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

### File API'yi kullanarak resim yükleme

Büyük dosyalar için veya aynı resim dosyasını tekrar tekrar kullanabilmek için Files API'yi kullanın. Aşağıdaki kod, bir resim dosyasını yükler ve ardından `generateContent` çağrısında dosyayı kullanır. Daha fazla bilgi ve örnek için [Files API kılavuzuna](https://ai.google.dev/gemini-api/docs/files?hl=tr) bakın.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#rest)Daha fazla

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

## Birden fazla resimle istem oluşturma

`contents` dizisine birden fazla resim `Part` nesnesi ekleyerek tek bir istemde birden fazla resim sağlayabilirsiniz. Bunlar satır içi veriler (yerel dosyalar veya URL'ler) ve File API referanslarının bir karışımı olabilir.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#rest)Daha fazla

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

## Nesne algılama

Modeller, bir görüntüdeki nesneleri algılayıp sınırlayıcı kutu koordinatlarını almak için eğitilir. Görüntü boyutlarına göre koordinatlar \[0, 1000\] aralığında ölçeklendirilir. Bu koordinatları orijinal resim boyutunuza göre ölçeklendirmeniz gerekir.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#python)Daha fazla

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

Daha fazla örnek için [Gemini çözüm kitabındaki](https://github.com/google-gemini/cookbook) aşağıdaki not defterlerini inceleyin:

- [2D uzamsal anlama not defteri](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=tr)
- [Deneysel 3D işaretleme not defteri](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=tr)

## Segmentasyon

Gemini 2.5'ten itibaren modeller yalnızca öğeleri algılamakla kalmaz, aynı zamanda bunları segmentlere ayırır ve kontur maskelerini sağlar.

Model, her öğenin bir segmentasyon maskesini temsil ettiği bir JSON listesi tahmin eder.
Her öğe, 0 ile 1000 arasında normalleştirilmiş koordinatlara sahip `[y0, x0, y1, x1]` biçiminde bir sınırlayıcı kutu ("`box_2d`"), nesneyi tanımlayan bir etiket ("`label`") ve son olarak sınırlayıcı kutunun içindeki segmentasyon maskesini içerir. Bu maske, 0 ile 255 arasında değerlere sahip bir olasılık haritası olan base64 kodlu png biçimindedir.
Maske, sınırlayıcı kutu boyutlarıyla eşleşecek şekilde yeniden boyutlandırılmalı, ardından güven eşiğinizde (orta nokta için 127) ikili hale getirilmelidir.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#python)Daha fazla

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

Daha ayrıntılı bir örnek için yemek kitabı kılavuzundaki [segmentasyon örneğine](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=tr#scrollTo=WQJTJ8wdGOKx) göz atın.

![Ahşap ve cam nesnelerin vurgulandığı, üzerinde küçük kekler olan bir masa](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=tr)Nesneler ve segmentasyon maskeleri içeren örnek bir segmentasyon çıkışı

## Desteklenen görsel biçimleri

Gemini aşağıdaki resim biçimi MIME türlerini destekler:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

Diğer dosya giriş yöntemleri hakkında bilgi edinmek için [Dosya giriş yöntemleri](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr) kılavuzuna bakın.

## Özellikler

Tüm Gemini modeli sürümleri çok formatlıdır ve görüntü açıklaması, görsel soru ve yanıtlama, görüntü sınıflandırma, nesne algılama ve segmentasyon dahil ancak bunlarla sınırlı olmamak üzere çok çeşitli görüntü işleme ve bilgisayarla görme görevlerinde kullanılabilir.

Gemini, kalite ve performans gereksinimlerinize bağlı olarak özel ML modelleri kullanma ihtiyacını azaltabilir.

En yeni model sürümleri, özellikle gelişmiş [nesne algılama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#object-detection) ve [segmentasyon](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#segmentation) gibi genel özelliklerin yanı sıra uzmanlık gerektiren görevlerin doğruluğunu artırmak için eğitilmiştir.

## Sınırlamalar ve temel teknik bilgiler

### Dosya sınırı

Gemini modelleri,istek başına en fazla 3.600 resim dosyasını destekler.

### Jeton hesaplama

- Her iki boyut da <= 384 piksel ise 258 jeton.
Daha büyük resimler, her biri 258 jeton değerinde olan 768x768 piksellik bloklar halinde düzenlenir.

Döşeme sayısını hesaplamak için kullanılan yaklaşık formül şöyledir:

- Kırpma birimi boyutunu hesaplayın. Bu boyut yaklaşık olarak floor(min(width, height) / 1.5) olur.
- Her boyutu kırpma birimi boyutuna bölün ve döşeme sayısını elde etmek için sonuçları çarpın.

Örneğin, 960x540 boyutlarındaki bir resmin kırpma birimi boyutu 360 olur. Her boyutu 360'a bölün. Döşeme sayısı 3 \* 2 = 6 olur.

### Medya çözünürlüğü

Gemini 3, `media_resolution` parametresiyle çok formatlı görüntü işleme üzerinde ayrıntılı kontrol sunar. `media_resolution` parametresi, **giriş resmi veya video karesi başına ayrılan maksimum jeton sayısını** belirler.
Daha yüksek çözünürlükler, modelin küçük metinleri okuma veya küçük ayrıntıları tanımlama becerisini artırır ancak jeton kullanımını ve gecikmeyi de artırır.

Parametre ve jeton hesaplamalarını nasıl etkileyebileceği hakkında daha fazla bilgi için [medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/media-resolution?hl=tr) kılavuzuna bakın.

## İpuçları ve en iyi uygulamalar

- Resimlerin doğru şekilde döndürüldüğünü doğrulayın.
- Net ve bulanık olmayan resimler kullanın.
- Metin içeren tek bir resim kullanırken metin istemini `contents` dizisinde resim kısmının _sonrasına_ yerleştirin.

## Sırada ne var?

Bu kılavuzda, resim dosyalarını nasıl yükleyeceğiniz ve resim girişlerinden nasıl metin çıkışları oluşturacağınız açıklanmaktadır. Daha fazla bilgi edinmek için aşağıdaki kaynaklara bakın:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr): Gemini ile kullanılacak dosyaları yükleme ve yönetme hakkında daha fazla bilgi edinin.
- [Sistem talimatları](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#system-instructions):
Sistem talimatları, modelin davranışını özel ihtiyaçlarınıza ve kullanım alanlarınıza göre yönlendirmenizi sağlar.
- [Dosya istemi stratejileri](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide): Gemini API, çok formatlı istem olarak da bilinen metin, resim, ses ve video verileriyle istemi destekler.
- [Güvenlikle ilgili bilgiler](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=tr): Üretken yapay zeka modelleri bazen yanlış, taraflı veya rahatsız edici gibi beklenmedik çıkışlar üretebilir. Bu tür çıkışlardan kaynaklanan zarar riskini sınırlamak için işleme sonrası ve uzman değerlendirmesi gereklidir.

Bu size yardımcı oldu mu?



 Geri bildirim gönderin



Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-02-19 UTC.


Bize geri bildirimde bulunmak mı istiyorsunuz?






\[\[\["Anlaması kolay","easyToUnderstand","thumb-up"\],\["Sorunumu çözdü","solvedMyProblem","thumb-up"\],\["Diğer","otherUp","thumb-up"\]\],\[\["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"\],\["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"\],\["Güncel değil","outOfDate","thumb-down"\],\["Çeviri sorunu","translationIssue","thumb-down"\],\["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"\],\["Diğer","otherDown","thumb-down"\]\],\["Son güncelleme tarihi: 2026-02-19 UTC."\],\[\],\[\]\]