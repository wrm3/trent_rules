[Skip to main content](https://cursor.com/docs/skills#main-content)

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

# Agent Skills

Agent Skills is an open standard for extending AI agents with specialized capabilities. Skills package domain-specific knowledge and workflows that agents can use to perform specific tasks.

## [What are skills?](https://cursor.com/docs/skills\#what-are-skills)

A skill is a portable, version-controlled package that teaches agents how to perform domain-specific tasks. Skills can include scripts, templates, and references that agents may act on using their tools.

Portable

Skills work across any agent that supports the Agent Skills standard.

Version-controlled

Skills are stored as files and can be tracked in your repository, or installed via GitHub repository links.

Actionable

Skills can include scripts, templates, and references that agents act on using their tools.

Progressive

Skills load resources on demand, keeping context usage efficient.

## [How skills work](https://cursor.com/docs/skills\#how-skills-work)

When Cursor starts, it automatically discovers skills from skill directories and makes them available to Agent. The agent is presented with available skills and decides when they are relevant based on context.

Skills can also be manually invoked by typing `/` in Agent chat and searching for the skill name.

## [Skill directories](https://cursor.com/docs/skills\#skill-directories)

Skills are automatically loaded from these locations:

| Location | Scope |
| --- | --- |
| `.agents/skills/` | Project-level |
| `.cursor/skills/` | Project-level |
| `~/.cursor/skills/` | User-level (global) |

For compatibility, Cursor also loads skills from Claude and Codex directories: `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, and `~/.codex/skills/`.

Each skill should be a folder containing a `SKILL.md` file:

```
.agents/
└── skills/
    └── my-skill/
        └── SKILL.md
```

Skills can also include optional directories for scripts, references, and assets:

```
.agents/
└── skills/
    └── deploy-app/
        ├── SKILL.md
        ├── scripts/
        │   ├── deploy.sh
        │   └── validate.py
        ├── references/
        │   └── REFERENCE.md
        └── assets/
            └── config-template.json
```

## [SKILL.md file format](https://cursor.com/docs/skills\#skillmd-file-format)

Each skill is defined in a `SKILL.md` file with YAML frontmatter:

```
---
name: my-skill
description: Short description of what this skill does and when to use it.
---

# My Skill

Detailed instructions for the agent.

## When to Use

- Use this skill when...
- This skill is helpful for...

## Instructions

- Step-by-step guidance for the agent
- Domain-specific conventions
- Best practices and patterns
- Use the ask questions tool if you need to clarify requirements with the user
```

### [Frontmatter fields](https://cursor.com/docs/skills\#frontmatter-fields)

| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Skill identifier. Lowercase letters, numbers, and hyphens only. Must match the parent folder name. |
| `description` | Yes | Describes what the skill does and when to use it. Used by the agent to determine relevance. |
| `license` | No | License name or reference to a bundled license file. |
| `compatibility` | No | Environment requirements (system packages, network access, etc.). |
| `metadata` | No | Arbitrary key-value mapping for additional metadata. |
| `disable-model-invocation` | No | When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context. |

## [Disabling automatic invocation](https://cursor.com/docs/skills\#disabling-automatic-invocation)

By default, skills are automatically applied when the agent determines they are relevant. Set `disable-model-invocation: true` to make a skill behave like a traditional slash command, where it is only included in context when you explicitly type `/skill-name` in chat.

## [Including scripts in skills](https://cursor.com/docs/skills\#including-scripts-in-skills)

Skills can include a `scripts/` directory containing executable code that agents can run. Reference scripts in your `SKILL.md` using relative paths from the skill root.

```
---
name: deploy-app
description: Deploy the application to staging or production environments. Use when deploying code or when the user mentions deployment, releases, or environments.
---

# Deploy App

Deploy the application using the provided scripts.

## Usage

Run the deployment script: `scripts/deploy.sh <environment>`

Where `<environment>` is either `staging` or `production`.

## Pre-deployment Validation

Before deploying, run the validation script: `python scripts/validate.py`
```

The agent reads these instructions and executes the referenced scripts when the skill is invoked. Scripts can be written in any language—Bash, Python, JavaScript, or any other executable format supported by the agent implementation.

Scripts should be self-contained, include helpful error messages, and handle edge cases gracefully.

## [Optional directories](https://cursor.com/docs/skills\#optional-directories)

Skills support these optional directories:

| Directory | Purpose |
| --- | --- |
| `scripts/` | Executable code that agents can run |
| `references/` | Additional documentation loaded on demand |
| `assets/` | Static resources like templates, images, or data files |

Keep your main `SKILL.md` focused and move detailed reference material to separate files. This keeps context usage efficient since agents load resources progressively—only when needed.

## [Viewing skills](https://cursor.com/docs/skills\#viewing-skills)

To view discovered skills:

1. Open **Cursor Settings** (Cmd+Shift+J on Mac, Ctrl+Shift+J on Windows/Linux)
2. Navigate to **Rules**
3. Skills appear in the **Agent Decides** section

## [Installing skills from GitHub](https://cursor.com/docs/skills\#installing-skills-from-github)

You can import skills from GitHub repositories:

1. Open **Cursor Settings → Rules**
2. In the **Project Rules** section, click **Add Rule**
3. Select **Remote Rule (Github)**
4. Enter the GitHub repository URL

## [Migrating rules and commands to skills](https://cursor.com/docs/skills\#migrating-rules-and-commands-to-skills)

Cursor includes a built-in `/migrate-to-skills` skill in 2.4 that helps you convert existing dynamic rules and slash commands to skills.

The migration skill converts:

- **Dynamic rules**: Rules that use the "Apply Intelligently" configuration—rules with `alwaysApply: false` (or undefined) and no `globs` patterns defined. These are converted to standard skills.
- **Slash commands**: Both user-level and workspace-level commands are converted to skills with `disable-model-invocation: true`, preserving their explicit invocation behavior.

To migrate:

1. Type `/migrate-to-skills` in Agent chat
2. The agent will identify eligible rules and commands and convert them to skills
3. Review the generated skills in `.cursor/skills/`

Rules with `alwaysApply: true` or specific `globs` patterns are not migrated, as they have explicit triggering conditions that differ from skill behavior. User rules are also not migrated since they are not stored on the file system.

## [Learn more](https://cursor.com/docs/skills\#learn-more)

Agent Skills is an open standard. Learn more at [agentskills.io](https://agentskills.io/).

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