[Kapërce te përmbajtja kryesore](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=sq)](https://ai.google.dev/)

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

[Merr çelësin API](https://aistudio.google.com/apikey?hl=sq) [Libër gatimi](https://github.com/google-gemini/cookbook) [Komuniteti](https://discuss.ai.google.dev/c/gemini-api/?hl=sq)

[Identifikohu](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fdocument-processing%3Fhl%3Dsq&prompt=select_account)

- Në këtë faqe
- [Kalimi i të dhënave PDF brenda rreshtit](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#inline_data)
- [Ngarkimi i PDF-ve duke përdorur API-në e Skedarëve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#large-pdfs)
  - [PDF të mëdha nga URL-të](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#large-pdfs-urls)
  - [PDF të mëdha të ruajtura lokalisht](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#large-pdfs-local)
- [Kalimi i shumë PDF-ve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#prompt-multiple)
- [Detajet teknike](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#technical-details)
  - [Modelet Gemini 3](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#gemini-3-models)
  - [Llojet e dokumenteve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#document-types)
  - [Praktikat më të mira](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#best-practices)
- [Çfarë vjen më pas](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#whats-next)

Pamja paraprake e Gemini 3.1 Flash-Lite është tani e disponueshme. [Provojeni në AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=sq) .


![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Kjo faqe është përkthyer nga [Cloud Translation API](https://cloud.google.com/translate/?hl=sq).


Switch to English


- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet, Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Ishte e dobishme?



 Dërgo komente



# Kuptimi i dokumentit

- Në këtë faqe
- [Kalimi i të dhënave PDF brenda rreshtit](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#inline_data)
- [Ngarkimi i PDF-ve duke përdorur API-në e Skedarëve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#large-pdfs)
  - [PDF të mëdha nga URL-të](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#large-pdfs-urls)
  - [PDF të mëdha të ruajtura lokalisht](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#large-pdfs-local)
- [Kalimi i shumë PDF-ve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#prompt-multiple)
- [Detajet teknike](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#technical-details)
  - [Modelet Gemini 3](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#gemini-3-models)
  - [Llojet e dokumenteve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#document-types)
  - [Praktikat më të mira](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#best-practices)
- [Çfarë vjen më pas](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#whats-next)

Modelet Gemini mund të përpunojnë dokumente në format PDF, duke përdorur vizionin nativ për të kuptuar të gjithë kontekstin e dokumentit. Kjo shkon përtej nxjerrjes së thjeshtë të tekstit, duke i lejuar Gemini-t të:

- Analizoni dhe interpretoni përmbajtjen, duke përfshirë tekstin, imazhet, diagramet, grafikët dhe tabelat, madje edhe në dokumente të gjata deri në 1000 faqe.
- Nxjerr informacionin në formate [të strukturuara të daljes](https://ai.google.dev/gemini-api/docs/structured-output?hl=sq) .
- Përmbledhni dhe përgjigjuni pyetjeve bazuar në elementët vizualë dhe tekstualë në një dokument.
- Transkripto përmbajtjen e dokumentit (p.sh. në HTML), duke ruajtur paraqitjet dhe formatimin, për përdorim në aplikacionet e rrjedhës së dytë.

Gjithashtu mund të kaloni dokumente jo-PDF në të njëjtën mënyrë, por Gemini do t'i shohë ato si tekst normal, gjë që do të eliminojë kontekstin si grafikët ose formatimin.

## Kalimi i të dhënave PDF brenda rreshtit

Mund të kaloni të dhëna PDF brenda kërkesës për `generateContent` . Kjo është më e përshtatshme për dokumente më të vogla ose përpunim të përkohshëm ku nuk keni nevojë të referoheni te skedari në kërkesat pasuese. Ne rekomandojmë përdorimin e [API-t të Skedarëve](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#large-pdfs) për dokumente më të mëdha që duhet t'i referoheni në ndërveprimet me shumë kthesa për të përmirësuar vonesën e kërkesës dhe për të zvogëluar përdorimin e bandwidth-it.

Shembulli i mëposhtëm ju tregon se si të merrni një PDF nga një URL dhe ta konvertoni atë në bajt për përpunim:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#pushtim)Më shumë

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

Gjithashtu mund të lexoni një PDF nga një skedar lokal për përpunim:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#shko)Më shumë

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

## Ngarkimi i PDF-ve duke përdorur API-në e Skedarëve

Ne ju rekomandojmë të përdorni API-n e Skedarëve për skedarë më të mëdhenj ose kur keni ndërmend të ripërdorni një dokument në kërkesa të shumëfishta. Kjo përmirëson vonesën e kërkesës dhe zvogëlon përdorimin e bandwidth-it duke shkëputur ngarkimin e skedarit nga kërkesat e modelit.

### PDF të mëdha nga URL-të

Përdorni API-n e Skedarëve për të thjeshtuar ngarkimin dhe përpunimin e skedarëve të mëdhenj PDF nga URL-të:

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#pushtim)Më shumë

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

### PDF të mëdha të ruajtura lokalisht

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#pushtim)Më shumë

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

Mund të verifikoni nëse API-ja e ka ruajtur me sukses skedarin e ngarkuar dhe të merrni meta të dhënat e tij duke thirrur [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=sq) . Vetëm `name` (dhe si zgjatim, `uri` ) janë unikë.

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#python)[PUSHTIM](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#pushtim)Më shumë

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

## Kalimi i shumë PDF-ve

API-ja Gemini është e aftë të përpunojë dokumente të shumëfishta PDF (deri në 1000 faqe) në një kërkesë të vetme, për sa kohë që madhësia e kombinuar e dokumenteve dhe kërkesa e tekstit qëndrojnë brenda dritares së kontekstit të modelit.

[Python](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#python)[JavaScript](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#javascript)[Shko](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#shko)[PUSHTIM](https://ai.google.dev/gemini-api/docs/document-processing?hl=sq#pushtim)Më shumë

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

## Detajet teknike

Gemini mbështet skedarë PDF deri në 50MB ose 1000 faqe. Ky limit vlen si për të dhënat e integruara ashtu edhe për ngarkimet e API-t të Skedarëve. Çdo faqe dokumenti është ekuivalente me 258 tokena.

Ndërkohë që nuk ka kufizime specifike për numrin e pikselëve në një dokument përveç [dritares së kontekstit](https://ai.google.dev/gemini-api/docs/long-context?hl=sq) të modelit, faqet më të mëdha zvogëlohen në një rezolucion maksimal prej 3072 x 3072 duke ruajtur raportin e tyre origjinal të aspektit, ndërsa faqet më të vogla shkallëzohen deri në 768 x 768 piksel. Nuk ka ulje të kostos për faqet me madhësi më të ulëta, përveç gjerësisë së brezit, ose përmirësim të performancës për faqet me rezolucion më të lartë.

### Modelet Gemini 3

Gemini 3 prezanton kontroll të detajuar mbi përpunimin e vizionit multimodal me parametrin `media_resolution` . Tani mund ta vendosni rezolucionin në të ulët, të mesëm ose të lartë për secilën pjesë të medias. Me këtë shtesë, përpunimi i dokumenteve PDF është përditësuar:

1. **Përfshirja e tekstit nativ:** Teksti i integruar nativisht në PDF nxirret dhe i ofrohet modelit.
2. **Faturimi dhe raportimi i tokenëve:**
   - **Nuk do të faturoheni** për tokenët që burojnë nga **teksti origjinal** i nxjerrë në PDF.
   - Në seksionin `usage_metadata` të përgjigjes së API-t, tokenët e gjeneruar nga përpunimi i faqeve PDF (si imazhe) tani llogariten sipas modalitetit `IMAGE` , jo sipas një modaliteti të veçantë `DOCUMENT` si në disa versione të mëparshme.

Për më shumë detaje rreth parametrit të rezolucionit të medias, shihni udhëzuesin e [rezolucionit të medias](https://ai.google.dev/gemini-api/docs/media-resolution?hl=sq) .

### Llojet e dokumenteve

Teknikisht, mund të kaloni lloje të tjera MIME për të kuptuar dokumentet, si TXT, Markdown, HTML, XML, etj. Megjithatë, vizioni i dokumenteve **_i kupton vetëm PDF-të në mënyrë kuptimplote_** . Llojet e tjera do të nxirren si tekst i pastër dhe modeli nuk do të jetë në gjendje të interpretojë atë që shohim në paraqitjen e këtyre skedarëve. Çdo specifikë e llojit të skedarit, si grafikët, diagramet, etiketat HTML, formatimi i Markdown, etj., do të humbasë.

Për të mësuar rreth metodave të tjera të futjes së skedarëve, shihni udhëzuesin e [metodave të futjes së skedarëve](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=sq) .

### Praktikat më të mira

Për rezultatet më të mira:

- Rrotulloni faqet në orientimin e saktë përpara se t'i ngarkoni.
- Shmangni faqet e paqarta.
- Nëse përdorni një faqe të vetme, vendosni tekstin e kërkuar pas faqes.

## Çfarë vjen më pas

Për të mësuar më shumë, shihni burimet e mëposhtme:

- [Strategjitë e nxitjes së skedarëve](https://ai.google.dev/gemini-api/docs/files?hl=sq#prompt-guide) : API Gemini mbështet nxitjen me të dhëna teksti, imazhi, audio dhe video, të njohura edhe si nxitje multimodale.
- [Udhëzimet e sistemit](https://ai.google.dev/gemini-api/docs/text-generation?hl=sq#system-instructions) : Udhëzimet e sistemit ju lejojnë të drejtoni sjelljen e modelit bazuar në nevojat dhe rastet tuaja specifike të përdorimit.

Ishte e dobishme?



 Dërgo komente



Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-01-13 UTC.


Duhet të na tregosh më shumë?






\[\[\["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"\],\["E zgjidhi problemin tim","solvedMyProblem","thumb-up"\],\["Tjetër","otherUp","thumb-up"\]\],\[\["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"\],\["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"\],\["E papërditësuar","outOfDate","thumb-down"\],\["Problem përkthimi","translationIssue","thumb-down"\],\["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"\],\["Tjetër","otherDown","thumb-down"\]\],\["Përditësimi i fundit: 2026-01-13 UTC."\],\[\],\[\]\]