[Ir al contenido principal](https://ai.google.dev/gemini-api/docs?hl=es-419#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=es-419)](https://ai.google.dev/)

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

[Cómo obtener una clave de API](https://aistudio.google.com/apikey?hl=es-419) [Guía de soluciones](https://github.com/google-gemini/cookbook) [Comunidad](https://discuss.ai.google.dev/c/gemini-api/?hl=es-419)

[Acceder](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Des-419&prompt=select_account)


Ya está disponible la versión preliminar de Gemini 3.1 Flash-Lite. [Pruébalo en AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=es-419).




- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

# API de Gemini

La ruta más rápida desde la instrucción hasta la producción con Gemini, Veo, Nano Banana y mucho más.

[Python](https://ai.google.dev/gemini-api/docs?hl=es-419#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=es-419#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=es-419#go)[Java](https://ai.google.dev/gemini-api/docs?hl=es-419#java)[C#](https://ai.google.dev/gemini-api/docs?hl=es-419#c)[REST](https://ai.google.dev/gemini-api/docs?hl=es-419#rest)Más

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

[Comenzar a desarrollar](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419)

Sigue nuestra guía de inicio rápido para obtener una clave de API y realizar tu primera llamada a la API en cuestión de minutos.

* * *

## Conoce los modelos

[Ver todos](https://ai.google.dev/gemini-api/docs/models?hl=es-419)

[auto\_awesome\\
Gemini 3.1 Pro\\
Nuevo\\
\\
Nuestro modelo más inteligente, el mejor del mundo para la comprensión multimodal, todo basado en un razonamiento de vanguardia.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) [spark\\
Gemini 3 Flash\\
Nuevo\\
\\
Rendimiento de clase Frontier que compite con modelos más grandes a una fracción del costo.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) [spark\\
Gemini 3.1 Flash-Lite\\
Nuevo\\
\\
Modelo de uso general de gran volumen y sensible a los costos con el rendimiento y la calidad de la serie Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=es-419) [🍌\\
Nano Banana 2 y Nano Banana Pro\\
\\
\\
Modelos de vanguardia para la generación y edición de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419) [video\_library\\
Veo 3.1\\
\\
\\
Nuestro modelo de generación de videos de vanguardia, con audio nativo.](https://ai.google.dev/gemini-api/docs/video?hl=es-419) [spark\\
Gemini Robotics\\
\\
\\
Un modelo de lenguaje de visión (VLM) que aporta las capacidades de agente de Gemini a la robótica y permite un razonamiento avanzado en el mundo físico.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=es-419)

## Explora las capacidades

[imagesmode\\
\\
Generación de imágenes nativa (Nano Banana)\\
\\
\\
Genera y edita imágenes altamente contextuales de forma nativa con Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419) [article\\
\\
Contexto largo\\
\\
\\
Ingresa millones de tokens en los modelos de Gemini y obtén información de imágenes, videos y documentos no estructurados.](https://ai.google.dev/gemini-api/docs/long-context?hl=es-419) [code\\
\\
Resultados estructurados\\
\\
\\
Restringe Gemini para que responda con JSON, un formato de datos estructurados adecuado para el procesamiento automatizado.](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419) [functions\\
\\
Llamada a función\\
\\
\\
Crea flujos de trabajo de agentes conectando Gemini a APIs y herramientas externas.](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) [videocam\\
\\
Generación de video con Veo 3.1\\
\\
\\
Crea contenido de video de alta calidad a partir de instrucciones de texto o imágenes con nuestro modelo de vanguardia.](https://ai.google.dev/gemini-api/docs/video?hl=es-419) [android\_recorder\\
\\
Agentes de voz con la API de Live\\
\\
\\
Crea aplicaciones y agentes de voz en tiempo real con la API de Live.](https://ai.google.dev/gemini-api/docs/live?hl=es-419) [build\\
\\
Herramientas\\
\\
\\
Conecta Gemini al mundo a través de herramientas integradas, como la Búsqueda de Google, el contexto de URL, Google Maps, la ejecución de código y el uso de la computadora.](https://ai.google.dev/gemini-api/docs/tools?hl=es-419) [stacks\\
\\
Comprensión de documentos\\
\\
\\
Procesa hasta 1,000 páginas de archivos PDF con comprensión multimodal completa o con otros tipos de archivos basados en texto.](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419) [cognition\_2\\
\\
Pensar\\
\\
\\
Explora cómo las capacidades de pensamiento mejoran el razonamiento para las tareas y los agentes complejos.](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)

[Google AI Studio\\
\\
\\
Prueba instrucciones, administra tus claves de API, supervisa el uso y crea prototipos.](https://aistudio.google.com/?hl=es-419) [group\\
\\
Comunidad de desarrolladores\\
\\
\\
Haz preguntas y encuentra soluciones de otros desarrolladores y de ingenieros de Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=es-419) [menu\_book\\
\\
Referencia de la API\\
\\
\\
Encuentra información detallada sobre la API de Gemini en la documentación de referencia oficial.](https://ai.google.dev/api?hl=es-419) [sensors\\
\\
Estado\\
\\
\\
Verifica el estado de la API de Gemini, Google AI Studio y nuestros servicios de modelos.](https://aistudio.google.com/status?hl=es-419)

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-03-03 (UTC)




\[\[\["Fácil de comprender","easyToUnderstand","thumb-up"\],\["Resolvió mi problema","solvedMyProblem","thumb-up"\],\["Otro","otherUp","thumb-up"\]\],\[\["Falta la información que necesito","missingTheInformationINeed","thumb-down"\],\["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"\],\["Desactualizado","outOfDate","thumb-down"\],\["Problema de traducción","translationIssue","thumb-down"\],\["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"\],\["Otro","otherDown","thumb-down"\]\],\["Última actualización: 2026-03-03 (UTC)"\],\[\],\[\]\]