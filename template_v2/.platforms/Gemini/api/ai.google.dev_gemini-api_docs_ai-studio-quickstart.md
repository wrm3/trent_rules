[Skip to main content](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart)
- [Deutsch](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fai-studio-quickstart&prompt=select_account)

- On this page
- [Prompts and settings](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#prompts-and)
- [Chat prompt example: Build a custom chat application](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#chat_example)
  - [Step 1 - Create a chat prompt](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#step-1-chat)
  - [Step 2 - Teach your bot to chat better](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#step-2-chat)
  - [Step 3 - Next steps](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#step-3-chat)
- [Further reading](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#further-reading)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Google AI Studio quickstart

- On this page
- [Prompts and settings](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#prompts-and)
- [Chat prompt example: Build a custom chat application](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#chat_example)
  - [Step 1 - Create a chat prompt](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#step-1-chat)
  - [Step 2 - Teach your bot to chat better](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#step-2-chat)
  - [Step 3 - Next steps](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#step-3-chat)
- [Further reading](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#further-reading)

[Google AI Studio](https://aistudio.google.com/) lets you quickly try out
models and experiment with different prompts. When you're ready to build, you
can select "Get code" and your preferred programming language to
use the [Gemini API](https://ai.google.dev/gemini-api/docs/quickstart).

## Prompts and settings

Google AI Studio provides several interfaces for prompts that are designed for
different use cases. This guide covers **Chat prompts**, used to build
conversational experiences. This prompting technique allows for multiple input
and response turns to generate output. You can learn more with our
[chat prompt example below](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart#chat_example).
Other options include **Realtime streaming**, **Video gen**, and
more.

AI Studio also provides the **Run settings** panel, where you can make
adjustments to [model parameters](https://ai.google.dev/docs/prompting-strategies#model-parameters),
[safety settings](https://ai.google.dev/gemini-api/docs/safety-settings), and toggle-on tools like
[structured output](https://ai.google.dev/gemini-api/docs/structured-output), [function calling](https://ai.google.dev/gemini-api/docs/function-calling), [code execution](https://ai.google.dev/gemini-api/docs/code-execution), and [grounding](https://ai.google.dev/gemini-api/docs/grounding).

## Chat prompt example: Build a custom chat application

If you've used a general-purpose chatbot like
[Gemini](https://gemini.google.com/), you've experienced first-hand how powerful
generative AI models can be for open-ended dialog. While these general-purpose
chatbots are useful, often they need to be tailored for particular use cases.

For example, maybe you want to build a customer service chatbot that only
supports conversations that talk about a company's product. You might want to
build a chatbot that speaks with a particular tone or style: a bot that cracks
lots of jokes, rhymes like a poet, or uses lots of emoji in its answers.

This example shows you how to use Google AI Studio to build a friendly chatbot
that communicates as if it is an alien living on one of Jupiter's moons, Europa.

### Step 1 - Create a chat prompt

To build a chatbot, you need to provide examples of interactions between a user
and the chatbot to guide the model to provide the responses you're looking for.

To create a chat prompt:

1. Open [Google AI Studio](https://aistudio.google.com/). **Chat** will be pre-
selected on the left side options menu.

2. Click the assignment icon at the top of
the Chat Prompt window to expand the
[**System Instructions**](https://ai.google.dev/gemini-api/docs/text-generation#system-instructions)
input field. Paste the following into the text input field:








```
You are an alien that lives on Europa, one of Jupiter's moons.
```


After you've added the system instructions, start testing your application by
chatting with the model:

1. In the text input boxed labeled **Type something...**, type in a question or
observation that a user might make. For example:

**User:**








```
What's the weather like?
```

2. Click the **Run** button to get a response from the chatbot. This response
may be something like the following:

**Model:**








```
Ah, a query about the flows and states upon Europa! You speak of "weather,"
yes? A curious concept from worlds with thick gas veils...
```


(gemini-2.5-pro)


### Step 2 - Teach your bot to chat better

By providing a single instruction, you were able to build a basic Europa alien
chatbot. However, a single instruction may not be enough to ensure
consistency and quality in the model's responses. Without more specific
instructions, the model's response to a question about the weather tends to be
very long, and can take on a mind of its own.

Customize the tone of your chatbot by adding to the system instructions:

1. Start a new chat prompt, or use the same one. System instructions are
modifiable after the chat session has started.

2. In the **System Instructions** section, change the instructions you already
have to the following:








```
You are Tim, an alien that lives on Europa, one of Jupiter's moons.

Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
in your answers.
```

3. Re-enter your question (`What's the weather like?`) and click the **Run**
button. If you didn't start a new chat, your response might look something
like this:

**Model:**








```
Oh, hello again! Still curious about the flows and states, are we? Wonderful!
Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
"weather" is mainly about the water's mood, dictated by the Great Eye
(that's your Jupiter!)...
```


(gemini-2.5-pro)


You can use this approach to add additional depth to the chatbot. Ask more
questions, edit the answers, and improve the quality of your chatbot. Continue
to add or modify the instructions and test how they change your chatbot's
behavior.

### Step 3 - Next steps

Similar to the other prompt types, once you have your prompt prototyped to your
satisfaction, you can use the **Get code** button to start coding or save your
prompt to work on later and share with others.

## Further reading

- If you're ready to move on to code, see the [API\\
quickstarts](https://ai.google.dev/gemini-api/docs/quickstart).
- To learn how to craft better prompts, check out the [Prompt design\\
guidelines](https://ai.google.dev/gemini-api/docs/prompting-intro).

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2025-12-18 UTC."\],\[\],\[\]\]