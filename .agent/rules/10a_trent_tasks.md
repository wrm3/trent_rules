---
description: Task creation, file format, status management, and pre-work verification
activation: always_on
---

---
description: "Task creation, file format, status management, and pre-work verification"
globs: 
alwaysApply: true
---

# Core Rules System

This rule consolidates the essential trent functionality into a single, efficient rule for daily coding work.

## Session Start: Context Loading

When any of these files exist in `.trent/`, display them at session start:

```
📌 SESSION CONTEXT
Mission: [from PROJECT_CONTEXT.md, 1 line]
Goals: G-01: [name] | G-02: [name]    (from PROJECT_GOALS.md — if exists)
Phase: [current phase]
Ideas: [N] active                     (from IDEA_BOARD.md — if exists)
```

**Idea Capture Triggers** — capture IMMEDIATELY to IDEA_BOARD.md when user says:
- "make a note of that" / "remember this idea" / "note that somewhere"
- "idea: ..." / "what if we..." / "eventually..." / "for later..."

See `19_trent_ideas_goals.md` for full IDEA_BOARD and PROJECT_GOALS protocols.

---

## Task Management

### Task Creation (MANDATORY PROCESS)

**🔴 CRITICAL: Create task file BEFORE changing to [📋]**

**Process** (follow in order):
1. Add to TASKS.md with `[ ]` status
2. **Immediately** create task file in `.trent/tasks/` with format: `taskXXX_descriptive_name.md`
   - NO underscore after "task" (e.g., `task052_` NOT `task_052_`)
   - Use hyphens for subtasks (e.g., `task039-1_` NOT `task039.1_`)
3. Include complete YAML frontmatter and all required sections
4. Update TASKS.md to `[📋]` status (file created, ready to start)
5. **Then** you can start work and change to `[🔄]`

**Never skip step 2-3**: "Strike while the metal is hot" - create file in same context

### Task File Format
```yaml
---
id: {id}
title: 'Task Title'
status: pending
priority: medium
phase: 0
subsystems: [affected_subsystems]
project_context: Brief connection to project goal
dependencies: [task_ids]
---
```

### Phase-Based Task Numbering

**Phase System**: Tasks are organized into logical phases representing project milestones or work stages.

**Task ID Numbering by Phase**:
- **Phase 0** (Setup/Infrastructure): Tasks start at `1` (1-99)
- **Phase 1** (Foundation): Tasks start at `100` (100-199)
- **Phase 2** (Core Development): Tasks start at `200` (200-299)
- **Phase 3** (Enhancement): Tasks start at `300` (300-399)
- **Phase N**: Tasks start at `N * 100`

**Examples**:
```
Phase 0: task001_setup_virtual_environment.md
Phase 0: task002_configure_mcp_server.md
Phase 1: task100_design_database_schema.md
Phase 1: task101_create_mysql_handler.md
Phase 2: task200_build_core_classes.md
Phase 2: task201_implement_api_endpoints.md
```

**Dynamic Phase Addition**:
- Phases can be added as project vision clarifies
- New phases can be inserted to pivot project direction
- Phases can be marked complete or cancelled
- Phase gaps are allowed (e.g., skip from Phase 2 to Phase 5)

**Phase Status Tracking** (in TASKS.md):
```markdown
## Phase 0: Project Setup [✅]
## Phase 1: Database Design [🔄]
## Phase 2: Core Development [ ]
```

### Task Status Management (ENFORCED PROGRESSION)

**Status Indicators**:
- `[ ]` = Task listed but **NO detailed file created yet** ⚠️ **BLOCKED - DO NOT START**
- `[📋]` = Task file created and ready to start ✅ **UNBLOCKED - CAN PROCEED**
- `[🔄]` = In Progress (actively working) - **Requires [📋] first**
- `[✅]` = Completed
- `[❌]` = Failed or blocked
- `[⏸️]` = Paused (work stopped, may resume later) - **Used for phases during pivots**

**🔴 CRITICAL RULE: Cannot Skip [📋]**
```
CORRECT: [ ] → [📋] → [🔄] → [✅]
WRONG:   [ ] → [🔄] (VIOLATION - no file created!)
WRONG:   [ ] → [✅] (VIOLATION - no file, no audit trail!)
```

**Before changing `[ ]` to `[📋]`**:
- [ ] Detailed task file created in `.trent/tasks/`
- [ ] YAML frontmatter included
- [ ] All required sections complete
- [ ] File follows naming: `taskXXX_description.md` (NO underscore after "task")

**Status Transitions**:
- **Ready**: Create file with YAML, update TASKS.md to `[📋]`
- **Start**: Update status to `in-progress`, update TASKS.md to `[🔄]` (requires `[📋]` first)
- **Complete**: Update status to `completed`, update TASKS.md to `[✅]`
- **Fail**: Update status to `failed`, update TASKS.md to `[❌]`


### � MANDATORY: Pre-Work File Verification (REGULATORY REQUIREMENT)

**PURPOSE**: Financial regulatory compliance (SOC 2, FFIEC) requires audit trails for all work. Task files are the audit record.

#### Pre-Flight Check (BEFORE ANY CODING)

**Before writing ANY code for a task, you MUST verify:**

```markdown
## � PRE-FLIGHT CHECK: Task {ID}

**File Verification:**
- [ ] Task file exists: `.trent/tasks/task{ID}_{name}.md`
- [ ] YAML frontmatter complete (id, title, status, priority, phase)
- [ ] Acceptance criteria defined
- [ ] TASKS.md shows [�] or [�] (NOT [ ])

**Result**: [VERIFIED ✅ / BLOCKED ❌]
```

**If BLOCKED**: Create the task file FIRST, then proceed.

#### Enforcement Rules

1. **NEVER mark a task [✅] if no file exists** - This is a compliance violation
2. **NEVER start coding if TASKS.md shows [ ]** - File must exist first
3. **RETROACTIVE tasks get special handling** (see below)

#### Retroactive Documentation (After-the-Fact)

When documenting work that was already completed without a task file:

**Use `[RETRO]` prefix in task title:**
```yaml
---
id: 42
title: '[RETRO] Fix encryption key derivation'
type: retroactive_fix
status: completed
created_date: '2026-02-03'
completed_date: '2026-02-03'
retroactive: true
retroactive_reason: 'Discovered and fixed during development session'
---
```

**Retroactive tasks:**
- ✅ CAN go directly from creation to [✅]
- ✅ MUST include `retroactive: true` in YAML
- ✅ MUST include `retroactive_reason` explaining why
- ❌ Should be the EXCEPTION, not the rule

#### Self-Check Before Task Completion

**Before marking ANY task complete, verify in this order:**

```
□ Does .trent/tasks/task{ID}_*.md exist?
  → NO: Create it NOW or mark as [RETRO]
  → YES: Continue

□ Does the file have complete YAML frontmatter?
  → NO: Add missing fields
  → YES: Continue

□ Does TASKS.md status match file status?
  → NO: Fix the mismatch
  → YES: Proceed with completion
```

#### Violation Detection

**At session start or when working on tasks, scan for violations:**

```markdown
� TASK FILE AUDIT

Checking TASKS.md entries against .trent/tasks/ files...

| Task | TASKS.md | File Exists | Status |
|------|----------|-------------|--------|
| 001 | [�] | ✅ task001_*.md | OK |
| 002 | [✅] | ❌ NO FILE | ⚠️ VIOLATION |
| 003 | [�] | ✅ task003_*.md | OK |

**Violations Found**: 1
**Action Required**: Create retroactive file for Task 002
```

