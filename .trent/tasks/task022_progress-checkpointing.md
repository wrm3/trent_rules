---
id: 22
title: 'Implement mid-task progress checkpointing (execution_progress in task YAML)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [resilience]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 20]
project_context: 'When an agent loses power/connection/token budget mid-task, the next agent must know where to resume — execution_progress prevents re-doing completed work and prevents incomplete work being skipped'
---

# Task 022: Implement mid-task progress checkpointing

## Objective
Add an `execution_progress` section to the task YAML schema (and the task file template) that agents update as they complete each acceptance criterion, enabling the next agent to resume from the exact checkpoint rather than restarting from scratch.

## Context
"Shit happens" — computers bluescreen, connections drop, token budgets hit. The current system has no recovery beyond "restart the task." The checkpoint system means a task that was 80% done at crash can be resumed at 80%, not 0%.

## YAML Addition to Task Files

Add to each task file, below the frontmatter, as a live-updated section:

```yaml
## Execution Progress
<!-- Updated by agent during execution — DO NOT EDIT MANUALLY -->
```

```yaml
execution_progress:
  last_updated: ''           # ISO timestamp of last checkpoint
  last_updated_by: ''        # agent_id that wrote this checkpoint
  percent_complete: 0        # 0-100 rough estimate
  completed_criteria:        # acceptance criteria that are DONE (copy text from task)
    - ''
  current_step: ''           # What the agent is actively working on right now
  next_step: ''              # What to do next if resuming from checkpoint
  files_modified: []         # List of files already changed (don't redo)
  files_created: []          # List of files already created
  blockers: []               # Any blockers discovered during execution
  notes: ''                  # Free-form notes for the resuming agent
```

## Checkpoint Protocol (rules for agents)

### When to checkpoint (write to execution_progress):
1. After completing each acceptance criterion
2. Before any destructive operation (delete, overwrite, migration)
3. Every ~15 minutes of active work
4. Immediately before requesting resources (API call, large computation)
5. After any git commit

### How to checkpoint:
```yaml
# In the task file, update execution_progress:
execution_progress:
  last_updated: "2026-03-06T02:30:00Z"
  last_updated_by: "cursor-agent-session-abc123"
  percent_complete: 45
  completed_criteria:
    - "File exists at template_v2/.trent/SPRINT.md"
    - "Sprint Rules section is present and complete"
  current_step: "Adding Exclusion Summary table"
  next_step: "Verify all placeholder fields use {curly_brace} format"
  files_modified:
    - "template_v2/.trent/SPRINT.md"
  files_created:
    - "template_v2/.trent/SPRINT.md"
```

### Resume protocol (when picking up a checkpointed task):
1. Read `execution_progress.completed_criteria` — skip these
2. Start from `execution_progress.next_step`
3. Check `execution_progress.files_modified` — don't re-create already-created files
4. Update `last_updated_by` to your own agent_id
5. Clear `current_step` when done (or set to "COMPLETE — awaiting verification")

## Acceptance Criteria
- [ ] `execution_progress:` YAML block added to task003 (task YAML schema)
- [ ] Checkpoint protocol documented in template_v2 rule files
- [ ] Task file template (in template_v2) includes `execution_progress:` section with empty values
- [ ] "When Stuck" section in task template references execution_progress

## Verification Steps
- [ ] task003 YAML schema includes execution_progress block
- [ ] Task file template has the section
- [ ] Protocol (when to checkpoint, how to resume) is in the rules

## When Stuck
- This is schema + documentation — no runtime code needed
- The AI agent writes directly to the task YAML file as its checkpoint log
