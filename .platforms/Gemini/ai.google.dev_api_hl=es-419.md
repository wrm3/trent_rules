[Ir al contenido principal](https://ai.google.dev/api?hl=es-419#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=es-419)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/api)
- [Deutsch](https://ai.google.dev/api?hl=de)
- [Español – América Latina](https://ai.google.dev/api?hl=es-419)
- [Français](https://ai.google.dev/api?hl=fr)
- [Indonesia](https://ai.google.dev/api?hl=id)
- [Italiano](https://ai.google.dev/api?hl=it)
- [Polski](https://ai.google.dev/api?hl=pl)
- [Português – Brasil](https://ai.google.dev/api?hl=pt-br)
- [Shqip](https://ai.google.dev/api?hl=sq)
- [Tiếng Việt](https://ai.google.dev/api?hl=vi)
- [Türkçe](https://ai.google.dev/api?hl=tr)
- [Русский](https://ai.google.dev/api?hl=ru)
- [עברית](https://ai.google.dev/api?hl=he)
- [العربيّة](https://ai.google.dev/api?hl=ar)
- [فارسی](https://ai.google.dev/api?hl=fa)
- [हिंदी](https://ai.google.dev/api?hl=hi)
- [বাংলা](https://ai.google.dev/api?hl=bn)
- [ภาษาไทย](https://ai.google.dev/api?hl=th)
- [中文 – 简体](https://ai.google.dev/api?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/api?hl=zh-tw)
- [日本語](https://ai.google.dev/api?hl=ja)
- [한국어](https://ai.google.dev/api?hl=ko)

[Cómo obtener una clave de API](https://aistudio.google.com/apikey?hl=es-419) [Guía de soluciones](https://github.com/google-gemini/cookbook) [Comunidad](https://discuss.ai.google.dev/c/gemini-api/?hl=es-419)

[Acceder](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fapi%3Fhl%3Des-419&prompt=select_account)

- En esta página
- [Extremos principales](https://ai.google.dev/api?hl=es-419#primary-endpoints)
- [Autenticación](https://ai.google.dev/api?hl=es-419#authentication)
- [Generación de contenido](https://ai.google.dev/api?hl=es-419#content-generation)
  - [Estructura del cuerpo de la solicitud](https://ai.google.dev/api?hl=es-419#request-body-structure)
  - [Estructura del cuerpo de la respuesta](https://ai.google.dev/api?hl=es-419#response-body-structure)
- [Ejemplos de solicitudes](https://ai.google.dev/api?hl=es-419#request-examples)
  - [Instrucción de solo texto](https://ai.google.dev/api?hl=es-419#text-only-prompt)
  - [Instrucción multimodal (texto e imagen)](https://ai.google.dev/api?hl=es-419#multimodal-prompt)
  - [Conversaciones de varios turnos (chat)](https://ai.google.dev/api?hl=es-419#multi-turn-conversations)
  - [Conclusiones clave](https://ai.google.dev/api?hl=es-419#key-takeaways)
- [Ejemplos de respuestas](https://ai.google.dev/api?hl=es-419#response-examples)
  - [Respuesta de solo texto](https://ai.google.dev/api?hl=es-419#text-only-response)
- [API en vivo (BidiGenerateContent) API de WebSockets](https://ai.google.dev/api?hl=es-419#live-api)
- [Modelos especializados](https://ai.google.dev/api?hl=es-419#specialized-models)
- [APIs de la plataforma](https://ai.google.dev/api?hl=es-419#platform-apis)
- [¿Qué sigue?](https://ai.google.dev/api?hl=es-419#whats-next)


Ya está disponible la versión preliminar de Gemini 3.1 Flash-Lite. [Pruébalo en AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=es-419).




- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Referencia de la API](https://ai.google.dev/api?hl=es-419)

¿Te resultó útil?



 Enviar comentarios



# Gemini API reference

- En esta página
- [Extremos principales](https://ai.google.dev/api?hl=es-419#primary-endpoints)
- [Autenticación](https://ai.google.dev/api?hl=es-419#authentication)
- [Generación de contenido](https://ai.google.dev/api?hl=es-419#content-generation)
  - [Estructura del cuerpo de la solicitud](https://ai.google.dev/api?hl=es-419#request-body-structure)
  - [Estructura del cuerpo de la respuesta](https://ai.google.dev/api?hl=es-419#response-body-structure)
- [Ejemplos de solicitudes](https://ai.google.dev/api?hl=es-419#request-examples)
  - [Instrucción de solo texto](https://ai.google.dev/api?hl=es-419#text-only-prompt)
  - [Instrucción multimodal (texto e imagen)](https://ai.google.dev/api?hl=es-419#multimodal-prompt)
  - [Conversaciones de varios turnos (chat)](https://ai.google.dev/api?hl=es-419#multi-turn-conversations)
  - [Conclusiones clave](https://ai.google.dev/api?hl=es-419#key-takeaways)
- [Ejemplos de respuestas](https://ai.google.dev/api?hl=es-419#response-examples)
  - [Respuesta de solo texto](https://ai.google.dev/api?hl=es-419#text-only-response)
- [API en vivo (BidiGenerateContent) API de WebSockets](https://ai.google.dev/api?hl=es-419#live-api)
- [Modelos especializados](https://ai.google.dev/api?hl=es-419#specialized-models)
- [APIs de la plataforma](https://ai.google.dev/api?hl=es-419#platform-apis)
- [¿Qué sigue?](https://ai.google.dev/api?hl=es-419#whats-next)

En esta referencia de la API, se describen las APIs estándar, de transmisión y en tiempo real que puedes usar para interactuar con los modelos de Gemini. Puedes usar las APIs de REST en cualquier entorno que admita solicitudes HTTP. Consulta la [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419) para comenzar a realizar tu primera llamada a la API. Si buscas referencias para nuestras bibliotecas y SDKs específicos del lenguaje, ve al vínculo de ese lenguaje en la navegación de la izquierda, en **Referencias del SDK**.

## Extremos principales

La API de Gemini se organiza en torno a los siguientes endpoints principales:

- **Generación de contenido estándar ( [`generateContent`](https://ai.google.dev/api/generate-content?hl=es-419#method:-models.generatecontent)):**
Es un extremo REST estándar que procesa tu solicitud y devuelve la respuesta completa del modelo en un solo paquete. Es ideal para tareas no interactivas en las que puedes esperar el resultado completo.
- **Generación de contenido de transmisión ( [`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=es-419#method:-models.streamgeneratecontent)):**
Usa eventos enviados por el servidor (SSE) para enviarte fragmentos de la respuesta a medida que se generan. Esto proporciona una experiencia más rápida e interactiva para aplicaciones como los chatbots.
- **API de Live ( [`BidiGenerateContent`](https://ai.google.dev/api/live?hl=es-419#send-messages)):** Es una API con estado basada en WebSocket para la transmisión bidireccional, diseñada para casos de uso conversacionales en tiempo real.
- **Modo por lotes ( [`batchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=es-419)):** Es un extremo REST estándar para enviar lotes de solicitudes `generateContent`.
- **Embeddings ( [`embedContent`](https://ai.google.dev/api/embeddings?hl=es-419)):** Es un extremo REST estándar que genera un vector de incorporación de texto a partir de la entrada `Content`.
- **APIs de Gen Media:** Son extremos para generar contenido multimedia con nuestros modelos especializados, como [Imagen para la generación de imágenes](https://ai.google.dev/api/models?hl=es-419#method:-models.predict) y [Veo para la generación de videos](https://ai.google.dev/api/models?hl=es-419#method:-models.predictlongrunning).
Gemini también tiene estas capacidades integradas, a las que puedes acceder con la API de `generateContent`.
- **APIs de plataforma:** Son extremos de utilidad que admiten capacidades principales, como [subir archivos](https://ai.google.dev/api/files?hl=es-419) y [contar tokens](https://ai.google.dev/api/tokens?hl=es-419).

## Autenticación

Todas las solicitudes a la API de Gemini deben incluir un encabezado `x-goog-api-key` con tu clave de API. Crea una con unos pocos clics en [Google AI Studio](https://aistudio.google.com/app/apikey?hl=es-419).

A continuación, se muestra un ejemplo de solicitud con la clave de API incluida en el encabezado:

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
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

Para obtener instrucciones sobre cómo pasar tu clave a la API con los SDKs de Gemini, consulta la guía [Cómo usar claves de la API de Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419).

## Generación de contenido

Este es el extremo central para enviar instrucciones al modelo. Existen dos extremos para generar contenido. La diferencia clave es cómo recibes la respuesta:

- **[`generateContent`](https://ai.google.dev/api/generate-content?hl=es-419#method:-models.generatecontent)**
**(REST)**:
Recibe una solicitud y proporciona una sola respuesta después de que el modelo finaliza toda su generación.
- **[`streamGenerateContent`](https://ai.google.dev/api/generate-content?hl=es-419#method:-models.streamgeneratecontent) (SSE)**: Recibe exactamente la misma solicitud, pero el modelo transmite fragmentos de la respuesta a medida que se generan. Esto proporciona una mejor experiencia del usuario para las aplicaciones interactivas, ya que te permite mostrar resultados parciales de inmediato.

### Estructura del cuerpo de la solicitud

El [cuerpo de la solicitud](https://ai.google.dev/api/generate-content?hl=es-419#request-body) es un objeto JSON que es **idéntico** para los modos estándar y de transmisión, y se compila a partir de algunos objetos principales:

- Objeto [`Content`](https://ai.google.dev/api/caching?hl=es-419#Content): Representa un solo turno en una conversación.
- Objeto [`Part`](https://ai.google.dev/api/caching?hl=es-419#Part): Es un fragmento de datos dentro de un turno de `Content` (como texto o una imagen).
- `inline_data` ( [`Blob`](https://ai.google.dev/api/caching?hl=es-419#Blob)): Es un contenedor para los bytes de medios sin procesar y su tipo de MIME.

En el nivel más alto, el cuerpo de la solicitud contiene un objeto `contents`, que es una lista de objetos `Content`, cada uno de los cuales representa turnos en la conversación. En la mayoría de los casos, para la generación de texto básica, tendrás un solo objeto `Content`, pero si deseas mantener el historial de conversaciones, puedes usar varios objetos `Content`.

A continuación, se muestra un cuerpo de solicitud de `generateContent` típico:

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
          "role": "user",\
          "parts": [\
              // A list of Part objects goes here\
          ]\
      },\
      {\
          "role": "model",\
          "parts": [\
              // A list of Part objects goes here\
          ]\
      }\
    ]
  }'
```

### Estructura del cuerpo de la respuesta

El [cuerpo de la respuesta](https://ai.google.dev/api/generate-content?hl=es-419#response-body) es similar para los modos de transmisión y estándar, excepto por lo siguiente:

- Modo estándar: El cuerpo de la respuesta contiene una instancia de [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=es-419#v1beta.GenerateContentResponse).
- Modo de transmisión: El cuerpo de la respuesta contiene un flujo de instancias de [`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=es-419#v1beta.GenerateContentResponse).

En términos generales, el cuerpo de la respuesta contiene un objeto `candidates`, que es una lista de objetos `Candidate`. El objeto `Candidate` contiene un objeto `Content` que tiene la respuesta generada que devolvió el modelo.

## Ejemplos de solicitudes

En los siguientes ejemplos, se muestra cómo se combinan estos componentes para diferentes tipos de solicitudes.

### Instrucción de solo texto

Una instrucción de texto simple consta de un array `contents` con un solo objeto `Content`. A su vez, el array `parts` de ese objeto contiene un solo objeto `Part` con un campo `text`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "parts": [\
          {\
            "text": "Explain how AI works in a single paragraph."\
          }\
        ]\
      }\
    ]
  }'
```

### Instrucción multimodal (texto e imagen)

Para proporcionar texto y una imagen en una instrucción, el array `parts` debe contener dos objetos `Part`: uno para el texto y otro para la imagen `inline_data`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{\
    "parts":[\
        {\
            "inline_data": {\
            "mime_type":"image/jpeg",\
            "data": "/9j/4AAQSkZJRgABAQ... (base64-encoded image)"\
            }\
        },\
        {"text": "What is in this picture?"},\
      ]\
    }]
  }'
```

### Conversaciones de varios turnos (chat)

Para crear una conversación con varios turnos, debes definir el array `contents` con varios objetos `Content`. La API usará todo este historial como contexto para la próxima respuesta. El `role` de cada objeto `Content` debe alternar entre `user` y `model`.

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "role": "user",\
        "parts": [\
          { "text": "Hello." }\
        ]\
      },\
      {\
        "role": "model",\
        "parts": [\
          { "text": "Hello! How can I help you today?" }\
        ]\
      },\
      {\
        "role": "user",\
        "parts": [\
          { "text": "Please write a four-line poem about the ocean." }\
        ]\
      }\
    ]
  }'
```

### Conclusiones clave

- `Content` es el sobre: Es el contenedor de nivel superior para un turno de mensaje, ya sea del usuario o del modelo.
- `Part` habilita la multimodalidad: Usa varios objetos `Part` dentro de un solo objeto `Content` para combinar diferentes tipos de datos (texto, URI de imagen, URI de video, etcétera).
- Elige tu método de datos:
  - Para los medios pequeños incorporados directamente (como la mayoría de las imágenes), usa un `Part` con `inline_data`.
  - Para archivos más grandes o archivos que quieras reutilizar en varias solicitudes, usa la API de File para subir el archivo y hacer referencia a él con una parte `file_data`.
- Administra el historial de conversaciones: Para las aplicaciones de chat que usan la API de REST, compila el array `contents` agregando objetos `Content` para cada turno, alternando entre los roles `"user"` y `"model"`. Si usas un SDK, consulta su documentación para conocer la forma recomendada de administrar el historial de conversaciones.

## Ejemplos de respuestas

En los siguientes ejemplos, se muestra cómo se combinan estos componentes para diferentes tipos de solicitudes.

### Respuesta de solo texto

Una respuesta de texto predeterminada consta de un array `candidates` con uno o más objetos `content` que contienen la respuesta del modelo.

A continuación, se muestra un ejemplo de una respuesta **estándar**:

```
{
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "text": "At its core, Artificial Intelligence works by learning from vast amounts of data ..."\
          }\
        ],\
        "role": "model"\
      },\
      "finishReason": "STOP",\
      "index": 1\
    }\
  ],
}
```

A continuación, se muestra una serie de respuestas de **transmisión**. Cada respuesta contiene un `responseId` que une la respuesta completa:

```
{
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "text": "The image displays"\
          }\
        ],\
        "role": "model"\
      },\
      "index": 0\
    }\
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  },
  "modelVersion": "gemini-2.5-flash-lite",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}

...

{
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "text": " the following materials:\n\n*   **Wood:** The accordion and the violin are primarily"\
          }\
        ],\
        "role": "model"\
      },\
      "index": 0\
    }\
  ],
  "usageMetadata": {
    "promptTokenCount": ...
  }
  "modelVersion": "gemini-2.5-flash-lite",
  "responseId": "mAitaLmkHPPlz7IPvtfUqQ4"
}
```

## API en vivo (BidiGenerateContent) API de WebSockets

La API de Live ofrece una API basada en WebSocket con estado para la transmisión bidireccional que permite casos de uso de transmisión en tiempo real. Puedes consultar la [guía de la API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419) y la [referencia de la API de Live](https://ai.google.dev/api/live?hl=es-419) para obtener más detalles.

## Modelos especializados

Además de la familia de modelos de Gemini, la API de Gemini ofrece extremos para modelos especializados, como [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=es-419), [Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=es-419) y modelos de [incorporación](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419). Puedes consultar estas guías en la sección Models.

## APIs de la plataforma

El resto de los extremos habilitan capacidades adicionales para usar con los extremos principales que se describieron hasta ahora. Consulta los temas [Modo por lotes](https://ai.google.dev/gemini-api/docs/batch-mode?hl=es-419) y [API de archivos](https://ai.google.dev/gemini-api/docs/files?hl=es-419) en la sección Guías para obtener más información.

## ¿Qué sigue?

Si recién comienzas, consulta las siguientes guías, que te ayudarán a comprender el modelo de programación de la API de Gemini:

- [Guía de inicio rápido de la API de Gemini](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419)
- [Guía de modelos de Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419)

También puedes consultar las guías de capacidades, que presentan diferentes funciones de la API de Gemini y proporcionan ejemplos de código:

- [Generación de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419)
- [Almacenamiento en caché del contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419)

¿Te resultó útil?



 Enviar comentarios



Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-02-25 (UTC)


¿Quieres brindar más información?






\[\[\["Fácil de comprender","easyToUnderstand","thumb-up"\],\["Resolvió mi problema","solvedMyProblem","thumb-up"\],\["Otro","otherUp","thumb-up"\]\],\[\["Falta la información que necesito","missingTheInformationINeed","thumb-down"\],\["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"\],\["Desactualizado","outOfDate","thumb-down"\],\["Problema de traducción","translationIssue","thumb-down"\],\["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"\],\["Otro","otherDown","thumb-down"\]\],\["Última actualización: 2026-02-25 (UTC)"\],\[\],\[\]\]