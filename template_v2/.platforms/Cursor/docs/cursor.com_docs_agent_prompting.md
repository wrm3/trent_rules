[Skip to main content](https://cursor.com/docs/agent/prompting#main-content)

## Command Palette

Search for a command to run...

## Get Started

[Welcome](https://cursor.com/docs) [Quickstart](https://cursor.com/docs/get-started/quickstart)
Models & Pricing

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

Agent

# Prompting agents

Direct Agent with text prompts in the chat input. You can attach context, images, and voice, and switch models at any point.

## [@ mentions](https://cursor.com/docs/agent/prompting\#mentions)

Type `@` in the chat input to attach specific context to your prompt. Start typing after `@` and Cursor shows matching suggestions.

- **Files**: `@auth.ts` to include a specific file
- **Folders**: `@src/components/` to include an entire folder (type `/` after selecting to navigate deeper)
- **Code symbols**: `@getUserById` to reference a specific function, class, or variable
- **Documentation**: `@Docs` to search indexed documentation, including your own (add via `@Docs > Add new doc`)
- **Past chats**: `@Past Chats` to reference context from a previous conversation

Use @ mentions when you know which files are relevant. If you're not sure which files matter, skip it. Agent finds relevant files through its own search.

Cursor 2.0 removed explicit items like `@Web`, `@Git`, `@Definitions`, `@Linter Errors`, and others from the context menu. Agent now self-gathers this context without manual attachment. For example, ask Agent to review changes on your branch instead of using `@Git`.

## [Image input](https://cursor.com/docs/agent/prompting\#image-input)

Attach images to your prompt to provide visual context for UI work, debugging, and design implementation.

- **Drag and drop** an image file into the chat input
- **Paste from clipboard** with `Cmd+VCtrl+V`, including screenshots

This is useful for implementing design mockups, debugging visual issues, and referencing error messages or stack traces without manual transcription.

## [Voice input](https://cursor.com/docs/agent/prompting\#voice-input)

Click the microphone icon in the chat input to dictate your prompt instead of typing. Speak naturally, include technical details like file and function names, and review the transcription before sending.

## [Changing models](https://cursor.com/docs/agent/prompting\#changing-models)

Use the model picker dropdown at the top of the chat input to switch models, or press `Cmd /Ctrl /` to cycle through models. The change applies to the current conversation going forward. Set a default model in **Cursor Settings > Models**.

- **Faster models** work well for quick edits and routine tasks
- **More capable models** are better for complex reasoning and multi-file refactoring

You can switch models mid-conversation, for example when a faster model handled exploration but you need deeper reasoning for implementation. See [Models & Pricing](https://cursor.com/docs/models-and-pricing) for the full list.

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