[Ir para o conteúdo principal](https://ai.google.dev/gemini-api/docs?hl=pt-br#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=pt-br)](https://ai.google.dev/)

`/`

- English
- Deutsch
- Español – América Latina
- Français
- Indonesia
- Italiano
- Polski
- Português – Brasil
- Shqip
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어

[Conferir a chave de API](https://aistudio.google.com/apikey?hl=pt-br) [Manual](https://github.com/google-gemini/cookbook) [Comunidade](https://discuss.ai.google.dev/c/gemini-api/?hl=pt-br)Fazer login


O Gemini 3.1 Flash-Lite já está disponível em pré-lançamento. [Teste no AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=pt-br).




- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

# API Gemini

O caminho mais rápido do comando à produção com o Gemini, o Veo, o Nano Banana e muito mais.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

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

### Go

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

### Java

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

### C\#

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

### REST

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

[Comece a criar](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br)

Siga nosso guia de início rápido para receber uma chave de API e fazer sua primeira chamada de API em minutos.

* * *

## Conheça os modelos

[Ver tudo](https://ai.google.dev/gemini-api/docs/models?hl=pt-br)

[auto\_awesome\\
Gemini 3.1 Pro\\
Novo\\
\\
Nosso modelo mais inteligente, o melhor do mundo para compreensão multimodal, tudo com base em um raciocínio de última geração.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) [spark\\
Gemini 3 Flash\\
Novo\\
\\
Desempenho de classe avançada que rivaliza com modelos maiores a uma fração do custo.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) [spark\\
Gemini 3.1 Flash-Lite\\
Novo\\
\\
Modelo de alto volume e sensível a custos com a performance e a qualidade da série Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=pt-br) [🍌\\
Nano Banana 2 e Nano Banana Pro\\
\\
\\
Modelos de edição e geração de imagens de última geração.](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) [video\_library\\
Veo 3.1\\
\\
\\
Nosso modelo de geração de vídeos de última geração, com áudio nativo.](https://ai.google.dev/gemini-api/docs/video?hl=pt-br) [spark\\
Gemini Robotics\\
\\
\\
Um modelo de visão-linguagem (VLM) que traz os recursos de agente do Gemini para a robótica e permite o raciocínio avançado no mundo físico.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pt-br)

## Conheça os recursos

[imagesmode\\
\\
Geração de imagens nativa (Nano Banana)\\
\\
\\
Gere e edite imagens altamente contextuais de forma nativa com o Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) [article\\
\\
Contexto longo\\
\\
\\
Insira milhões de tokens nos modelos do Gemini e extraia insights de imagens, vídeos e documentos não estruturados.](https://ai.google.dev/gemini-api/docs/long-context?hl=pt-br) [code\\
\\
Respostas estruturadas\\
\\
\\
Restrinja o Gemini a responder com JSON, um formato de dados estruturados adequado para processamento automatizado.](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) [functions\\
\\
Chamada de função\\
\\
\\
Crie fluxos de trabalho com agentes conectando o Gemini a APIs e ferramentas externas.](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) [videocam\\
\\
Geração de vídeos com o Veo 3.1\\
\\
\\
Crie conteúdo de vídeo de alta qualidade com base em comandos de texto ou imagem usando nosso modelo de última geração.](https://ai.google.dev/gemini-api/docs/video?hl=pt-br) [android\_recorder\\
\\
Agentes de voz com a API Live\\
\\
\\
Crie aplicativos e agentes de voz em tempo real com a API Live.](https://ai.google.dev/gemini-api/docs/live?hl=pt-br) [build\\
\\
Ferramentas\\
\\
\\
Conecte o Gemini ao mundo com ferramentas integradas como a Pesquisa Google, o contexto de URL, o Google Maps, a execução de código e o uso de computadores.](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br) [stacks\\
\\
Document Understanding\\
\\
\\
Processe até 1.000 páginas de arquivos PDF com compreensão multimodal completa ou outros tipos de arquivos baseados em texto.](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br) [cognition\_2\\
\\
Pensando\\
\\
\\
Saiba como as capacidades de pensamento melhoram o raciocínio para tarefas e agentes complexos.](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)

[Google AI Studio\\
\\
\\
Testar comandos, gerenciar chaves de API, monitorar o uso e criar protótipos.](https://aistudio.google.com/?hl=pt-br) [group\\
\\
Comunidade de desenvolvedores\\
\\
\\
Tire dúvidas e encontre soluções com outros desenvolvedores e engenheiros do Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=pt-br) [menu\_book\\
\\
Referência da API\\
\\
\\
Encontre informações detalhadas sobre a API Gemini na documentação de referência oficial.](https://ai.google.dev/api?hl=pt-br) [sensors\\
\\
Status\\
\\
\\
Confira o status da API Gemini, do Google AI Studio e dos nossos serviços de modelo.](https://aistudio.google.com/status?hl=pt-br)

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-03-03 UTC.




\[\[\["Fácil de entender","easyToUnderstand","thumb-up"\],\["Meu problema foi resolvido","solvedMyProblem","thumb-up"\],\["Outro","otherUp","thumb-up"\]\],\[\["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"\],\["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"\],\["Desatualizado","outOfDate","thumb-down"\],\["Problema na tradução","translationIssue","thumb-down"\],\["Problema com as amostras / o código","samplesCodeIssue","thumb-down"\],\["Outro","otherDown","thumb-down"\]\],\["Última atualização 2026-03-03 UTC."\],\[\],\[\]\]