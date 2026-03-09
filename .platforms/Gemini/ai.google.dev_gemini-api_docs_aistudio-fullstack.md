[Skip to main content](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/aistudio-fullstack)
- [Deutsch](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Faistudio-fullstack&prompt=select_account)

- On this page
- [Server-side runtime](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#server-side)
  - [Using npm packages](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#using_npm_packages)
- [Managing secrets securely](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#secrets)
  - [Setting up OAuth](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#oauth-setup)
- [Building multiplayer experiences](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#multiplayer)
  - [Tips for testing multiplayer apps](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#testing-multiplayer)
- [Best practices](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#best-practices)
- [What's Next?](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#whats-next)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Developing Full-Stack Apps in Google AI Studio

- On this page
- [Server-side runtime](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#server-side)
  - [Using npm packages](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#using_npm_packages)
- [Managing secrets securely](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#secrets)
  - [Setting up OAuth](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#oauth-setup)
- [Building multiplayer experiences](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#multiplayer)
  - [Tips for testing multiplayer apps](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#testing-multiplayer)
- [Best practices](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#best-practices)
- [What's Next?](https://ai.google.dev/gemini-api/docs/aistudio-fullstack#whats-next)

Google AI Studio now supports full-stack development, enabling you to build
applications that go beyond client-side prototypes. With a
server-side runtime, you can manage secrets, connect to external APIs, and build
real-time multiplayer experiences.

## Server-side runtime

Google AI Studio applications can now include a server-side component (Node.js).
This lets you:

- **Execute server-side logic**: Run code that shouldn't be exposed to the
client.
- **Access npm packages**: The [Antigravity Agent](https://antigravity.google/docs/agent)
can install and use packages from the vast npm ecosystem.
- **Handle secrets**: Securely use API keys and credentials.

### Using npm packages

You don't need to manually run `npm install`. Simply ask the Agent to add
functionality that requires a package, and it will handle the installation and
import.

**Example**: \> "Use `axios` to fetch data from the external API."

## Managing secrets securely

With server-side code and secrets management, you can now build apps that
interact with the world.

- **Third-party APIs**: Connect to services like Stripe, SendGrid, or custom
REST APIs.
- **Databases**: Connect to external databases (e.g., via Supabase, Firebase,
or MongoDB Atlas) to persist data beyond the session.

When building real-world apps, you often need to connect to third-party services
(like Twilio, Slack, or databases) that require API keys. You can add keys
manually with the following steps:

1. **Add a secret**: Go to the **Settings** menu in Google AI Studio and look
for the Secrets section.
2. **Store your key**: Add your API keys or secret tokens here.
3. **Access in code**: The Agent can write server-side code that accesses these
secrets securely (typically via environment variables), ensuring they are
never exposed to the client-side browser.

When needed, the agent will
also show a card in the chat prompting you to add keys whenever a new secret is
needed or when a key new key is detected in the project's env variables.

### Setting up OAuth

One key use case for secrets management is to set up OAuth to connect to other
websites or apps. When your prompt includes instructions about connecting to a
3rd party app that requires OAuth authentication, the agent will provide
instructions on how to set up OAuth for that application. These instructions
will include the necessary callback URLs to configure your OAuth Application.
You can also find the callback URLs under **Integrations** in the Settings panel.

## Building multiplayer experiences

The full-stack runtime enables real-time collaboration features.

- **Real-time state**: You can ask the Agent to build features like "a live
chat," "a collaborative whiteboard," or "a multiplayer game."
- **Synced sessions**: The server manages the state, allowing multiple users
to interact with the same application instance in real-time.

**Example prompt**: \> "Make this a multiplayer game where players can see each
other's cursors."

### Tips for testing multiplayer apps

You can test multiplayer mode in two ways before deploying your app.

1. Open your app in Google AI Studio Build mode in multiple tabs. When
developing in Build mode, your app is in a dev container. Opening the
app in multiple tabs will let you simulate multiple players using your app.
2. Share the app with others using the **Share** menu at the top right.
then use the **Shared URL** from the **Integrations**
tab of the **Share** menu to use the app with the players that you've shared
your app with.

## Best practices

- **Secrets security**: Always use the Secrets manager for sensitive keys.
Never hardcode them in your files.
- **Separation of concerns**: Keep your UI logic in the client-side framework
(React/Angular) and your business logic/data handling on the server side.
- **Error handling**: Ensure your server-side code robustly handles errors
from external API calls to prevent the app from crashing.

## What's Next?

- [Build Apps in Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode)
- [App Gallery](https://aistudio.google.com/apps?source=showcase)

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-20 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-02-20 UTC."\],\[\],\[\]\]