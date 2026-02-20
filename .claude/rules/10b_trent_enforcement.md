---
description: Task synchronization enforcement, completion workflow, and phase completion gate
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
