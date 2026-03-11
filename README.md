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

### Step 1 — Clone and configure

```bash
git clone https://github.com/your-org/trent_rules.git
cd trent_rules

# Copy the example environment file
copy .env.example .env       # Windows
# cp .env.example .env       # Linux/Mac
```

Edit `.env`. Minimum required to get the server running:

```env
# PostgreSQL — used by RAG, memory, and crawl registry
POSTGRES_DB=knowledge_base
POSTGRES_USER=knowledge_base
POSTGRES_PASSWORD=choose_a_strong_password

# OpenAI — required for RAG embeddings
OPENAI_API_KEY=sk-...

# Anthropic — used for research and vision analysis (optional but recommended)
ANTHROPIC_API_KEY=sk-ant-...
```

Additional optional settings in `.env`:

| Variable | When you need it |
|---|---|
| `PERPLEXITY_API_KEY` | `research_deep` tool — multi-source web research |
| `ORACLE_USER` / `ORACLE_PASSWORD` / `ORACLE_DSN` | Oracle DB tools |
| `MEDIAWIKI_*` | MediaWiki integration (run with `--profile mediawiki`) |
| `FIRECRAWL_API_KEY` | Platform docs crawler (run with `--profile platform-docs`) |
| `PGADMIN_EMAIL` / `PGADMIN_PASSWORD` | pgAdmin UI (run with `--profile admin`) |

---

### Step 2 — Start the Docker stack

From the `docker/` directory (recommended — avoids "variable not set" warnings):

```bash
cd docker
docker compose --env-file ../.env up -d
```

Or from repo root:

```bash
docker compose -f docker/docker-compose.yml up -d
```

**What starts:**

| Service | Port | Description |
|---|---|---|
| `trent` MCP server | `8082` | 28 MCP tools + REST admin UI |
| `postgres` | `5433` | PostgreSQL with pgvector |
| `pgadmin` *(optional)* | `8083` | DB admin UI — add `--profile admin` |
| `mediawiki` *(optional)* | `8880` | Wiki — add `--profile mediawiki` |

**Verify the server is up:**

```bash
# Check running containers
docker ps | grep trent

# Check logs (should show "28 plugins loaded")
docker logs trent_rules_docker --tail 30

# Health check
curl http://localhost:8082/health
# PowerShell:
Invoke-WebRequest -Uri "http://localhost:8082/health" -UseBasicParsing
```

**Web UIs (no API key needed):**
- `http://localhost:8082/admin/db` — DB Explorer (browse all Postgres tables)
- `http://localhost:8082/admin/trent` — Task Visualizer (interactive DAG of `.trent/` tasks)
- `http://localhost:8083` — pgAdmin (if started with `--profile admin`)

---

### Step 3 — Connect MCP to your IDE

**Cursor IDE** — add to your project's `.cursor/mcp.json` (or Cursor Settings → MCP → Add):

```json
{
  "mcpServers": {
    "user-trent_rules_docker": {
      "url": "http://localhost:8082/mcp",
      "transport": "streamable-http"
    }
  }
}
```

To verify in Cursor: open the MCP panel and confirm `user-trent_rules_docker` shows as connected with 28 tools.

**Claude Code** — add to `.claude/settings.local.json` in your project:

```json
{
  "mcpServers": {
    "user-trent_rules_docker": {
      "type": "streamable-http",
      "url": "http://localhost:8082/mcp"
    }
  }
}
```

Or via CLI:
```bash
claude mcp add user-trent_rules_docker --transport streamable-http http://localhost:8082/mcp
```

**Verify tools are visible:**
```bash
# Claude Code CLI
claude mcp list
```

---

### Step 4 — Install trent into a new project

With the MCP server connected, open your target project in your IDE and run:

**Cursor:**
```
@trent-setup
```
Or call the MCP tool directly in chat:
```
Use the trent_install tool:
  project_path: "C:/path/to/your/project"
  use_v2: true
```

**Claude Code:**
```
/trent-setup
```

**What `trent_install` creates:**

```
your-project/
├── .trent/
│   ├── TASKS.md                    # Master task list — source of truth
│   ├── PROJECT_CONTEXT.md          # Mission, phase, goals
│   ├── ARCHITECTURE_CONSTRAINTS.md # Non-negotiable decisions
│   ├── PRD.md                      # Product Requirements Document (blank)
│   ├── BUGS.md                     # Bug tracking
│   ├── SUBSYSTEMS.md               # Component registry
│   ├── IDEA_BOARD.md               # Ideas not yet ready for tasks
│   ├── PROJECT_GOALS.md            # Strategic goals (G-01, G-02...)
│   ├── .project_id                 # Unique project ID for memory tools
│   ├── tasks/                      # Individual task files (task001_name.md)
│   └── phases/                     # Phase documentation
├── .cursor/
│   ├── rules/                      # 8 slim always-apply rules
│   ├── agents/                     # 42 on-demand agents
│   ├── skills/                     # 56+ on-demand skills
│   └── commands/                   # 24 @trent-* shortcut commands
├── .claude/
│   ├── rules/                      # Same 8 rules (.md format)
│   ├── agents/                     # Same 42 agents
│   ├── skills/                     # Same 56+ skills
│   └── commands/                   # 24 /trent-* commands
└── .agent/                         # Gemini rules and skills
```

**After install, start planning:**
```
@trent-plan        ← runs the 27-question requirements interview, generates PRD.md
@trent-phase-add   ← define Phase 0 with your first batch of tasks
@trent-task-new    ← create your first task
```

---

### Alternative: Windows Dynamic Links (Single Shared Storage)

Instead of installing a full copy of trent into each project, you can use **Windows Dynamic Links** — junction points that make every project folder point to your single `trent_rules` installation. Any edit to an agent, skill, or rule in one project is instantly reflected in all other projects.

**When to use this approach:**
- You work on many projects on the same Windows machine
- You want agent/skill/rule updates to propagate everywhere immediately — no re-installs
- You're the primary developer and want a single source of truth for all trent configuration

**How it works:**

Copy `windows_dynamic_links.bat` (from the root of this repo) into your project folder and run it as Administrator. It creates Windows junction links for the four trent config directories:

```
your-project/
├── .agent     → G:\trent_rules\.agent     (junction link)
├── .claude    → G:\trent_rules\.claude    (junction link)
├── .cursor    → G:\trent_rules\.cursor    (junction link)
└── .platforms → G:\trent_rules\.platforms (junction link)
```

The junction links behave exactly like real folders — your IDE, git, and all tools see them as local directories. But writes go directly to `trent_rules`, so installing a new skill or editing a rule in any project updates the shared source immediately.

**Steps:**

```bat
REM 1. Copy windows_dynamic_links.bat into your project folder
REM 2. Open a terminal as Administrator
REM 3. Navigate to your project folder
cd C:\path\to\your-project

REM 4. Run the script
windows_dynamic_links.bat
```

**Before running**, open `windows_dynamic_links.bat` and verify the `SHARED` path matches where your `trent_rules` repo lives:

```bat
REM Edit this line to match your actual trent_rules location:
set SHARED=G:\trent_rules
```

> **Note:** Junction links are Windows-only (`mklink /J`). On Linux/Mac, use `ln -s` to create equivalent symbolic links. Junction links are not followed by git — your project repo stays clean.

**Trade-offs vs. standard install:**

| | Standard Install (`trent_install`) | Dynamic Links |
|---|---|---|
| Updates | Re-run `trent_install` to get new agents/skills | Instant — edits in any project apply everywhere |
| Project isolation | Each project has its own copy | All projects share one copy |
| Works on | All platforms | Windows only (junction links) |
| Teammate compatibility | ✅ They get their own copy | ❌ Only works on machines with same drive layout |

---

## Commands — Full Reference

Commands use `@trent-` prefix in Cursor, `/trent-` in Claude Code. All 24 commands:

### Project Setup

| Command | What it does | Example |
|---|---|---|
| `@trent-setup` | Initialize `.trent/` folder structure in a new project. Detects if project already exists and protects existing data. | `@trent-setup` |
| `@trent-plan` | Run the 27-question requirements interview and generate a full PRD. Covers users, scale, security, deployment, constraints. | `@trent-plan I want to build a multi-tenant API` |
| `@trent-status` | Session start command — loads project goals, current phase, active tasks, and blockers. | `@trent-status` |

### Task Management

| Command | What it does | Example |
|---|---|---|
| `@trent-task-new` | Create a new task with full YAML spec (id, title, priority, subsystems, acceptance criteria, verification steps). | `@trent-task-new add JWT auth to the API` |
| `@trent-task-update` | Update a task's status, add evidence, or change priority. Atomically updates both task file and TASKS.md. | `@trent-task-update task 42 is done, here's the test output` |
| `@trent-task-sync-check` | Validate that TASKS.md entries and `.trent/tasks/` files are in sync. Detects orphans and phantoms. | `@trent-task-sync-check` |
| `@trent-workflow` | Assess task complexity, expand complex tasks into sub-tasks, run sprint planning, visualize Kanban flow. | `@trent-workflow` |

### Phase Management

| Command | What it does | Example |
|---|---|---|
| `@trent-phase-add` | Add a new phase — atomically creates the TASKS.md header AND the `.trent/phases/phaseN_name.md` file. | `@trent-phase-add Phase 2: Core API` |
| `@trent-phase-pivot` | Pivot to a new direction — marks old phase as paused, creates new phase with pivot reason recorded. | `@trent-phase-pivot we're switching from REST to GraphQL` |
| `@trent-phase-sync-check` | Validate that TASKS.md phase headers and `.trent/phases/` files are in sync. | `@trent-phase-sync-check` |

### Quality & Review

| Command | What it does | Example |
|---|---|---|
| `@trent-review` | Comprehensive code review — security vulnerabilities, performance, reusability, code duplication. | `@trent-review` (with files open) |
| `@trent-qa` | Activate quality assurance — runs quality checklist, checks for code smells, validates test coverage. | `@trent-qa` |
| `@trent-qa-report` | Generate quality metrics report — bug counts by severity, resolution rates, phase health. | `@trent-qa-report` |
| `@trent-bug-report` | Log a bug to BUGS.md with severity classification, reproduction steps, and a linked task. | `@trent-bug-report the login endpoint returns 500 when email has a + sign` |
| `@trent-bug-fix` | Document a bug fix — updates BUGS.md status, closes the task, records the resolution. | `@trent-bug-fix BUG-007` |

### Git

| Command | What it does | Example |
|---|---|---|
| `@trent-git-commit` | Create a well-structured git commit following trent conventions with task references. | `@trent-git-commit` |

### Ideas & Goals

| Command | What it does | Example |
|---|---|---|
| `@trent-idea-capture` | Immediately capture an idea to IDEA_BOARD.md. Triggered by "make a note of that", "someday...", etc. | `@trent-idea-capture add dark mode someday` |
| `@trent-idea-review` | Review and evaluate IDEA_BOARD entries — change status, promote to tasks, shelve stale ideas. | `@trent-idea-review` |
| `@trent-goal-update` | Create or update PROJECT_GOALS.md with strategic goals tied to success metrics. | `@trent-goal-update` |

### Autonomous Operations

| Command | What it does | Example |
|---|---|---|
| `@trent-sprint` | Run a 2-hour autonomous sprint — reads SPRINT.md, claims tasks, implements, sets to awaiting-verification. | `@trent-sprint` |
| `@trent-cleanup` | Nightly housekeeping — resets stale TTL claims, regenerates SPRINT.md and ACTIVE_BACKLOG.md, computes health score. | `@trent-cleanup` |

### External Sources

| Command | What it does | Example |
|---|---|---|
| `@trent-harvest` | Analyze an external repo, article, or video and present a menu of ideas to selectively adopt. Nothing is changed without your approval. | `@trent-harvest https://github.com/some/project` |
| `@trent-analyze-codebase` | Deep merge two of YOUR OWN projects — full architecture mapping, comparison, integration plan. | `@trent-analyze-codebase` |
| `@trent-issue-fix` | Fix a GitHub issue — reads the issue, creates a task, implements the fix. | `@trent-issue-fix #42` |

---

## Agents — Full Reference

Agents are loaded on-demand — they only use context when active. 42 agents total.

### trent System Agents (19)

These activate automatically when you run trent commands or describe a trent-related task.

| Agent | Activates when... |
|---|---|
| `trent-task-manager` | Creating, updating, completing, or querying tasks in `.trent/` |
| `trent-planner` | Creating PRDs, adding phases, pivoting direction, defining subsystems |
| `trent-qa-engineer` | Reporting bugs, tracking issues, documenting fixes, managing BUGS.md |
| `trent-verifier` | Verifying completed tasks — two-stage: spec compliance then code quality |
| `trent-workflow-manager` | Expanding complex tasks into sub-tasks, scoring complexity, planning sprints |
| `trent-code-reviewer` | Security audits, performance reviews, code quality, running `@trent-review` |
| `trent-autonomous` | Running autonomous sprint execution, nightly cleanup, managing task TTL/claims |
| `trent-platform-parity` | Syncing rules/agents/skills across `.cursor/`, `.claude/`, `.agent/` |
| `trent-ideas-goals` | Capturing ideas to IDEA_BOARD.md, updating PROJECT_GOALS.md |
| `trent-python-dev` | Working on Python projects, setting up UV virtual environments |
| `trent-project-manager` | Setting up trent in new projects, grooming `.trent/` files, fixing placeholders |
| `trent-memory` | Capturing session memory for Gemini/VS Code sessions |
| `trent-infrastructure` | Organizing project files, scope boundaries, preventing over-engineering |
| `trent-multi-agent` | Coordinating parallel agents, setting up git worktrees |
| `trent-self-improvement` | Auditing the trent system for inconsistencies, proposing improvements |
| `trent-task-expander` | Assessing task complexity, expanding complex tasks into sub-tasks |
| `trent-project-files` | Updating AGENTS.md/CLAUDE.md after phase changes or new MCP tools |
| `trent-cursor-cli` | Running Cursor CLI commands, using the `agent` terminal command |
| `trent-claude-cli` | Running Claude Code CLI commands, managing MCP servers from CLI |

### General Development Agents (23)

| Agent | Role |
|---|---|
| `backend-developer` | API design, microservices, server-side logic, database integration |
| `frontend-developer` | React, TypeScript, UI components, responsive design |
| `full-stack-developer` | End-to-end features across frontend and backend |
| `api-designer` | REST/GraphQL API design, versioning, documentation |
| `solution-architect` | High-level system design, technology selection, scalability |
| `code-reviewer` | Comprehensive code review — quality, security, best practices |
| `qa-engineer` | Test planning, manual testing, bug tracking, quality metrics |
| `orchestrator` | Coordinates parallel execution of multiple subagents |
| `agent-creator` | Designing new AI agent definitions for Cursor/Claude |
| `skill-creator` | Designing new skill definitions |
| `cursor-config-maintainer` | Maintaining `.cursor/` project configuration |
| `claude-config-maintainer` | Maintaining `.claude/` project configuration |
| `cursor-cli` | Cursor CLI operations, Cloud Agent handoff |
| `claude-cli` | Claude Code CLI, headless/CI pipelines |
| `mlops-engineer` | ML operations, model deployment, training pipelines |
| `ai-model-developer` | AI/ML model development |
| `ai-model-trainer` | Model training and fine-tuning |
| `harvest-analyst` | Harvesting ideas from external sources (read-only, no auto-changes) |
| `codebase-analyst` | Deep merge of your own projects, architecture mapping |
| `trent-codebase-analyst` | Analyzing external codebases for integration |
| `trent-planner` *(alias)* | Planning questionnaire and PRD generation |
| `silicon-valley-superfan` | HBO Silicon Valley show knowledge base (trivia, character arcs) |
| `trent-project-initializer` | Project scaffolding and initial setup |

---

## Skills — Full Reference

Skills are explicit workflow invocations — they provide deep procedural knowledge for a specific task. 56+ skills total. Zero context cost when not active.

### trent Workflow Skills (32)

| Skill | What it provides |
|---|---|
| `trent-task-management` | Task lifecycle, status enforcement, YAML schema, sync rules |
| `trent-task-new` | Step-by-step: create task file + TASKS.md entry atomically |
| `trent-task-update` | Step-by-step: update status in task file + TASKS.md atomically |
| `trent-task-sync-check` | Detect and fix orphans/phantoms between TASKS.md and task files |
| `trent-planning` | PRD creation, phase management, subsystems documentation |
| `trent-plan` | Full 27-question requirements interview workflow |
| `trent-phase-add` | Add a new phase atomically (TASKS.md header + phase file) |
| `trent-phase-pivot` | Pivot workflow — pause old phase, create new with pivot reason |
| `trent-phase-sync-check` | Validate TASKS.md phase headers vs `.trent/phases/` files |
| `trent-phase-archive` | Archive completed phase task files into `phases/phaseN/` subfolder |
| `trent-setup` | Initialize trent in a new project — create all `.trent/` files |
| `trent-status` | Session start: load context, phase, goals, active tasks |
| `trent-grooming` | Heal `.trent/` files — fix placeholders, sync TASKS.md, validate YAML |
| `trent-qa` | Quality assurance workflow — bug lifecycle, quality gates |
| `trent-bug-report` | Document a new bug in BUGS.md + create linked task |
| `trent-bug-fix` | Fix workflow — update BUGS.md status + close task |
| `trent-qa-report` | Generate quality metrics — bug counts, resolution rates |
| `trent-review` | Comprehensive code review (security, perf, reusability) |
| `trent-code-reviewer` | Deep code review following trent standards |
| `trent-workflow` | Task complexity scoring, sub-task expansion, sprint planning |
| `trent-sprint` | Autonomous 2-hour sprint — claim, implement, verify tasks |
| `trent-cleanup` | Nightly cleanup — TTL resets, SPRINT.md, ACTIVE_BACKLOG.md, health score |
| `trent-git-commit` | Well-structured commits with task references and agent footers |
| `trent-ideas-goals` | IDEA_BOARD.md and PROJECT_GOALS.md management |
| `trent-idea-capture` | Immediately capture an idea (triggered by "make a note of that") |
| `trent-idea-review` | Review and evaluate IDEA_BOARD entries |
| `trent-goal-update` | Create or update PROJECT_GOALS.md |
| `trent-harvest` | Selective harvest from external sources — present menu, nothing auto-applied |
| `trent-visualizer` | Open task dependency DAG at `/admin/trent` |
| `trent-task-management` *(alias)* | Full task system reference |
| `trent-ideas-goals` *(alias)* | Ideas and goals reference |
| `youtube-video-analysis` | Download, transcribe, analyze YouTube videos via MCP tools |

### Development Skills (12)

| Skill | What it provides |
|---|---|
| `trent-planning` | Planning questionnaire, PRD template, phase conventions |
| `ai-ml-development` | AI/ML model training, RLHF, deployment, MLOps |
| `github-integration` | GitHub workflows, issues, PRs, releases, API operations |
| `mcp-builder` | Build MCP servers in Python (FastMCP) or Node/TypeScript |
| `claude-code-project-config` | Maintain `.claude/` project configuration |
| `cursor-project-config` | Maintain `.cursor/` project configuration |
| `claude-cli` | Claude Code CLI reference — flags, headless mode, Agent SDK |
| `cursor-cli` | Cursor CLI reference — agent command, modes, Cloud Agents |
| `codebase-integration-analysis` | Deep merge your own projects — architecture mapping |
| `selective-harvest` | Analyze external sources, present selective improvement menu |
| `project-setup` | Initialize new project structure and documentation |
| `skill-creator` | Create new skills for Cursor/Claude |
| `agent-creator` | Create new agent definitions for Cursor/Claude |
| `silicon-valley-superfan` | HBO Silicon Valley knowledge base |

### Creative / Video / 3D Skills (13)

| Skill | What it provides |
|---|---|
| `ai-video-generation` | Generate AI videos — text-to-video, image-to-video, 40+ models |
| `ai-avatar-lipsync` | Create talking head videos with audio-driven lipsync |
| `manim-animation` | Python mathematical animation with Manim Community |
| `remotion-video` | Programmatic video creation with React/Remotion |
| `animated-gif-creator` | Optimized animated GIF creation with composable animations |
| `explainer-video` | Explainer video production — script formulas, pacing, storyboarding |
| `storyboard-creation` | Film storyboarding — shot vocabulary, camera angles |
| `animation-principles` | The 12 Disney animation principles for interactive/UI animation |
| `algorithmic-art` | Generative art with p5.js — seeded randomness, flow fields |
| `3d-performance` | 3D web scene optimization — LOD strategies, frustum culling |
| `asset-optimization` | 3D asset optimization pipeline using gltf-transform |
| `video-ad-specs` | Platform-specific video ad specs with AIDA framework |
| `pipeline-validation` | Multi-agent validation gates for animation/video production |

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
# --- Start ---
cd docker

# Core stack (MCP + Postgres)
docker compose --env-file ../.env up -d

# With pgAdmin database UI
docker compose --env-file ../.env --profile admin up -d

# With MediaWiki
docker compose --env-file ../.env --profile mediawiki up -d

# With Firecrawl platform docs crawler
docker compose --env-file ../.env --profile platform-docs up -d

# All profiles
docker compose --env-file ../.env --profile admin --profile mediawiki --profile platform-docs up -d

# --- Monitor ---
docker ps                                          # List running containers
docker logs trent_rules_docker --tail 30          # View MCP server logs
docker logs trent_rules_docker -f                 # Follow logs live

# --- Rebuild after code changes ---
docker compose --env-file ../.env up -d --build trent

# --- Database ---
# Apply a new SQL migration
docker exec -i trent_rules_postgres psql -U knowledge_base -d knowledge_base < docker/init_db/09_migration.sql

# Open psql shell
docker exec -it trent_rules_postgres psql -U knowledge_base -d knowledge_base

# --- Stop ---
docker compose down                  # Stop, keep data
docker compose down -v               # Stop and DELETE all data (destructive)
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
