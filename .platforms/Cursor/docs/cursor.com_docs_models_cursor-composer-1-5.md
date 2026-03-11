[Skip to main content](https://cursor.com/docs/models/cursor-composer-1-5#main-content)

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

![Cursor](https://cursor.com/docs-static/images/providers/cursor.svg)

# Composer 1.5

Model ID

composer-1.5

Context window

200k

Max context

-

Provider

Cursor

Capabilities

AgentThinking

Speed

Fast

Cost

Medium

Intelligence

High

Composer 1.5 is Cursor's own agentic model. It's tuned for the rapid back-and-forth of interactive coding and sits between Sonnet 4.5 and Opus 4.5 in intelligence. On individual plans, Composer draws from the Auto usage pool, so the effective per-token cost is lower than the listed API price.

## [Strengths](https://cursor.com/docs/models/cursor-composer-1-5\#strengths)

- Faster than Opus and other thinking models. Tuned for interactive agent sessions and everyday coding.
- Draws from the Auto usage pool on individual plans, resulting in more usage.
- Supports reasoning tokens for complex tasks while staying fast.
- Behavior tuned for tool use, file edits, and terminal operations inside Cursor. Strong for subagent tasks where speed matters.

## [Limitations](https://cursor.com/docs/models/cursor-composer-1-5\#limitations)

- Weaker than frontier models on complex configuration, documentation, and zero-to-one builds.
- Not as suitable for longer horizon tasks running for many hours or days.

## [Tools](https://cursor.com/docs/models/cursor-composer-1-5\#tools)

Composer 1.5 has access to all agent tools when used with Cursor including:

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

## [Pricing](https://cursor.com/docs/models/cursor-composer-1-5\#pricing)

On individual plans, Composer 1.5 draws from the **Auto + Composer** usage pool, which includes significantly more usage than the API pool. Your effective per-token cost is lower than the listed price below.

On team and enterprise plans, the API price below is charged directly. All prices are per million tokens.

| Name | Input | Cache Write | Cache Read | Output |
| --- | --- | --- | --- | --- |
| ![Cursor](https://cursor.com/docs-static/images/providers/cursor.svg)<br>[Composer 1.5](https://cursor.com/docs/models/cursor-composer-1-5) | $3.5 | - | $0.35 | $17.5 |

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