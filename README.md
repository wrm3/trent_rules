# trent

## AI Development System — Hybrid Agents & Skills Architecture

**File-based task management + specialized AI agents + on-demand skills for Cursor, Claude Code, Codex, and OpenCode.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Version](https://img.shields.io/badge/version-6.0.0-green.svg)](#)

---

## What is trent?

**trent** is a structured AI development system built around three layers:

1. **Minimal always-apply rules** (~281 lines) — session start, git workflow, enforcement guardrails
2. **19 specialized agents** — domain owners for tasks, planning, QA, verification, and more
3. **25 on-demand skills** — explicit workflows invoked when needed

The `.trent/` folder is the persistent project backbone: tasks, phases, PRDs, bugs, goals, and memory — all file-based and IDE-independent.

### Why Hybrid?

The old monolithic rules system loaded ~5,480 lines on every response. The hybrid loads ~281 lines always, with agents and skills loaded only when relevant. **95% context reduction** means more of your context window goes to your actual code.

---

## Platform Support

| Platform | Config Location | Rules | Agents | Skills | Commands |
|---|---|---|---|---|---|
| Cursor IDE | `.cursor/` | `.mdc` rules | `.cursor/agents/` | `.cursor/skills/` | `@trent-*` |
| Claude Code | `.claude/` | `.md` rules | `.claude/agents/` | `.claude/skills/` | `/trent-*` |
| Codex (OpenAI) | `.codex/` | via INSTALL.md | copied to project | copied to project | natural language |
| OpenCode | `.opencode/` | via INSTALL.md | copied to project | copied to project | natural language |
| Gemini/Agent | `.agent/` | `.md` rules | N/A | `.agent/skills/` | workflows |

---

## Architecture

```
trent/
├── .cursor/            # Cursor IDE config
│   ├── rules/          # 8 always-apply .mdc rules (~281 lines total)
│   ├── agents/         # 19 specialized agents
│   ├── skills/         # 25 on-demand skills
│   └── commands/       # 24 @trent-* commands
├── .claude/            # Claude Code config (parity with .cursor/)
│   ├── rules/          # 8 always-apply .md rules
│   ├── agents/         # 19 specialized agents
│   ├── skills/         # 25 on-demand skills
│   └── commands/       # 24 /trent-* commands
├── .agent/             # Gemini/Antigravity config
│   ├── rules/          # 8 always-apply .md rules
│   ├── skills/         # 25 on-demand skills
│   └── workflows/      # workflow equivalents
├── .codex/             # OpenAI Codex bootstrap
│   └── INSTALL.md
├── .opencode/          # OpenCode bootstrap
│   └── INSTALL.md
├── docker/             # MCP server (RAG, research, Oracle, memory)
└── .trent/             # THIS PROJECT's task data
```

---

## The 19 Agents

| Agent | Purpose |
|---|---|
| `trent-task-manager` | Task CRUD, TASKS.md sync, phase completion gate |
| `trent-planner` | PRDs, phases, subsystems, planning questionnaire |
| `trent-qa-engineer` | Bug tracking, BUGS.md, quality gates |
| `trent-verifier` | Adversarial two-stage verification (spec compliance → code quality) |
| `trent-workflow-manager` | Task expansion, sprint planning, complexity scoring |
| `trent-infrastructure` | File organization, scope control, project structure |
| `trent-autonomous` | Unattended sprint/cleanup, TTL management, blast radius |
| `trent-self-improvement` | System audits, inconsistency detection |
| `trent-project-files` | AGENTS.md and CLAUDE.md maintenance |
| `trent-platform-parity` | Cross-IDE sync, Firecrawl registry |
| `trent-multi-agent` | Parallel agent coordination, git worktrees |
| `trent-memory` | Session memory capture, user identity |
| `trent-cursor-cli` | Cursor CLI quick reference |
| `trent-claude-cli` | Claude Code CLI quick reference |
| `trent-codebase-analyst` | External codebase analysis for integration |
| `trent-ideas-goals` | IDEA_BOARD.md, PROJECT_GOALS.md |
| `trent-code-reviewer` | Security, performance, reusability reviews |
| `trent-python-dev` | Python standards, UV environment management |
| `trent-project-manager` | New project init, .trent/ grooming and healing |

---

## The 25 Skills

**Task Management:** `trent-task-new` · `trent-task-update` · `trent-task-sync-check` · `trent-status`

**Phase Management:** `trent-phase-add` · `trent-phase-pivot` · `trent-phase-sync-check` · `trent-phase-archive`

**Planning:** `trent-plan` · `trent-setup` · `trent-sprint` · `trent-cleanup` · `trent-workflow`

**Quality:** `trent-review` · `trent-qa` · `trent-qa-report` · `trent-bug-report` · `trent-bug-fix`

**Ideas & Goals:** `trent-idea-capture` · `trent-idea-review` · `trent-goal-update` · `trent-harvest`

**Utilities:** `trent-git-commit` · `trent-grooming` · `trent-visualizer`

---

## MCP Server (Docker)

The Docker MCP server provides tools for RAG, research, Oracle DB, MediaWiki, and memory:

```bash
cd docker && docker compose up -d
```

**Key tools:** `rag_search` · `rag_ingest_text` · `research_deep` · `oracle_query` · `oracle_execute` · `memory_search` · `memory_capture_session` · `trent_install` · `trent_health_report` · `md_to_html`

Admin UI: `http://localhost:8082/admin/db` (DB Explorer) · `http://localhost:8082/admin/trent` (Task Visualizer)

---

## Task Status System

| Indicator | Meaning |
|---|---|
| `[ ]` | Listed in TASKS.md, no file yet |
| `[📋]` | Task file created, ready to start |
| `[🔄]` | In progress |
| `[🔍]` | Awaiting cross-agent verification |
| `[✅]` | Completed |
| `[❌]` | Failed/Cancelled |
| `[⏸️]` | Paused (phase pivot) |

---

## Installation

### Cursor IDE
trent ships with your project via `.cursor/` config. For a new project, use the `trent_install` MCP tool or run `@trent-setup`.

### Claude Code
Same as Cursor — `.claude/` config ships with the project. Run `/trent-setup`.

### Codex (OpenAI)
See `.codex/INSTALL.md` — paste the bootstrap URL into your Codex prompt.

### OpenCode
See `.opencode/INSTALL.md` — paste the bootstrap URL into your OpenCode prompt.

---

## Security

- Never commit API keys, tokens, or passwords
- Use environment variables for secrets (`.env` at repo root, never committed)
- Oracle credentials passed per-query via MCP tool parameters
- Always use parameterized queries

---

**Version**: 6.0.0 — Hybrid Architecture  
**Last Updated**: 2026-03-09  
**Supported Platforms**: Cursor IDE · Claude Code · Codex · OpenCode · Gemini/Agent
