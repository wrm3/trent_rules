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

See `30_trent_ideas_goals.md` for full IDEA_BOARD and PROJECT_GOALS protocols.

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
- `[📝]` = Spec being written by an agent (TTL: 1 hour — if expired, reset to `[📋]`)
- `[🔄]` = In Progress (actively claimed by agent, has TTL) - **Requires [📋] first**
- `[🔍]` = Awaiting Verification (implementation done, pending review by a DIFFERENT agent)
- `[⏳]` = Resource-Gated (waiting on GPU/storage/API credits/hardware/human decision)
- `[✅]` = Completed (verified by a different agent than the implementer)
- `[❌]` = Failed/Cancelled (after max retries or explicit cancellation)
- `[⏸️]` = Paused (work stopped, may resume later — used for phases during pivots)
- `[🌾]` = Harvested (task body reused as input for different approach — original preserved)

**🔴 CRITICAL RULE: Cannot Skip [📋] or [🔍]**
```
CORRECT: [ ] → [📋] → [🔄] → [🔍] → [✅]
WRONG:   [ ] → [🔄] (VIOLATION - no file created!)
WRONG:   [ ] → [✅] (VIOLATION - no file, no audit trail!)
WRONG:   [🔄] → [✅] (VIOLATION - implementer cannot self-verify!)
```

**Before changing `[ ]` to `[📋]`**:
- [ ] Detailed task file created in `.trent/tasks/`
- [ ] YAML frontmatter included
- [ ] All required sections complete
- [ ] File follows naming: `taskXXX_description.md` (NO underscore after "task")

**Status Transitions**:
- **Ready**: Create file with YAML, update TASKS.md to `[📋]`
- **Start**: Update status to `in-progress`, update TASKS.md to `[🔄]` (requires `[📋]` first)
- **Complete**: Update status to `awaiting-verification`, update TASKS.md to `[🔍]` — wait for verifier
- **Verified**: Verifier (different agent) sets `status: completed`, update TASKS.md to `[✅]`
- **Fail**: Update status to `failed`, update TASKS.md to `[❌]`
- **Harvest**: Use when a task's work product is still valuable even though the original approach was abandoned

### Harvested Task Lifecycle

A task is `harvested` when:
- The implementation approach was superseded (e.g., pivoted to a different architecture)
- The task's work informed a new direction but wasn't completed as originally specified
- Another task rendered this one obsolete, but the research/code has reference value

**Harvesting a task:**
```yaml
status: harvested
```
Update TASKS.md: any status → `[🌾]`

**Rules for harvested tasks:**
- NEVER delete harvested task files — they are reference material
- Add a note at the top of the harvested task explaining what superseded it
- Reference the harvest in the new task's `project_context` field
- Harvested tasks do NOT count toward completion metrics (excluded from health score)
- Cleanup agent may prompt for archiving after 90 days


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



---

---
description: "Task synchronization enforcement, completion workflow, and phase completion gate"
globs: 
alwaysApply: true
---

### 🚨 MANDATORY: Task Synchronization Enforcement

**CRITICAL**: TASKS.md and individual task files MUST always be in sync. This is enforced through atomic operations and validation checks.

#### Atomic Update Rule (BOTH OR NEITHER)

**When changing task status, you MUST update BOTH files in the SAME response:**

```
✅ CORRECT (Atomic):
1. Update task file YAML: status: completed
2. Update TASKS.md: [🔄] → [✅]
3. Confirm BOTH updates in response

❌ WRONG (Split):
Response 1: Update task file only
Response 2: Update TASKS.md later  ← VIOLATION!
```

**Enforcement Pattern - Use This Template:**
```markdown
## Task Sync Update
- **Task ID**: {id}
- **Task File**: `.trent/tasks/task{id}_{name}.md`
  - Old status: {old_yaml_status}
  - New status: {new_yaml_status}
- **TASKS.md Entry**:
  - Old: [{old_indicator}] Task {id}: {title}
  - New: [{new_indicator}] Task {id}: {title}
- **Sync Status**: ✅ SYNCHRONIZED
```

#### Pre-Operation Validation

**Before ANY task operation, validate current sync state:**

1. **Read TASKS.md** - Note the status indicator for the task
2. **Read task file** - Note the `status:` field in YAML
3. **Compare** - They MUST match according to this mapping:

| TASKS.md Indicator | Task File YAML Status |
|--------------------|-----------------------|
| `[ ]` | (file may not exist) |
| `[📋]` | `status: pending` |
| `[🔄]` | `status: in-progress` |
| `[✅]` | `status: completed` |
| `[❌]` | `status: failed` |

4. **If mismatch detected** - FIX IT FIRST before proceeding:
```markdown
⚠️ **SYNC MISMATCH DETECTED**
- TASKS.md shows: [🔄] (in-progress)
- Task file shows: status: completed
- **Action**: Correcting TASKS.md to [✅] to match task file
```

#### Session Start Sync Check

**At the START of any session involving tasks, run this check:**

```
📋 TASK SYNC VALIDATION
Checking .trent/tasks/ against TASKS.md...

Task 001: TASKS.md [📋] ↔ File status: pending ✅ SYNCED
Task 002: TASKS.md [🔄] ↔ File status: in-progress ✅ SYNCED
Task 003: TASKS.md [✅] ↔ File status: completed ✅ SYNCED
Task 004: TASKS.md [🔄] ↔ File status: completed ⚠️ MISMATCH - FIXING

Sync Status: 3/4 synced, 1 fixed
```

**Run this check when:**
- User asks about task status
- User asks to work on a task
- User asks for project status
- Starting work on any task-related operation

#### Orphan Detection

**Check for orphaned files (task files not in TASKS.md):**

```
📋 ORPHAN CHECK
Files in .trent/tasks/ not listed in TASKS.md:
- task099_forgotten_task.md ← ORPHAN DETECTED

Action: Add to TASKS.md or delete if obsolete
```

**Check for phantom entries (TASKS.md entries without files):**

```
📋 PHANTOM CHECK  
Entries in TASKS.md without corresponding files:
- Task 055: Setup caching [📋] ← NO FILE EXISTS

Action: Create file or remove from TASKS.md
```

#### Sync Violation Response

**If you detect a sync violation, respond with:**

```markdown
🚨 **TASK SYNC VIOLATION DETECTED**

**Violation Type**: {mismatch|orphan|phantom}
**Details**: {specific issue}

**Automatic Correction Applied:**
- {what was fixed}

**Prevention**: Always use atomic updates (both files in same response)
```

#### Mandatory Sync Confirmation

**Every response that modifies task status MUST end with:**

```markdown
---
**Task Sync Confirmation:**
- Task {ID} file: status: {status} ✅
- TASKS.md entry: [{indicator}] ✅
- Sync verified: ✅
---
```

### 🚨 MANDATORY: Task Completion Enforcement

**CRITICAL RULE**: When you finish implementing a task, you MUST complete the full workflow.

**Automatic Completion Triggers** (start workflow when ANY occur):
- ✅ Code changes implemented and accepted
- ✅ Feature finished and working
- ✅ Bug fixed and verified
- ✅ All acceptance criteria satisfied

#### Task Completion Workflow (5 Steps)

**Step 0: File Existence Check (BLOCKING)**
```markdown
## � TASK FILE CHECK: Task {ID}

**Searching for**: .trent/tasks/task{ID}_*.md
**Result**: [FOUND ✅ / NOT FOUND ❌]

If NOT FOUND:
- Create task file NOW (or mark as [RETRO] if after-the-fact)
- DO NOT PROCEED until file exists
```

**� STOP**: If file does not exist, you CANNOT mark the task complete. Create the file first.


**Step 1: Validation Check**
Before marking complete, verify the work:

```markdown
## 🔍 Task Completion Validation

### Compile/Import Check
- [ ] Code compiles without errors
- [ ] All imports resolve correctly
- [ ] No syntax errors

### Acceptance Check
- [ ] Task objective achieved
- [ ] Acceptance criteria satisfied
- [ ] User expectations met

### Reusability Check (see 04_code_reusability.md)
- [ ] No duplicated logic introduced (checked against existing shared modules)
- [ ] New utility functions placed in lib/utils/ or shared/, not defined inline
- [ ] Existing shared modules used where applicable
- [ ] No magic numbers/strings hardcoded (use lib/config/constants)

**Validation Result**: [PASS/FAIL]
```

If validation FAILS, fix issues before proceeding.

**Step 2: Update Task Status (Atomic)**
```
□ Update task file: status: completed
□ Update TASKS.md: [🔄] → [✅]
```

**Step 3: Git Commit (Semi-Automatic)**
After validation passes, offer git commit:

```markdown
## 📦 Task Commit

Task #{ID} validated and complete!

**Changes to commit:**
- {list modified files}

**Suggested commit:**
```bash
git add {relevant_files}
git commit -m "{type}({subsystems}): {task_title}

Task: #{task_id}
Phase: {phase}
Agent: {agent_id}
Rules-Version: 5.1.0

{brief_summary}"
```

**Options:**
- "commit" or just press Enter - Run the commit
- "skip" - Continue without committing
- "edit: {message}" - Use custom message
```

**Commit Type Mapping:**
| Task Type | Commit Prefix |
|-----------|---------------|
| `feature` | `feat` |
| `bug_fix` | `fix` |
| `refactor` | `refactor` |
| `documentation` | `docs` |
| `task` (default) | `feat` |

**Step 4: Project Files Analysis**
Check if completed task affects project instruction files:

```markdown
## 📋 Project Files Impact Analysis

**Task Type**: {task_type}
**Subsystems**: {affected_subsystems}

**agents.md Update Needed?**
- [ ] Added new MCP tool → YES, document in agents.md
- [ ] Added new command → YES, add to commands table
- [ ] Added new skill → YES, add to skills list
- [ ] Added new agent → YES, add to agents table
- [ ] Changed task workflow → YES, update task management section
- [ ] Changed status indicators → YES, update status section
- [ ] Added new feature → MAYBE, if user-facing
- [ ] Bug fix only → NO
- [ ] Refactor only → NO
- [ ] Documentation only → NO

**CLAUDE.md Update Needed?**
- [ ] Changed tech stack → YES
- [ ] Added new directory → YES, update structure
- [ ] Changed dev commands → YES
- [ ] Changed conventions → YES
- [ ] Phase pivot occurred → YES, update current phase

**Update Required**: [YES/NO]
```

**If Update Required:**
```markdown
## 🔄 Project Files Update

**agents.md changes:**
- {what to add/update}

**CLAUDE.md changes:**
- {what to add/update}

Shall I update these files? (yes/no/skip)
```

**Step 5: Confirmation**
```markdown
---
**Task Completion Summary:**
- Task {ID}: {title} → [✅] COMPLETED
- Validation: ✅ PASSED
- Files updated: task{ID}_name.md, TASKS.md
- Git commit: {commit_hash} (or "skipped")
- Project files: {updated/not needed}
---
```


**Self-Check at END of Every Response**:
```
□ Did I complete work for a task?
  → FIRST: Verify task file exists in .trent/tasks/
  → If no file: CREATE IT NOW (or mark [RETRO] if after-the-fact)
  → Run validation check
  → Update task file + TASKS.md (ATOMIC)
  → Offer git commit
  → Check project files impact
  → Confirm completion

□ Does the task file exist? (BLOCKING CHECK - REGULATORY)
  → If marking [✅] and no file exists: STOP, create file first
  → Task files are the audit trail for compliance
  → No file = No completion allowed

□ Did I offer git commit? (MANDATORY CHECK)
  → If task completed and no commit offered, offer it NOW
  → Never end response without commit offer after task completion

□ Did I check project files impact? (MANDATORY CHECK)
  → If task added MCP tool/command/skill/agent, update agents.md
  → If task changed tech stack/structure, update CLAUDE.md

□ Did I introduce duplicated code that should be a shared module? (REUSABILITY CHECK)
  → If logic appears 3+ times: extract to lib/ or shared/ BEFORE completing
  → If new utilities defined inline: move to lib/utils/
  → Reference 04_code_reusability.md for folder conventions

□ Did I mention ANY error, warning, or defect — even "pre-existing" or "unrelated"? (BUG LOG CHECK)
  → YES: Is there a BUG-NNN entry in .trent/BUGS.md for it?
    → NO: CREATE THE BUG ENTRY NOW — "pre-existing" is not an exemption
    → YES: Reference the BUG-NNN in this response
  → Using phrases like "pre-existing error", "unrelated error", "was already there",
    "existing lint warning", "TypeScript error", "compile error" WITHOUT logging a bug
    = SYSTEM VIOLATION (see 23_trent_qa.md Zero-Tolerance Error Reporting)

□ Did I capture institutional memory? (MEMORY CHECK — Tasks 080 + 081)
  → Before starting any task: run memory_search for the subsystem
    query: "what happened last time in {subsystem}?"
    Use memory_context MCP tool if available for token-budgeted context
  → After completing a task: capture session summary via memory_capture_session
    Include: what was built, what failed, what was learned, what to watch out for
  → This is MANDATORY — not optional — for all tasks with blast_radius: medium or high
  → Skipping memory capture for a completed task = SYSTEM VIOLATION
```

**Failure to Complete Workflow = SYSTEM VIOLATION**
**Failure to Offer Git Commit = SYSTEM VIOLATION**
**Marking [✅] Without Task File = COMPLIANCE VIOLATION**

### � MANDATORY: Phase Completion Gate

**Before starting ANY task in Phase N+1, you MUST:**

1. **Verify Phase N Complete**: All tasks show [✅] (no [ ] or [�])
2. **Generate Phase SWOT Analysis**:

```markdown
# � Phase {N} Completion Analysis: {Phase Name}

## SWOT Analysis

### � Strengths
- [What went well, code quality wins, good patterns]

### ⚠️ Weaknesses  
- [Areas needing improvement, technical debt, gaps]

### � Opportunities
- [Improvements for next phase, optimizations]

### � Threats
- [Risks carrying forward, dependencies, security]

## Code Quality Assessment
- Test Coverage: [estimate]
- Documentation: [complete/partial/missing]
- Error Handling: [robust/adequate/needs work]

## Recommendation: [READY TO PROCEED / NEEDS REMEDIATION]

---
**User Approval Required**: Type "proceed" to continue to Phase {N+1}.
```

3. **WAIT for User Approval**: Do NOT start Phase N+1 until user says "proceed", "approved", or "continue"

4. **Prompt for Git Commit** after user approves:

```markdown
## � Phase {N} Git Commit

Phase approved! Suggested commit:

**Tasks completed in this phase:**
- #{task_id1}: {title1}
- #{task_id2}: {title2}
- ...

**Subsystems affected:** {list from phase file}

```bash
git add .
git commit -m "phase({N}): {Phase Name} complete

Tasks completed:
- #{task_id1}: {title1}
- #{task_id2}: {title2}

Subsystems: {subsystems}
Phase: {N}"

git tag phase-{N}-complete
```

**Options:**
- "commit" or Enter - Run the commit and tag
- "skip" - Proceed without committing  
- "edit: {message}" - Use custom message
```

5. **Complete commit/skip** before starting Phase N+1

**Phase Gate Violation**: Starting new phase without approval = BLOCKED
