# Google Antigravity Architecture

**Last Updated**: 2026-02-19
**Official Website**: https://antigravity.google
**Docs**: https://antigravity.google/docs
**Version Documented**: Public Preview (Released Nov 18, 2025)

## Overview

Google Antigravity is Google's AI-first IDE built for the "agent-first era." Powered by Gemini 3 Pro, it provides an autonomous, agentic development experience with both a synchronous **Editor view** (IDE-style) and an asynchronous **Agent Manager** (mission control for multiple agents/workspaces). It supports multi-model access (Gemini 3 Pro, Flash, Claude Sonnet 4.5, GPT).

**Key differentiator**: Antigravity's agent can autonomously plan, execute, browse the web, run terminal commands, and verify its own work using "Artifacts" — tangible deliverables like task lists, implementation plans, walkthroughs, and browser recordings.

## Directory Structure

```
~/.gemini/GEMINI.md              # Global rules (apply to ALL workspaces)
~/.gemini/antigravity/           # Global Antigravity data
│   ├── brain/                   # Conversation artifacts
│   ├── knowledge/               # Persistent curated Knowledge Items
│   ├── conversations/           # Encrypted conversation state
│   ├── implicit/                # Encrypted implicit learned context
│   ├── browser_recordings/      # WebP videos from browser sessions
│   ├── skills/                  # Global skills (shared across projects)
│   ├── mcp_config.json          # Global MCP server config
│   └── user_settings.pb         # User preferences (protobuf)

project-root/
├── .agent/
│   ├── rules/                   # Workspace-specific rules (.md files)
│   │   ├── always_on_rule.md    # Always applied
│   │   ├── task_management.md   # trent task management rule
│   │   └── *.md                 # Other workspace rules
│   ├── skills/                  # Workspace-level skill packages
│   │   └── my-custom-skill/
│   │       ├── SKILL.md         # YAML frontmatter + instructions
│   │       └── templates/       # Supporting assets
│   └── workflows/               # Slash-command workflows (.md files)
│       ├── trent-task-new.md    # /trent-task-new
│       ├── trent-status.md      # /trent-status
│       └── *.md                 # Other workflows
├── AGENTS.md                    # Universal agent instructions (all platforms)
├── GEMINI.md                    # Antigravity-specific overrides (optional)
├── GUARDRAILS.md                # Learned constraints to prevent repeated failures
└── mcp_config.json              # MCP server connections (project-level)
```

**Note**: The `.agent/` folder lives at workspace root or git root. Antigravity reads from the closest git root.

## Rules System

### File Format

Rules are standard **Markdown** files (`.md`) with optional YAML frontmatter.

```yaml
---
description: "Brief description of what this rule does"
activation: "always_on"   # always_on | glob | model_decision | manual
globs:
  - "**/*.ts"             # Only required for activation: "glob"
---

# Rule Title

## Rule Content
[Markdown content with instructions, examples, and guidelines]
```

**Character Limit**: 12,000 characters per rule file.

### Rule Activation Types

| Activation | Description | Use Case |
|------------|-------------|----------|
| `always_on` | Applied to every agent conversation | Global coding standards, project context |
| `glob` | Applied when editing files matching pattern | Language-specific rules (e.g., `**/*.py`) |
| `model_decision` | AI decides whether rule is relevant | Contextual rules (e.g., "when working with databases") |
| `manual` | Only applied when `@rule-name` mentioned | On-demand reference rules |

### @ Mentions in Rules

Rules can reference other files using `@filename`:
- **Relative path**: Resolved relative to the rule file's location
- **Absolute path**: Resolved as `/path/to/file.md`, fallback to `workspace/path/to/file.md`
- **Example**: `@/path/to/AGENTS.md` - Include project overview

### Global vs Workspace Rules

| Level | Location | Purpose |
|-------|----------|---------|
| **Global** | `~/.gemini/GEMINI.md` | Personal preferences, coding style across all projects |
| **Workspace** | `.agent/rules/*.md` | Project-specific rules, team standards, framework preferences |

**Hierarchy**: Workspace rules → Global rules → System rules (immutable)

### GEMINI.md (Project Root)

`GEMINI.md` in the project root serves as Antigravity-specific project overrides — the Antigravity equivalent of `CLAUDE.md`. It supplements `AGENTS.md` with Gemini-specific context.

**Priority order in Antigravity**: `AGENTS.md` → `GEMINI.md` → `.agent/rules/` → built-in defaults

### GUARDRAILS.md

`GUARDRAILS.md` is a unique Antigravity feature — a learned constraints file. As the agent encounters failures and edge cases, it can write to `GUARDRAILS.md` to capture constraints that prevent repeating the same mistakes.

Example content:
```markdown
# GUARDRAILS

## Database
- NEVER drop tables without explicit user confirmation
- ALWAYS backup before schema migrations

## API
- NEVER expose raw error messages to frontend
- ALWAYS validate input before database queries
```

### ⚠️ Known Issue: Config Conflict

Both Antigravity IDE and Gemini CLI use `~/.gemini/GEMINI.md` as global config. This can cause conflicts if both tools are used. Track this issue: https://github.com/google-gemini/gemini-cli/issues/16058

**Workaround**: Keep global rules minimal and put project-specific config in `.agent/rules/`.

## Skills System

Antigravity supports **Skills** — reusable knowledge packages nearly identical to Claude Code and Cursor skills.

### Location

| Level | Path |
|-------|------|
| **Workspace** | `.agent/skills/skill-name/SKILL.md` |
| **Global** | `~/.gemini/antigravity/skills/skill-name/SKILL.md` |

### Skill File Format

```yaml
---
name: skill-name
description: What this skill does and when to use it
---

# Skill: Skill Name

## Overview
[Brief description]

## Instructions
[Detailed instructions for using this skill]

## Examples
[Usage examples]
```

**Migration note**: Skills are the **most portable component** between platforms. The `SKILL.md` format is nearly identical between Cursor, Claude Code, and Antigravity. Moving skills requires minimal changes — just update the folder location.

### Skills vs Rules

| | Skills | Rules |
|--|--------|-------|
| **Purpose** | Reusable knowledge module | Persistent constraint/instruction |
| **Activation** | Loaded on relevance (lazy) | Always-on or glob-activated |
| **Location** | `.agent/skills/*/SKILL.md` | `.agent/rules/*.md` |
| **Size** | Unlimited (+ supporting files) | 12,000 char limit per file |

## Workflows System

Workflows are slash-command automations stored as Markdown files. They define step-by-step sequences of agent actions for repetitive tasks.

### File Format

```markdown
---
description: "What this workflow does"
---

# Workflow: workflow-name

## Description
Brief description of the workflow's purpose.

## Steps

### Step 1: [Step Name]
[Instructions for the agent]

### Step 2: [Step Name]
// turbo
[Instructions for auto-execution without approval]

### Step 3: [Step Name]
[More instructions]
```

### Invocation

```
/workflow-name
```

Workflows are invoked in the Agent chat using a `/` prefix. You can call other workflows from within a workflow: `Call /other-workflow`.

### Turbo Mode

Place `// turbo` above a step to allow the agent to execute it automatically without asking for user approval:

```markdown
### Step 2: Run Tests
// turbo
Run the test suite: `npm test`
```

### Workflow Files

| Location | Purpose |
|----------|---------|
| `.agent/workflows/*.md` | Workspace-specific workflows |
| `~/.gemini/antigravity/global_workflows/*.md` | Global workflows (all workspaces) |

## Artifacts System

Antigravity generates structured **Artifacts** as the agent works. These are tangible deliverables the user can review and comment on.

| Artifact | Description |
|----------|-------------|
| `task.md` | Living task checklist, broken into subtasks |
| `implementation_plan.md` | Technical blueprint before coding begins |
| `walkthrough.md` | Post-completion proof-of-work document |
| Screenshots | Visual verification of UI changes |
| Browser recordings | Video of agent's browser interactions |
| Code diffs | Structured view of code changes |

**Artifact Review Policy**:
- `Request Review` - Agent pauses and waits for user review
- `Always Proceed` - Agent continues automatically

### Rule Ideas for Artifacts

You can write rules to customize artifact behavior:

```markdown
# Artifact Rules

- Always include a "Security Implications" section in implementation_plan.md
- Always break task.md into sub-tasks of no more than 1 hour each
- Always include a "Rollback Plan" in walkthrough.md
```

## Knowledge Items System

Knowledge Items (KIs) are Antigravity's **automatic persistent memory**. The agent creates and updates KIs from conversation history.

- **What they store**: Important patterns, solutions, user preferences, code snippets, architecture insights
- **How they work**: Auto-analyzed from conversations, stored with title + summary + artifacts
- **How they're used**: KI summaries always available to agent; full KI artifacts loaded when relevant
- **Location**: `~/.antigravity/` (not project files — managed in Agent Manager UI)

Unlike Cursor rules or Claude Code skills (which you manually create), KIs are **auto-generated** and represent learned knowledge over time.

## Agent Manager

The Agent Manager is Antigravity's "mission control" surface (toggle with `Cmd+E` / `Ctrl+E`):
- Manage multiple workspaces simultaneously
- Spawn and observe multiple parallel agents
- Inbox notifications for agent progress
- View and manage Knowledge Items
- View Artifacts from completed tasks

## Agent Modes

| Mode | Description | When to Use |
|------|-------------|-------------|
| `Fast` | Executes directly, no planning | Simple tasks (rename, small edits) |
| `Planning` | Plans first, produces Artifacts | Complex tasks, new features, research |

## Settings

### Terminal Command Auto Execution

| Setting | Behavior |
|---------|----------|
| `Always Proceed` | Auto-run (except deny list) |
| `Request Review` | Always ask (except allow list) |

Allow/deny lists configured per-workspace in Agent Settings.

### Non-Workspace File Access

By default, agent only accesses workspace files and `~/.antigravity/`. Enable non-workspace access cautiously (exposes local secrets to agent).

## MCP Integration

Antigravity supports MCP (Model Context Protocol) for tool integration.

### Configuration Locations

| Level | File |
|-------|------|
| **Project-level** | `mcp_config.json` at project root |
| **Global** | `~/.gemini/antigravity/mcp_config.json` |

### Format

```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["/path/to/server/index.js"]
    }
  }
}
```

**Migration note**: MCP configurations are largely compatible between Cursor and Antigravity. Both use the same stdio/SSE protocol. The main difference is file location (`mcp_config.json` vs `.cursor/mcp.json`).

## Multi-Model Support

Antigravity provides access to multiple models (subject to rate limits refreshed every 5 hours):
- **Gemini 3 Pro** - Primary model, most capable
- **Gemini 3 Flash** - Faster, lower cost (added Dec 2025)
- **Nano Banana Pro** - (added Nov 2025)
- **Claude Sonnet 4.5** - Anthropic's model
- **GPT-OSS** - OpenAI's model

## Cross-Platform Compatibility

### Comparison with Cursor and Claude Code

| Feature | Antigravity | Cursor | Claude Code |
|---------|-------------|--------|-------------|
| **Type** | Standalone IDE | Standalone IDE | VSCode Ext / CLI |
| **Rules Location** | `.agent/rules/` | `.cursor/rules/` | `.claude/rules/` |
| **File Format** | `.md` ✅ | `.mdc` ⚠️ | `.md` ✅ |
| **Global Config** | `~/.gemini/GEMINI.md` | Cursor Settings | N/A (CLAUDE.md per project) |
| **Commands** | `/workflow-name` | `@command-name` | `/command-name` |
| **Skills** | ❌ No | ✅ Yes | ✅ Yes |
| **SubAgents** | ❌ No | ✅ Yes | ✅ Yes |
| **Hierarchical Context** | ✅ Global + Workspace | ❌ No | ❌ No |
| **Artifacts** | ✅ Yes (unique) | ❌ No | ❌ No |
| **Knowledge Items** | ✅ Auto-generated | ❌ No | ⚠️ Memory (manual) |
| **Multi-model** | ✅ Yes | ✅ Yes | ❌ Claude only |
| **Browser Control** | ✅ Built-in | ✅ Via extension | ❌ No |
| **MCP Support** | ✅ Yes | ✅ Yes | ✅ Yes |
| **AGENTS.md** | ✅ Reads natively | ✅ Reads natively | ✅ Reads natively |

### Migration: Cursor → Antigravity

```powershell
# 1. Create .agent/ directories
New-Item -ItemType Directory -Force .agent/rules, .agent/skills, .agent/workflows

# 2. Copy and rename rules (.mdc → .md)
Copy-Item .cursor/rules/*.mdc .agent/rules/
Get-ChildItem .agent/rules -Filter "*.mdc" | Rename-Item -NewName { $_.Name -replace '\.mdc$','.md' }

# 3. Update YAML frontmatter in each rule
# Change: alwaysApply: true → activation: "always_on"
# Change: globs: [...] → keep (compatible with Antigravity glob activation)

# 4. Copy skills (nearly identical format!)
Copy-Item -Recurse .cursor/skills/* .agent/skills/
# Skills work as-is — minimal or no changes needed

# 5. Convert commands to workflows
Copy-Item .cursor/commands/*.md .agent/workflows/
# Update invocation docs: @command-name → /command-name

# 6. Agents → Workflow steps (no equivalent in Antigravity)
# Merge key agent instructions into always_on rules

# 7. Create GEMINI.md from CLAUDE.md content (restructure for Gemini context)

# 8. Create mcp_config.json from .cursor/mcp.json (rename + move to project root)
```

### Migration: Claude Code → Antigravity

```powershell
# 1. Create .agent/ directories
New-Item -ItemType Directory -Force .agent/rules, .agent/skills, .agent/workflows

# 2. Copy rules (already .md format — minimal changes!)
Copy-Item .claude/rules/*.md .agent/rules/
# Update YAML frontmatter: alwaysApply: true → activation: "always_on"

# 3. Copy skills (format is nearly identical!)
Copy-Item -Recurse .claude/skills/* .agent/skills/

# 4. Convert commands to workflows (/ prefix is the same!)
Copy-Item .claude/commands/*.md .agent/workflows/
# Commands already use / prefix — invocation is compatible!

# 5. CLAUDE.md → GEMINI.md (restructure for Gemini context)

# 6. Create mcp_config.json from settings.local.json mcpServers section
```

### AGENTS.md Compatibility

Antigravity reads `AGENTS.md` at the workspace root, making it the **universal** cross-platform instructions file (works with Cursor, Claude Code, Windsurf, Copilot, Antigravity, and 15+ others). Recommended as the primary project context file.

## trent System Integration

### Adapting trent for Antigravity

The trent task management system maps to Antigravity as follows:

| trent Concept | Antigravity Implementation |
|---------------|---------------------------|
| Rules (`.cursor/rules/*.mdc`) | `.agent/rules/*.md` |
| Commands (`@trent-*`) | Workflows (`/trent-*`) |
| Skills (`.cursor/skills/`) | `.agent/skills/*/SKILL.md` (nearly identical format!) |
| Agents (`.cursor/agents/`) | Workflow steps or Planning mode prompts |
| `CLAUDE.md` | `GEMINI.md` (Antigravity-specific overrides) |
| Hooks | Not directly supported (use workflows) |
| `AGENTS.md` | `AGENTS.md` (same — universal standard!) |

### Recommended File Structure for trent + Antigravity

```
project-root/
├── AGENTS.md                    # Universal instructions (all platforms)
├── GEMINI.md                    # Antigravity-specific context (like CLAUDE.md)
├── GUARDRAILS.md                # Learned failure constraints
├── mcp_config.json              # MCP servers (project-level)
├── .agent/
│   ├── rules/
│   │   ├── 00_always.md         # Response format, timestamps
│   │   ├── 10_trent_core.md     # Task management rules
│   │   ├── 11_trent_planning.md # Planning rules
│   │   ├── 12_trent_qa.md       # QA rules
│   │   ├── 13_trent_workflow.md # Workflow rules
│   │   └── 30_project.md        # Project-specific rules
│   ├── skills/                  # trent skills adapted for Antigravity
│   │   ├── trent-planning/
│   │   │   └── SKILL.md
│   │   └── trent-code-reviewer/
│   │       └── SKILL.md
│   └── workflows/
│       ├── trent-setup.md        # /trent-setup
│       ├── trent-task-new.md     # /trent-task-new
│       ├── trent-status.md       # /trent-status
│       ├── trent-plan.md         # /trent-plan
│       ├── trent-review.md       # /trent-review
│       └── trent-git-commit.md   # /trent-git-commit
└── .trent/                       # Task data (universal, unchanged)
    ├── TASKS.md
    ├── PLAN.md
    └── tasks/
```

### Dual-IDE Strategy (Cursor + Antigravity)

To maintain a project that works in both:

1. **`AGENTS.md`** — Universal bridge (works in both, identical content)
2. **`CLAUDE.md`** — Claude Code/Cursor-specific context
3. **`GEMINI.md`** — Antigravity-specific context
4. **`.cursor/`** — Cursor-specific config (ignored by Antigravity)
5. **`.agent/`** — Antigravity-specific config (ignored by Cursor)
6. **`.trent/`** — Task management data (portable, works in both)

## Best Practices

### Rules
```
✅ Use .md extension (standard markdown)
✅ Use activation: "always_on" for project-wide standards
✅ Use activation: "glob" for language-specific rules
✅ Keep rules under 12,000 characters each (hard limit)
✅ Use @filename to reference AGENTS.md for project context
✅ Keep global GEMINI.md minimal; put project rules in .agent/rules/
```

### Workflows
```
✅ Use /workflow-name slash prefix for invocation
✅ Use // turbo for safe, repeatable automated steps
✅ Break complex tasks into multi-step workflows
✅ Call other workflows from within a workflow
✅ Let agent generate workflows from successful conversation patterns
```

### Artifacts
```
✅ Use Planning mode for complex tasks (enables artifacts)
✅ Set Artifact Review Policy to "Request Review" for critical features
✅ Write rules to customize artifact content (security sections, rollback plans)
✅ Use browser recordings as UI verification evidence
```

## Troubleshooting

### Rules Not Loading
1. ✅ Verify rules are in `.agent/rules/` (NOT `.agent/` root)
2. ✅ Ensure YAML frontmatter is valid
3. ✅ Check `activation` field is correct value
4. ✅ Restart Antigravity
5. ✅ Verify file size is under 12,000 characters

### Workflows Not Working
1. ✅ Use `/workflow-name` (not `@`)
2. ✅ Workflow file must be in `.agent/workflows/`
3. ✅ File must be `.md` format
4. ✅ Check workflow invocation is correct

### Global/Workspace Config Conflicts
1. ✅ Keep `~/.gemini/GEMINI.md` minimal
2. ✅ Put project rules in `.agent/rules/`
3. ✅ Watch GitHub issue #16058 for CLI/IDE conflict resolution

## Official Resources

- **Website**: https://antigravity.google
- **Docs**: https://antigravity.google/docs
- **Blog**: https://antigravity.google/blog
- **Download**: https://antigravity.google/download
- **X (Twitter)**: https://x.com/antigravity
- **LinkedIn**: https://linkedin.com/company/google-antigravity
- **YouTube**: https://youtube.com/@GoogleAntigravity
- **Community Resources**: https://antigravity.codes (unofficial)
- **Rules Library**: https://antigravity.codes/rules

## Version History

- **2026-02-19**: Initial documentation
  - Documented `.agent/rules/` and `.agent/workflows/` system
  - Explained Artifacts, Knowledge Items, Agent Manager
  - Added cross-platform migration guides
  - Documented trent integration approach
  - Noted GEMINI.md conflict issue with Gemini CLI

---

**Critical Notes**:
1. **Use `.md` extension** (not `.mdc`) for Antigravity rules
2. **Use `/workflow-name`** for workflow invocation (not `@`)
3. **12,000 character limit** per rule file
4. **Antigravity is in public preview** — verify docs quarterly as features evolve
5. **AGENTS.md** is the recommended cross-platform project context file
