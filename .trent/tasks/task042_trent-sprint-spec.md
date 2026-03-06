---
id: 42
title: 'Create @trent-sprint command spec (2-hour sprint agent responsibilities)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [autonomous, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [40, 41, 43, 44]
project_context: 'The sprint agent is the workhorse of autonomous operation — runs every 2 hours, claims tasks from SPRINT.md, executes them, updates evidence, transitions to [🔍] — this spec defines exactly what it does and does not do'
---

# Task 042: Create @trent-sprint command spec

## Objective
Create the `@trent-sprint` command template in `template_v2/` — the specification for the 2-hour sprint agent that claims and executes tasks from SPRINT.md autonomously.

## Sprint Agent Workflow

```
1. INITIALIZATION (always runs first)
   a. Read PROJECT_CONTEXT.md — load constraints, health, sprint config
   b. Read ARCHITECTURE_CONSTRAINTS.md — commit to memory
   c. Check SPRINT.md — is it still valid? (valid_until not expired)
   d. If SPRINT.md expired: wait for cleanup agent or skip session
   e. git pull — sync to latest state
   f. Scan for any tasks another agent left in [🔄] with expired TTL — skip them (cleanup handles)

2. TASK SELECTION
   a. Read SPRINT.md eligible task list
   b. Filter: skip any task already claimed (claimed_by is set)
   c. Filter: skip requires_solo_agent: true if other active claims detected
   d. Select highest-priority available task
   e. If no tasks available: write note to CLEANUP_REPORT and exit cleanly

3. TASK CLAIMING (atomic)
   a. Read task YAML — confirm status: pending
   b. Update task YAML: claimed_by, claimed_at, claim_expires_at, status: in_progress
   c. Update TASKS.md: [📋] → [🔄]
   d. IMMEDIATELY git commit: "claim(task-{id}): {agent_id}"
   e. If git commit fails (conflict): abort claim, select different task

4. PRE-IMPLEMENTATION
   a. Fill Pre-Mortem section
   b. Run spec freshness check (see task027)
   c. Verify resource_requirements are available
   d. If any check fails: set resource_gated or spec_outdated status, commit, exit

5. IMPLEMENTATION
   a. Checkpoint every ~15 minutes (execution_progress)
   b. Follow task acceptance criteria in order
   c. DO NOT scope-creep — if you find related improvements, add to IDEA_BOARD, don't do them now
   d. DO NOT modify other tasks' files
   e. Commit frequently: after each acceptance criterion is met

6. COMPLETION
   a. Fill evidence_of_completion section
   b. Update task YAML: status: awaiting_verification
   c. Update TASKS.md: [🔄] → [🔍]
   d. git commit: "impl(task-{id}): complete — awaiting verification"
   e. DO NOT mark the task [✅] — that requires a different agent

7. MULTI-TASK SPRINT
   a. If time remains in sprint window: return to step 2 (select next task)
   b. Maximum tasks per sprint: 15 (or PROJECT_CONTEXT.md setting)
   c. After last task: write sprint summary to CLEANUP_REPORT.md append section

8. CLEAN EXIT
   a. If hitting token limit: checkpoint current state, release claim cleanly
   b. git commit: "checkpoint(task-{id}): sprint ending — state saved, resumable"
   c. Exit — do not leave tasks in ambiguous state
```

## What Sprint Agent MUST NOT Do
- Mark tasks `[✅]` — only verification agents do this
- Modify tasks not in the sprint list
- Skip the claim-commit (step 3d) — this is how other agents know you're working
- Ignore ARCHITECTURE_CONSTRAINTS.md
- Continue past 3 failures on the same approach (Ralph Wiggum rule)
- Modify TASKS.md other than status changes for claimed tasks

## Acceptance Criteria
- [ ] `@trent-sprint` command template created in `template_v2/.cursor/commands/`
- [ ] Full 8-step workflow documented
- [ ] "MUST NOT" list documented
- [ ] Clean exit protocol (token limit / connection loss) documented
- [ ] Parity: command created in `.claude/commands/` and `.agent/commands/`

## Verification Steps
- [ ] Command file exists in all 3 IDE command directories
- [ ] Workflow steps 1-8 all present
- [ ] Ralph Wiggum rule referenced in implementation step
- [ ] Clean exit documented

## When Stuck
- task040 (cleanup spec) and task043 (atomic claiming) are prerequisites for full context
- The core principle: sprint agent CLAIMS and IMPLEMENTS, never VERIFIES
