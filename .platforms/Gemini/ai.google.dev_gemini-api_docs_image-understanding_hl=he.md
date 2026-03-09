[דילוג לתוכן הראשי](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=he)](https://ai.google.dev/)

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

[אחזור מפתח API](https://aistudio.google.com/apikey?hl=he) [ספר המתכונים](https://github.com/google-gemini/cookbook) [קהילה](https://discuss.ai.google.dev/c/gemini-api/?hl=he)

[היכנס](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dhe&prompt=select_account)

- בדף הזה
- [העברת תמונות ל-Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#image-input)
  - [העברת נתונים של תמונות מוטבעות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#inline-image)
  - [העלאת תמונות באמצעות File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#upload-image)
- [יצירת הנחיה עם כמה תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#multiple-images)
- [זיהוי אובייקטים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#object-detection)
- [פילוח](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#segmentation)
- [אילו פורמטים של תמונות נתמכים?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#supported-formats)
- [יכולות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#capabilities)
- [מגבלות ומידע טכני חשוב](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#technical-details-image)
  - [מגבלת קבצים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#file_limit)
  - [חישוב טוקנים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#token_calculation)
  - [רזולוציית המדיה](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#media_resolution)
- [טיפים ושיטות מומלצות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#tips-best-practices)
- [המאמרים הבאים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#whats-next)


השקנו את Gemini 3.1 Flash-Lite Preview. [אפשר לנסות את זה ב-AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=he).




- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

המידע עזר לך?



 שליחת משוב



# הבנת תמונות

- בדף הזה
- [העברת תמונות ל-Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#image-input)
  - [העברת נתונים של תמונות מוטבעות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#inline-image)
  - [העלאת תמונות באמצעות File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#upload-image)
- [יצירת הנחיה עם כמה תמונות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#multiple-images)
- [זיהוי אובייקטים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#object-detection)
- [פילוח](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#segmentation)
- [אילו פורמטים של תמונות נתמכים?](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#supported-formats)
- [יכולות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#capabilities)
- [מגבלות ומידע טכני חשוב](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#technical-details-image)
  - [מגבלת קבצים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#file_limit)
  - [חישוב טוקנים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#token_calculation)
  - [רזולוציית המדיה](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#media_resolution)
- [טיפים ושיטות מומלצות](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#tips-best-practices)
- [המאמרים הבאים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#whats-next)

מודלים של Gemini מבוססים על מולטי-מודאליות מההתחלה, ולכן הם יכולים לבצע מגוון רחב של משימות עיבוד תמונות וראייה ממוחשבת, כולל תיוג תמונות, סיווג תמונות ומענה לשאלות על תמונות, בלי צורך לאמן מודלים מיוחדים של למידת מכונה.

בנוסף ליכולות הכלליות של מודלים מרובי-מוֹדָלִים, מודלים של Gemini מציעים **דיוק משופר** בתרחישי שימוש ספציפיים כמו [זיהוי אובייקטים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#object-detection) ו [פילוח](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#segmentation), באמצעות אימון נוסף.

## העברת תמונות ל-Gemini

יש שתי דרכים לספק תמונות כקלט ל-Gemini:

- [העברת נתוני תמונה מוטבעים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#inline-image): מתאים לקבצים קטנים יותר (גודל הבקשה הכולל קטן מ-20MB, כולל הנחיות).
- [העלאת תמונות באמצעות File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#upload-image): מומלץ לקבצים גדולים יותר או לשימוש חוזר בתמונות בכמה בקשות.

### העברת נתונים של תמונות מוטבעות

אפשר להעביר נתונים של תמונות מוטבעות בבקשה אל `generateContent`. אפשר לספק נתוני תמונה כמחרוזות מקודדות של Base64 או על ידי קריאה ישירה של קבצים מקומיים (בהתאם לשפה).

בדוגמה הבאה מוצג אופן הקריאה של תמונה מקובץ מקומי והעברה שלה ל-API של `generateContent` לצורך עיבוד.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#rest)עוד

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

אפשר גם לאחזר תמונה מכתובת URL, להמיר אותה לבייטים ולהעביר אותה אל `generateContent`, כמו בדוגמאות הבאות.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#rest)עוד

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

### העלאת תמונות באמצעות File API

כדי להשתמש בקובץ תמונה גדול או להשתמש בקובץ תמונה שוב ושוב, צריך להשתמש ב-Files API. בדוגמת הקוד הבאה, קובץ תמונה מועלה ואז נעשה בו שימוש בקריאה ל-`generateContent`. מידע נוסף ודוגמאות זמינים [במדריך לשימוש ב-Files API](https://ai.google.dev/gemini-api/docs/files?hl=he).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#rest)עוד

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

## יצירת הנחיה עם כמה תמונות

אפשר לספק כמה תמונות בהנחיה אחת על ידי הכללת כמה אובייקטים של תמונות במערך `Part``contents`. יכול להיות שיהיה שילוב של נתונים מוטבעים (קבצים מקומיים או כתובות URL) והפניות ל-File API.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#rest)עוד

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

## זיהוי אובייקטים

המודלים מאומנים לזיהוי אובייקטים בתמונה ולקבלת הקואורדינטות של התיבה התוחמת שלהם. הקואורדינטות, ביחס לממדי התמונה, מותאמות לטווח \[0, 1000\]. צריך לבטל את שינוי הגודל של הקואורדינטות האלה על סמך גודל התמונה המקורי.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#python)עוד

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

דוגמאות נוספות זמינות ב-notebooks הבאים ב [ספר המתכונים של Gemini](https://github.com/google-gemini/cookbook):

- [מחברת להבנה מרחבית דו-ממדית](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=he)
- [מחברת ניסיונית עם הצבעה בתלת-ממד](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=he)

## פילוח

החל מ-Gemini 2.5, המודלים לא רק מזהים פריטים אלא גם מבצעים פילוח שלהם ומספקים את מסכות המתאר שלהם.

המודל חוזה רשימת JSON, שבה כל פריט מייצג מסכת פילוח.
לכל פריט יש תיבת תוחמת ('`box_2d`') בפורמט `[y0, x0, y1, x1]` עם קואורדינטות מנורמלות בין 0 ל-1,000, תווית ('`label`') שמזהה את האובייקט, ולבסוף מסכת הפילוח בתוך התיבה התוחמת, כקובץ PNG עם קידוד base64 שהוא מפת הסתברות עם ערכים בין 0 ל-255.
צריך לשנות את הגודל של המסכה כך שיתאים למידות של תיבת התוחמת, ואז לבצע בינאריזציה לפי סף מהימנות (127 לנקודת האמצע).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#python)עוד

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

דוגמה מפורטת יותר זמינה במדריך [דוגמה לפילוח](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=he#scrollTo=WQJTJ8wdGOKx).

![שולחן עם קאפקייקים, כשהאובייקטים מעץ ומזכוכית מודגשים](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=he)דוגמה לפלט של פילוח עם אובייקטים ומסכות פילוח

## אילו פורמטים של תמונות נתמכים?

‫Gemini תומך בסוגי ה-MIME הבאים של פורמטים של תמונות:

- ‫PNG – `image/png`
- ‫JPEG – `image/jpeg`
- WEBP – `image/webp`
- HEIC – `image/heic`
- HEIF - `image/heif`

מידע על שיטות אחרות להזנת קבצים זמין במדריך בנושא [שיטות להזנת קבצים](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he).

## יכולות

כל הגרסאות של מודל Gemini הן מולטי-מודאליות, ואפשר להשתמש בהן במגוון רחב של משימות עיבוד תמונות וראייה ממוחשבת, כולל, בין היתר, יצירת כיתובים לתמונות, מענה על שאלות שקשורות לאובייקטים חזותיים, סיווג תמונות, זיהוי אובייקטים ופילוח תמונות.

יכול להיות ש-Gemini יצמצם את הצורך בשימוש במודלים מיוחדים של למידת מכונה, בהתאם לדרישות האיכות והביצועים שלכם.

הגרסאות העדכניות של המודלים אומנו במיוחד כדי לשפר את הדיוק של משימות ייעודיות, בנוסף ליכולות כלליות כמו [זיהוי אובייקטים](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#object-detection) ו [פילוח](https://ai.google.dev/gemini-api/docs/image-understanding?hl=he#segmentation) משופרים.

## מגבלות ומידע טכני חשוב

### מגבלת קבצים

מודלים של Gemini תומכים בעד 3,600 קבצים של תמונות לכל בקשה.

### חישוב טוקנים

- ‫258 טוקנים אם שני המימדים הם ‎384 פיקסלים או פחות.
תמונות גדולות יותר מחולקות למשבצות של 768x768 פיקסלים, וכל משבצת עולה 258 טוקנים.

נוסחה משוערת לחישוב מספר המשבצות:

- חישוב הגודל של יחידת החיתוך, שהוא בערך: floor(min(width, height) / 1.5).
- מחלקים כל מאפיין בגודל יחידת החיתוך ומכפילים את התוצאות כדי לקבל את מספר האריחים.

לדוגמה, אם התמונה היא בגודל 960x540, גודל יחידת החיתוך יהיה 360. מחלקים כל מאפיין ב-360 ומקבלים את מספר האריחים 3 \* 2 = 6.

### רזולוציית המדיה

‫Gemini 3 מציג שליטה מפורטת בעיבוד של ראייה מולטימודאלית באמצעות הפרמטר `media_resolution`. הפרמטר `media_resolution` קובע את **המספר המקסימלי של טוקנים שמוקצים לכל תמונה או פריים של סרטון קלט.**
רזולוציות גבוהות יותר משפרות את היכולת של המודל לקרוא טקסט קטן או לזהות פרטים קטנים, אבל הן מגדילות את השימוש בטוקנים ואת זמן האחזור.

לפרטים נוספים על הפרמטר ועל האופן שבו הוא יכול להשפיע על חישובי האסימונים, אפשר לעיין במדריך בנושא [רזולוציית מדיה](https://ai.google.dev/gemini-api/docs/media-resolution?hl=he).

## טיפים ושיטות מומלצות

- מוודאים שהתמונות מסובבות בצורה נכונה.
- השתמשו בתמונות ברורות ולא מטושטשות.
- כשמשתמשים בתמונה אחת עם טקסט, צריך למקם את הנחיית הטקסט _אחרי_ החלק של התמונה במערך `contents`.

## המאמרים הבאים

במדריך הזה מוסבר איך להעלות קובצי תמונות וליצור פלט טקסט מקלט תמונה. מידע נוסף זמין במשאבים הבאים:

- ‫ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he): מידע נוסף על העלאה וניהול של קבצים לשימוש עם Gemini
- [הוראות למערכת](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#system-instructions):
הוראות למערכת מאפשרות לכם לכוון את התנהגות המודל בהתאם לצרכים הספציפיים ולתרחישי השימוש שלכם.
- [אסטרטגיות להנחיות עם קבצים](https://ai.google.dev/gemini-api/docs/files?hl=he#prompt-guide): Gemini API תומך בהנחיות עם נתוני טקסט, תמונה, אודיו ווידאו, שנקראות גם הנחיות מרובות מצבים.
- [הנחיות בנושא בטיחות](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=he): לפעמים מודלים של AI גנרטיבי יוצרים תוצאות לא צפויות, כמו תוצאות לא מדויקות, מוטות או פוגעניות. עיבוד תמונה (Post Processing) והערכה אנושית חיוניים כדי לצמצם את הסיכון לנזק שעלול להיגרם כתוצאה מתוצאות כאלה.

המידע עזר לך?



 שליחת משוב



אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב [מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-02-19 (שעון UTC).


רוצה לתת לנו משוב?






\[\[\["התוכן קל להבנה","easyToUnderstand","thumb-up"\],\["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"\],\["סיבה אחרת","otherUp","thumb-up"\]\],\[\["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"\],\["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"\],\["התוכן לא עדכני","outOfDate","thumb-down"\],\["בעיה בתרגום","translationIssue","thumb-down"\],\["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"\],\["סיבה אחרת","otherDown","thumb-down"\]\],\["עדכון אחרון: 2026-02-19 (שעון UTC)."\],\[\],\[\]\]