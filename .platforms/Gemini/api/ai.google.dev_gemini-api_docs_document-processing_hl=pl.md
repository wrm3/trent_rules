[Przejdź do głównej treści](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=pl)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/document-processing)
- [Deutsch](https://ai.google.dev/gemini-api/docs/document-processing?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/document-processing?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/document-processing?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/document-processing?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/document-processing?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/document-processing?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/document-processing?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/document-processing?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/document-processing?hl=ko)

[Pobierz klucz interfejsu API](https://aistudio.google.com/apikey?hl=pl) [Książka kucharska](https://github.com/google-gemini/cookbook) [Społeczność](https://discuss.ai.google.dev/c/gemini-api/?hl=pl)

[Zaloguj się](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fdocument-processing%3Fhl%3Dpl&prompt=select_account)

- Na tej stronie
- [Przekazywanie danych PDF w tekście](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#inline_data)
- [Przesyłanie plików PDF za pomocą interfejsu Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs)
  - [Duże pliki PDF z adresów URL](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs-urls)
  - [Duże pliki PDF przechowywane lokalnie](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs-local)
- [Przekazywanie wielu plików PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#prompt-multiple)
- [Szczegóły techniczne](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#technical-details)
  - [Modele Gemini 3](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#gemini-3-models)
  - [Typy dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#document-types)
  - [Sprawdzone metody](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#best-practices)
- [Co dalej?](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#whats-next)


Wersja testowa Gemini 3.1 Flash-Lite jest już dostępna. [Wypróbuj w AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=pl)

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Czy te wskazówki były pomocne?



 Prześlij opinię



# rozumienie dokumentów;

- Na tej stronie
- [Przekazywanie danych PDF w tekście](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#inline_data)
- [Przesyłanie plików PDF za pomocą interfejsu Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs)
  - [Duże pliki PDF z adresów URL](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs-urls)
  - [Duże pliki PDF przechowywane lokalnie](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs-local)
- [Przekazywanie wielu plików PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#prompt-multiple)
- [Szczegóły techniczne](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#technical-details)
  - [Modele Gemini 3](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#gemini-3-models)
  - [Typy dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#document-types)
  - [Sprawdzone metody](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#best-practices)
- [Co dalej?](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#whats-next)

Modele Gemini mogą przetwarzać dokumenty w formacie PDF, korzystając z natywnego systemu wizyjnego, aby zrozumieć kontekst całego dokumentu. To nie tylko wyodrębnianie tekstu. Gemini może też:

- Analizuj i interpretuj treści, w tym tekst, obrazy, diagramy, wykresy i tabele, nawet w długich dokumentach (do 1000 stron).
- Wyodrębnianie informacji w formatach [danych strukturalnych](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl).
- podsumowywać dokumenty i odpowiadać na pytania na podstawie elementów wizualnych i tekstowych;
- Transkrybuj zawartość dokumentu (np. do formatu HTML), zachowując układy i formatowanie, aby można było używać jej w aplikacjach podrzędnych.

W ten sam sposób możesz też przekazywać dokumenty inne niż PDF, ale Gemini będzie je traktować jako zwykły tekst, co spowoduje utratę kontekstu, np. wykresów czy formatowania.

## Przekazywanie danych PDF w tekście

Dane PDF możesz przekazywać w treści żądania wysyłanego do `generateContent`. Jest to najlepsze rozwiązanie w przypadku mniejszych dokumentów lub tymczasowego przetwarzania, gdy nie musisz odwoływać się do pliku w kolejnych żądaniach. W przypadku większych dokumentów, do których chcesz się odwoływać w interakcjach wieloetapowych, zalecamy używanie [interfejsu Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs). Pozwoli to zmniejszyć opóźnienie żądań i wykorzystanie przepustowości.

Poniższy przykład pokazuje, jak pobrać plik PDF z adresu URL i przekonwertować go na bajty do przetworzenia:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#rest)Więcej

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

# Retrieve and encode the PDF byte
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[\
        types.Part.from_bytes(\
            data=doc_data,\
            mime_type='application/pdf',\
        ),\
        prompt\
    ]
)

print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const pdfResp = await fetch('https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf')
        .then((response) => response.arrayBuffer());

    const contents = [\
        { text: "Summarize this document" },\
        {\
            inlineData: {\
                mimeType: 'application/pdf',\
                data: Buffer.from(pdfResp).toString("base64")\
            }\
        }\
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: contents
    });
    console.log(response.text);
}

main();
```

```
package main

import (
    "context"
    "fmt"
    "io"
    "net/http"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfResp, _ := http.Get("https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf")
    var pdfBytes []byte
    if pdfResp != nil && pdfResp.Body != nil {
        pdfBytes, _ = io.ReadAll(pdfResp.Body)
        pdfResp.Body.Close()
    }

    parts := []*genai.Part{
        &genai.Part{
            InlineData: &genai.Blob{
                MIMEType: "application/pdf",
                Data:     pdfBytes,
            },
        },
        genai.NewPartFromText("Summarize this document"),
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
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},\
          {"text": "'$PROMPT'"}\
        ]\
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

Możesz też odczytać plik PDF z pliku lokalnego w celu przetworzenia:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#go)Więcej

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[\
      types.Part.from_bytes(\
        data=filepath.read_bytes(),\
        mime_type='application/pdf',\
      ),\
      prompt])
print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const contents = [\
        { text: "Summarize this document" },\
        {\
            inlineData: {\
                mimeType: 'application/pdf',\
                data: Buffer.from(fs.readFileSync("content/343019_3_art_0_py4t4l_convrt.pdf")).toString("base64")\
            }\
        }\
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: contents
    });
    console.log(response.text);
}

main();
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
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfBytes, _ := os.ReadFile("path/to/your/file.pdf")

    parts := []*genai.Part{
        &genai.Part{
            InlineData: &genai.Blob{
                MIMEType: "application/pdf",
                Data:     pdfBytes,
            },
        },
        genai.NewPartFromText("Summarize this document"),
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

## Przesyłanie plików PDF za pomocą interfejsu Files API

W przypadku większych plików lub gdy zamierzasz używać dokumentu w wielu żądaniach, zalecamy korzystanie z interfejsu Files API. Zmniejsza to opóźnienie żądań i wykorzystanie przepustowości przez oddzielenie przesyłania plików od żądań modelu.

### Duże pliki PDF z adresów URL

Użyj interfejsu File API, aby uprościć przesyłanie i przetwarzanie dużych plików PDF z adresów URL:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#rest)Więcej

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[sample_doc, prompt])
print(response.text)
```

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {

    const pdfBuffer = await fetch("https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf")
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    const content = [\
        'Summarize this document',\
    ];

    if (file.uri && file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3-flash-preview',
        contents: content,
    });

    console.log(response.text);

}

main();
```

```
package main

import (
  "context"
  "fmt"
  "io"
  "net/http"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, _ := genai.NewClient(ctx, &genai.ClientConfig{
    APIKey:  os.Getenv("GEMINI_API_KEY"),
    Backend: genai.BackendGeminiAPI,
  })

  pdfURL := "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
  localPdfPath := "A17_FlightPlan_downloaded.pdf"

  respHttp, _ := http.Get(pdfURL)
  defer respHttp.Body.Close()

  outFile, _ := os.Create(localPdfPath)
  defer outFile.Close()

  _, _ = io.Copy(outFile, respHttp.Body)

  uploadConfig := &genai.UploadFileConfig{MIMEType: "application/pdf"}
  uploadedFile, _ := client.Files.UploadFromPath(ctx, localPdfPath, uploadConfig)

  promptParts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Summarize this document"),
  }
  contents := []*genai.Content{
    genai.NewContentFromParts(promptParts, genai.RoleUser), // Specify role
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
PDF_PATH="https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
DISPLAY_NAME="A17_FlightPlan"
PROMPT="Summarize this document"

# Download the PDF from the provided URL
wget -O "${DISPLAY_NAME}.pdf" "${PDF_PATH}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
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
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"text": "'$PROMPT'"},\
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]\
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

### Duże pliki PDF przechowywane lokalnie

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#rest)Więcej

```
from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

# Retrieve and encode the PDF byte
file_path = pathlib.Path('large_file.pdf')

# Upload the PDF using the File API
sample_file = client.files.upload(
    file=file_path,
)

prompt="Summarize this document"

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[sample_file, "Summarize this document"])
print(response.text)
```

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const file = await ai.files.upload({
        file: 'path-to-localfile.pdf'
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    const content = [\
        'Summarize this document',\
    ];

    if (file.uri && file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3-flash-preview',
        contents: content,
    });

    console.log(response.text);

}

main();
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
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })
    localPdfPath := "/path/to/file.pdf"

    uploadConfig := &genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile, _ := client.Files.UploadFromPath(ctx, localPdfPath, uploadConfig)

    promptParts := []*genai.Part{
        genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
        genai.NewPartFromText("Give me a summary of this pdf file."),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(promptParts, genai.RoleUser),
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
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME=TEXT
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"text": "Can you add a few more lines to this poem?"},\
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]\
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

Możesz sprawdzić, czy interfejs API prawidłowo zapisał przesłany plik, i pobrać jego metadane, wywołując [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=pl). Tylko `name` (a co za tym idzie, `uri`) jest niepowtarzalny.

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#python)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#rest)Więcej

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.txt')
fpath.write_text('hello')

file = client.files.upload(file='example.txt')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
```

```
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/files/$name > file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## Przekazywanie wielu plików PDF

Interfejs Gemini API może przetwarzać wiele dokumentów PDF (do 1000 stron) w ramach jednego żądania, o ile łączny rozmiar dokumentów i prompta tekstowego mieści się w oknie kontekstu modelu.

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#javascript)[Go](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#go)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#rest)Więcej

```
from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805"
doc_url_2 = "https://arxiv.org/pdf/2403.05530"

# Retrieve and upload both PDFs using the File API
doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[sample_pdf_1, sample_pdf_2, prompt]
)

print(response.text)
```

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function uploadRemotePDF(url, displayName) {
    const pdfBuffer = await fetch(url)
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: displayName,
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    return file;
}

async function main() {
    const content = [\
        'What is the difference between each of the main benchmarks between these two papers? Output these in a table.',\
    ];

    let file1 = await uploadRemotePDF("https://arxiv.org/pdf/2312.11805", "PDF 1")
    if (file1.uri && file1.mimeType) {
        const fileContent = createPartFromUri(file1.uri, file1.mimeType);
        content.push(fileContent);
    }
    let file2 = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2")
    if (file2.uri && file2.mimeType) {
        const fileContent = createPartFromUri(file2.uri, file2.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3-flash-preview',
        contents: content,
    });

    console.log(response.text);
}

main();
```

```
package main

import (
    "context"
    "fmt"
    "io"
    "net/http"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    docUrl1 := "https://arxiv.org/pdf/2312.11805"
    docUrl2 := "https://arxiv.org/pdf/2403.05530"
    localPath1 := "doc1_downloaded.pdf"
    localPath2 := "doc2_downloaded.pdf"

    respHttp1, _ := http.Get(docUrl1)
    defer respHttp1.Body.Close()

    outFile1, _ := os.Create(localPath1)
    _, _ = io.Copy(outFile1, respHttp1.Body)
    outFile1.Close()

    respHttp2, _ := http.Get(docUrl2)
    defer respHttp2.Body.Close()

    outFile2, _ := os.Create(localPath2)
    _, _ = io.Copy(outFile2, respHttp2.Body)
    outFile2.Close()

    uploadConfig1 := &genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile1, _ := client.Files.UploadFromPath(ctx, localPath1, uploadConfig1)

    uploadConfig2 := &genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile2, _ := client.Files.UploadFromPath(ctx, localPath2, uploadConfig2)

    promptParts := []*genai.Part{
        genai.NewPartFromURI(uploadedFile1.URI, uploadedFile1.MIMEType),
        genai.NewPartFromURI(uploadedFile2.URI, uploadedFile2.MIMEType),
        genai.NewPartFromText("What is the difference between each of the " +
                              "main benchmarks between these two papers? " +
                              "Output these in a table."),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(promptParts, genai.RoleUser),
    }

    modelName := "gemini-3-flash-preview"
    result, _ := client.Models.GenerateContent(
        ctx,
        modelName,
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

```
DOC_URL_1="https://arxiv.org/pdf/2312.11805"
DOC_URL_2="https://arxiv.org/pdf/2403.05530"
DISPLAY_NAME_1="Gemini_paper"
DISPLAY_NAME_2="Gemini_1.5_paper"
PROMPT="What is the difference between each of the main benchmarks between these two papers? Output these in a table."

# Function to download and upload a PDF
upload_pdf() {
  local doc_url="$1"
  local display_name="$2"

  # Download the PDF
  wget -O "${display_name}.pdf" "${doc_url}"

  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c < "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}"
  echo "NUM_BYTES: ${NUM_BYTES}"

  local tmp_header_file=upload-header.tmp

  # Initial resumable request
  curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2> /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
  rm "${tmp_header_file}"

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2> /dev/null > "file_info_${display_name}.json"

  local file_uri=$(jq ".file.uri" "file_info_${display_name}.json")
  echo "file_uri for ${display_name}: ${file_uri}"

  # Clean up the downloaded PDF
  rm "${display_name}.pdf"

  echo "${file_uri}"
}

# Upload the first PDF
file_uri_1=$(upload_pdf "${DOC_URL_1}" "${DISPLAY_NAME_1}")

# Upload the second PDF
file_uri_2=$(upload_pdf "${DOC_URL_2}" "${DISPLAY_NAME_2}")

# Now generate content using both files
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"file_data": {"mime_type": "application/pdf", "file_uri": '$file_uri_1'}},\
          {"file_data": {"mime_type": "application/pdf", "file_uri": '$file_uri_2'}},\
          {"text": "'$PROMPT'"}\
        ]\
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Szczegóły techniczne

Gemini obsługuje pliki PDF o rozmiarze do 50 MB lub 1000 stron. Ten limit dotyczy zarówno danych wbudowanych, jak i przesyłania za pomocą interfejsu Files API. Każda strona dokumentu jest równoważna 258 tokenom.

Nie ma konkretnych limitów liczby pikseli w dokumencie poza [oknem kontekstowym](https://ai.google.dev/gemini-api/docs/long-context?hl=pl) modelu. Większe strony są zmniejszane do maksymalnej rozdzielczości 3072 x 3072 pikseli przy zachowaniu pierwotnego współczynnika proporcji, a mniejsze strony są powiększane do 768 x 768 pikseli. W przypadku stron o mniejszych rozmiarach nie ma obniżki kosztów (poza przepustowością) ani poprawy wydajności w przypadku stron o wyższej rozdzielczości.

### Modele Gemini 3

Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem obrazu multimodalnego za pomocą parametru `media_resolution`. Teraz możesz ustawić rozdzielczość na niską, średnią lub wysoką w przypadku poszczególnych komponentów multimedialnych. W ramach tej zmiany zaktualizowaliśmy sposób przetwarzania dokumentów PDF:

1. **Uwzględnianie tekstu natywnego:** tekst natywnie osadzony w pliku PDF jest wyodrębniany i przekazywany do modelu.
2. **Raporty o płatnościach i tokenach:**
   - Za tokeny pochodzące z wyodrębnionego **tekstu natywnego** w plikach PDF **nie są naliczane opłaty**.
   - W sekcji `usage_metadata` odpowiedzi interfejsu API tokeny wygenerowane podczas przetwarzania stron PDF (jako obrazów) są teraz zliczane w ramach `IMAGE`, a nie w ramach osobnego trybu `DOCUMENT`, jak w niektórych wcześniejszych wersjach.

Więcej informacji o parametrze rozdzielczości multimediów znajdziesz w przewodniku [Rozdzielczość multimediów](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl).

### Typy dokumentów

Technicznie możesz przekazywać inne typy MIME do rozpoznawania dokumentów, takie jak TXT, Markdown, HTML, XML itp. Jednak funkcja widzenia dokumentów **_rozumie tylko pliki PDF_**. Inne typy zostaną wyodrębnione jako czysty tekst, a model nie będzie w stanie zinterpretować tego, co widzimy w renderowaniu tych plików. Utracisz wszystkie elementy charakterystyczne dla danego typu pliku, takie jak wykresy, diagramy, tagi HTML, formatowanie Markdown itp.

Więcej informacji o innych metodach wprowadzania plików znajdziesz w przewodniku [Metody wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

### Sprawdzone metody

Aby uzyskać najlepsze wyniki:

- Przed przesłaniem obróć strony do właściwej orientacji.
- Unikaj rozmazanych stron.
- Jeśli używasz jednej strony, umieść prompt tekstowy po niej.

## Co dalej?

Więcej informacji znajdziesz w tych materiałach:

- [Strategie promptowania plików:](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide) interfejs Gemini API obsługuje promptowanie za pomocą danych tekstowych, obrazów, dźwięku i wideo, czyli promptowanie multimodalne.
- [Instrukcje systemowe:](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions)
instrukcje systemowe pozwalają sterować zachowaniem modelu na podstawie konkretnych potrzeb i przypadków użycia.

Czy te wskazówki były pomocne?



 Prześlij opinię



O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-01-13 UTC.


Chcesz przekazać coś jeszcze?






\[\[\["Łatwo zrozumieć","easyToUnderstand","thumb-up"\],\["Rozwiązało to mój problem","solvedMyProblem","thumb-up"\],\["Inne","otherUp","thumb-up"\]\],\[\["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"\],\["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"\],\["Nieaktualne treści","outOfDate","thumb-down"\],\["Problem z tłumaczeniem","translationIssue","thumb-down"\],\["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"\],\["Inne","otherDown","thumb-down"\]\],\["Ostatnia aktualizacja: 2026-01-13 UTC."\],\[\],\[\]\]