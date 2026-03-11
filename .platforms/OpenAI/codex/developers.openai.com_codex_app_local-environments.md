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

  - [Using skills to accelerate OSS maintenance](https://developers.openai.com/blog/skills-agents-sdk)
  - [Building frontend UIs with Codex and Figma](https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma)
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

Local environments let you configure setup steps for worktrees as well as common actions for a project.

You configure your local environments through the [Codex app settings](codex://settings) pane. You can check the generated file into your project’s Git repository to share with others.

Codex stores this configuration inside the `.codex` folder at the root of your
project. If your repository contains more than one project, open the project
directory that contains the shared `.codex` folder.

## Setup scripts

Since worktrees run in different directories than your local tasks, your project might not be fully set up and might be missing dependencies or files that aren’t checked into your repository. Setup scripts run automatically when Codex creates a new worktree at the start of a new thread.

Use this script to run any command required to configure your environment, such as installing dependencies or running a build process.

For example, for a TypeScript project you might want to install the dependencies and do an initial build using a setup script:

```
npm install
npm run build


```

If your setup is platform-specific, define setup scripts for macOS, Windows, or Linux to override the default.

## Actions

Use actions to define common tasks like starting your app’s development server or running your test suite. These actions appear in the Codex app top bar for quick access. The actions will be run within the app’s [integrated terminal](https://developers.openai.com/codex/app/features#integrated-terminal).

Actions are helpful to keep you from typing common actions like triggering a build for your project or starting a development server. For one-off quick debugging you can use the integrated terminal directly.

![Project actions list shown in Codex app settings](https://developers.openai.com/images/codex/app/actions-light.webp)![Project actions list shown in Codex app settings](https://developers.openai.com/images/codex/app/actions-dark.webp)

![Project actions list shown in Codex app settings](https://developers.openai.com/images/codex/app/actions-light.webp)![Project actions list shown in Codex app settings](https://developers.openai.com/images/codex/app/actions-dark.webp)

For example, for a Node.js project you might create a “Run” action that contains the following script:

```
npm start


```

If the commands for your action are platform-specific, define platform-specific scripts for macOS, Windows, and Linux.

To identify your actions, choose an icon associated with each action.