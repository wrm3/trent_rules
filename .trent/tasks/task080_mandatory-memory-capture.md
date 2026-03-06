---
id: 80
title: 'Make memory capture mandatory at task completion'
type: feature
status: pending
priority: high
phase: 0
subsystems: [memory, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [70]
project_context: 'Memory capture is currently optional and frequently skipped — making it mandatory at task completion means every completed task generates a memory record, building institutional knowledge automatically over time'
---

# Task 080: Make memory capture mandatory at task completion

## Objective
Update the task completion workflow in `template_v2/` to make memory capture a mandatory step — not optional. Every `[✅]` completion must generate a memory record.

## The Mandatory Memory Capture Step

Add as Step 5 in the Task Completion Workflow (after git commit, before final confirmation):

```markdown
## Step 5: Memory Capture (MANDATORY — do not skip)

After task is marked [✅] and commit is made, call the memory MCP tool:

```python
memory_capture_session(
    project_id="{project_id from PROJECT_CONTEXT.md}",
    session_summary="""
    Task {ID}: {title} — COMPLETED
    
    Subsystem: {subsystem}
    Phase: {phase}
    Agent: {agent_id}
    Model: {model_used}
    
    What was accomplished:
    {bullet list of what was done — from completed acceptance criteria}
    
    Key decisions made:
    {any approach choices, tradeoffs, or design decisions}
    
    Files changed:
    {from execution_progress.files_modified}
    
    Lessons learned:
    {anything that would help the next agent on this subsystem}
    
    Evidence of completion:
    {brief summary of how verification was confirmed}
    """,
    tags=["{subsystem}", "task-completion", "phase-{N}"]
)
```

**If memory MCP is unavailable**: Write the same content to `.trent/memory/task_{ID}_completion.md` as fallback.

**Self-check**: Before marking response complete:
- [ ] memory_capture_session was called OR fallback file was written
- [ ] Did NOT skip because it seemed optional — it is NOT optional
```

## Why This Matters

Add to rule documentation:

> Memory capture at task completion is how the system learns. When an autonomous agent starts a task at 2am and the previous agent left a memory record, the new agent has context it cannot get from reading code alone. Skipping memory capture degrades every future agent's context. The cost is ~30 seconds of prompt writing. The benefit accumulates over every future session.

## Acceptance Criteria
- [ ] Task completion workflow in rule 20 (template_v2) has Step 5: Memory Capture
- [ ] memory_capture_session call template documented
- [ ] Fallback (local file) documented
- [ ] "Not optional" language is explicit
- [ ] Tags include subsystem and phase

## Verification Steps
- [ ] Step 5 exists in task completion workflow
- [ ] memory_capture_session call has required fields
- [ ] Fallback path documented

## When Stuck
- This adds a step to the task completion workflow in rule 20 (task070)
- If task070 hasn't been done yet, add this step to the task070 spec as an additional requirement
