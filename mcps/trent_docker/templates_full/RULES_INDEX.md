# Rules Index

> Quick reference for all Cursor rules in this system.
> 
> **Location**: `.cursor/rules/`
> **Format**: `.mdc` files (Markdown Cursor format)

---

## Core Rules (Always Applied)

| # | Rule | Description |
|---|------|-------------|
| 00 | `00_always.mdc` | Response format: timestamp, tools, context usage |
| 01 | `01_documentation.mdc` | Documentation standards, file naming conventions |
| 02 | `02_git_workflow.mdc` | Git commit messages, branching, collaboration |
| 03 | `03_code_review.mdc` | Code review guidelines, security, quality |

## Trent System Rules

| # | Rule | Description |
|---|------|-------------|
| 10 | `10_trent_core.mdc` | Core task management, file organization, coding standards |
| 11 | `11_trent_planning.mdc` | PRD generation, phases, subsystems, scope validation |
| 12 | `12_trent_qa.mdc` | Bug tracking, design fixes, quality management |
| 13 | `13_trent_workflow.mdc` | Task expansion, sprints, Kanban, visualization |
| 14 | `14_trent_index.mdc` | System overview, directory structure, commands |
| 15 | `15_trent_agents_multi.mdc` | Parallel agent workflows, Git worktrees |
| 16 | `16_trent_self_improvement.mdc` | Self-improvement protocol for rule issues |
| 17 | `17_trent_project_files.mdc` | agents.md and CLAUDE.md management |
| 18 | `18_current_datetime_awareness.mdc` | Current date awareness, research triggers |

## Platform Rules

| # | Rule | Description |
|---|------|-------------|
| 30 | `30_powershell.mdc` | PowerShell command reference, terminal integration |
| 31 | `31_curl.mdc` | Curl command fix for Windows PowerShell |

## Specialty Rules (Agent-Requestable)

| # | Rule | Description |
|---|------|-------------|
| 60 | `60_product_development.mdc` | Startup product development best practices |
| 61 | `61_resource_access.mdc` | Startup resources: cloud, labs, grants |
| 70 | `70_parallel_workflows.mdc` | Multi-agent parallel execution coordination |

---

## Rule Numbering Convention

| Range | Category |
|-------|----------|
| 00-09 | Core/Always Applied |
| 10-19 | Trent System |
| 20-29 | Reserved |
| 30-39 | Platform/Environment |
| 40-49 | Reserved |
| 50-59 | Reserved |
| 60-69 | Specialty/Domain |
| 70-79 | Advanced Workflows |

## Rule Count Summary

- **Total Rules**: 18
- **Always Applied**: 14
- **Agent-Requestable**: 4

## Rule Application

### Always Applied
Rules in ranges 00-39 are automatically loaded and applied to every conversation.

### Agent-Requestable
Rules in ranges 60+ are loaded on-demand when relevant to the task.

## How Rules Work

```yaml
# Rule frontmatter (in .mdc files)
---
description: "What this rule does"
globs: ["*.py", "*.js"]  # Optional: file patterns
alwaysApply: true        # Or false for on-demand
---

# Rule content follows...
```

---

*Last updated: 2026-02-01*
