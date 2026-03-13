[Skip to main content](https://cursor.com/docs/cloud-agent#main-content)

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

Cloud Agents

# Cloud Agents

media loading

### Network Error

A network error caused the media download to fail.



PlayPause

en0:00

en0:00

PlayPause10

Seek backward
10
10

Seek forward
10
0:00 / 0:00

MuteUnmute

Quality1x

Playback rate

Audio

Captions

start airplaystop airplay

Start castingStop casting

Enter picture in picture modeExit picture in picture mode

Enter fullscreen modeExit fullscreen mode![](https://image.mux.com/8mLzOme7z023leEyvXELSwngipHZR65vqjU6yuQPN6ok/thumbnail.webp)

Cloud agents leverage the same [agent fundamentals](https://cursor.com/learn/agents) but run in isolated environments in the cloud instead of on your local machine.

## [Why use Cloud Agents?](https://cursor.com/docs/cloud-agent\#why-use-cloud-agents)

You can run as many agents as you want in parallel, and they do not require your local machine to be connected to the internet.

Because they have access to their own virtual machine, cloud agents can build, test, and interact with the changed software. They can also use computers to control the desktop and browser. Cloud agents support [MCP servers](https://cursor.com/docs/mcp), giving them access to external tools and data sources like databases, APIs, and third-party services.

## [How to access](https://cursor.com/docs/cloud-agent\#how-to-access)

You can kick off cloud agents from wherever you work:

1. **Cursor Web**: Start and manage agents from [cursor.com/agents](https://cursor.com/agents) on any device
2. **Cursor Desktop**: Select **Cloud** in the dropdown under the agent input
3. **Slack**: Use the @cursor command to kick off an agent
4. **GitHub**: Comment `@cursor` on a PR or issue to kick off an agent
5. **Linear**: Use the @cursor command to kick off an agent
6. **API**: Use the API to kick off an agent

For a native-feeling mobile experience, install Cursor as a Progressive Web
App (PWA). On **iOS**, open [cursor.com/agents](https://cursor.com/agents) in
Safari, tap the share button, then "Add to Home Screen". On **Android**, open
the URL in Chrome, tap the menu, then "Install App".

[Use Cursor in Slack\\
\\
Learn more about setting up and using the Slack integration, including\\
triggering agents and receiving notifications.](https://cursor.com/docs/integrations/slack)

## [How it works](https://cursor.com/docs/cloud-agent\#how-it-works)

### [GitHub or GitLab connection](https://cursor.com/docs/cloud-agent\#github-or-gitlab-connection)

Cloud agents clone your repo from GitHub or GitLab and work on a separate branch, then push changes to your repo for handoff.

You need read-write privileges to your repo and any dependent repos or submodules. Support for other providers like Bitbucket is coming later.

## [Models](https://cursor.com/docs/cloud-agent\#models)

Cloud Agents use a curated selection of models that always run in [Max Mode](https://cursor.com/docs/models-and-pricing#max-mode).

There is no toggle to turn Max Mode off for Cloud Agents.

## [MCP support](https://cursor.com/docs/cloud-agent\#mcp-support)

Cloud agents can use [MCP (Model Context Protocol)](https://cursor.com/docs/mcp) servers configured for your team. Add and manage MCP servers through the MCP dropdown in [cursor.com/agents](https://cursor.com/agents).

Both HTTP and stdio transports are supported. OAuth is supported for MCP servers that need it. See [Cloud Agent capabilities](https://cursor.com/docs/cloud-agent/capabilities) for setup details.

## [Related pages](https://cursor.com/docs/cloud-agent\#related-pages)

Cloud Agents are charged at API pricing for the selected [model](https://cursor.com/docs/models-and-pricing#model-pricing). You'll be asked to set a spend limit when you first start using them.

- Learn more about [Cloud agent capabilities](https://cursor.com/docs/cloud-agent/capabilities).
- Learn more about [Cloud agent security](https://cursor.com/docs/cloud-agent/security-network).
- Learn more about [Cloud agent settings](https://cursor.com/docs/cloud-agent/settings).

## [Troubleshooting](https://cursor.com/docs/cloud-agent\#troubleshooting)

### Agent runs are not starting

- Ensure you're logged in and have connected your GitHub or GitLab account.
- Check that you have the necessary repository permissions.
- You need to be on a trial or paid plan with usage-based pricing enabled.
- To enable usage-based pricing, go to your [Dashboard](https://www.cursor.com/dashboard?tab=settings) settings tab.

### My secrets aren't available to the cloud agent

- Ensure you've added secrets in [cursor.com/dashboard?tab=cloud-agents](https://cursor.com/dashboard?tab=cloud-agents)
- Secrets are workspace/team-scoped; make sure you're using the correct account
- Try restarting the cloud agent after adding new secrets

### Can't find the Secrets tab

- If you don't see it, ensure you have the necessary permissions

### Do snapshots copy .env.local files?

Snapshots save your base environment configuration (installed packages, system dependencies, etc.).
If you include `.env.local` files during snapshot creation, they will be saved. However, using the Secrets tab
in Cursor Settings is the recommended approach for managing environment variables.

### Slack integration not working

Verify that your workspace admin has installed the Cursor Slack app and that
you have the proper permissions.

## [Naming History](https://cursor.com/docs/cloud-agent\#naming-history)

Cloud Agents were formerly called Background Agents.

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