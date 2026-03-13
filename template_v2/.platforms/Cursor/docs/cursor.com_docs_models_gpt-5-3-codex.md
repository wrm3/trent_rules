[Skip to main content](https://cursor.com/docs/models/gpt-5-3-codex#main-content)

## Command Palette

Search for a command to run...

## Get Started

[Welcome](https://cursor.com/docs) [Quickstart](https://cursor.com/docs/get-started/quickstart)
Models & Pricing

[Overview](https://cursor.com/docs/models-and-pricing)

[Claude 4.6 Sonnet](https://cursor.com/docs/models/claude-4-6-sonnet)

[Claude 4.6 Opus](https://cursor.com/docs/models/claude-opus-4-6)

[Gemini 3.1 Pro](https://cursor.com/docs/models/gemini-3-1-pro)

[Gemini 3 Flash](https://cursor.com/docs/models/gemini-3-flash)

[GPT-5.4](https://cursor.com/docs/models/gpt-5-4)

[GPT-5.3 Codex](https://cursor.com/docs/models/gpt-5-3-codex)

[Grok Code](https://cursor.com/docs/models/grok-code)

[Composer 1.5](https://cursor.com/docs/models/cursor-composer-1-5)

## Agent

[Overview](https://cursor.com/docs/agent/overview) [Planning](https://cursor.com/docs/agent/plan-mode) [Prompting](https://cursor.com/docs/agent/prompting) [Debugging](https://cursor.com/docs/agent/debug-mode)
Tools
[Parallel Agents](https://cursor.com/docs/configuration/worktrees) [Security](https://cursor.com/docs/agent/security)

## Customizing

[Plugins](https://cursor.com/docs/plugins) [Rules](https://cursor.com/docs/rules) [Skills](https://cursor.com/docs/skills) [Subagents](https://cursor.com/docs/subagents) [Hooks](https://cursor.com/docs/hooks) [MCP](https://cursor.com/docs/mcp)

## Cloud Agents

[Overview](https://cursor.com/docs/cloud-agent) [Setup](https://cursor.com/docs/cloud-agent/setup) [Capabilities](https://cursor.com/docs/cloud-agent/capabilities) [Bugbot](https://cursor.com/docs/bugbot) [Best Practices](https://cursor.com/docs/cloud-agent/best-practices) [Security & Network](https://cursor.com/docs/cloud-agent/security-network) [Settings](https://cursor.com/docs/cloud-agent/settings) [API](https://cursor.com/docs/cloud-agent/api/endpoints)

## Integrations

[Slack](https://cursor.com/docs/integrations/slack) [Linear](https://cursor.com/docs/integrations/linear) [GitHub](https://cursor.com/docs/integrations/github) [GitLab](https://cursor.com/docs/integrations/gitlab) [JetBrains](https://cursor.com/docs/integrations/jetbrains) [Deeplinks](https://cursor.com/docs/reference/deeplinks)

## CLI

[Overview](https://cursor.com/docs/cli/overview) [Installation](https://cursor.com/docs/cli/installation) [Capabilities](https://cursor.com/docs/cli/using) [Shell Mode](https://cursor.com/docs/cli/shell-mode) [ACP](https://cursor.com/docs/cli/acp) [Headless / CI](https://cursor.com/docs/cli/headless)
Reference

## Teams & Enterprise

Teams

Enterprise

Models

![OpenAI](https://cursor.com/docs-static/images/providers/openai-dark.svg)![OpenAI](https://cursor.com/docs-static/images/providers/openai-light.svg)

# GPT-5.3 Codex

Model ID

gpt-5.3-codex

Context window

272k

Max context

-

Provider

OpenAI

Capabilities

AgentThinking

Speed

Medium

Cost

Medium

Intelligence

Frontier

GPT-5.3 Codex is OpenAI's flagship coding model. It leads Terminal-Bench by a wide margin and performs on par with Opus 4.6 on our internal benchmarks, at roughly one-third the price. Much faster than previous GPT generations. A strong default for most coding tasks.

## [Strengths](https://cursor.com/docs/models/gpt-5-3-codex\#strengths)

- Leads Terminal-Bench by a wide margin. Competitive with Opus 4.6 on our internal benchmarks.
- About one-third the price of Opus with comparable quality on most tasks. Good for daily coding, long debugging sessions, and cost-conscious teams.
- Grinds through complex, multi-step problems and deep debugging sessions.

## [Limitations](https://cursor.com/docs/models/gpt-5-3-codex\#limitations)

- Code style is less polished than Opus on architecture-heavy tasks.
- Terminal-Bench skews toward general reasoning; real-world coding gains may differ.

## [Tools](https://cursor.com/docs/models/gpt-5-3-codex\#tools)

GPT-5.3 Codex has access to all agent tools when used with Cursor including:

### Semantic search

Search your [indexed codebase](https://cursor.com/docs/context/semantic-search) by meaning, not exact matches.

### Search files and folders

Find files by name, read directory structures, and grep for patterns.

### Web

Generate search queries and fetch results from the web.

### Read files

Read file contents, including images for vision-capable models.

### Edit files

Suggest edits and apply them automatically.

### Run shell commands

Execute terminal commands and monitor output.

### Browser

Control a browser to take screenshots, test applications, and verify visual changes. See the [Browser documentation](https://cursor.com/docs/agent/browser).

### Image generation

Generate images from text descriptions or reference images.

### Ask questions

Ask clarifying questions while continuing to work in the background.

### Fetch rules

Retrieve [rules](https://cursor.com/docs/rules) based on type and description.

Learn more about [how tools work](https://cursor.com/docs/agent/overview#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling).

## [Pricing](https://cursor.com/docs/models/gpt-5-3-codex\#pricing)

Cursor [plans](https://cursor.com/docs/models-and-pricing) include two usage pools. GPT-5.3 Codex draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

| Name | Input | Cache Write | Cache Read | Output |
| --- | --- | --- | --- | --- |
| ![OpenAI](https://cursor.com/docs-static/images/providers/openai-dark.svg)![OpenAI](https://cursor.com/docs-static/images/providers/openai-light.svg)<br>[GPT-5.3 Codex](https://cursor.com/docs/models/gpt-5-3-codex) | $1.75 | - | $0.175 | $14 |

A high reasoning effort variant (`gpt-5.3-codex-high`) is available for tasks that need deeper analysis.

English

- English
- 简体中文
- 日本語
- 繁體中文
- Español
- Français
- Português
- 한국어
- Русский
- Türkçe
- Bahasa Indonesia
- Deutsch

Agent

Sonnet 4.6

Tokenizer OffContext: 0/200k (0%)

Open chat