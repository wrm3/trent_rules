[Skip to main content](https://ai.google.dev/gemini-api/docs/tools#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/tools)
- [Deutsch](https://ai.google.dev/gemini-api/docs/tools?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/tools?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/tools?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/tools?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/tools?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/tools?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/tools?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/tools?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/tools?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/tools?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/tools?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/tools?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/tools?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/tools?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/tools?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/tools?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/tools?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/tools?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Ftools&prompt=select_account)

- On this page
- [Available built-in tools](https://ai.google.dev/gemini-api/docs/tools#build-in-tools)
- [Available Agents](https://ai.google.dev/gemini-api/docs/tools#available-agents)
- [How tools execution works](https://ai.google.dev/gemini-api/docs/tools#how-tools-execution-works)
  - [Built-in tool flow](https://ai.google.dev/gemini-api/docs/tools#built-in_tool_flow)
  - [Custom tool flow (Function Calling)](https://ai.google.dev/gemini-api/docs/tools#custom_tool_flow_function_calling)
- [Structured outputs vs. function Calling](https://ai.google.dev/gemini-api/docs/tools#structured_outputs_vs_function_calling)
- [Structured outputs with tools](https://ai.google.dev/gemini-api/docs/tools#structured-outputs)
- [Building agents](https://ai.google.dev/gemini-api/docs/tools#building-agents)
  - [Agent frameworks](https://ai.google.dev/gemini-api/docs/tools#agent_frameworks)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Using Tools & Agents with Gemini API

- On this page
- [Available built-in tools](https://ai.google.dev/gemini-api/docs/tools#build-in-tools)
- [Available Agents](https://ai.google.dev/gemini-api/docs/tools#available-agents)
- [How tools execution works](https://ai.google.dev/gemini-api/docs/tools#how-tools-execution-works)
  - [Built-in tool flow](https://ai.google.dev/gemini-api/docs/tools#built-in_tool_flow)
  - [Custom tool flow (Function Calling)](https://ai.google.dev/gemini-api/docs/tools#custom_tool_flow_function_calling)
- [Structured outputs vs. function Calling](https://ai.google.dev/gemini-api/docs/tools#structured_outputs_vs_function_calling)
- [Structured outputs with tools](https://ai.google.dev/gemini-api/docs/tools#structured-outputs)
- [Building agents](https://ai.google.dev/gemini-api/docs/tools#building-agents)
  - [Agent frameworks](https://ai.google.dev/gemini-api/docs/tools#agent_frameworks)

Tools and Agents extend the capabilities of Gemini models, enabling them to take
action in the world, access real-time information, and perform complex
computational tasks. Models can use tools in both standard request-response
interactions and real-time streaming sessions using the
[Live API](https://ai.google.dev/gemini-api/docs/live-tools).

- **Tools** are specific capabilities (like Google Search or Code Execution)
that a model can use to answer queries.
- **Agents** are systems that can plan, execute, and synthesize multi-step
tasks to achieve a user goal.

The Gemini API provides a suite of fully managed, built-in tools and agents
optimized for Gemini models, or you can define custom tools using [Function\\
Calling](https://ai.google.dev/gemini-api/docs/function-calling).

## Available built-in tools

| Tool | Description | Use Cases |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search) | Ground responses in current events and facts from the web to reduce hallucinations. | \- Answering questions about recent events <br> \- Verifying facts with diverse sources |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding) | Build location-aware assistants that can find places, get directions, and provide rich local context. | \- Planning travel itineraries with multiple stops <br> \- Finding local businesses based on user criteria |
| [Code Execution](https://ai.google.dev/gemini-api/docs/code-execution) | Allow the model to write and run Python code to solve math problems or process data accurately. | \- Solving complex mathematical equations <br> \- Processing and analyzing text data precisely |
| [URL Context](https://ai.google.dev/gemini-api/docs/url-context) | Direct the model to read and analyze content from specific web pages or documents. | \- Answering questions based on specific URLs or documents <br> \- Retrieving information across different web pages |
| [Computer Use (Preview)](https://ai.google.dev/gemini-api/docs/computer-use) | Enable Gemini to view a screen and generate actions to interact with web browser UIs (Client-side execution). | \- Automating repetitive web-based workflows <br> \- Testing web application user interfaces |
| [File Search](https://ai.google.dev/gemini-api/docs/file-search) | Index and search your own documents to enable Retrieval Augmented Generation (RAG). | \- Searching technical manuals <br> \- Question answering over proprietary data |

See the [Pricing page](https://ai.google.dev/gemini-api/docs/pricing#pricing_for_tools) for details
on costs associated with specific tools.

## Available Agents

| Agent | Description | Use Cases |
| --- | --- | --- |
| [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research) | Autonomously plans, executes, and synthesizes multi-step research tasks. | \- Market analysis <br> \- Due diligence <br> \- Literature reviews |

## How tools execution works

Tools allow the model to request actions during a conversation. The flow differs
depending on whether the tool is built-in (managed by Google) or custom (managed
by you).

### Built-in tool flow

For built-in tools like Google Search or Code Execution, the entire process
happens within one API call:

1. **You** send a prompt: "What is the square root of the latest stock price of
GOOG?"
2. **Gemini** decides it needs tools and executes them on Google's servers
(e.g., searches for the stock price, then runs Python code to calculate the
square root).
3. **Gemini** sends back the final answer grounded in the tool results.

### Custom tool flow (Function Calling)

For custom tools and Computer Use, your application handles the execution:

1. **You** send a prompt along with functions (tools) declarations.
2. **Gemini** might send back a structured JSON to call a specific function
(for example, `{"name": "get_order_status", "args": {"order_id": "123"}}`).
3. **You** execute the function in your application or environment.
4. **You** send the function results back to Gemini.
5. **Gemini** uses the results to generate a final response or another tool
call.

Learn more in the [Function calling guide](https://ai.google.dev/gemini-api/docs/function-calling).

## Structured outputs vs. function Calling

Gemini offers two methods for generating structured outputs. Use [Function\\
calling](https://ai.google.dev/gemini-api/docs/function-calling) when the model needs to perform an
intermediate step by connecting to your own tools or data systems. Use
[Structured Outputs](https://ai.google.dev/gemini-api/docs/structured-output) when you strictly need
the model's final response to adhere to a specific schema, such as for rendering
a custom UI.

## Structured outputs with tools

You can combine [Structured Outputs](https://ai.google.dev/gemini-api/docs/structured-output) with
built-in tools to ensure that model responses grounded in external data or
computation still adhere to a strict schema.

See [Structured outputs with tools](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe#structured_outputs_with_tools)
for code examples.

## Building agents

Agents are systems that use models and tools to complete multi-step tasks. While
Gemini provides the reasoning capabilities (the "brain") and the essential tools
(the "hands"), you often need an orchestration framework to manage the agent's
memory, plan loops, and perform complex tool chaining.

To maximize reliability in multi-step workflows, you should craft instructions
that explicitly control how the model reasons and plans. While Gemini provides
strong general reasoning, complex agents benefit from prompts that enforce
specific behaviors like persistence in the face of issues, risk assessment, and
proactive planning.

See the [Agentic workflows](https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-workflows)
for strategies on designing these prompts. Here is a example, of a [system\\
instruction](https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-si-template) that
improved performance on several agentic benchmarks by around 5%.

### Agent frameworks

Gemini integrates with leading open-source agent frameworks such as:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example): Build
stateful, complex application flows and multi-agent systems using graph
structures.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index): Connect Gemini agents to
your private data for RAG-enhanced workflows.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example): Orchestrate collaborative,
role-playing autonomous AI agents.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example): Build
AI-powered user interfaces and agents in JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): An
open-source framework for building and orchestrating interoperable AI
agents.

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-02-19 UTC."\],\[\],\[\]\]