# CLAUDE.md - trent

## Project Overview
trent is a comprehensive AI-powered task management and development system for Cursor IDE and Claude Code. It provides structured task tracking, project planning, quality assurance, and workflow management through a file-based system with enforced synchronization.

## Tech Stack
- **Rules**: Cursor `.mdc` format (Markdown Cursor) - Claude Code reads this CLAUDE.md instead
- **Skills**: Markdown with YAML frontmatter in `.cursor/skills/`
- **Agents**: Markdown in `.cursor/agents/`
- **MCP Server**: Python with FastMCP, PostgreSQL/pgvector for RAG, Oracle support
- **Task Files**: Markdown with YAML frontmatter
- **Package Management**: UV for Python

## Key Directories
```
.cursor/                # Cursor IDE configuration
├── rules/              # .mdc rule files (trent core: 10-19)
├── skills/             # 35+ AI skill definitions
├── agents/             # 25+ Specialized agent definitions
├── commands/           # 19 @trent-* commands
└── hooks/              # PowerShell automation hooks

.claude/                # Claude Code configuration
└── settings.local.json # MCP and permissions config

.trent/                 # Task management data
├── PLAN.md             # Product Requirements Document
├── TASKS.md            # Master task list (source of truth)
├── PROJECT_CONTEXT.md  # Project mission and goals
├── SUBSYSTEMS.md       # Component registry
├── tasks/              # Individual task files
└── phases/             # Phase documentation

docker/                 # MCP server (Docker)
├── trent/              # Main MCP server code
├── fstrent_mcp_video_analyzer/  # Video analysis MCP
└── templates*/         # Installation templates

docs/                   # Project documentation
temp_scripts/           # Test and utility scripts
```

## Development Commands
```bash
# Start MCP server (Docker)
cd docker && docker-compose up -d

# Check MCP server status
docker ps | grep trent

# View MCP logs
docker logs trent -f

# Rebuild after changes
cd docker && docker-compose up -d --build trent
```

## MCP Tools Available
| Tool | Description |
|------|-------------|
| `rag_search` | Semantic search in knowledge base |
| `rag_ingest_text` | Add content to knowledge base |
| `rag_list_subjects` | List available knowledge bases |
| `research_deep` | Comprehensive research with Perplexity |
| `research_search` | Web search for research |
| `oracle_query` | Read-only SQL on Oracle |
| `oracle_execute` | Write SQL on Oracle |
| `mediawiki_page` | MediaWiki CRUD operations |
| `mediawiki_search` | Search MediaWiki |
| `install_trent` | Install trent templates |
| `md_to_html` | Convert markdown to HTML |
| `video_analyze` | Full YouTube video analysis |
| `video_extract_transcript` | Extract video transcripts |

---

## Response Format Requirements

**Include in EVERY response footer:**
```
---
2026-02-01 09:45 UTC
Model: Claude Opus 4, Tokens: ~12,500 input / ~800 output, Est. Cost: ~$0.16
Context: 45% used (Rules: ~15%, MCP: ~8%, Conversation: ~18%, Skills/Other: ~4%)
Tools: Shell, Read, StrReplace
---
```

**File Size Warnings:**
- 800+ lines: Suggest refactoring
- 900+ lines: Insist on refactoring  
- 1000+ lines: Strongly insist on refactoring

**Python Projects:** Always use UV for virtual environment management

---

## CRITICAL: Task Management Rules

### Direct Edit Policy
**EDIT THESE FILES DIRECTLY WITHOUT ASKING PERMISSION:**
- `.trent/PLAN.md` - Product Requirements
- `.trent/TASKS.md` - Task checklist  
- `.trent/BUGS.md` - Bug tracking
- `.trent/PROJECT_CONTEXT.md` - Project mission
- `.trent/SUBSYSTEMS.md` - Component registry
- All files in `.trent/tasks/`
- All files in `.trent/phases/`

These are working files, not user source code. Edit them directly without confirmation prompts.

### Task Status Indicators
- `[ ]` - Pending (no task file yet) - **BLOCKED, DO NOT START**
- `[📋]` - Ready (task file created) - **CAN PROCEED**
- `[🔄]` - In Progress (actively working)
- `[✅]` - Completed
- `[❌]` - Failed/Cancelled
- `[⏸️]` - Paused

### Task Status Progression (ENFORCED)
```
CORRECT: [ ] → [📋] → [🔄] → [✅]
WRONG:   [ ] → [🔄]  (VIOLATION - no file created!)
```

**Before changing `[ ]` to `[📋]`:**
1. Create detailed task file in `.trent/tasks/`
2. Include YAML frontmatter
3. Complete all required sections
4. File naming: `taskXXX_description.md` (NO underscore after "task")

### Phase-Based Task Numbering
| Phase | Task ID Range | Purpose |
|-------|---------------|---------|
| Phase 0 | 1-99 | Setup, infrastructure |
| Phase 1 | 100-199 | Foundation, database |
| Phase 2 | 200-299 | Core development |
| Phase 3 | 300-399 | Enhancement |
| Phase N | N×100 to N×100+99 | Custom phases |

### Atomic Updates (MANDATORY)
When changing task status, update BOTH files in the SAME response:
1. Update task file YAML: `status: completed`
2. Update TASKS.md: `[🔄]` → `[✅]`

**NEVER update one without the other.**

### Task File Format
```yaml
---
id: {id}
title: 'Task Title'
status: pending|in-progress|completed|failed
priority: critical|high|medium|low
phase: 0
subsystems: [affected_subsystems]
project_context: Brief connection to project goal
dependencies: [task_ids]
---

# Task: {title}

## Objective
[Clear, actionable goal]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

### Task Completion Workflow
When you finish implementing a task:
1. **Validate**: Code compiles, imports resolve, acceptance criteria met
2. **Update Status**: Task file + TASKS.md atomically
3. **Offer Git Commit**: Always offer to commit after task completion
4. **Check Project Files**: Update agents.md/CLAUDE.md if new tools/features added

---

## Phase Management

### Phase Synchronization (MANDATORY)
TASKS.md phase headers and phase files MUST always be in sync.

**Atomic Phase Creation:**
```
✅ CORRECT (Atomic):
1. Add phase header to TASKS.md: "### Phase 2: Core Development"
2. Create phase file: .trent/phases/phase2_core-development.md
3. Confirm BOTH in response

❌ WRONG (Split):
Response 1: Add header to TASKS.md only
Response 2: Create phase file later  ← VIOLATION!
```

**Status Mapping:**
| TASKS.md Header | Phase File YAML |
|-----------------|-----------------|
| `### Phase N: Name` | `status: planning` |
| `### Phase N: Name [🔄]` | `status: in_progress` |
| `### Phase N: Name [✅]` | `status: completed` |
| `### Phase N: Name [❌]` | `status: cancelled` |
| `### Phase N: Name [⏸️]` | `status: paused` |

### Phase File Format
```yaml
---
phase: 0
name: 'Setup & Infrastructure'
status: planning|in_progress|completed|cancelled|paused
subsystems: [database, api, authentication]
task_range: '1-99'
prerequisites: []
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase {N}: {Phase Name}

## Overview
{Brief description}

## Objectives
- {Objective 1}

## Deliverables
- [ ] {Deliverable 1}

## Acceptance Criteria
- [ ] {Criterion 1}
```

### Phase Pivot Workflow
1. Update old phase file: `status: paused` or `cancelled`
2. Update TASKS.md: Add `[⏸️]` or `[❌]` to old phase header
3. Create new phase file with `pivoted_from` and `pivot_reason`
4. Add new header to TASKS.md

---

## Bug Tracking System

### Bug Classification
- **Critical**: System crashes, data loss, security vulnerabilities
- **High**: Major feature failures, performance degradation >50%
- **Medium**: Minor feature issues, usability problems
- **Low**: Cosmetic issues, enhancement requests

### Bug Task Integration
When a bug is identified:
1. Create BUGS.md entry with bug details
2. Create corresponding task in TASKS.md with `[BUG]` prefix
3. Create task file in tasks/ folder with bug type
4. Link bug to affected phases
5. Track resolution through task completion

### Bug Lifecycle
1. Bug Discovery → 2. Bug Documentation → 3. Task Creation → 4. Investigation → 5. Fix Implementation → 6. Verification → 7. Documentation → 8. Closure

---

## Task Expansion System

### Complexity Scoring (1-10+ scale)
- **Estimated Effort (4 pts)**: Task takes >2-3 developer days
- **Cross-Subsystem Impact (3 pts)**: Affects multiple subsystems
- **Multiple Components (3 pts)**: Changes across unrelated modules
- **High Uncertainty (2 pts)**: Requirements unclear
- **Multiple Outcomes (2 pts)**: Several distinct outcomes
- **Dependency Blocking (2 pts)**: Large prerequisite for subsequent tasks

### Complexity Matrix
```
0-3 points  | Simple Task    | Proceed normally
4-6 points  | Moderate Task  | Consider expansion
7-10 points | Complex Task   | Expansion required (MANDATORY)
11+ points  | High Complex   | Must expand before creation
```

### Sub-Task Format
**Filename**: `task{parent_id}-{sub_id}_name.md` (e.g., `task042-1_setup_database.md`)

```yaml
---
id: "42-1"
title: 'Setup Database'
type: task
status: pending
priority: high
parent_task: 42
dependencies: []
---
```

### Story Point Scale
- **1 SP**: Minor fixes (< 1 hour)
- **2 SP**: Small features (1-4 hours)
- **3 SP**: Medium complexity (4-8 hours)
- **5 SP**: Complex features (1-2 days)
- **8 SP**: Large tasks requiring expansion

---

## Multi-Agent Coordination

### Core Principles
1. **Single Message = Parallel Execution**: Multiple agents in ONE message run in parallel
2. **Different Agent Types Only**: Cannot run same agent type simultaneously
3. **Independent Tasks Only**: Parallelize tasks with no dependencies
4. **Clear Boundaries**: Each agent needs isolated, well-defined scope
5. **Optimal Count**: 3-5 agents in parallel is the sweet spot

### Agent Substitutions
When you need multiple similar agents:
- **Backend work**: backend-developer, full-stack-developer, api-designer
- **Frontend work**: frontend-developer, full-stack-developer
- **Database work**: database-expert, full-stack-developer, backend-developer
- **Documentation**: technical-writer, api-designer

### Git Worktrees for Parallel Agents
When running multiple agents in parallel on same files:
```bash
# Create worktrees
git worktree add ../project-agent1 -b task-101
git worktree add ../project-agent2 -b task-102

# After completion, merge
git checkout main
git merge task-101 -m "Merge task-101"
git merge task-102 -m "Merge task-102"

# Cleanup
git worktree remove ../project-agent1
git worktree remove ../project-agent2
```

---

## PRD Template (PLAN.md)

```markdown
# PRD: [Project/Feature Title]

## 1. Product overview
### 1.1 Document title and version
### 1.2 Product summary

## 2. Goals
### 2.1 Business goals
### 2.2 User goals
### 2.3 Non-goals

## 3. User personas
### 3.1 Key user types
### 3.2 Basic persona details
### 3.3 Role-based access

## 4. Phases
### 4.1 Phase Overview
### 4.2 Phase References

## 5. User experience
### 5.1 Entry points & first-time user flow
### 5.2 Core experience
### 5.3 Advanced features & edge cases

## 6. Narrative

## 7. Success metrics
### 7.1 User-centric metrics
### 7.2 Business metrics
### 7.3 Technical metrics

## 8. Technical considerations
### 8.1 Affected subsystems
### 8.2 Integration points
### 8.3 Data storage & privacy
### 8.4 Scalability & performance
### 8.5 Potential challenges

## 9. Milestones & sequencing

## 10. User stories
```

---

## Scope Validation Questions

Before creating any PRD, ask:

1. **User Context**: Personal use, small team, or broader deployment?
2. **Security Requirements**: Minimal, standard, enhanced, or enterprise?
3. **Scalability**: Basic, moderate, high, or enterprise?
4. **Feature Complexity**: Minimal, standard, feature-rich, or enterprise?
5. **Integration Needs**: Standalone, basic, standard, or enterprise?

### Over-Engineering Prevention
- **Authentication**: Don't add role permissions unless requested
- **Database**: Use simple file-based unless DB explicitly requested
- **API**: Don't add comprehensive REST beyond required
- **Architecture**: Default monolith unless scale requires separation

---

## Codebase Analysis Commands

### @trent-analyze-codebase
Deep merge two or more of YOUR OWN projects together.

**Process:**
1. Launch 3-4 parallel explore agents
2. Create architecture map in `docs/`
3. Create comparison document in `docs/`
4. Create phase + tasks in `.trent/`
5. Verify deliverables

### @trent-harvest
Analyze external sources and present selective improvement suggestions.

**Process:**
1. Load project context (SUBSYSTEMS.md, TASKS.md, PLAN.md)
2. Analyze external source
3. Present numbered menu of suggestions (max 15-20)
4. User chooses which to adopt
5. Only approved items become tasks

---

## Project Files Management

### agents.md vs CLAUDE.md
| File | Primary Use | Read By |
|------|-------------|---------|
| `agents.md` | Universal AI agent instructions | Cursor, Windsurf, Copilot, 15+ others |
| `CLAUDE.md` | Claude-specific project context | Claude Code |

### Protected Sections
Use markers to protect trent-managed sections:
```markdown
<!-- TRENT SYSTEM SECTION - DO NOT EDIT MANUALLY -->
...content...
<!-- END TRENT SYSTEM SECTION -->
```

### Update Triggers
**Update agents.md when:**
- New MCP tools added
- New commands added
- New skills/agents added
- Task workflow changes

**Update CLAUDE.md when:**
- Project structure changes
- Tech stack changes
- Phase created/pivoted
- New directories added

---

## Coding Conventions

### Python (PEP 8)
- Use black formatter (88-100 char line length)
- Add type hints where possible
- Write comprehensive docstrings
- Use UV for virtual environment management

### JavaScript/React
- Use ESLint + Prettier
- Functional components with hooks
- TypeScript when available

### File Naming
- **Task files**: `task{id}_{name}.md` (e.g., `task042_setup_database.md`)
- **Sub-tasks**: `task{id}-{sub}_name.md` (e.g., `task042-1_create_schema.md`)
- **Phase files**: `phase{N}_{name}.md` (e.g., `phase0_setup.md`)
- **Documentation**: `YYYYMMDD_HHMMSS_Cursor_TOPIC.md` in `docs/`

### Documentation Location
- **docs/**: All documentation except core planning
- **Project root**: Only README.md, LICENSE, CHANGELOG.md, agents.md, CLAUDE.md
- **.trent/**: Only core planning documents

---

## Available Commands

| Command | Description |
|---------|-------------|
| `@trent-setup` | Initialize trent system |
| `@trent-status` | Project status overview |
| `@trent-task-new` | Create a new task |
| `@trent-task-update` | Update task status |
| `@trent-task-sync-check` | Validate task synchronization |
| `@trent-plan` | Create PRD and project planning |
| `@trent-review` | Comprehensive code review |
| `@trent-qa` | Quality assurance activation |
| `@trent-qa-report` | Generate quality metrics |
| `@trent-bug-report` | Report/document a bug |
| `@trent-bug-fix` | Fix a reported bug |
| `@trent-git-commit` | Create well-structured commits |
| `@trent-issue-fix` | Fix GitHub issue |
| `@trent-phase-add` | Add new project phase |
| `@trent-phase-pivot` | Pivot project direction |
| `@trent-phase-sync-check` | Validate phase synchronization |
| `@trent-workflow` | Task expansion, sprint planning |
| `@trent-analyze-codebase` | Deep merge your own projects |
| `@trent-harvest` | Harvest ideas from external sources |

---

## Available Agents

### Core Development
| Agent | Best For |
|-------|----------|
| `backend-developer` | Backend APIs, business logic |
| `frontend-developer` | User interfaces, responsive design |
| `full-stack-developer` | Complete features |
| `database-expert` | Database work |
| `api-designer` | API contracts |

### DevOps & Infrastructure
| Agent | Best For |
|-------|----------|
| `devops-engineer` | Deployment automation |
| `docker-specialist` | Container optimization |
| `kubernetes-specialist` | Kubernetes operations |
| `cicd-specialist` | CI/CD pipelines |
| `cloud-engineer` | Cloud architecture |
| `solution-architect` | Architectural decisions |
| `security-auditor` | Security reviews |

### Quality & Testing
| Agent | Best For |
|-------|----------|
| `test-runner` | Running and fixing tests |
| `qa-engineer` | Quality assurance |
| `code-reviewer` | Code reviews |
| `debugger` | Debugging issues |

### Specialized
| Agent | Best For |
|-------|----------|
| `technical-writer` | Technical documentation |
| `orchestrator` | Complex multi-agent tasks |
| `codebase-analyst` | Deep merge your own projects |
| `harvest-analyst` | Harvest ideas from external sources |
| `silicon-valley-superfan` | HBO Silicon Valley trivia |

---

## PowerShell Notes (Windows)

### curl is aliased to Invoke-WebRequest
```powershell
# WRONG - hangs on Uri prompt
curl -s http://localhost:5000/api

# CORRECT
curl.exe -s http://localhost:5000/api
# OR
Invoke-WebRequest -Uri "http://localhost:5000/api" -UseBasicParsing
```

### Command Separators
- Use `;` instead of `&&` for command chaining
- Multi-line python -c commands will fail - use single line or scripts

### Get Timestamp
```powershell
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
```

---

## Self-Improvement Protocol

When you identify issues with the trent system:

```markdown
## 🔧 Trent System Issue Detected

**Category**: [Inconsistency/Weak Enforcement/Missing Feature/Documentation Gap]

**Location(s)**: 
- [File and line/section]

**Issue Description**:
[What's wrong]

**Proposed Solution**:
[Specific fix]

**Options**:
1. ✅ **Accept** - Implement the proposed solution
2. ❌ **Decline** - Keep current behavior
3. 🔄 **Alternative** - Provide a different solution
```

---

## Security
- Never commit API keys, tokens, or passwords
- Use environment variables for secrets
- Always use parameterized queries for databases
- Oracle credentials passed per-query (not stored)
- Validate all user input

---

## This Repository's Purpose

This is the **source repository** for the trent system. It contains:
- The complete rule set for task management
- Templates for installing trent in other projects
- MCP server for RAG, research, Oracle, and video analysis tools
- Documentation and examples

When making changes here, consider:
1. Does this affect the docker/templates/ files?
2. Does this need to update agents.md trent section?
3. Should this trigger a version bump?

---

**Version**: 4.0.0
**Last Updated**: 2026-02-16
**Supported IDEs**: Cursor, Claude Code
