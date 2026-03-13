[Skip to main content](https://cursor.com/docs/configuration/worktrees#main-content)

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

# Parallel Agents

This feature allows you to run multiple agents locally in parallel, or run a single prompt across multiple models at once.

Parallel agents run in their own worktree, allowing them to make edits, or build and test code without interfering with each other.

A worktree is a Git feature that lets you use multiple branches of one repository at once.
Each worktree has its own set of files and changes.

Cursor automatically creates and configures worktrees for you, and we currently have a 1:1 mapping of agents to worktrees. You can also add custom instructions to [configure the worktree setup](https://cursor.com/docs/configuration/worktrees#initialization-script), like installing dependencies or applying database migrations.

## [Basic Worktree usage](https://cursor.com/docs/configuration/worktrees\#basic-worktree-usage)

The most basic way to use worktrees in Cursor is to run a single agent in a worktree.

![Basic worktree usage](https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fworktrees%2Fworktree-dropdown.png&w=1920&q=75&dpl=dpl_7zPiZUsTD7ownHrxp4Gk37N86tFn)

When the agent run is complete, click the "Apply" button to apply the agent's changes to your local branch. This is different from the "Keep" button in local agents.

If you'd like to see all worktrees in your git repository, you can run the command `git worktree list` in your terminal. The output will look like this:

```
/.../<repo>                                  15ae12e   [main]
/Users/<you>/.cursor/worktrees/<repo>/98Zlw  15ae12e   [feat-1-98Zlw]
/Users/<you>/.cursor/worktrees/<repo>/a4Xiu  15ae12e   [feat-2-a4Xiu]
```

# Best-of-N - Use multiple models at once

A powerful feature of worktrees is the ability to run a single prompt on multiple models at once.

![Basic best-of-N usage](https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fworktrees%2Fworktree-bon.png&w=1920&q=75&dpl=dpl_7zPiZUsTD7ownHrxp4Gk37N86tFn)

Once you submit a prompt, you will see two cards, one for each model. Click across the cards to see the changes made by each Agent.

![Best-of-N cards](https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fworktrees%2Fworktree-bon-cards.png&w=1920&q=75&dpl=dpl_7zPiZUsTD7ownHrxp4Gk37N86tFn)

Then, click the "Apply" button to apply the changes to your checked out branch.

### [When to use multiple models](https://cursor.com/docs/configuration/worktrees\#when-to-use-multiple-models)

Running the same prompt across multiple models is especially useful for:

- **Hard problems** where different models might take different approaches
- **Comparing code quality** across model families to find the best solution
- **Finding edge cases** one model might miss that another catches
- **Benchmarking** which models work best for your specific codebase

Having multiple models attempt the same problem and picking the best result significantly improves the final output, especially for harder tasks.

Configure notifications and sounds in Cursor settings so you know when parallel agents finish their work.

## ["Apply" Functionality](https://cursor.com/docs/configuration/worktrees\#apply-functionality)

When you run a parallel agent, you will see a "Apply" button. Clicking this button will apply the changes to your checked out branch. The way this process works is the following:

1. When Cursor creates a worktree, all new files and edited files in your primary working tree are brought along to the worktree (the only exception is files that are ignored by Git).
2. The agent will perform its work in isolation inside this worktree, and potentially make edits to files.
3. When you click "Apply", we try to cleanly merge those changes in to your primary working tree.

If you're applying multiple times inside the same Best-of-N run, Cursor will ask you how you'd like to proceed:

- You have the option to "Full Overwrite" (replace the full contents of every file with the changes from the agent in the worktree)
- Try to "merge" between multiple options using the native conflict resolution UI

## [Initialization Script](https://cursor.com/docs/configuration/worktrees\#initialization-script)

You can customize the worktree setup by editing the `.cursor/worktrees.json` file. Cursor finds this file in the following order:

1. In the worktree path
2. In the root path of your project

### [Configuration options](https://cursor.com/docs/configuration/worktrees\#configuration-options)

The `worktrees.json` file supports three configuration keys:

- **`setup-worktree-unix`**: Commands or script path for macOS/Linux. Takes precedence over `setup-worktree` on Unix systems.
- **`setup-worktree-windows`**: Commands or script path for Windows. Takes precedence over `setup-worktree` on Windows.
- **`setup-worktree`**: Generic fallback for all operating systems.

Each key accepts either:

- **An array of shell commands** \- executed sequentially in the worktree
- **A string filepath** \- path to a script file relative to `.cursor/worktrees.json`

## [Example setup configurations](https://cursor.com/docs/configuration/worktrees\#example-setup-configurations)

### [Using command arrays](https://cursor.com/docs/configuration/worktrees\#using-command-arrays)

#### [Node.js project](https://cursor.com/docs/configuration/worktrees\#nodejs-project)

```
{
  "setup-worktree": [\
    "npm ci",\
    "cp $ROOT_WORKTREE_PATH/.env .env"\
  ]
}
```

We do not recommend symlinking dependencies into the worktree, as this can cause issues in the
main worktree. Instead, we recommend using fast package managers such as `bun`, `pnpm` or `uv`
in the Python ecosystem to install dependencies.

#### [Python project with virtual environment](https://cursor.com/docs/configuration/worktrees\#python-project-with-virtual-environment)

```
{
  "setup-worktree": [\
    "python -m venv venv",\
    "source venv/bin/activate && pip install -r requirements.txt",\
    "cp $ROOT_WORKTREE_PATH/.env .env"\
  ]
}
```

#### [Project with database migrations](https://cursor.com/docs/configuration/worktrees\#project-with-database-migrations)

```
{
  "setup-worktree": [\
    "npm ci",\
    "cp $ROOT_WORKTREE_PATH/.env .env",\
    "npm run db:migrate"\
  ]
}
```

#### [Build and link dependencies](https://cursor.com/docs/configuration/worktrees\#build-and-link-dependencies)

```
{
  "setup-worktree": [\
    "pnpm install",\
    "pnpm run build",\
    "cp $ROOT_WORKTREE_PATH/.env.local .env.local"\
  ]
}
```

### [Using script files](https://cursor.com/docs/configuration/worktrees\#using-script-files)

For complex setups, you can reference script files instead of inline commands:

```
{
  "setup-worktree-unix": "setup-worktree-unix.sh",
  "setup-worktree-windows": "setup-worktree-windows.ps1",
  "setup-worktree": [\
    "echo 'Using generic fallback. For better support, define OS-specific scripts.'"\
  ]
}
```

Place your scripts in the `.cursor/` directory alongside `worktrees.json`:

**setup-worktree-unix.sh** (Unix/macOS):

```
#!/bin/bash
set -e

# Install dependencies
npm ci

# Copy environment file
cp "$ROOT_WORKTREE_PATH/.env" .env

# Run database migrations
npm run db:migrate

echo "Worktree setup complete!"
```

**setup-worktree-windows.ps1** (Windows):

```
$ErrorActionPreference = 'Stop'

# Install dependencies
npm ci

# Copy environment file
Copy-Item "$env:ROOT_WORKTREE_PATH\.env" .env

# Run database migrations
npm run db:migrate

Write-Host "Worktree setup complete!"
```

### [OS-specific configurations](https://cursor.com/docs/configuration/worktrees\#os-specific-configurations)

You can provide different setup commands for different operating systems:

```
{
  "setup-worktree-unix": [\
    "npm ci",\
    "cp $ROOT_WORKTREE_PATH/.env .env",\
    "chmod +x scripts/*.sh"\
  ],
  "setup-worktree-windows": [\
    "npm ci",\
    "copy %ROOT_WORKTREE_PATH%\\.env .env"\
  ]
}
```

### [Debugging](https://cursor.com/docs/configuration/worktrees\#debugging)

If you would like to debug the worktree setup script, open the "Output" bottom panel and select "Worktrees Setup" from the dropdown.

## [Worktrees Cleanup](https://cursor.com/docs/configuration/worktrees\#worktrees-cleanup)

Cursor automatically manages worktrees to prevent excessive disk usage:

- **Per-workspace limit**: Each workspace can have up to 20 worktrees
- **Automatic cleanup**: When you create a new worktree and exceed the limit, Cursor automatically removes the oldest worktrees

Worktrees are removed based on last access time, with the oldest worktrees being removed first. Cleanup is applied per-workspace, so worktrees from different repositories don't interfere with each other. This is done on a schedule, which can be configured in the settings:

```
{
  // 2.1 and above only:
  "cursor.worktreeCleanupIntervalHours": 6,
  "cursor.worktreeMaxCount": 20
}
```

## [Worktrees in the SCM Pane](https://cursor.com/docs/configuration/worktrees\#worktrees-in-the-scm-pane)

If you would like to visualize Cursor-created worktrees in the SCM Pane, you can enable the `git.showCursorWorktrees` setting (defaults to `false`).

![Worktrees in the SCM Pane](https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fworktrees%2Fworktrees-scm.png&w=1920&q=75&dpl=dpl_7zPiZUsTD7ownHrxp4Gk37N86tFn)

## [Language Server Protocol (LSP) Support](https://cursor.com/docs/configuration/worktrees\#language-server-protocol-lsp-support)

For performance reasons, Cursor currently does not support LSP in worktrees. The agent will not be able to lint files. We are working on supporting this functionality.

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