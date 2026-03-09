# trent

**AI-powered development system — context management, task tracking, spec-driven design, and a shared MCP toolbox for Cursor, Claude Code, and Gemini.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Version](https://img.shields.io/badge/version-6.0.0-green.svg)](#)

---

## What does trent do?

Working with AI coding assistants without structure leads to drift: the AI forgets what you built last session, proposes solutions that conflict with decisions you made a week ago, writes code that duplicates things already in your codebase, and has no idea which tasks are done vs which are still pending.

**trent solves this by giving the AI a persistent, structured project memory.**

### Context Management
Every session starts with a loaded project state: current phase, active goals, task status, and architectural constraints — all from files the AI reads automatically. The AI doesn't guess where the project is; it knows.

The **hybrid architecture** keeps always-apply rules under 300 lines (~281). Detailed agent knowledge only loads when relevant. Your context window goes to your actual code instead of loading 5,000 lines of rules on every response.

### Task & Phase Management
Tasks live in `.trent/tasks/` as structured Markdown files with YAML frontmatter. The master list is `.trent/TASKS.md`. Phases group tasks into milestones. The AI can create, update, complete, and sync tasks — with audit trails, dependency tracking, and phase completion gates.

Tasks can't be marked complete without evidence. A separate agent verifies the work adversarially — checking spec compliance first, then code quality. No rubber-stamping.

### Spec-Driven Design
Before any code is written, `@trent-plan` generates a PRD using a 27-question requirements framework covering users, scale, security, deployment, and constraints. Phases and subsystems follow from the spec. Architectural constraints go in `ARCHITECTURE_CONSTRAINTS.md` — the AI checks them before every implementation.

### Quality Enforcement
Bugs get logged immediately — "pre-existing" is not an exemption. Every bug gets a `BUG-NNN` entry in `.trent/BUGS.md`. Task completion requires a git commit offer. The enforcement rules fire on every response without needing an active agent.

### Shared MCP Toolbox
The Docker MCP server gives every project access to RAG search, deep research, Oracle DB, MediaWiki, session memory, and trent project installation — without each project running its own infrastructure.

---

## Platform Support

| Platform | Config | Rules | Agents | Skills | Commands |
|---|---|---|---|---|---|
| Cursor IDE | `.cursor/` | `.mdc` | `.cursor/agents/` | `.cursor/skills/` | `@trent-*` |
| Claude Code | `.claude/` | `.md` | `.claude/agents/` | `.claude/skills/` | `/trent-*` |
| Gemini/Agent | `.agent/` | `.md` | N/A | `.agent/skills/` | workflows |
| Codex (OpenAI) | `.codex/` | INSTALL.md | — | — | natural language |
| OpenCode | `.opencode/` | INSTALL.md | — | — | natural language |

---

## Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/your-org/trent_rules.git
cd trent_rules
```

### 2. Set up environment variables

```bash
cp docker/.env.example .env
```

Edit `.env` and fill in:

```env
# Required — PostgreSQL (RAG, memory, crawl registry)
POSTGRES_PASSWORD=your_secure_password

# Optional — enables AI research tools
OPENAI_API_KEY=sk-...

# Optional — enables deep research
PERPLEXITY_API_KEY=pplx-...

# Optional — enables Oracle DB access
ORACLE_USER=...
ORACLE_PASSWORD=...
ORACLE_DSN=host:port/service

# Optional — enables MediaWiki integration
MEDIAWIKI_URL=https://your-wiki/api.php
MEDIAWIKI_USERNAME=...
MEDIAWIKI_PASSWORD=...
```

### 3. Start the MCP server

```bash
cd docker
docker compose up -d
```

This starts:
- **PostgreSQL** with pgvector (RAG, memory, crawl registry)
- **trent MCP server** (28 tools available via HTTP)
- **Firecrawl** (optional — `--profile platform-docs` for platform doc crawling)

Verify it's running:

```bash
docker ps | grep trent_rules
# or
docker logs trent_rules_docker --tail 20
```

Admin UI: `http://localhost:8082/admin/db` (DB Explorer) · `http://localhost:8082/admin/trent` (Task Visualizer)

### 4. Connect the MCP server to your IDE

**Cursor IDE** — add to `.cursor/mcp.json` or Cursor Settings → MCP:

```json
{
  "mcpServers": {
    "trent": {
      "url": "http://localhost:8082/mcp",
      "transport": "streamable-http"
    }
  }
}
```

**Claude Code** — add to `.claude/settings.local.json`:

```json
{
  "mcpServers": {
    "trent": {
      "type": "streamable-http",
      "url": "http://localhost:8082/mcp"
    }
  }
}
```

### 5. Install trent into a project

From your IDE with the MCP server connected, run in any project:

**Cursor:** `@trent-setup` or call the MCP tool directly:
```
trent_install(project_path="/path/to/your/project", use_v2=True)
```

**Claude Code:** `/trent-setup`

This creates the `.trent/` folder structure, initializes `TASKS.md`, `PROJECT_CONTEXT.md`, `ARCHITECTURE_CONSTRAINTS.md`, and copies the agent/skill/rule configs.

---

## Project Structure (after install)

```
your-project/
├── .trent/
│   ├── TASKS.md                    # Master task list — source of truth
│   ├── PROJECT_CONTEXT.md          # Mission, phase, goals
│   ├── ARCHITECTURE_CONSTRAINTS.md # Non-negotiable decisions
│   ├── PRD.md                      # Product Requirements Document
│   ├── BUGS.md                     # Bug tracking
│   ├── SUBSYSTEMS.md               # Component registry
│   ├── IDEA_BOARD.md               # Ideas not yet ready for tasks
│   ├── PROJECT_GOALS.md            # Strategic goals (G-01, G-02...)
│   ├── tasks/                      # Individual task files (task001_name.md)
│   └── phases/                     # Phase documentation
├── .cursor/                        # Cursor IDE rules, agents, skills, commands
├── .claude/                        # Claude Code rules, agents, skills, commands
└── .agent/                         # Gemini rules and skills
```

---

## Key Commands

**Start a new project:**
```
@trent-setup       — initialize .trent/ folder and ask planning questions
@trent-plan        — generate PRD from 27-question requirements interview
@trent-phase-add   — add a new phase with tasks
```

**Daily development:**
```
@trent-task-new    — create a task with full YAML spec
@trent-task-update — update status, add evidence
@trent-status      — session start: load goals, phase, task list
@trent-review      — code review (security, perf, reusability)
```

**Quality:**
```
@trent-bug-report  — log a bug to BUGS.md with severity
@trent-qa          — run quality checklist
@trent-sprint      — autonomous 2-hour sprint (claims + implements tasks)
```

**Ideas & memory:**
```
@trent-idea-capture — "make a note of that" → IDEA_BOARD.md
@trent-harvest      — analyze an external codebase for ideas to adopt
```

---

## The Agent & Skill System

trent uses a **hybrid architecture**: 8 slim always-apply rules (~281 lines) that load every response, plus 19 specialized agents and 56 on-demand skills that load only when needed.

### Agents (loaded on-demand by the AI)

| Agent | When it activates |
|---|---|
| `trent-task-manager` | Creating, updating, or completing tasks |
| `trent-planner` | PRDs, phases, planning questionnaire |
| `trent-qa-engineer` | Bug reports, BUGS.md, quality gates |
| `trent-verifier` | Cross-agent two-stage task verification |
| `trent-workflow-manager` | Task expansion, sprint planning, Kanban |
| `trent-code-reviewer` | Security, performance, reusability reviews |
| `trent-autonomous` | Unattended sprint/cleanup runs |
| `trent-platform-parity` | Keeping .cursor/.claude/.agent in sync |
| `trent-ideas-goals` | IDEA_BOARD.md and PROJECT_GOALS.md |
| `trent-python-dev` | Python projects, UV environment management |
| `trent-project-manager` | New project init, .trent/ healing |
| `trent-memory` | Session memory capture (Gemini/VS Code) |
| *(+ 7 more)* | infrastructure, multi-agent, CLI refs, etc. |

### Skills (explicit workflow invocation)

Grouped by function: **Task** · **Phase** · **Planning** · **Quality** · **Ideas** · **Utilities** · **Video/3D** (13 creative skills from Manim to Remotion)

---

## MCP Tools — Full Reference

The Docker MCP server exposes **28 tools** over SSE/HTTP at `http://localhost:8082/mcp`. All tools are available to any connected IDE.

### RAG / Knowledge Base

| Tool | Description |
|---|---|
| `rag_search` | Semantic search across stored knowledge (pgvector). Pass a query and optional subject. |
| `rag_ingest_text` | Add raw text or markdown to the knowledge base under a subject. |
| `rag_list_subjects` | List all available knowledge base subjects (namespaced collections). |

### Research

| Tool | Description |
|---|---|
| `research_deep` | Comprehensive multi-source research via Perplexity. Best for "what is X" or "compare A vs B". |
| `research_search` | Lightweight web search. Fast, single-source answers. |

### Oracle Database

| Tool | Description |
|---|---|
| `oracle_query` | Read-only SQL on Oracle (`SELECT`, `DESCRIBE`, `EXPLAIN`). Credentials passed per call. |
| `oracle_execute` | Write SQL on Oracle (`INSERT`, `UPDATE`, `DELETE`, `CREATE`, `ALTER`). Credentials passed per call. |

### MediaWiki

| Tool | Description |
|---|---|
| `mediawiki_page` | Create, read, update, or check pages in a MediaWiki instance. |
| `mediawiki_search` | Full-text search across a MediaWiki instance. Returns titles + excerpts. |

### Agent Memory

| Tool | Description |
|---|---|
| `memory_search` | Semantic search across all stored agent sessions and memory captures. |
| `memory_search_combined` | Semantic search across BOTH agent memory AND the RAG knowledge base simultaneously. |
| `memory_capture_session` | Call at end of session — AI self-reports summary for future context injection. |
| `memory_capture_insight` | Capture a specific insight, preference, or decision for long-term memory. |
| `memory_context` | Retrieve token-budgeted context block for session-start injection. |
| `memory_sessions` | List recent sessions for a project (for browsing what was worked on). |
| `memory_ingest_session` | Ingest raw IDE session turns from file adapters (Cursor, Claude Code automatic capture). |
| `memory_setup_user` | Create or update `~/.trent/user_config.json` for memory identity tracking. |

### Platform Documentation

| Tool | Description |
|---|---|
| `platform_docs_search` | Semantic search over Firecrawl-crawled Cursor, Claude Code, and Gemini docs. Requires `--profile platform-docs`. |
| `check_crawl_freshness` | Check if a platform's docs are fresh in the shared crawl registry. Prevents redundant re-crawls across projects. |
| `update_crawl_registry` | Record a successful platform doc crawl. Called automatically by the scheduler. |

### trent System

| Tool | Description |
|---|---|
| `trent_install` | Install or upgrade the full trent environment into a project directory. Pass `use_v2=True` for current architecture. |
| `trent_health_report` | Compute health score (0–100) for a trent project. Returns subsystem breakdown, stale claims, blocked tasks. |
| `trent_plan_reset` | Reset `.trent/` to blank template. Requires `confirm=True`. Destructive — clears task data. |
| `trent_validate_task` | Validate a task against `ARCHITECTURE_CONSTRAINTS.md` before claiming. Returns `valid`, `warnings`, `violations`. |
| `trent_server_status` | Health check — returns server version, loaded plugins, DB connectivity. |

### Video Analysis (YouTube)

| Tool | Description |
|---|---|
| `video_analyze` | Full analysis pipeline: metadata + transcript + key frames + AI vision description. |
| `video_extract_metadata` | Extract video title, description, duration, channel, view count. |
| `video_extract_transcript` | Extract auto-generated or manual captions. |
| `video_extract_frames` | Extract key frames from a video at intervals. |
| `video_get_playlist` | List all video IDs and metadata from a YouTube playlist. |
| `video_check_new` | Check a playlist for videos added since last check (for automation pipelines). |
| `video_batch_process` | Process multiple videos concurrently with configurable concurrency. |

### Utilities

| Tool | Description |
|---|---|
| `md_to_html` | Convert markdown to a beautifully styled, self-contained HTML document. |
| `get_service_url` | Returns the base URL for a named service in the trent stack (e.g., `admin`, `pgadmin`). |

---

## REST API (Admin & Memory Endpoints)

The MCP server also exposes HTTP REST endpoints for browser access and automation.

### Admin / DB Explorer (`http://localhost:8082`)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/admin/db` | **DB Explorer UI** — browse all Postgres schemas and tables |
| `GET` | `/admin/db/tables` | List all tables with schema, row count, size |
| `GET` | `/admin/db/tables/{schema}/{table}/data` | Paginated table data with filtering |
| `POST` | `/admin/db/query` | Execute arbitrary SQL and return results as JSON |
| `GET` | `/admin/trent` | **Task Visualizer UI** — interactive DAG of `.trent/` tasks by phase |
| `GET` | `/admin/trent/data` | Raw task data as JSON (phase groupings, statuses, dependencies) |
| `GET` | `/admin/trent/task/{task_id}` | Full detail for a single task (YAML + markdown body) |

### Memory REST (`http://localhost:8082`)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/memory/health` | Memory subsystem health check |
| `POST` | `/memory/ingest` | Ingest a raw session file (used by IDE file adapters) |
| `POST` | `/memory/capture` | Capture a session summary (used by `memory_capture_session` tool) |
| `POST` | `/memory/insight` | Capture a specific insight (used by `memory_capture_insight` tool) |
| `GET` | `/memory/context` | Retrieve context block for session injection |

### Install REST

| Method | Endpoint | Description |
|---|---|---|
| `GET/POST` | `/install/download` | Download trent template bundle for offline installation |

---

## Docker Commands Reference

```bash
# Start everything
cd docker && docker compose up -d

# With platform docs crawling (optional, requires FIRECRAWL_API_KEY)
cd docker && docker compose --profile platform-docs up -d

# Rebuild after code changes
cd docker && docker compose up -d --build trent

# View logs
docker logs trent_rules_docker -f

# Apply a new SQL migration manually
cat docker/init_db/09_new_migration.sql | docker exec -i trent_rules_postgres psql -U knowledge_base -d knowledge_base

# Stop everything
cd docker && docker compose down
```

---

## Security

- Never commit `.env` — it's gitignored
- Oracle credentials are passed per-query, never stored in the server
- Always use parameterized queries for any DB access
- API keys (OpenAI, Perplexity, Firecrawl) live only in `.env`

---

**Version**: 6.0.0  
**Last Updated**: 2026-03-09  
**Supported Platforms**: Cursor IDE · Claude Code · Gemini · Codex · OpenCode
