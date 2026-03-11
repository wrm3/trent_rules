[Skip to main content](https://cursor.com/docs/plugins#main-content)

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

Customizing

# Plugins

Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundles. They work in the Cursor IDE. Browse community-built plugins or [build your own](https://cursor.com/docs/plugins#creating-plugins) to share with other developers.

Cursor CLI does not support plugins yet. Only MCP servers from plugins are supported in Cloud Agents.

## [What plugins contain](https://cursor.com/docs/plugins\#what-plugins-contain)

A plugin can bundle any combination of these components:

| Component | Description |
| --- | --- |
| **Rules** | Persistent AI guidance and coding standards (`.mdc` files) |
| **Skills** | Specialized agent capabilities for complex tasks |
| **Agents** | Custom agent configurations and prompts |
| **Commands** | Agent-executable command files |
| **MCP Servers** | Model Context Protocol integrations |
| **Hooks** | Automation scripts triggered by events |

## [The marketplace](https://cursor.com/docs/plugins\#the-marketplace)

The [Cursor Marketplace](https://cursor.com/marketplace) is where you discover and install plugins. Plugins are distributed as Git repositories and submitted through the Cursor team. Every plugin is [manually reviewed](https://cursor.com/help/security-and-privacy/marketplace-security) before it's listed. Browse available plugins at [cursor.com/marketplace](https://cursor.com/marketplace) or search by keyword in the marketplace panel.

## [Team marketplaces](https://cursor.com/docs/plugins\#team-marketplaces)

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

Enter fullscreen modeExit fullscreen mode![](https://image.mux.com/CdVMfFAlX7IT9jlLWEy011I1200TBeR9Ip3JN01xujhjmI/thumbnail.webp)

Team marketplaces are available on Teams and Enterprise plans.

- Teams plan: up to 1 team marketplace
- Enterprise plan: unlimited team marketplaces

On eligible accounts, the **Team Marketplaces** section appears below **Plugins** in dashboard settings. If you do not see it yet, rollout may still be in progress for your account.

On Enterprise plans, only admins can add team marketplaces from **Dashboard ->**
**Settings -> Plugins**.

### [Required vs optional plugins](https://cursor.com/docs/plugins\#required-vs-optional-plugins)

When you assign a plugin to a distribution group, you can set it as required or optional:

- **Required**: After you click **Save**, the plugin is installed automatically for everyone in that distribution group.
- **Optional**: The plugin is available to everyone in that distribution group, and each developer can choose whether to install it.

### [How do distribution groups work with SCIM?](https://cursor.com/docs/plugins\#how-do-distribution-groups-work-with-scim)

Distribution groups can be controlled with [SCIM](https://cursor.com/docs/account/teams/scim)-synced directory groups. If your organization uses SCIM, manage group membership in your identity provider, and Cursor will sync those group updates.

## [Add a team marketplace](https://cursor.com/docs/plugins\#add-a-team-marketplace)

Use this flow to import a GitHub repository as a team marketplace:

1. Go to **Dashboard -> Settings -> Plugins**.
2. In **Team Marketplaces**, click **Import**.
3. Paste the GitHub repository URL and continue.
4. Review the parsed plugins. Optionally set Team Access groups, then continue.
5. Set the marketplace name and description, then save.

Example repository to try:

- [fieldsphere/cursor-team-marketplace-template](https://github.com/fieldsphere/cursor-team-marketplace-template)

## [Where developers find team marketplaces](https://cursor.com/docs/plugins\#where-developers-find-team-marketplaces)

Developers can find team marketplaces in the marketplace panel in Cursor.

- Open the marketplace panel in Cursor.
- Look for plugins from your team marketplace.
- Install optional plugins directly from that panel.
- Required plugins are installed automatically when admins save the required setting for your distribution group.

## [Installing plugins](https://cursor.com/docs/plugins\#installing-plugins)

Install plugins from the marketplace. Plugins can be scoped to a project or installed at the user level.

### [MCP Apps deeplinks](https://cursor.com/docs/plugins\#mcp-apps-deeplinks)

Share MCP server configurations using install links:

```
cursor://anysphere.cursor-deeplink/mcp/install?name=$NAME&config=$BASE64_ENCODED_CONFIG
```

See [MCP install links](https://cursor.com/docs/mcp/install-links) for details on generating these links.

## [Managing installed plugins](https://cursor.com/docs/plugins\#managing-installed-plugins)

### [MCP servers](https://cursor.com/docs/plugins\#mcp-servers)

Toggle MCP servers on or off from Cursor Settings:

1. Open Settings ( `Cmd+Shift+JCtrl+Shift+J`)
2. Go to **Features** \> **Model Context Protocol**
3. Click the toggle next to any server

Disabled servers won't load or appear in chat.

### [Rules and skills](https://cursor.com/docs/plugins\#rules-and-skills)

Manage rules and skills from the Rules section of Cursor Settings. Toggle individual rules between **Always**, **Agent Decides**, and **Manual** modes. Skills appear in the **Agent Decides** section and can be invoked manually with `/skill-name` in chat.

## [Creating plugins](https://cursor.com/docs/plugins\#creating-plugins)

A plugin is a directory with a `.cursor-plugin/plugin.json` manifest and your components (rules, skills, agents, commands, hooks, or MCP servers). Start from the [plugin template repository](https://github.com/cursor/plugin-template) or create one from scratch:

```
my-plugin/
├── .cursor-plugin/
│   └── plugin.json
├── rules/
│   └── coding-standards.mdc
├── skills/
│   └── code-reviewer/
│       └── SKILL.md
└── .mcp.json
```

The manifest only requires a `name` field. Components are discovered automatically from their default directories, or you can specify custom paths in the manifest.

```
{
  "name": "my-plugin",
  "description": "Custom development tools",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

When your plugin is ready, submit it for review at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish). For multi-plugin repositories, add a marketplace manifest at `.cursor-plugin/marketplace.json`.

See the [Plugins reference](https://cursor.com/docs/reference/plugins) for the full manifest schema, component formats, and submission checklist.

## [FAQ](https://cursor.com/docs/plugins\#faq)

### Are marketplace plugins reviewed for security?

Yes. Every plugin is manually reviewed before it's listed. All plugins must be open source, and we review each update before publishing. See [Marketplace security](https://cursor.com/help/security-and-privacy/marketplace-security) for details on vetting, update reviews, and how to report issues.

### How do I create a plugin?

Create a directory with a `.cursor-plugin/plugin.json` manifest file, add your rules, skills, agents, commands, or other components, and submit it to the Cursor team. See the [Plugins reference](https://cursor.com/docs/reference/plugins) for the full guide.

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