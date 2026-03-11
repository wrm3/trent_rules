[Chuyển ngay đến nội dung chính](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=vi)](https://ai.google.dev/)

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

[Lấy khoá API](https://aistudio.google.com/apikey?hl=vi) [Sổ tay nấu ăn](https://github.com/google-gemini/cookbook) [Cộng đồng](https://discuss.ai.google.dev/c/gemini-api/?hl=vi)

[Đăng nhập](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fimage-understanding%3Fhl%3Dvi&prompt=select_account)

- Trên trang này
- [Truyền hình ảnh cho Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#image-input)
  - [Truyền dữ liệu hình ảnh cùng dòng](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#inline-image)
  - [Tải hình ảnh lên bằng File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#upload-image)
- [Đưa ra câu lệnh bằng nhiều hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#multiple-images)
- [Phát hiện vật thể](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#object-detection)
- [Phân đoạn](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#segmentation)
- [Định dạng hình ảnh được hỗ trợ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#supported-formats)
- [Tính năng](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#capabilities)
- [Hạn chế và thông tin kỹ thuật chính](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#technical-details-image)
  - [Giới hạn về tệp](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#file_limit)
  - [Cách tính toán mã thông báo](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#token_calculation)
  - [Độ phân giải của nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#media_resolution)
- [Mẹo và phương pháp hay nhất](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#tips-best-practices)
- [Bước tiếp theo](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#whats-next)


Bản xem trước Gemini 3.1 Flash-Lite hiện đã ra mắt. [Dùng thử trong AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=vi).




- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Thông tin này có hữu ích không cho bạn không?



 Gửi ý kiến phản hồi



# Hiểu hình ảnh

- Trên trang này
- [Truyền hình ảnh cho Gemini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#image-input)
  - [Truyền dữ liệu hình ảnh cùng dòng](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#inline-image)
  - [Tải hình ảnh lên bằng File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#upload-image)
- [Đưa ra câu lệnh bằng nhiều hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#multiple-images)
- [Phát hiện vật thể](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#object-detection)
- [Phân đoạn](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#segmentation)
- [Định dạng hình ảnh được hỗ trợ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#supported-formats)
- [Tính năng](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#capabilities)
- [Hạn chế và thông tin kỹ thuật chính](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#technical-details-image)
  - [Giới hạn về tệp](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#file_limit)
  - [Cách tính toán mã thông báo](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#token_calculation)
  - [Độ phân giải của nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#media_resolution)
- [Mẹo và phương pháp hay nhất](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#tips-best-practices)
- [Bước tiếp theo](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#whats-next)

Các mô hình Gemini được xây dựng từ đầu theo hướng đa phương thức, mở ra nhiều nhiệm vụ xử lý hình ảnh và thị giác máy tính, bao gồm nhưng không giới hạn ở việc chú thích hình ảnh, phân loại và trả lời câu hỏi bằng hình ảnh mà không cần phải huấn luyện các mô hình học máy chuyên biệt.

Ngoài các khả năng đa phương thức chung, các mô hình Gemini còn mang đến **độ chính xác cao hơn** cho các trường hợp sử dụng cụ thể như [phát hiện đối tượng](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#object-detection) và [phân đoạn](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#segmentation), thông qua quá trình huấn luyện bổ sung.

## Truyền hình ảnh cho Gemini

Bạn có thể cung cấp hình ảnh làm dữ liệu đầu vào cho Gemini bằng 2 phương thức:

- [Truyền dữ liệu hình ảnh nội tuyến](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#inline-image): Phù hợp với các tệp nhỏ hơn (tổng kích thước yêu cầu nhỏ hơn 20 MB, bao gồm cả câu lệnh).
- [Tải hình ảnh lên bằng File API](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#upload-image): Nên dùng cho các tệp lớn hơn hoặc để dùng lại hình ảnh trong nhiều yêu cầu.

### Truyền dữ liệu hình ảnh cùng dòng

Bạn có thể truyền dữ liệu hình ảnh cùng dòng trong yêu cầu đến `generateContent`. Bạn có thể cung cấp dữ liệu hình ảnh dưới dạng chuỗi được mã hoá Base64 hoặc bằng cách đọc trực tiếp các tệp cục bộ (tuỳ thuộc vào ngôn ngữ).

Ví dụ sau đây cho thấy cách đọc hình ảnh từ một tệp cục bộ và truyền hình ảnh đó đến API `generateContent` để xử lý.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#rest)Thêm

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

Bạn cũng có thể tìm nạp hình ảnh từ một URL, chuyển đổi hình ảnh đó thành byte và truyền đến `generateContent` như trong các ví dụ sau.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#rest)Thêm

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

### Tải hình ảnh lên bằng File API

Đối với các tệp lớn hoặc để có thể sử dụng cùng một tệp hình ảnh nhiều lần, hãy sử dụng Files API. Mã sau đây tải một tệp hình ảnh lên, sau đó dùng tệp đó trong một lệnh gọi đến `generateContent`. Hãy xem [hướng dẫn về Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi) để biết thêm thông tin và ví dụ.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#rest)Thêm

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

## Đưa ra câu lệnh bằng nhiều hình ảnh

Bạn có thể cung cấp nhiều hình ảnh trong một câu lệnh bằng cách thêm nhiều đối tượng hình ảnh `Part` vào mảng `contents`. Đây có thể là sự kết hợp giữa dữ liệu nội tuyến (tệp cục bộ hoặc URL) và các tham chiếu đến File API.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#rest)Thêm

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

## Phát hiện vật thể

Các mô hình được huấn luyện để phát hiện các đối tượng trong hình ảnh và lấy toạ độ của khung hình chữ nhật. Toạ độ, so với kích thước hình ảnh, tỷ lệ thành \[0, 1000\]. Bạn cần giảm tỷ lệ các toạ độ này dựa trên kích thước hình ảnh gốc.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#python)Thêm

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

Để xem thêm ví dụ, hãy tham khảo các sổ tay sau trong [Sổ tay về Gemini](https://github.com/google-gemini/cookbook):

- [Sổ tay về khả năng nhận biết không gian 2D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=vi)
- [Sổ tay thử nghiệm về thao tác trỏ 3D](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb?hl=vi)

## Phân đoạn

Bắt đầu từ Gemini 2.5, các mô hình không chỉ phát hiện mà còn phân đoạn các mục và cung cấp mặt nạ đường viền của các mục đó.

Mô hình này dự đoán một danh sách JSON, trong đó mỗi mục đại diện cho một mặt nạ phân đoạn.
Mỗi mục có một khung hình chữ nhật ("`box_2d`") ở định dạng `[y0, x0, y1, x1]` với toạ độ được chuẩn hoá từ 0 đến 1000, một nhãn ("`label`") xác định đối tượng và cuối cùng là mặt nạ phân đoạn bên trong khung hình chữ nhật, dưới dạng png được mã hoá base64 là bản đồ xác suất có giá trị từ 0 đến 255.
Bạn cần đổi kích thước mặt nạ cho phù hợp với kích thước của khung hình chữ nhật, sau đó nhị phân hoá ở ngưỡng tin cậy (127 cho điểm giữa).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#python)Thêm

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

Hãy xem [ví dụ về phân đoạn](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb?hl=vi#scrollTo=WQJTJ8wdGOKx) trong hướng dẫn về sổ tay để biết một ví dụ chi tiết hơn.

![Một chiếc bàn có bánh cupcake, trong đó các vật dụng bằng gỗ và thuỷ tinh được làm nổi bật](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=vi)Ví dụ về kết quả phân đoạn có các đối tượng và mặt nạ phân đoạn

## Định dạng hình ảnh được hỗ trợ

Gemini hỗ trợ các loại MIME sau đây cho định dạng hình ảnh:

- PNG – `image/png`
- JPEG – `image/jpeg`
- WEBP – `image/webp`
- HEIC – `image/heic`
- HEIF – `image/heif`

Để tìm hiểu về các phương thức nhập tệp khác, hãy xem hướng dẫn [Phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi).

## Tính năng

Tất cả các phiên bản mô hình Gemini đều là mô hình đa phương thức và có thể được sử dụng trong nhiều tác vụ xử lý hình ảnh và thị giác máy tính, bao gồm nhưng không giới hạn ở việc chú thích hình ảnh, trả lời câu hỏi về hình ảnh, phân loại hình ảnh, phát hiện và phân đoạn đối tượng.

Gemini có thể giảm nhu cầu sử dụng các mô hình học máy chuyên biệt, tuỳ thuộc vào yêu cầu về chất lượng và hiệu suất của bạn.

Các phiên bản mô hình mới nhất được huấn luyện đặc biệt để cải thiện độ chính xác của các tác vụ chuyên biệt ngoài các chức năng chung, chẳng hạn như tính năng [phát hiện đối tượng](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#object-detection) và [phân đoạn](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#segmentation) nâng cao.

## Hạn chế và thông tin kỹ thuật chính

### Giới hạn về tệp

Các mô hình Gemini hỗ trợ tối đa 3.600 tệp hình ảnh cho mỗi yêu cầu.

### Cách tính toán mã thông báo

- 258 mã thông báo nếu cả hai chiều đều <= 384 pixel.
Các hình ảnh lớn hơn được chia thành các ô có kích thước 768x768 pixel, mỗi ô có giá 258 mã thông báo.

Công thức sơ bộ để tính số lượng ô như sau:

- Tính kích thước đơn vị cắt xén, xấp xỉ bằng: floor(min(width, height) / 1.5).
- Chia từng phương diện cho kích thước đơn vị cắt và nhân với nhau để có số lượng ô.

Ví dụ: đối với hình ảnh có kích thước 960x540, kích thước đơn vị cắt sẽ là 360. Chia mỗi chiều cho 360 và số lượng ô là 3 \* 2 = 6.

### Độ phân giải của nội dung nghe nhìn

Gemini 3 giới thiệu khả năng kiểm soát chi tiết đối với quy trình xử lý hình ảnh đa phương thức bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi khung hình đầu vào của hình ảnh hoặc video.**
Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản nhỏ hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ.

Để biết thêm thông tin về tham số này và mức độ ảnh hưởng của tham số này đến việc tính toán mã thông báo, hãy xem hướng dẫn về [độ phân giải của nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi).

## Mẹo và phương pháp hay nhất

- Xác minh rằng hình ảnh được xoay đúng cách.
- Sử dụng hình ảnh rõ ràng, không bị mờ.
- Khi sử dụng một hình ảnh có văn bản, hãy đặt câu lệnh dạng văn bản _sau_ phần hình ảnh trong mảng `contents`.

## Bước tiếp theo

Hướng dẫn này cho bạn biết cách tải tệp hình ảnh lên và tạo đầu ra văn bản từ đầu vào hình ảnh. Để tìm hiểu thêm, hãy xem các tài nguyên sau:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi): Tìm hiểu thêm về cách tải lên và quản lý tệp để sử dụng với Gemini.
- [Hướng dẫn hệ thống](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#system-instructions): Hướng dẫn hệ thống giúp bạn điều hướng hành vi của mô hình dựa trên nhu cầu và trường hợp sử dụng cụ thể của bạn.
- [Chiến lược đưa ra câu lệnh cho tệp](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide): Gemini API hỗ trợ đưa ra câu lệnh bằng dữ liệu văn bản, hình ảnh, âm thanh và video, còn được gọi là câu lệnh đa phương thức.
- [Hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi): Đôi khi, các mô hình AI tạo sinh tạo ra kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Hậu xử lý và đánh giá của con người là những bước cần thiết để hạn chế nguy cơ gây hại từ những kết quả đầu ra như vậy.

Thông tin này có hữu ích không cho bạn không?



 Gửi ý kiến phản hồi



Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-02-19 UTC.


Bạn muốn chia sẻ thêm với chúng tôi?






\[\[\["Dễ hiểu","easyToUnderstand","thumb-up"\],\["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"\],\["Khác","otherUp","thumb-up"\]\],\[\["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"\],\["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"\],\["Đã lỗi thời","outOfDate","thumb-down"\],\["Vấn đề về bản dịch","translationIssue","thumb-down"\],\["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"\],\["Khác","otherDown","thumb-down"\]\],\["Cập nhật lần gần đây nhất: 2026-02-19 UTC."\],\[\],\[\]\]