# trent

## AI Development System for Cursor IDE

**AI-powered task management and development tools for Cursor IDE and Claude Code.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](#)

---

## What is trent?

**trent** is a file-based task management and AI development system designed for Cursor IDE. It provides:

- **Task Management** - File-based tracking with enforced workflows
- **34+ AI Agents** - Specialized agents for backend, frontend, DevOps, QA, and more
- **29+ AI Skills** - CI/CD, cloud, document manipulation, research, and more
- **Oracle Database Tools** - Query and execute via MCP (no API keys needed)
- **Project Planning** - PRDs, phases, and quality assurance

### How It Works

```
+---------------------------------------------------------+
|            .trent/ (Task Data)                          |
|  +-- PLAN.md        (Product Requirements)              |
|  +-- TASKS.md       (Master task list)                  |
|  +-- BUGS.md        (Bug tracking)                      |
|  +-- tasks/         (Individual task files)              |
+---------------------------------------------------------+
                          ^
                          |
                   +------v------+
                   |   Cursor    |
                   |    IDE      |
                   |  .cursor/   |
                   |   rules/    |
                   |   skills/   |
                   |   agents/   |
                   +------+------+
                          |
                   +------v------+
                   |   Docker    |
                   |  MCP Server |
                   |  (Oracle,   |
                   |   md_to_html)|
                   +-------------+
```

---

## Quick Start

See **[CURSOR_SETUP.md](CURSOR_SETUP.md)** for complete setup instructions.

### TL;DR

```bash
# 1. Clone
git clone <repo-url> trent_rules
cd trent_rules

# 2. Start Docker MCP server
cd docker && docker-compose up -d

# 3. Add to Cursor MCP settings
# { "mcpServers": { "trent": { "url": "http://localhost:8084/mcp" } } }

# 4. Use in Cursor chat
# @trent-status
```

---

## Project Structure

```
trent_rules/
├── .cursor/              # AI configuration (auto-loaded by Cursor)
│   ├── agents/           # 34+ specialized agents
│   ├── skills/           # 29+ AI skills
│   ├── rules/            # 25 rules (.mdc format)
│   ├── commands/         # 19 @trent-* commands
│   └── hooks/            # PowerShell hooks
├── .trent/               # Task management data
│   ├── PLAN.md           # Product Requirements Document
│   ├── TASKS.md          # Master task list (source of truth)
│   ├── BUGS.md           # Bug tracking
│   ├── PROJECT_CONTEXT.md # Project mission
│   ├── SUBSYSTEMS.md     # Component registry
│   ├── tasks/            # Individual task files
│   └── phases/           # Phase documentation
├── docker/               # MCP server (single Docker container)
├── docs/                 # Project documentation
├── AGENTS.md             # AI agent instructions
├── CLAUDE.md             # Claude-specific context
├── CURSOR_SETUP.md       # Setup guide
├── LICENSE               # Apache 2.0
└── NOTICE                # Attribution
```

---

## Features

### Task Management
- Create, update, and track tasks with enforced status progression
- Priority levels (Critical, High, Medium, Low)
- Task dependencies and sub-tasks
- Automatic task expansion for complex work
- Phase-based task numbering (Phase N = IDs N*100 to N*100+99)

### Project Planning
- Product Requirements Documents (PRD)
- Feature specifications and user stories
- Phase management with pivot support
- Scope validation and over-engineering prevention

### Bug Tracking
- Centralized bug tracking in BUGS.md
- Severity classification (Critical/High/Medium/Low)
- Bug-to-task relationships
- Resolution tracking through task completion

### Quality Assurance
- Comprehensive code review agents
- Test runner integration
- Quality metrics and reporting

---

## MCP Tools

The Docker MCP server provides these tools (no API keys required):

| Tool | Description |
|------|-------------|
| `oracle_query` | Read-only SQL queries on Oracle databases |
| `oracle_execute` | Write operations on Oracle (INSERT, UPDATE, DDL) |
| `md_to_html` | Convert markdown to styled, self-contained HTML |
| `trent_server_status` | Health check |

---

## Specialized Agents

| Agent | Description |
|-------|-------------|
| `backend-developer` | API design, server logic |
| `frontend-developer` | React, TypeScript, UI |
| `full-stack-developer` | End-to-end features |
| `database-expert` | Schema design, queries |
| `devops-engineer` | CI/CD, infrastructure |
| `docker-specialist` | Containerization |
| `kubernetes-specialist` | K8s management |
| `security-auditor` | Security reviews |
| `code-reviewer` | Code quality |
| `orchestrator` | Multi-agent coordination |
| ... and 24+ more! | |

---

## Key Commands

Use these in Cursor chat with `@` prefix:

| Command | Description |
|---------|-------------|
| `@trent-status` | Project status overview |
| `@trent-task-new` | Create a new task |
| `@trent-task-update` | Update task status |
| `@trent-plan` | Project planning |
| `@trent-review` | Code review |
| `@trent-qa` | Quality assurance |
| `@trent-git-commit` | Structured git commits |
| `@trent-workflow` | Task expansion, sprint planning |
| `@trent-analyze-codebase` | Deep merge your own projects |
| `@trent-harvest` | Harvest ideas from external sources |

See `cursor_inventory.txt` for the complete list of all items.

---

## Team Collaboration

### Git Workflow

```bash
# Initial setup
git add .trent/ .cursor/
git commit -m "Add trent system"
git push

# Daily workflow
git pull                    # Get latest changes
# Work on tasks in Cursor
git add .trent/             # Stage task changes
git commit -m "Update tasks"
git push
```

---

## Use Cases

### Solo Developer
Install in all projects. All planning stays consistent across projects.

### Small Team
Everyone uses Cursor with the same configuration. All work tracked in shared `.trent/` files.

---

## Documentation

- **[CURSOR_SETUP.md](CURSOR_SETUP.md)** - Setup guide for new users
- **[AGENTS.md](AGENTS.md)** - Full agent/skill/command reference
- **[CLAUDE.md](CLAUDE.md)** - Claude-specific project context
- **[cursor_inventory.txt](cursor_inventory.txt)** - Complete inventory

---

## License

Copyright 2025-2026 Warren R. Martel III. All rights reserved.

Licensed under the MIT License. See [LICENSE](LICENSE) for full terms and [NOTICE](NOTICE) for attribution.
