---
description: Core trent rules for task management, file organization, and tool integration
globs: 
alwaysApply: true
---
# Core Rules System

This rule consolidates the essential trent functionality into a single, efficient rule for daily coding work.

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
- `[📝]` = **Agent is actively writing the spec/task file** ⏳ **TTL: 1 HOUR**
- `[📋]` = Task file created and ready to start ✅ **UNBLOCKED - CAN PROCEED**
- `[🔄]` = In Progress (actively being coded) ⏳ **TTL: 2 HOURS**
- `[✅]` = Completed
- `[❌]` = Failed or blocked
- `[⏸️]` = Paused (work stopped, may resume later) - **Used for phases during pivots**

**🔴 CRITICAL RULE: Full Status Flow**
```
CORRECT: [ ] → [📝] → [📋] → [🔄] → [✅]
```

### 🚨 Multi-Agent Concurrency (CRITICAL)

Multiple AI agents (Cursor, Claude Code Extension, Claude Code CLI) may work this backlog simultaneously. To prevent duplicate work:

**When picking up a task:**
1. Read TASKS.md - **skip any task marked `[📝]` or `[🔄]`** (another agent has it)
2. If you pick a `[ ]` task to spec: **immediately** mark it `[📝]` in TASKS.md
3. If you pick a `[📋]` task to code: **immediately** mark it `[🔄]` in TASKS.md
4. Write `status_changed` timestamp in the task file YAML:
   ```yaml
   status: speccing  # or: in-progress
   status_changed: '2026-02-07T14:30:00Z'
   ```

**Stale task recovery (TTL expiry):**
- `[📝]` with `status_changed` **older than 1 hour** = abandoned spec attempt. Treat as `[ ]`, grab it.
- `[🔄]` with `status_changed` **older than 2 hours** = abandoned coding. Treat as `[📋]`, grab it.
- No `status_changed` timestamp on an active task = assume stale, available for pickup.

This is self-healing: dead/rate-limited agents don't create permanent locks.

**Before changing `[ ]` to `[📝]`** (speccing):
- [ ] Mark `[📝]` in TASKS.md immediately (claim it visually)
- [ ] Then create detailed task file in `.trent/tasks/`
- [ ] Include YAML frontmatter with `status: speccing` and `status_changed` timestamp
- [ ] All required sections complete
- [ ] File follows naming: `taskXXX_description.md` (NO underscore after "task")
- [ ] Update TASKS.md to `[📋]` when spec is done

**Status Transitions**:
- **Speccing**: Mark `[📝]` in TASKS.md, set `status: speccing` + `status_changed` in task file
- **Ready**: Spec complete, update task file to `status: pending`, update TASKS.md to `[📋]`
- **Start**: Update status to `in-progress` + `status_changed`, update TASKS.md to `[🔄]`
- **Complete**: Update status to `completed`, update TASKS.md to `[✅]`
- **Fail**: Update status to `failed`, update TASKS.md to `[❌]`

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

#### Task Completion Workflow (4 Steps)

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
  → Run validation check
  → Update task file + TASKS.md (ATOMIC)
  → Offer git commit
  → Check project files impact
  → Confirm completion

□ Did I offer git commit? (MANDATORY CHECK)
  → If task completed and no commit offered, offer it NOW
  → Never end response without commit offer after task completion

□ Did I check project files impact? (MANDATORY CHECK)
  → If task added MCP tool/command/skill/agent, update agents.md
  → If task changed tech stack/structure, update CLAUDE.md
```

**Failure to Complete Workflow = SYSTEM VIOLATION**
**Failure to Offer Git Commit = SYSTEM VIOLATION**

### 🚨 MANDATORY: Phase Completion Gate

**Before starting ANY task in Phase N+1, you MUST:**

1. **Verify Phase N Complete**: All tasks show [✅] (no [ ] or [🔄])
2. **Generate Phase SWOT Analysis**:

```markdown
# 📊 Phase {N} Completion Analysis: {Phase Name}

## SWOT Analysis

### 💪 Strengths
- [What went well, code quality wins, good patterns]

### ⚠️ Weaknesses  
- [Areas needing improvement, technical debt, gaps]

### 🚀 Opportunities
- [Improvements for next phase, optimizations]

### 🔴 Threats
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
## 📦 Phase {N} Git Commit

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

## File Organization

### Working Directory: `/.trent/` (99% of operations)
- Active task management (TASKS.md updates)
- Project planning (PRD creation, goals)
- Documentation updates
- Memory archival operations

### Template Directory: `/templates/trent/` (1% of operations)
- Updating installation templates
- Adding rules that ALL projects need
- MCP server deployment preparation

### File Categories
- **Config**: Configuration files, environment settings, build scripts
- **Source**: Application code, business logic, utilities
- **Data**: Schemas, migrations, seed data, static resources
- **Tests**: Unit tests, integration tests, test utilities
- **Docs**: Documentation, README files, architectural diagrams
- **Tools**: Build tools, scripts, development utilities

### Project Documentation Rules
- **Project Documentation**: All `.md` files documenting project aspects go in `docs/` folder in project root
- **Auto-Create**: If `docs/` folder doesn't exist, create it automatically
- **Examples**: API documentation, architecture docs, user guides, technical specifications

### Test Scripts Rules
- **Test Scripts**: All script files for testing project code go in `temp_scripts/` folder in project root
- **Auto-Create**: If `temp_scripts/` folder doesn't exist, create it automatically
- **Examples**: Test automation scripts, data validation scripts, performance testing scripts

### ⚠️ CRITICAL: File Placement Rules (MUST FOLLOW)
- **.trent/**: ONLY core planning documents (PLAN.md, TASKS.md, BUGS.md, PROJECT_CONTEXT.md, SUBSYSTEMS.md, FILE_REGISTRY.md, MCP_TOOLS_INVENTORY.md)
- **docs/**: ALL temporary, migration, or ad-hoc documentation files (including setup summaries, conversion reports, migration files, etc.)
- **temp_scripts/**: Test scripts and utility files
- **NEVER** place task migration files, conversion summaries, or temporary documentation in `.trent/`

### 🚨 NO PERMISSION REQUIRED - Direct Edit Policy

**CRITICAL FOR Cursor AI IDE:**

The following files in `.trent/` are **working files** that SHOULD BE EDITED DIRECTLY WITHOUT ASKING FOR USER PERMISSION:

**Core Planning Files (CAPITALIZED names):**
- `PLAN.md` - Product Requirements Document
- `TASKS.md` - Master task checklist
- `PROJECT_CONTEXT.md` - Project mission and goals
- `BUGS.md` - Bug tracking
- `SUBSYSTEMS.md` - Component registry
- `FILE_REGISTRY.md` - File organization documentation
- `MCP_TOOLS_INVENTORY.md` - Tool inventory

**Task Files:**
- All files in `.trent/tasks/` (e.g., `task001_description.md`)
- All files in `.trent/phases/` 

**Rules:**
- ✅ **EDIT DIRECTLY** - These are your working files, not user source code
- ✅ **NO CONFIRMATION NEEDED** - Just make the edit
- ✅ **NO "Should I update...?" PROMPTS** - Just do it
- ✅ **AUTO-CREATE** - Create missing files with templates automatically
- ✅ **SILENT OPERATIONS** - Create folders/files silently, report what was done

**Why?** These files track YOUR work as an AI assistant. They are management artifacts, not user deliverables. The user will review changes in their IDE's diff view.

### Auto-Creation Rules
- **Auto-Create Folders**: Always create missing folders (`docs/`, `temp_scripts/`, `.trent/`, etc.) without asking
- **Auto-Create Templates**: Create missing `.md` files with blank templates if they don't exist
- **Direct Editing**: Edit files directly - user will accept/reject final changes in their IDE

### Complete System Setup
When initializing or updating the system, automatically create:

#### Required Folders:
- `.trent/` - Main system directory
- `.trent/tasks/` - Task files directory
- `.trent/phases/` - Phase documentation directory
- `docs/` - Project documentation directory
- `temp_scripts/` - Test scripts directory

#### Required Template Files:
- `.trent/PLAN.md` - Product Requirements Document template
- `.trent/TASKS.md` - Master task checklist template
- `.trent/PROJECT_CONTEXT.md` - Project context template
- `.trent/SUBSYSTEMS.md` - Component registry template
- `.trent/FILE_REGISTRY.md` - File structure documentation template
- `.trent/MCP_TOOLS_INVENTORY.md` - Tool inventory template

#### File Placement Reminder:
- **Migration files, conversion summaries, setup reports**: Place in `docs/` folder, NOT in `.trent/`
- **Core planning documents only**: Keep `.trent/` clean and focused

## Tool Integration (MCP)

### Tool-First Principle
**Before implementing any solution manually, check available MCP tools first.**

### Tool Categories
- **Web/Browser**: Navigation, clicking, form filling, content extraction
- **Database**: Read queries, write operations, schema management
- **Research**: Web search, content scraping, API calls
- **Screen/Visual**: Screenshots, image analysis, visual automation
- **Code/System**: Code execution, system commands, file operations

### Tool Workflow Patterns
- **Web Testing**: Database Read → Web Interaction → Visual Tools → Database Verification
- **Database Operations**: Read Current State → Make Changes → Verify Changes
- **Research**: Search → Extract → Process → Document

## Context Management

### Project Context Display
When starting tasks, display:
```
📋 PROJECT CONTEXT OVERVIEW
🎯 Mission: [Brief mission from PROJECT_CONTEXT.md]
📍 Current Phase: [Phase and focus area]
✅ Success Criteria: [Key objectives for current phase]
🔄 Current Status: [Active tasks, progress, blockers]
🛡️ Scope Boundaries: [Key limitations and approved complexity]
```

### Context Optimization
- **75% threshold**: Archive low-priority content automatically
- **90% threshold**: Emergency cleanup, defer non-essential content
- **Priority levels**: Critical (always retained) → High → Medium → Low (aggressive cleanup)

## Scope Control

### Over-Engineering Prevention
- **Authentication**: Don't add role permissions unless requested
- **Database**: Use simple file-based unless DB explicitly requested
- **API**: Don't add comprehensive REST beyond required
- **Architecture**: Default monolith unless scale requires separation

### Scope Validation Questions
1. **User Context**: Personal use, small team, or broader deployment?
2. **Security Requirements**: Minimal, standard, enhanced, or enterprise?
3. **Scalability**: Basic, moderate, high, or enterprise?
4. **Feature Complexity**: Minimal, standard, feature-rich, or enterprise?
5. **Integration Needs**: Standalone, basic, standard, or enterprise?

## Coding Standards

### Python
- Follow PEP 8 guidelines (relaxed enforcement)
- Use black formatter, 88-100 character line length
- Use type hints when possible
- Write comprehensive docstrings

### JavaScript/React
- Follow ESLint configuration, use Prettier for formatting
- Use functional components with hooks
- Use React.memo, useCallback, useMemo for performance
- Use Jest and React Testing Library for testing


## Integration Points

### Task System Integration
- Automatically record metrics during task lifecycle events
- Track effort estimation accuracy for continuous improvement
- Monitor task pipeline health and bottlenecks

### File System Integration
- Use FILE_REGISTRY.md to understand current system structure
- Map file organization to component architecture
- Identify component boundaries from directory structure

### Tool System Integration
- Reference MCP_TOOLS_INVENTORY.md for available tools
- Use tool combinations for comprehensive workflows
- Validate tool selection against task requirements

## Template Maintenance and Platform Architecture

### Platform Architecture Reference

When maintaining this template or adding new features, **ALWAYS** consult the `.trent/` folder for platform-specific requirements and compatibility considerations.

**Key Documentation:**
- `.trent/PLATFORM_COMPARISON.md` - Cross-platform comparison table
- `.trent/CURSOR.md` - Cursor specific architecture
- `.trent/PLATFORM_ARCHITECTURE.md` - Overview and maintenance schedule

### When to Reference Platform Architecture

**ALWAYS check `.trent/` platform documentation before:**
1. Adding new rules or commands
2. Modifying task file formats or naming conventions
3. Creating new instructions or documentation
4. Updating file organization structure
5. Making changes that affect cross-IDE compatibility

### Critical Platform Differences

**File Formats (IMPORTANT):**
- Cursor: Uses `.mdc` for rules files (Markdown Cursor) - UNIQUE to Cursor
- Other platforms: Use `.md` files
- Task files: Use `.md` with YAML frontmatter (cross-platform compatible)

**Platform-Specific Features:**
- Cursor: Now Has Skills and SubAgents (no equivalent in Cursor)
- Cursor: Uses `.mdc` rule format (other platforms can't read these)
- Commands: Cursor uses `@command`, not `/command`

**Universal Features (work everywhere):**
- `.trent/` task management system
- YAML frontmatter in task files
- Markdown documentation
- Standard file organization
- Task status indicators ([ ], [📋], [🔄], [✅])

### Periodic Verification

**Quarterly Review (Every 3 Months):**
- [ ] Check Cursor official documentation for updates
- [ ] Check other platform documentation for new features
- [ ] Test template on multiple platforms
- [ ] Update `.trent/` platform documentation
- [ ] Update PLATFORM_COMPARISON.md if differences found
- [ ] Document any breaking changes

### Adding Features Cross-Platform

When adding features to this template, ensure compatibility:

1. **Test on multiple platforms**: Test thoroughly
2. **Document compatibility**: Update `.trent/CURSOR.md` and other platform docs
3. **Provide fallbacks**: For features that don't work on all platforms
4. **Update comparison table**: Add new features to PLATFORM_COMPARISON.md
5. **Migration guides**: Update if file structure or format changes

### Template Maintenance Workflow

When maintaining this template:

1. **Check platform docs** in `.trent/`
2. **Identify compatibility requirements** from PLATFORM_COMPARISON.md
3. **Make Cursor-specific changes** in `.cursor/rules/*.mdc` files
4. **Update platform documentation** in `.trent/CURSOR.md`
5. **Update comparison table** if new differences emerge

### File Format Rules for Cursor

**Cursor Rules (.mdc files):**
- MUST use `.mdc` extension (not `.md`)
- Located in `.cursor/rules/` directory
- Can be in subdirectories (e.g., `.cursor/rules/trent/`)
- Include YAML frontmatter with `description`, `globs`, `alwaysApply`

**Cursor Commands:**
- Located in `.cursor/rules/*/commands/` directories
- Use `@command` prefix (not `/command`)
- Can reference rules and other commands

### Resources

- **Platform Comparison**: `.trent/PLATFORM_COMPARISON.md`
- **Cursor Architecture**: `.trent/CURSOR.md`
- **Official Cursor Docs**: https://docs.cursor.com
- **Platform Architecture Overview**: `.trent/PLATFORM_ARCHITECTURE.md`

---

*This consolidated rule provides all essential trent functionality in a single, efficient rule optimized for daily coding work.*