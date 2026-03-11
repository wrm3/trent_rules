[Chuyển ngay đến nội dung chính](https://ai.google.dev/gemini-api/docs?hl=vi#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=vi)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs)
- [Deutsch](https://ai.google.dev/gemini-api/docs?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs?hl=ko)

[Lấy khoá API](https://aistudio.google.com/apikey?hl=vi) [Sổ tay nấu ăn](https://github.com/google-gemini/cookbook) [Cộng đồng](https://discuss.ai.google.dev/c/gemini-api/?hl=vi)

[Đăng nhập](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dvi&prompt=select_account)


Bản xem trước Gemini 3.1 Flash-Lite hiện đã ra mắt. [Dùng thử trong AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=vi).




- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

# Gemini API

Con đường nhanh nhất từ câu lệnh đến sản phẩm hoàn chỉnh nhờ Gemini, Veo, Nano Banana và nhiều công cụ khác.

[Python](https://ai.google.dev/gemini-api/docs?hl=vi#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=vi#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=vi#go)[Java](https://ai.google.dev/gemini-api/docs?hl=vi#java)[C#](https://ai.google.dev/gemini-api/docs?hl=vi#c)[REST](https://ai.google.dev/gemini-api/docs?hl=vi#rest)Thêm

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
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
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "parts": [\
          {\
            "text": "Explain how AI works in a few words"\
          }\
        ]\
      }\
    ]
  }'
```

[Bắt đầu xây dựng](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi)

Hãy làm theo hướng dẫn Bắt đầu nhanh của chúng tôi để lấy khoá API và thực hiện lệnh gọi API đầu tiên chỉ trong vài phút.

* * *

## Làm quen với các mô hình

[Xem tất cả](https://ai.google.dev/gemini-api/docs/models?hl=vi)

[auto\_awesome\\
Gemini 3.1 Pro\\
Mới\\
\\
Mô hình thông minh nhất của chúng tôi, mô hình tốt nhất trên thế giới về khả năng hiểu đa phương thức, tất cả đều được xây dựng trên nền tảng suy luận tiên tiến hàng đầu.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) [spark\\
Gemini 3 Flash\\
Mới\\
\\
Hiệu suất ở cấp độ tiên tiến, ngang bằng với các mô hình lớn hơn nhưng chỉ tốn một phần chi phí.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) [spark\\
Gemini 3.1 Flash-Lite\\
Mới\\
\\
Mô hình hiệu suất cao, tiết kiệm chi phí, có hiệu suất và chất lượng của dòng Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=vi) [🍌\\
Nano Banana 2 và Nano Banana Pro\\
\\
\\
Mô hình tạo và chỉnh sửa hình ảnh tiên tiến.](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) [video\_library\\
Veo 3.1\\
\\
\\
Mô hình tạo video tân tiến của chúng tôi, có âm thanh gốc.](https://ai.google.dev/gemini-api/docs/video?hl=vi) [spark\\
Gemini Robotics\\
\\
\\
Một mô hình thị giác-ngôn ngữ (VLM) mang các tính năng tác nhân của Gemini đến với ngành robotics và cho phép suy luận nâng cao trong thế giới thực.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=vi)

## Khám phá các khả năng

[imagesmode\\
\\
Tạo hình ảnh gốc (Nano Banana)\\
\\
\\
Tạo và chỉnh sửa hình ảnh có độ phù hợp cao một cách tự nhiên bằng Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) [article\\
\\
Ngữ cảnh dài\\
\\
\\
Nhập hàng triệu mã thông báo vào các mô hình Gemini và rút ra thông tin từ hình ảnh, video và tài liệu không có cấu trúc.](https://ai.google.dev/gemini-api/docs/long-context?hl=vi) [code\\
\\
Đầu ra có cấu trúc\\
\\
\\
Giới hạn Gemini chỉ phản hồi bằng JSON, một định dạng dữ liệu có cấu trúc phù hợp để xử lý tự động.](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) [functions\\
\\
Gọi hàm\\
\\
\\
Tạo quy trình công việc dựa trên tác nhân bằng cách kết nối Gemini với các API và công cụ bên ngoài.](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) [videocam\\
\\
Tạo video bằng Veo 3.1\\
\\
\\
Tạo nội dung video chất lượng cao từ câu lệnh văn bản hoặc hình ảnh bằng mô hình tân tiến của chúng tôi.](https://ai.google.dev/gemini-api/docs/video?hl=vi) [android\_recorder\\
\\
Voice Agents with Live API\\
\\
\\
Xây dựng các ứng dụng và tác nhân thoại theo thời gian thực bằng Live API.](https://ai.google.dev/gemini-api/docs/live?hl=vi) [build\\
\\
Công cụ\\
\\
\\
Kết nối Gemini với thế giới thông qua các công cụ tích hợp như Google Tìm kiếm, Bối cảnh URL, Google Maps, Thực thi mã và Sử dụng máy tính.](https://ai.google.dev/gemini-api/docs/tools?hl=vi) [stacks\\
\\
Hiểu tài liệu\\
\\
\\
Xử lý tối đa 1.000 trang tệp PDF với khả năng hiểu đầy đủ nhiều phương thức hoặc các loại tệp dựa trên văn bản khác.](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi) [cognition\_2\\
\\
Tư duy\\
\\
\\
Khám phá cách các khả năng tư duy cải thiện khả năng suy luận cho các tác vụ và tác nhân phức tạp.](https://ai.google.dev/gemini-api/docs/thinking?hl=vi)

[Google AI Studio\\
\\
\\
Thử nghiệm câu lệnh, quản lý khoá API, theo dõi mức sử dụng và tạo nguyên mẫu.](https://aistudio.google.com/?hl=vi) [group\\
\\
Cộng đồng nhà phát triển\\
\\
\\
Đặt câu hỏi và tìm giải pháp từ các nhà phát triển khác và kỹ sư của Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=vi) [menu\_book\\
\\
Tài liệu tham khảo API\\
\\
\\
Tìm thông tin chi tiết về Gemini API trong tài liệu tham khảo chính thức.](https://ai.google.dev/api?hl=vi) [sensors\\
\\
Trạng thái\\
\\
\\
Kiểm tra trạng thái của Gemini API, Google AI Studio và các dịch vụ mô hình của chúng tôi.](https://aistudio.google.com/status?hl=vi)

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-03-03 UTC.




\[\[\["Dễ hiểu","easyToUnderstand","thumb-up"\],\["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"\],\["Khác","otherUp","thumb-up"\]\],\[\["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"\],\["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"\],\["Đã lỗi thời","outOfDate","thumb-down"\],\["Vấn đề về bản dịch","translationIssue","thumb-down"\],\["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"\],\["Khác","otherDown","thumb-down"\]\],\["Cập nhật lần gần đây nhất: 2026-03-03 UTC."\],\[\],\[\]\]