---
description: "Task creation, status enforcement, sync rules, completion workflow, phase gates"
globs:
alwaysApply: true
---

# Task Management

## Session Start: Context Loading

When `.trent/` exists, display at session start:
```
📌 SESSION CONTEXT
Mission: [from PROJECT_CONTEXT.md, 1 line]
Goals: G-01: [name] | G-02: [name]    (from PROJECT_GOALS.md)
Phase: [current phase]
Ideas: [N] active                     (from IDEA_BOARD.md)
```

**Idea Capture Triggers** — capture IMMEDIATELY to IDEA_BOARD.md when user says:
"make a note of that", "remember this idea", "idea: ...", "what if we...", "eventually...", "for later..."
See `30_trent_ideas_goals.md` for full protocol.

---

## Task Creation (MANDATORY)

**CRITICAL: Create task file BEFORE changing to [📋]. NEVER skip this.**

1. Add to TASKS.md with `[ ]` status
2. **Immediately** create task file: `.trent/tasks/taskXXX_descriptive_name.md`
   - NO underscore after "task" (e.g., `task052_` NOT `task_052_`)
   - Hyphens for subtasks (e.g., `task039-1_` NOT `task039.1_`)
3. Include complete YAML frontmatter
4. Update TASKS.md to `[📋]`
5. Start work → change to `[🔄]`

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

| Phase | ID Range | Purpose |
|-------|----------|---------|
| 0 | 1-99 | Setup, infrastructure |
| 1 | 100-199 | Foundation |
| 2 | 200-299 | Core development |
| N | N×100 to N×100+99 | Custom phases |

Phase gaps are allowed. Phases can be added, completed, cancelled, or paused at any time.

---

## Task Status (ENFORCED PROGRESSION)

| Indicator | YAML Status | Meaning |
|-----------|-------------|---------|
| `[ ]` | (no file) | Listed, **BLOCKED — DO NOT START** |
| `[📋]` | `pending` | File created, **CAN PROCEED** |
| `[🔄]` | `in-progress` | Actively working |
| `[✅]` | `completed` | Done |
| `[❌]` | `failed` | Failed or blocked |
| `[⏸️]` | `paused` | Paused (used for phases during pivots) |

**ENFORCED: Cannot skip [📋]**
```
CORRECT: [ ] → [📋] → [🔄] → [✅]
WRONG:   [ ] → [🔄]  ← VIOLATION (no file!)
WRONG:   [ ] → [✅]  ← VIOLATION (no audit trail!)
```

---

## Sync Enforcement (MANDATORY)

### Atomic Update Rule

**When changing task status, you MUST update BOTH files in the SAME response:**
1. Task file YAML `status` field
2. TASKS.md status indicator

**Split updates across responses = VIOLATION.**

### Status Mapping

| TASKS.md | Task File YAML |
|----------|----------------|
| `[ ]` | (file may not exist) |
| `[📋]` | `status: pending` |
| `[🔄]` | `status: in-progress` |
| `[✅]` | `status: completed` |
| `[❌]` | `status: failed` |

**If mismatch detected: FIX IT FIRST before any other operation.**

### Orphan & Phantom Detection

- **Orphan**: Task file exists in `.trent/tasks/` but not listed in TASKS.md → Add to TASKS.md or delete
- **Phantom**: Entry in TASKS.md with `[📋]`+ but no file exists → Create file or remove entry

---

## Pre-Work Verification (BLOCKING)

**Before writing ANY code for a task:**

1. Task file MUST exist in `.trent/tasks/`
2. YAML frontmatter MUST be complete (id, title, status, priority, phase)
3. TASKS.md MUST show `[📋]` or `[🔄]` (NOT `[ ]`)

**If any check fails: Create the task file FIRST. Do NOT proceed without it.**

### Retroactive Tasks (EXCEPTION ONLY)

When documenting already-completed work without a prior task file:
- Use `[RETRO]` prefix in title
- Set `retroactive: true` and `retroactive_reason` in YAML
- CAN go directly to `[✅]`
- **MUST be the EXCEPTION, not the rule**

---

## Task Completion Workflow (5 Steps)

**Triggers**: Code accepted, feature working, bug fixed, acceptance criteria met.

**Step 0: File Existence Check (BLOCKING)**
- Task file MUST exist. If not: create it (or mark `[RETRO]`). **Cannot complete without file.**

**Step 1: Validation**
- Code compiles, imports resolve, no syntax errors
- Task objective and acceptance criteria met
- No 3-strike reusability violations (see `04_code_reusability.md`)

**Step 2: Atomic Status Update**
- Update task file: `status: completed`
- Update TASKS.md: `[🔄]` → `[✅]`
- **Both in same response. No exceptions.**

**Step 3: Offer Git Commit**
- Offer commit with format: `{type}({subsystems}): {task_title}`
- Type mapping: feature→`feat`, bug_fix→`fix`, refactor→`refactor`, docs→`docs`

**Step 4: Project Files Impact Check**
- Added MCP tool/command/skill/agent? → Update agents.md
- Changed tech stack/structure/conventions? → Update CLAUDE.md
- Bug fix or refactor only? → No update needed

**Step 5: Confirm completion in response**

**Failure to complete this workflow = SYSTEM VIOLATION**

---

## Phase Completion Gate

**Before starting ANY task in Phase N+1:**

1. **Verify**: ALL Phase N tasks show `[✅]`
2. **Generate SWOT**: Strengths, Weaknesses, Opportunities, Threats for the completed phase
3. **WAIT for user approval**: Do NOT proceed until user says "proceed"/"approved"/"continue"
4. **Offer phase git commit**: `phase({N}): {Phase Name} complete` with tag `phase-{N}-complete`

**Starting a new phase without approval = BLOCKED**

---

## End-of-Response Self-Check (MANDATORY)

**Run this check at the END of EVERY response:**

```
□ Did I complete work for a task?
  → Verify task file exists → Run validation → Atomic status update
  → Offer git commit → Check project files impact → Confirm

□ Did I mention ANY error, warning, or defect?
  → "pre-existing", "unrelated", "was already there", "compile error",
    "lint warning", "TypeScript error" → MUST create BUG entry
  → See 23_trent_qa.md Zero-Tolerance Error Reporting

□ Did I offer git commit after task completion?
  → If not, offer it NOW

□ Did I introduce duplicated code (3-strike rule)?
  → Extract to lib/ or shared/ BEFORE completing
```

**Marking [✅] without task file = COMPLIANCE VIOLATION**
**Mentioning errors without BUG entry = SYSTEM VIOLATION**
