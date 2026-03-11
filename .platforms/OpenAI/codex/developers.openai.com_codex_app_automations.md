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

Automate recurring tasks in the background. Codex adds findings to the inbox, or automatically archives the task if there’s nothing to report. You can combine automations with [skills](https://developers.openai.com/codex/skills) for more complex tasks.

Automations run locally in the Codex app. The app needs to be running, and the
selected project needs to be available on disk.

In Git repositories, each automation run starts in a new
[worktree](https://developers.openai.com/codex/app/worktrees) so it doesn’t interfere with your main
checkout. In non-version-controlled projects, automations run directly in the
project directory.

![Automation creation form with schedule and prompt fields](https://developers.openai.com/images/codex/app/create-automation-light.webp)![Automation creation form with schedule and prompt fields](https://developers.openai.com/images/codex/app/create-automation-dark.webp)

![Automation creation form with schedule and prompt fields](https://developers.openai.com/images/codex/app/create-automation-light.webp)![Automation creation form with schedule and prompt fields](https://developers.openai.com/images/codex/app/create-automation-dark.webp)

## Managing tasks

All automations and their runs can be found in the automations pane inside your Codex app sidebar.

The “Triage” section acts as your inbox. Automation runs with findings show up there, and you can filter your inbox to show all automation runs or only unread ones.

When an automation runs in a Git repository, Codex uses a dedicated background [worktree](https://developers.openai.com/codex/app/features#worktree-support). In non-version-controlled projects, automations run directly in the project directory. Consider using Git to enable running on background worktrees. You can have the same automation run on multiple projects.

Automations use your default sandbox settings. In read-only mode, tool calls fail if they require modifying files, network access, or working with apps on your computer. With full access enabled, background automations carry elevated risk. You can adjust sandbox settings in [Settings](https://developers.openai.com/codex/app/settings) and selectively allowlist commands with [rules](https://developers.openai.com/codex/rules).

To keep automations maintainable and shareable across teams, you can use [skills](https://developers.openai.com/codex/skills) to define the action and provide tools and context to Codex. You can explicitly trigger a skill as part of an automation by using `$skill-name` inside your automation.

## Testing automations safely

Before you schedule an automation, test the prompt manually in a regular thread
first. This helps you confirm:

- The prompt is clear and scoped correctly.
- The selected model and tools behave as expected.
- The resulting diff is reviewable.

When you start scheduling runs, review the first few outputs closely and adjust
the prompt or cadence as needed.

## Worktree cleanup for automations

For Git repositories, automations run in worktrees. Frequent schedules can
create many worktrees over time. Archive automation runs you no longer need,
and avoid pinning runs unless you intend to keep their worktrees.

## Permissions and security model

Automations are designed to run unattended and use your default sandbox
settings.

- If your sandbox mode is **read-only**, tool calls fail if they require
modifying files, accessing network, or working with apps on your computer.
Consider updating sandbox settings to workspace write.
- If your sandbox mode is **workspace-write**, tool calls fail if they require
modifying files outside the workspace, accessing network, or working with apps
on your computer. You can selectively allowlist commands to run outside the
sandbox using [rules](https://developers.openai.com/codex/rules).
- If your sandbox mode is **full access**, background automations carry
elevated risk, as Codex may modify files, run commands, and access network
without asking. Consider updating sandbox settings to workspace write, and
using [rules](https://developers.openai.com/codex/rules) to selectively define which commands the agent
can run with full access.

If you are in a managed environment, admins can restrict these behaviors using
admin-enforced requirements. For example, they can disallow `approval_policy = "never"` or constrain allowed sandbox modes. See
[Admin-enforced requirements (`requirements.toml`)](https://developers.openai.com/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

Automations use `approval_policy = "never"` when your organization policy
allows it. If `approval_policy = "never"` is disallowed by admin requirements,
automations fall back to the approval behavior of your selected mode.

## Examples

### Automatically create new skills

```
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.


```

### Stay up-to-date with your project

```
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch <DIRECTORY>

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments


```

### Combining automations with skills to fix your own bugs

Create a new skill that tries to fix a bug introduced by your own commits by creating a new `$recent-code-bugfix` and [store it in your personal skills](https://developers.openai.com/codex/skills#where-to-save-skills).

```
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.


```

Afterward, create a new automation:

```
Check my commits from the last 24h and submit a $recent-code-bugfix.


```