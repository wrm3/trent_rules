[Zum Hauptinhalt springen](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=de)](https://ai.google.dev/)

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

[API-Schlüssel abrufen](https://aistudio.google.com/apikey?hl=de) [Kochbuch](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/?hl=de)

[Anmelden](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fdocument-processing%3Fhl%3Dde&prompt=select_account)

- Auf dieser Seite
- [PDF-Daten inline übergeben](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#inline_data)
- [PDFs mit der Files API hochladen](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#large-pdfs)
  - [Große PDFs aus URLs](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#large-pdfs-urls)
  - [Lokal gespeicherte große PDFs](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#large-pdfs-local)
- [Mehrere PDFs übergeben](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#prompt-multiple)
- [Technische Details](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#technical-details)
  - [Gemini 3-Modelle](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#gemini-3-models)
  - [Dokumenttypen](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#document-types)
  - [Best Practices](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#best-practices)
- [Nächste Schritte](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#whats-next)


Gemini 3.1 Flash-Lite ist jetzt als Vorabversion verfügbar. [In AI Studio ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=de)

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

War das hilfreich?



 Feedback geben



# Verständnis von Dokumenten

- Auf dieser Seite
- [PDF-Daten inline übergeben](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#inline_data)
- [PDFs mit der Files API hochladen](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#large-pdfs)
  - [Große PDFs aus URLs](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#large-pdfs-urls)
  - [Lokal gespeicherte große PDFs](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#large-pdfs-local)
- [Mehrere PDFs übergeben](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#prompt-multiple)
- [Technische Details](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#technical-details)
  - [Gemini 3-Modelle](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#gemini-3-models)
  - [Dokumenttypen](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#document-types)
  - [Best Practices](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#best-practices)
- [Nächste Schritte](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#whats-next)

Gemini-Modelle können Dokumente im PDF-Format verarbeiten und dabei die native Vision nutzen, um den gesamten Dokumentkontext zu erfassen. Das geht über die reine Textextraktion hinaus und ermöglicht Gemini Folgendes:

- Inhalte wie Text, Bilder, Diagramme, Grafiken und Tabellen analysieren und interpretieren, auch in langen Dokumenten mit bis zu 1.000 Seiten.
- Informationen in [strukturierte Ausgabeformate](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) extrahieren.
- Dokumente zusammenfassen und Fragen dazu beantworten, basierend auf visuellen und textlichen Elementen.
- Dokumentinhalte transkribieren (z.B. in HTML), wobei Layouts und Formatierung für die Verwendung in nachgelagerten Anwendungen beibehalten werden.

Sie können auch Nicht-PDF-Dokumente auf dieselbe Weise übergeben, aber Gemini betrachtet sie als normalen Text, wodurch Kontext wie Diagramme oder Formatierung verloren geht.

## PDF-Daten inline übergeben

Sie können PDF-Daten inline in der Anfrage an `generateContent` übergeben. Diese Methode eignet sich am besten für kleinere Dokumente oder für die temporäre Verarbeitung, wenn Sie in nachfolgenden Anfragen nicht auf die Datei verweisen müssen. Für größere Dokumente, auf die Sie in Interaktionen mit mehreren Durchgängen verweisen müssen, empfehlen wir die [Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#large-pdfs), um die Latenz von Anfragen zu verbessern und die Bandbreitennutzung zu reduzieren.

Das folgende Beispiel zeigt, wie Sie ein PDF von einer URL abrufen und zur Verarbeitung in Byte konvertieren:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#rest)Mehr

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

Sie können auch eine PDF-Datei aus einer lokalen Datei zum Verarbeiten lesen:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#ok)Mehr

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

## PDFs mit der Files API hochladen

Wir empfehlen die Verwendung der Files API für größere Dateien oder wenn Sie ein Dokument in mehreren Anfragen wiederverwenden möchten. Dadurch wird die Anfrage-Latenz verbessert und die Bandbreitennutzung reduziert, da der Dateiupload von den Modellanfragen entkoppelt wird.

### Große PDFs aus URLs

Mit der File API können Sie große PDF-Dateien über URLs einfacher hochladen und verarbeiten:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#rest)Mehr

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

### Lokal gespeicherte große PDFs

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#rest)Mehr

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

Sie können prüfen, ob die API die hochgeladene Datei erfolgreich gespeichert hat, und die Metadaten abrufen, indem Sie [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=de) aufrufen. Nur die `name` (und damit auch die `uri`) sind eindeutig.

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#python)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#rest)Mehr

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

## Mehrere PDFs übergeben

Die Gemini API kann mehrere PDF-Dokumente (bis zu 1.000 Seiten) in einer einzigen Anfrage verarbeiten, sofern die kombinierte Größe der Dokumente und des Text-Prompts innerhalb des Kontextfensters des Modells liegt.

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#javascript)[Ok](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#ok)[REST](https://ai.google.dev/gemini-api/docs/document-processing?hl=de#rest)Mehr

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

## Technische Details

Gemini unterstützt PDF-Dateien mit einer Größe von bis zu 50 MB oder 1.000 Seiten. Dieses Limit gilt sowohl für Inline-Daten als auch für Uploads über die Files API. Jede Dokumentseite entspricht 258 Tokens.

Es gibt keine spezifischen Beschränkungen für die Anzahl der Pixel in einem Dokument, abgesehen vom [Kontextfenster](https://ai.google.dev/gemini-api/docs/long-context?hl=de) des Modells. Größere Seiten werden jedoch auf eine maximale Auflösung von 3072 × 3072 Pixel herunterskaliert, wobei ihr ursprüngliches Seitenverhältnis beibehalten wird. Kleinere Seiten werden auf 768 × 768 Pixel hochskaliert. Bei Seiten mit geringerer Größe gibt es keine Kostensenkung (außer bei der Bandbreite) und bei Seiten mit höherer Auflösung keine Leistungssteigerung.

### Gemini 3-Modelle

Mit Gemini 3 wird die detaillierte Steuerung der multimodalen Bildverarbeitung mit dem Parameter `media_resolution` eingeführt. Sie können die Auflösung jetzt für jeden einzelnen Media-Teil auf „Niedrig“, „Mittel“ oder „Hoch“ festlegen. Durch diese Ergänzung wurde die Verarbeitung von PDF-Dokumenten aktualisiert:

1. **Einbeziehung von nativem Text**:Text, der nativ in die PDF-Datei eingebettet ist, wird extrahiert und dem Modell zur Verfügung gestellt.
2. **Abrechnung und Token-Berichte**:
   - Für Tokens, die aus dem extrahierten **nativen Text** in PDFs stammen, **werden keine Gebühren berechnet**.
   - Im Abschnitt `usage_metadata` der API-Antwort werden Tokens, die durch die Verarbeitung von PDF-Seiten (als Bilder) generiert wurden, jetzt unter der Modalität `IMAGE` gezählt und nicht unter einer separaten Modalität `DOCUMENT` wie in einigen früheren Versionen.

Weitere Informationen zum Parameter für die Media-Auflösung finden Sie im Leitfaden [Media-Auflösung](https://ai.google.dev/gemini-api/docs/media-resolution?hl=de).

### Dokumenttypen

Technisch gesehen können Sie andere MIME-Typen für die Dokumentanalyse übergeben, z. B. TXT, Markdown, HTML, XML usw. Die Dokumentanalyse **_versteht jedoch nur PDFs_**. Andere Typen werden als reiner Text extrahiert und das Modell kann nicht interpretieren, was in der Darstellung dieser Dateien zu sehen ist. Alle dateitypspezifischen Elemente wie Diagramme, HTML-Tags und Markdown-Formatierung gehen verloren.

Informationen zu anderen Methoden für die Dateieingabe finden Sie im Leitfaden [Methoden für die Dateieingabe](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de).

### Best Practices

Für optimale Ergebnisse:

- Drehen Sie die Seiten vor dem Hochladen in die richtige Ausrichtung.
- Vermeiden Sie unscharfe Seiten.
- Wenn Sie eine einzelne Seite verwenden, platzieren Sie den Text-Prompt nach der Seite.

## Nächste Schritte

Weitere Informationen finden Sie in den folgenden Ressourcen:

- [Strategien für Dateiprompts](https://ai.google.dev/gemini-api/docs/files?hl=de#prompt-guide): Die Gemini API unterstützt Prompts mit Text-, Bild-, Audio- und Videodaten, auch bekannt als multimodale Prompts.
- [Systemanweisungen](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#system-instructions): Mit Systemanweisungen können Sie das Verhalten des Modells entsprechend Ihren spezifischen Anforderungen und Anwendungsfällen steuern.

War das hilfreich?



 Feedback geben



Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-01-13 (UTC).


Haben Sie Feedback für uns?






\[\[\["Leicht verständlich","easyToUnderstand","thumb-up"\],\["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"\],\["Sonstiges","otherUp","thumb-up"\]\],\[\["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"\],\["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"\],\["Nicht mehr aktuell","outOfDate","thumb-down"\],\["Problem mit der Übersetzung","translationIssue","thumb-down"\],\["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"\],\["Sonstiges","otherDown","thumb-down"\]\],\["Zuletzt aktualisiert: 2026-01-13 (UTC)."\],\[\],\[\]\]