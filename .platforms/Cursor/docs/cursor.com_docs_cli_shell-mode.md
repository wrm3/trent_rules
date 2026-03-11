[Skip to main content](https://cursor.com/docs/cli/shell-mode#main-content)

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

CLI

# Shell Mode

Shell Mode runs shell commands directly from the CLI without leaving your conversation. Use it for quick, non-interactive commands with safety checks and output displayed in the conversation.

## [Command execution](https://cursor.com/docs/cli/shell-mode\#command-execution)

Commands run in your login shell (`$SHELL`) with the CLI's working directory and environment. Chain commands to run in other directories:

```
cd subdir && npm test
```

## [Output](https://cursor.com/docs/cli/shell-mode\#output)

Large outputs are truncated automatically and long-running processes timeout to maintain performance.

## [Limitations](https://cursor.com/docs/cli/shell-mode\#limitations)

- Commands timeout after 30 seconds
- Long-running processes, servers, and interactive prompts are not supported
- Use short, non-interactive commands for best results

## [Permissions](https://cursor.com/docs/cli/shell-mode\#permissions)

Commands are checked against your permissions and team settings before execution. See [Permissions](https://cursor.com/docs/cli/reference/permissions) for detailed configuration.

Admin policies may block certain commands, and commands with redirection cannot be allowlisted inline.

## [Usage guidelines](https://cursor.com/docs/cli/shell-mode\#usage-guidelines)

Shell Mode works well for status checks, quick builds, file operations, and environment inspection.

Avoid long-running servers, interactive applications, and commands requiring input.

Each command runs independently - use `cd <dir> && ...` to run commands in other directories.

## [Troubleshooting](https://cursor.com/docs/cli/shell-mode\#troubleshooting)

- If a command hangs, cancel with `Ctrl+C` and add non-interactive flags
- When prompted for permissions, approve once or add to allowlist with `Tab`
- For truncated output, use `Ctrl+O` to expand
- To run in different directories, use `cd <dir> && ...` since changes don't persist
- Shell Mode supports zsh and bash from your `$SHELL` variable

## [FAQ](https://cursor.com/docs/cli/shell-mode\#faq)

### Does \`cd\` persist across runs?

No. Each command runs independently. Use `cd <dir> && ...` to run commands in different directories.

### Can I change the timeout?

No. Commands are limited to 30 seconds and this is not configurable.

### Where are permissions configured?

Permissions are managed by CLI and team configuration. Use the decision banner to add commands to allowlists.

### How do I exit Shell Mode?

Press `EscapeEsc` when the input is empty, `Backspace`/ `Delete` on empty input, or `Ctrl+C` to clear and exit.

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