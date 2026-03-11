## Search the Codex docs

Close

Clear

Primary navigation

Clear

### Getting Started

- [Overview](https://developers.openai.com/codex)
- [Quickstart](https://developers.openai.com/codex/quickstart)
- [Explore](https://developers.openai.com/codex/explore)
- [Pricing](https://developers.openai.com/codex/pricing)
- Concepts

  - [Prompting](https://developers.openai.com/codex/prompting)
  - [Customization](https://developers.openai.com/codex/concepts/customization)
  - [Sandboxing](https://developers.openai.com/codex/concepts/sandboxing)
  - [Multi-agents](https://developers.openai.com/codex/concepts/multi-agents)
  - [Workflows](https://developers.openai.com/codex/workflows)
  - [Models](https://developers.openai.com/codex/models)
  - [Cyber Safety](https://developers.openai.com/codex/concepts/cyber-safety)

### Using Codex

- App

  - [Overview](https://developers.openai.com/codex/app)
  - [Features](https://developers.openai.com/codex/app/features)
  - [Settings](https://developers.openai.com/codex/app/settings)
  - [Review](https://developers.openai.com/codex/app/review)
  - [Automations](https://developers.openai.com/codex/app/automations)
  - [Worktrees](https://developers.openai.com/codex/app/worktrees)
  - [Local Environments](https://developers.openai.com/codex/app/local-environments)
  - [Commands](https://developers.openai.com/codex/app/commands)
  - [Windows](https://developers.openai.com/codex/app/windows)
  - [Troubleshooting](https://developers.openai.com/codex/app/troubleshooting)

- IDE Extension

  - [Overview](https://developers.openai.com/codex/ide)
  - [Features](https://developers.openai.com/codex/ide/features)
  - [Settings](https://developers.openai.com/codex/ide/settings)
  - [IDE Commands](https://developers.openai.com/codex/ide/commands)
  - [Slash commands](https://developers.openai.com/codex/ide/slash-commands)

- CLI

  - [Overview](https://developers.openai.com/codex/cli)
  - [Features](https://developers.openai.com/codex/cli/features)
  - [Command Line Options](https://developers.openai.com/codex/cli/reference)
  - [Slash commands](https://developers.openai.com/codex/cli/slash-commands)

- Web

  - [Overview](https://developers.openai.com/codex/cloud)
  - [Environments](https://developers.openai.com/codex/cloud/environments)
  - [Internet Access](https://developers.openai.com/codex/cloud/internet-access)

- Integrations

  - [GitHub](https://developers.openai.com/codex/integrations/github)
  - [Slack](https://developers.openai.com/codex/integrations/slack)
  - [Linear](https://developers.openai.com/codex/integrations/linear)

- Codex Security

  - [Overview](https://developers.openai.com/codex/security)
  - [Setup](https://developers.openai.com/codex/security/setup)
  - [Improving the threat model](https://developers.openai.com/codex/security/threat-model)
  - [FAQ](https://developers.openai.com/codex/security/faq)

### Configuration

- Config File

  - [Config Basics](https://developers.openai.com/codex/config-basic)
  - [Advanced Config](https://developers.openai.com/codex/config-advanced)
  - [Config Reference](https://developers.openai.com/codex/config-reference)
  - [Sample Config](https://developers.openai.com/codex/config-sample)

- [Speed](https://developers.openai.com/codex/speed)
- [Rules](https://developers.openai.com/codex/rules)
- [AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [MCP](https://developers.openai.com/codex/mcp)
- [Skills](https://developers.openai.com/codex/skills)
- [Multi-agents](https://developers.openai.com/codex/multi-agent)

### Administration

- [Authentication](https://developers.openai.com/codex/auth)
- [Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security)
- Enterprise

  - [Admin Setup](https://developers.openai.com/codex/enterprise/admin-setup)
  - [Governance](https://developers.openai.com/codex/enterprise/governance)
  - [Managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration)

- [Windows](https://developers.openai.com/codex/windows)

### Automation

- [Non-interactive Mode](https://developers.openai.com/codex/noninteractive)
- [Codex SDK](https://developers.openai.com/codex/sdk)
- [App Server](https://developers.openai.com/codex/app-server)
- [MCP Server](https://developers.openai.com/codex/guides/agents-sdk)
- [GitHub Action](https://developers.openai.com/codex/github-action)

### Learn

- [Videos](https://developers.openai.com/codex/videos)
- Blog

  - [Building frontend UIs with Codex and Figma](https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma)
  - [Run long horizon tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
  - [View all](https://developers.openai.com/blog/topic/codex)

- Cookbooks

  - [Codex Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)
  - [Modernizing your Codebase with Codex](https://developers.openai.com/cookbook/examples/codex/code_modernization)
  - [View all](https://developers.openai.com/cookbook/topic/codex)

- [Building AI Teams](https://developers.openai.com/codex/guides/build-ai-native-engineering-team)

### Community

- [Ambassadors](https://developers.openai.com/codex/ambassadors)
- [Open Source Program](https://developers.openai.com/codex/community/codex-for-oss)
- [Meetups](https://developers.openai.com/codex/community/meetups)

### Releases

- [Changelog](https://developers.openai.com/codex/changelog)
- [Feature Maturity](https://developers.openai.com/codex/feature-maturity)
- [Open Source](https://developers.openai.com/codex/open-source)

[API Dashboard](https://platform.openai.com/login)

Search
⌘

K

Copy PageMore page actions

Copy PageMore page actions

Use these settings to customize the Codex IDE extension.

## Change a setting

To change a setting, follow these steps:

1. Open your editor settings.
2. Search for `Codex` or the setting name.
3. Update the value.

The Codex IDE extension uses the Codex CLI. Configure some behavior, such as the default model, approvals, and sandbox settings, in the shared `~/.codex/config.toml` file instead of in editor settings. See [Config basics](https://developers.openai.com/codex/config-basic).

## Settings reference

| Setting | Description |
| --- | --- |
| `chatgpt.cliExecutable` | Development only: Path to the Codex CLI executable. You don’t need to set this unless you’re actively developing the Codex CLI. If you set this manually, parts of the extension might not work as expected. |
| `chatgpt.commentCodeLensEnabled` | Show CodeLens above to-do comments so you can complete them with Codex. |
| `chatgpt.localeOverride` | Preferred language for the Codex UI. Leave empty to detect automatically. |
| `chatgpt.openOnStartup` | Focus the Codex sidebar when the extension finishes starting. |
| `chatgpt.runCodexInWindowsSubsystemForLinux` | Windows only: Run Codex in WSL when Windows Subsystem for Linux (WSL) is available. Recommended for improved sandbox security and better performance. Codex agent mode on Windows currently requires WSL. Changing this setting reloads VS Code to apply the change. |