# agents.md - trent

> **AI Development System for Cursor IDE & Claude Code**
> This file follows the agents.md format for AI agent instructions.
> Compatible with both Cursor (`.cursor/`) and Claude Code (`.claude/`).

---

## 📋 Project Overview

**trent** - A comprehensive AI-powered development system

**Purpose**: Provide a unified development environment for **Cursor IDE** and **Claude Code** with extensive agent capabilities, skills, and task management.

**Core Features**:
- **Task Management**: Create, track, and complete tasks with status tracking
- **Project Planning**: PRD creation, feature specifications, scope management
- **Quality Assurance**: Bug tracking, severity classification, resolution tracking
- **Specialized Agents**: 50+ agents for different development roles
- **Development Skills**: 49+ skills covering databases, DevOps, research, and more
- **Dual IDE Support**: Full parity between `.cursor/` and `.claude/` configurations

---

## 📁 Project Structure

```
.trent/                        # Core task management (READ THIS FIRST)
├── PLAN.md                    # Product Requirements Document
├── TASKS.md                   # Master task checklist with status
├── BUGS.md                    # Bug tracking
├── PROJECT_CONTEXT.md         # Project mission and goals
├── SUBSYSTEMS.md              # Component registry
├── tasks/                     # Individual task files (task{id}_name.md)
└── templates/                 # Task/plan templates

.cursor/                       # Cursor IDE configuration
├── skills/                    # 49+ AI Skills
├── agents/                    # 52+ Specialized agents
│   └── sdk/                   # Agent SDK & primitives
├── rules/                     # .mdc format rules (trent core: 10-19)
├── commands/                  # 25 @trent-* and @sv-* commands
└── hooks/                     # PowerShell automation hooks

.claude/                       # Claude Code configuration (parity with .cursor/)
├── skills/                    # 49+ AI Skills (same as .cursor/)
├── agents/                    # 52+ Specialized agents (same as .cursor/)
├── rules/                     # .md format rules (same content, .md extension)
├── commands/                  # 25 /trent-* and /sv-* commands
├── hooks/                     # PowerShell automation hooks
├── hooks.json                 # Hook event configuration
└── settings.local.json        # MCP and permissions config

docker/                        # MCP Server (Docker)
├── trent/                     # Main server code + plugins
├── fstrent_mcp_video_analyzer/ # Video analysis MCP
└── docker-compose.yml

templates/                     # Install templates (trent-only, canonical source)
templates_full/                # Full install templates (all skills/agents)

docs/                          # Project documentation
```

---

## 🤖 Available Agents

### Core Development Agents

| Agent | Description | Best For |
|-------|-------------|----------|
| `backend-developer` | API design, server logic, database integration | Backend APIs, business logic |
| `frontend-developer` | React, TypeScript, UI components | User interfaces, responsive design |
| `full-stack-developer` | End-to-end implementation | Complete features |
| `database-expert` | Schema design, query optimization | Database work |
| `api-designer` | REST/GraphQL API design | API contracts |

### DevOps & Infrastructure

| Agent | Description | Best For |
|-------|-------------|----------|
| `cloud-engineer` | Cloud architecture and services | Cloud infrastructure |
| `devops-engineer` | CI/CD, infrastructure as code | Deployment automation |
| `docker-specialist` | Containerization, Docker Compose | Container optimization |
| `kubernetes-specialist` | K8s cluster management, Helm | Kubernetes operations |
| `portainer-specialist` | Container management UI | Portainer management |
| `cicd-specialist` | Pipeline automation | CI/CD pipelines |
| `solution-architect` | System architecture, tech selection | Architectural decisions |
| `security-auditor` | Vulnerability assessment, compliance | Security reviews |

### Quality & Testing

| Agent | Description | Best For |
|-------|-------------|----------|
| `test-runner` | Automated testing, fix failures | Running and fixing tests |
| `qa-engineer` | Test planning, quality metrics | Quality assurance |
| `code-reviewer` | Code quality, best practices | Code reviews |
| `debugger` | Error diagnosis, root cause analysis | Debugging issues |

### Specialized Agents

| Agent | Description | Best For |
|-------|-------------|----------|
| `orchestrator` | Multi-agent coordination | Complex multi-agent tasks |
| `agent-creator` | Create new agent definitions | Meta/system |
| `skill-creator` | Create new skill definitions | Meta/system |
| `trent-project-initializer` | Project setup | Scaffolding |
| `trent-task-expander` | Task breakdown, complexity assessment | Task decomposition |
| `codebase-analyst` | Deep merge your own projects | Project integration |
| `harvest-analyst` | Harvest ideas from external sources | Selective improvements |
| `claude-cli` | Claude CLI operations | IDE automation |
| `cursor-cli` | Cursor CLI operations | IDE automation |
| `accounting-finance-specialist` | Financial operations | Accounting |
| `mlops-engineer` | ML operations | ML pipelines |
| `sales-marketing-specialist` | Sales and marketing | Go-to-market |
| `silicon-valley-superfan` | HBO Silicon Valley expert | Show trivia and references |
| `startup-formation-specialist` | Business formation | Entity setup |
| `startup-operations-specialist` | Operations | Business ops |
| `technical-writer` | Documentation, API docs | Technical documentation |
| `video-producer` | Video production | Media content |

---

## 🛠️ Available Skills

### Core Task Management
- `trent-task-management` - Task lifecycle and status management
- `trent-planning` - PRD creation, phase management, and project planning
- `trent-qa` - Bug tracking and quality assurance
- `trent-code-reviewer` - Comprehensive code reviews

### Database Development
- `hanx-database-tools` - MySQL database operations

### Research & Documentation
- `research-methodology` - Systematic research approaches
- `deep-research` - Comprehensive research with analysis

### Integration & Tools
- `github-integration` - GitHub workflows and automation
- `atlassian-integration` - Jira/Confluence integration
- `web-tools` - Web browsing and search
- `mcp-builder` - MCP server development
- `rag-mcp-server` - RAG knowledge base integration

### Business & Startup
- `startup-resource-access` - Grants, accelerators, resources
- `startup-vc-fundraising` - Fundraising and pitch decks
- `startup-product-development` - Product development lifecycle
- `patent-filing-ai` - Patent documentation assistance

### DevOps & Infrastructure
- `cicd-pipelines` - CI/CD pipeline creation and management
- `cloud-engineering` - Cloud architecture and IaC
- `kubernetes-operations` - K8s cluster management
- `portainer-management` - Container management UI

### Document Skills
- `document-skills/docx` - Word document creation and editing
- `document-skills/pdf` - PDF manipulation and analysis
- `document-skills/pptx` - Presentation creation
- `document-skills/xlsx` - Spreadsheet operations

### Codebase Analysis
- `codebase-integration-analysis` - Deep project merging and architecture mapping
- `selective-harvest` - Harvest improvements from external sources

### Utilities
- `project-setup` - Project initialization
- `skill-creator` - Create new skills
- `agent-creator` - Create new agent definitions
- `template-skill` - Skill creation template
- `internal-comms` - Internal communications
- `computer-use-agent` - Desktop automation
- `artifacts-builder` - Complex HTML artifact creation
- `automatic-rag-checking` - Automatic RAG validation
- `silicon-valley-superfan` - HBO Silicon Valley knowledge base

---

## MCP Tools (Docker Server)

| Tool | Description |
|------|-------------|
| `oracle_query` | Read-only SQL on Oracle (SELECT, DESCRIBE) |
| `oracle_execute` | Write SQL on Oracle (INSERT, UPDATE, DDL) |
| `md_to_html` | Convert markdown to styled HTML |
| `trent_install` | Install full trent environment to a project |
| `trent_rules_update` | Update IDE configs/rules (preserves .trent/ task data) |
| `trent_plan_reset` | Reset .trent/ to blank template (requires confirm=True) |
| `trent_server_status` | Health check |

---

## ✅ Task Management

### Task File Format

```yaml
---
id: {number}
title: 'Task Title'
type: feature|bug_fix|refactor|documentation
status: pending|in_progress|completed|failed
priority: critical|high|medium|low
phase: 0
subsystems: [affected_components]
project_context: How this task relates to project goals
dependencies: [other_task_ids]
---

# Task: {title}

## Objective
[Clear, actionable goal]

## Acceptance Criteria
- [ ] Specific outcome 1
- [ ] Specific outcome 2
```

### Task Status Indicators (Windows-Safe)

- `[ ]` - Pending (not started)
- `[📋]` - Ready (task file created)
- `[🔄]` - In Progress
- `[✅]` - Completed
- `[❌]` - Failed/Cancelled

### Phase-Based Task Numbering

| Phase | Task ID Range | Purpose |
|-------|---------------|---------|
| Phase 0 | 1-99 | Setup, infrastructure |
| Phase 1 | 100-199 | Foundation, database |
| Phase 2 | 200-299 | Core development |
| Phase N | N×100 to N×100+99 | Custom phases |

---

## 🚨 Direct Edit Policy

**CRITICAL**: The following files should be edited DIRECTLY without asking for permission:

### Files to Edit Freely
- `.trent/PLAN.md` - Product Requirements
- `.trent/TASKS.md` - Task checklist
- `.trent/BUGS.md` - Bug tracking
- `.trent/PROJECT_CONTEXT.md` - Project mission
- All files in `.trent/tasks/`
- All files in `.trent/phases/`

**Why?** These are working files, not user source code. Edit them directly without confirmation prompts.

---

## 🔧 Commands

Commands use the `trent-` prefix.

### All Commands

| Command | Description |
|---------|-------------|
| `trent-bug-report` | Report/document a bug |
| `trent-bug-fix` | Fix a reported bug |
| `trent-git-commit` | Create well-structured commits |
| `trent-issue-fix` | Fix GitHub issue |
| `trent-phase-add` | Add new project phase |
| `trent-phase-pivot` | Pivot project direction |
| `trent-phase-sync-check` | Validate phase synchronization |
| `trent-plan` | Create PRD and project planning |
| `trent-qa` | Quality assurance activation |
| `trent-qa-report` | Generate quality metrics |
| `trent-plan` | Create PRD and project planning |
| `trent-review` | Comprehensive code review |
| `trent-setup` | Initialize trent system |
| `trent-status` | Project status overview |
| `trent-task-new` | Create a new task |
| `trent-task-sync-check` | Validate task synchronization |
| `trent-task-update` | Update task status |
| `trent-workflow` | Task expansion, sprint planning |
| `trent-analyze-codebase` | Deep merge your own projects |
| `trent-harvest` | Harvest ideas from external sources |
| `trent-idea-capture` | Capture an idea to IDEA_BOARD.md |
| `trent-idea-review` | Review and evaluate IDEA_BOARD entries |
| `trent-goal-update` | Create or update PROJECT_GOALS.md |

### Usage
- **Cursor**: `@trent-setup`, `@trent-task-new`, etc. (commands in `.cursor/commands/`)
- **Claude Code**: `/trent-setup`, `/trent-task-new`, etc. (commands in `.claude/commands/`)

---

## 📝 Code Style Guidelines

### Python (PEP 8)
- Use black formatter (88-100 char line length)
- Add type hints where possible
- Write comprehensive docstrings

### JavaScript/React
- Use ESLint + Prettier
- Functional components with hooks
- TypeScript when available

---

## 📊 Documentation Standards

### File Naming Convention

**Format**: `YYYYMMDD_HHMMSS_Cursor_TOPIC_NAME.md`

**Example**: `docs/20260126_143000_Cursor_PROJECT_SETUP.md`

### File Location Rules

- **docs/** - All documentation except core planning
- **Project root** - Only README.md, LICENSE, CHANGELOG.md, AGENTS.md, CLAUDE.md
- **.trent/** - Only core planning documents

---

## 📋 Quick Reference

### When Starting Work
1. Read `.trent/PROJECT_CONTEXT.md`
2. Check `.trent/TASKS.md` for current tasks
3. Create task file before starting work

### When Completing Work
1. Update task file status to `completed`
2. Update TASKS.md status to `[✅]`
3. Commit changes

### Using Parallel Agents
- Use 3-5 agents in parallel for optimal performance
- Only parallelize independent tasks
- Each agent type can only have one active instance
- Define clear boundaries for each agent

---

<!-- NOTE: This is the SOURCE REPOSITORY for trent -->
<!-- The entire file documents the trent system itself -->
<!-- For projects USING trent, templates are in /templates/ and /templates_full/ -->
<!-- Both .cursor/ and .claude/ directories maintain full parity -->

---

## 🔒 Security

- Never commit API keys, tokens, or passwords
- Use environment variables for secrets
- Always use parameterized queries for databases
- Validate all user input

---

**Version**: 4.1.0
**Last Updated**: 2026-02-19
**Supported IDEs**: Cursor IDE (`.cursor/`), Claude Code (`.claude/`)
**Platform Parity**: Agents, skills, commands, and hooks are identical between both IDEs
