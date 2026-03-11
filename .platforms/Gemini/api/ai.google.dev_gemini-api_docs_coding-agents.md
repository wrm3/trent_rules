[Skip to main content](https://ai.google.dev/gemini-api/docs/coding-agents#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/coding-agents)
- [Deutsch](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/coding-agents?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/coding-agents?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/coding-agents?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/coding-agents?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Fcoding-agents&prompt=select_account)

- On this page
- [Available skills](https://ai.google.dev/gemini-api/docs/coding-agents#available-skills)
  - [gemini-api-dev](https://ai.google.dev/gemini-api/docs/coding-agents#gemini-api-dev)
  - [gemini-interactions-api](https://ai.google.dev/gemini-api/docs/coding-agents#gemini-interactions-api)
- [Verify installation](https://ai.google.dev/gemini-api/docs/coding-agents#verify-installation)
  - [1\. Verify agent behavior](https://ai.google.dev/gemini-api/docs/coding-agents#gemini-test)
  - [Verify manifest](https://ai.google.dev/gemini-api/docs/coding-agents#manifest-check)
- [Troubleshooting](https://ai.google.dev/gemini-api/docs/coding-agents#troubleshooting)
  - [Agent didn't discover the skill](https://ai.google.dev/gemini-api/docs/coding-agents#agent-discovery)
  - [Global vs. local conflict](https://ai.google.dev/gemini-api/docs/coding-agents#global-local-conflict)
- [Resources](https://ai.google.dev/gemini-api/docs/coding-agents#resources)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Set up your coding agent

- On this page
- [Available skills](https://ai.google.dev/gemini-api/docs/coding-agents#available-skills)
  - [gemini-api-dev](https://ai.google.dev/gemini-api/docs/coding-agents#gemini-api-dev)
  - [gemini-interactions-api](https://ai.google.dev/gemini-api/docs/coding-agents#gemini-interactions-api)
- [Verify installation](https://ai.google.dev/gemini-api/docs/coding-agents#verify-installation)
  - [1\. Verify agent behavior](https://ai.google.dev/gemini-api/docs/coding-agents#gemini-test)
  - [Verify manifest](https://ai.google.dev/gemini-api/docs/coding-agents#manifest-check)
- [Troubleshooting](https://ai.google.dev/gemini-api/docs/coding-agents#troubleshooting)
  - [Agent didn't discover the skill](https://ai.google.dev/gemini-api/docs/coding-agents#agent-discovery)
  - [Global vs. local conflict](https://ai.google.dev/gemini-api/docs/coding-agents#global-local-conflict)
- [Resources](https://ai.google.dev/gemini-api/docs/coding-agents#resources)

AI coding assistants are powerful but have limitations—training data cuts off
at a specific date, missing new API features and changes. Without access to
Gemini-specific documentation, agents may suggest generic patterns instead of
optimized approaches.

[Gemini API skills](https://github.com/google-gemini/gemini-skills)
address these gaps by giving your coding
agent direct access to the latest Gemini API documentation, integration
patterns, and best practices. This ensures your agent can offer more accurate
and specific code examples and guidance. By installing these skills, your
coding assistant stays current with the evolving Gemini API and its recommended
usage.

## Available skills

The following skills are available. Install the ones relevant to your use case.

- **[skills.sh](https://skills.sh/)**: Recommended. The open standard for portable agent behaviors.
- **[Context7](https://context7.com/)**: Supported for users already utilizing the Context7 ecosystem.

### gemini-api-dev

The core Gemini API development skill:

- Points your coding agent to official Gemini API documentation
- Provides best practices for building Gemini-powered applications
- Includes recommended patterns for common integrations

#### Install with skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Install with Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-interactions-api

Skill for building apps with the
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions). The Interactions API is a
unified interface for interacting with Gemini models and agents, designed for
agentic applications. This skill covers:

- Text generation, multi-turn chat, and streaming
- Function calling, structured output, and image generation
- Background execution and Deep Research agents
- Server-side conversation state management
- Python and TypeScript SDK patterns

#### Install with skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Install with Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Verify installation

After installing, confirm that your coding agent has indexed the skill and can
access the live Gemini API documentation.

### 1. Verify agent behavior

The most reliable way to verify is to ask your agent a technical question about Gemini API.

**Prompt:** "How do I use context caching with the Gemini API?"

A successful installation will:

- Reference specific Gemini methods like `cacheContent` or
`cachedContents.create`.
- Show an indicator that it is "Using skill: gemini-api-dev".

### Verify manifest

If the agent gives a generic answer, use the specific "discovery" command for
your environment to verify the skill is loaded.

| Environment | Verification method |
| --- | --- |
| Claude Code | Type `/skills` in the terminal to list all active manifests. |
| Cursor | Open **Settings > Rules**. Verify `gemini-api-dev` appears under "Agent Decides." |
| Antigravity | Type `/skills list` or check the **Customizations > Rules** sidebar. |
| Gemini CLI | Run `gemini skills list` or use the `/skills` slash command in-session. |
| Copilot | Type `@gemini /skills` (or just `/skills`) to view active extensions. |

## Troubleshooting

If your agent provides only general information or fails to recognize
Gemini-specific methods, check the following:

### Agent didn't discover the skill

Most agents index skills only on startup.

**Fix:** Completely restart your IDE (Cursor/VS Code) or exit and re-open your
terminal-based agent (Claude Code).

### Global vs. local conflict

If you installed with the `--global` flag, your agent might be ignoring it in
favor of project-specific rules.

**Fix:** Try installing the skill directly into your project root without the
global flag:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Resources

- [Gemini API skills on GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions)
- [Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [Libraries](https://ai.google.dev/gemini-api/docs/libraries)

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-03-05 UTC."\],\[\],\[\]\]