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

## Prompts

You interact with Codex by sending prompts (user messages) that describe what you want it to do.

Example prompts:

```
Explain how the transform module works and how other modules use it.


```

```
Add a new command-line option `--json` that outputs JSON.


```

When you submit a prompt, Codex works in a loop: it calls the model and then performs any actions (file reads, file edits, tool calls, and so on) indicated by the model output. This process ends when the task is complete or you cancel it.

As with ChatGPT, Codex is only as effective as the instructions you give it. Here are some tips we find helpful when prompting Codex:

- Codex produces higher-quality outputs when it can verify its work. Include steps to reproduce an issue, validate a feature, and run linting and pre-commit checks.
- Codex handles complex work better when you break it into smaller, focused steps. Smaller tasks are easier for Codex to test and for you to review. If you’re not sure how to split a task up, ask Codex to propose a plan.

For more ideas about prompting Codex, refer to [workflows](https://developers.openai.com/codex/workflows).

## Threads

A thread is a single session: your prompt plus the model outputs and tool calls that follow. A thread can include multiple prompts. For example, your first prompt might ask Codex to implement a feature, and a follow-up prompt might ask it to add tests.

A thread is said to be “running” when Codex is actively working on it. You can run multiple threads at once, but avoid having two threads modify the same files. You can also resume a thread later by continuing it with another prompt.

Threads can run either locally or in the cloud:

- **Local threads** run on your machine. Codex can read and edit your files and run commands, so you can see what changes and use your existing tools. To reduce the risk of unwanted changes outside your workspace, local threads run in a [sandbox](https://developers.openai.com/codex/agent-approvals-security).
- **Cloud threads** run in an isolated [environment](https://developers.openai.com/codex/cloud/environments). Codex clones your repository and checks out the branch it’s working on. Cloud threads are useful when you want to run work in parallel or delegate tasks from another device. To use cloud threads with your repo, push your code to GitHub first. You can also [delegate tasks from your local machine](https://developers.openai.com/codex/ide/cloud-tasks), which includes your current working state.

## Context

When you submit a prompt, include context that Codex can use, such as references to relevant files and images. The Codex IDE extension automatically includes the list of open files and the selected text range as context.

As the agent works, it also gathers context from file contents, tool output, and an ongoing record of what it has done and what it still needs to do.

All information in a thread must fit within the model’s **context window**, which varies by model. Codex monitors and reports the remaining space. For longer tasks, Codex may automatically **compact** the context by summarizing relevant information and discarding less relevant details. With repeated compaction, Codex can continue working on complex tasks over many steps.