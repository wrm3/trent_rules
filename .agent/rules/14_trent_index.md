---
description: trent system overview and command index
activation: always_on
---
---
description: 
globs: 
alwaysApply: true
---
# trent System Overview

Whenever you use this rule, start your message with the following:

"Accessing trent system overview..."

The trent system is a consolidated, practical task management framework optimized for daily coding work with minimal context overhead.

## 🚨 Session Start Protocol (MANDATORY)

**When user mentions tasks, phases, project status, or any trent-related operation, FIRST run sync validation:**

```markdown
📋 TRENT SYNC VALIDATION (Session Start)

**Task Sync Check:**
- Comparing .trent/tasks/ files against TASKS.md entries...
- [Results: X synced, Y mismatches, Z orphans]

**Phase Sync Check:**
- Comparing .trent/phases/ files against TASKS.md headers...
- [Results: X synced, Y mismatches, Z orphans]

**Status**: [ALL SYNCED ✅ / ISSUES FOUND ⚠️]
```

**If issues found**: Fix them BEFORE proceeding with user's request.

## Core Rules (4 Consolidated Files)

### 1. **`rules.mdc`** - Core System Management
- **Task Management**: YAML-based task lifecycle with Windows-safe emojis
- **Task Synchronization**: Enforced sync between TASKS.md and task files
- **File Organization**: Template vs working directory management
- **Tool Integration**: MCP tool-first approach and automation
- **Context Management**: Project awareness and goal alignment
- **Scope Control**: Anti-scope-creep validation and over-engineering prevention
- **Coding Standards**: Python, JavaScript/React standards
- **Template Setup**: MCP deployment template initialization

### 2. **`plans.mdc`** - Planning & Requirements
- **PRD Generation**: Product Requirements Document creation (high-level only)
- **Phase Management**: Phases tracked in TASKS.md with sync to phase files
- **Phase Synchronization**: Enforced sync between TASKS.md headers and phase files
- **Subsystems Registry**: Component tracking with SUBSYSTEMS.md template
- **Planning Questionnaire**: 27-question requirements gathering framework
- **Scope Clarification**: Scope validation and assumption checking
- **Codebase Analysis**: Automatic project analysis and subsystem discovery

### 3. **`qa.mdc`** - Quality Assurance
- **Bug Tracking**: Bug identification, categorization, and resolution tracking
- **Design Fixes**: Retroactive documentation for completed fixes
- **Documentation Templates**: Standardized templates for tasks, bugs, and fixes
- **Quality Workflows**: Bug lifecycle and quality management processes

### 4. **`workflow.mdc`** - Workflow Management
- **Task Expansion**: Complexity assessment and sub-task breakdown
- **Methodology Integration**: Kanban flow, WIP limits, DevOps practices
- **Workflow Diagrams**: Mermaid diagram generation for visualization
- **Architecture Visualization**: System component relationship diagrams
- **Sprint Planning**: Iteration planning and story point estimation

### 5. **`19_trent_ideas_goals.md`** - Idea Board & Project Goals
- **IDEA_BOARD.md**: Parking lot for ideas not yet ready for development
- **PROJECT_GOALS.md**: Strategic north star loaded into every session
- **Trigger Detection**: Auto-captures when user says "make note of this", "idea:", etc.
- **Goal Validation**: AI checks new tasks against PROJECT_GOALS before proceeding
- **Lifecycle Management**: raw → evaluating → accepted (task/phase) | shelved

### 6. **`self_improvement.mdc`** - System Self-Improvement
- **Issue Detection**: Automatic identification of system inconsistencies
- **Issue Reporting**: Structured protocol for reporting issues to user
- **Solution Proposals**: Concrete fixes with user approval workflow
- **Continuous Improvement**: Tracking and resolving system issues over time

### 6. **`project_files.mdc`** - Project Instruction Files
- **agents.md Management**: Universal AI agent instructions file
- **CLAUDE.md Management**: Claude-specific project context file
- **Section Markers**: Protected trent sections with HTML comment markers
- **Multi-Tool Compatibility**: Coexistence with other AI systems
- **Template Maintenance**: Templates for new project installation

## Directory Structure
```
.trent/
├── tasks/                # Active task files (taskNNN_name.md)
├── phases/               # Phase documentation (phaseN_name.md)
├── memory/               # Historical archives (using Cursor's built-in memory)
├── TASKS.md              # Master task checklist (organized by phase)
├── BUGS.md               # Bug tracking (subset of TASKS.md)
├── PROJECT_CONTEXT.md    # Project mission
├── PLAN.md               # Product Requirements Document
├── SUBSYSTEMS.md         # Component registry
├── FILE_REGISTRY.md      # File documentation
├── IDEA_BOARD.md         # Ideas parking lot (not ready for tasks yet)
└── PROJECT_GOALS.md      # Strategic goals — AI loads at session start

docs/                     # Project documentation (migration files, setup summaries)
temp_scripts/             # Test and utility scripts
```

## Phase-Based Task Numbering
- **Phase 0** (1-99): Setup, infrastructure, environment
- **Phase 1** (100-199): Foundation, database, core handlers
- **Phase 2** (200-299): Core development, main features
- **Phase N** (N×100 to N×100+99): Custom phase scope

⚠️ **CRITICAL**: Migration files, conversion summaries, and temporary documentation go in `docs/` folder, NOT in `.trent/`

## Key Features

### Context Optimization
- **85% Reduction**: From 26+ rules to 4 consolidated rules
- **Cursor Integration**: Built-in memory system + commands
- **Single-Level Rules**: No progressive disclosure complexity
- **Tool-First Approach**: MCP tool integration for automation

### Practical Daily Use
- **Clear Hierarchy**: PLAN → PHASES → TASKS → BUGS
- **Windows-Safe Emojis**: ✅ 🔄 ❌ for task status
- **Simplified Workflows**: Focus on essential coding tasks
- **No Rule Conflicts**: Clean, predictable activation

### Commands Available (Unified `trent-` prefix, grouped alphabetically)

**Bug Commands:**
- `@trent-bug-report` - Report a bug
- `@trent-bug-fix` - Fix a reported bug

**Git Commands:**
- `@trent-git-commit` - Create commits

**Issue Commands:**
- `@trent-issue-fix` - Fix GitHub issue

**Phase Commands:**
- `@trent-phase-add` - Add a new phase
- `@trent-phase-pivot` - Pivot to new direction
- `@trent-phase-sync-check` - Validate TASKS.md ↔ phase file synchronization

**QA Commands:**
- `@trent-qa` - Activate quality assurance
- `@trent-qa-report` - Generate quality metrics

**Task Commands:**
- `@trent-task-new` - Create a new task
- `@trent-task-update` - Update task status
- `@trent-task-sync-check` - Validate TASKS.md ↔ task file synchronization

**Idea & Goals Commands:**
- `@trent-idea-capture` - Capture an idea to IDEA_BOARD.md
- `@trent-idea-review` - Review and evaluate IDEA_BOARD entries
- `@trent-goal-update` - Create or update PROJECT_GOALS.md

**Other Commands:**
- `@trent-plan` - Activate planning system
- `@trent-review` - Code review
- `@trent-setup` - Initialize system
- `@trent-status` - Project status overview
- `@trent-workflow` - Activate workflow management

---

*This consolidated system provides a solid, practical workhorse optimized for daily coding work with minimal context overhead while preserving 95% of original functionality.*


