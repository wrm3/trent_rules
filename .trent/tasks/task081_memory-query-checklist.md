---
id: 81
title: 'Add institutional memory query to agent pre-task checklist'
type: feature
status: pending
priority: high
phase: 0
subsystems: [memory, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [34, 80]
project_context: 'An autonomous agent starting a task at 2am should query memory for what happened in this subsystem last time — prevents repeating past mistakes and gives context that git log alone does not provide'
---

# Task 081: Add institutional memory query to pre-task checklist

## Objective
Add a mandatory memory query step to the agent pre-task checklist in `template_v2/` — before starting any task, agents query the memory system for relevant prior context on that subsystem.

## The Memory Query Step

Add to Pre-Mortem / Pre-Implementation Checks (task034):

```markdown
### Memory Context Query (Mandatory)

Before starting implementation, query the memory system:

```python
# Query for prior context on this subsystem
context = memory_context(
    project_id="{project_id}",
    query="recent work in {subsystem} subsystem",
    budget_tokens=2000
)

# If context found — review it for:
# - Recent completions in this subsystem (what changed?)
# - Recent failures in this subsystem (what NOT to repeat?)
# - Lessons learned from similar tasks
```

**What to look for in memory results:**
- `[COMPLETED]` entries → recent completed tasks in subsystem (don't undo their work)
- `[FAILED]` entries → approaches that didn't work (don't repeat them)
- `[LESSON]` entries → explicit guidance from prior agents

**If memory returns no results:** Note in Pre-Mortem that this is a "cold start" in this subsystem — proceed with extra care.

**If memory MCP is unavailable:** Check `.trent/memory/` folder for any local memory files.
```

## Integration with Execution Progress

Add to execution_progress notes when relevant memory was found:

```yaml
execution_progress:
  notes: "Memory context: Found 3 prior completions in {subsystem}. Note: task{N} previously tried {approach} and it failed — using {alternative_approach} instead."
```

## Acceptance Criteria
- [ ] Memory query step added to Pre-Mortem pre-implementation checklist (task034 template)
- [ ] memory_context() call template with correct parameters
- [ ] "What to look for" guidance documented
- [ ] Cold start case documented
- [ ] Fallback to local .trent/memory/ documented
- [ ] Integration with execution_progress notes

## Verification Steps
- [ ] Pre-implementation checklist has memory query step
- [ ] memory_context() call is the right MCP tool (verify against AGENTS.md tool list)
- [ ] Cold start case handled

## When Stuck
- Check AGENTS.md for the exact memory_context() tool signature
- This step should happen BEFORE the Pre-Mortem, not after — having context before thinking about failure modes is more useful
