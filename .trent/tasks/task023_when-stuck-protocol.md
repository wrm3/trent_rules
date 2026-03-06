---
id: 23
title: 'Add "When Stuck" protocol section to task file template'
type: feature
status: pending
priority: high
phase: 0
subsystems: [resilience, template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1, 3]
project_context: '"When Stuck" gives agents explicit escape routes before they enter a Ralph Wiggum loop — defines when to stop, how to escalate, and what to document so the next agent does not repeat the same dead-end'
---

# Task 023: Add "When Stuck" protocol section to task file template

## Objective
Add a mandatory `## When Stuck` section to the task file template in `template_v2/`, and document the formal "When Stuck" protocol that agents follow when they hit a blocker, dead-end, or repeat failure.

## Context
Current task files already have an informal "When Stuck" section, but it's not standardized and doesn't define escalation paths. Agents that hit a wall often either (a) loop indefinitely trying the same approach, (b) silently mark the task done without completing it, or (c) abandon without documentation. The formal protocol gives a third option: stop, document, escalate.

## When Stuck Template (add to task file template)

```markdown
## When Stuck

**Before looping or abandoning, follow this protocol:**

### Step 1: Document the blocker (in execution_progress)
```yaml
execution_progress:
  blockers:
    - description: "What exactly is failing"
      approach_tried: "What you tried"
      error_or_result: "Exact error message or result"
      attempts: 1
```

### Step 2: Check failure_history
If `failure_history` already shows 2+ entries for the same blocker type:
→ DO NOT try a third time
→ Skip to Step 4 (escalate)

### Step 3: Try one alternative approach
- Research: web search for current best practice
- Check: git log for how similar problems were solved in this project
- Check: SYSTEM_EXPERIMENTS.md for past attempts on this subsystem
- Try: a different implementation path (not the same one again)

### Step 4: Escalate and exit cleanly
If still blocked after one alternative:
1. Update task YAML: `status: failed`, `failure_reason: approach_exhausted`
2. Update `failure_history` with details
3. Update TASKS.md: change `[🔄]` to `[❌]`
4. Add an AI-IDEA to IDEA_BOARD.md: "This blocker needs human review: {details}"
5. Git commit: `"chore(task-{id}): escalate — approach exhausted, needs human review"`
6. STOP — do not attempt more approaches

### Escalation Ladder
| Attempts | Action |
|----------|--------|
| 1st failure | Try alternative approach |
| 2nd failure | Research + try different path |
| 3rd failure | Escalate: set failed, add IDEA_BOARD entry, commit, stop |

**Ralph Wiggum Rule**: More than 3 attempts at the same task with same failure = loop.
The loop does not get better with more attempts. Stop and escalate.
```

## Project-Specific Hints (customize per task)

Each task file should also have project-specific hints in its `## When Stuck` section. For example, task004:

```markdown
### Task-Specific Hints
- This is a pure template task — no logic required
- If unsure about field names, see task003 (YAML schema) for consistent naming
- The cleanup agent (task040) defines the population logic — don't invent it here
```

## Acceptance Criteria
- [ ] Task file template in template_v2 has `## When Stuck` section
- [ ] When Stuck section includes the 4-step protocol
- [ ] Escalation ladder table is present
- [ ] Ralph Wiggum Rule is explicitly named
- [ ] `failure_reason: approach_exhausted` documented as a valid failure_reason (cross-ref task021)
- [ ] Template includes placeholder for task-specific hints

## Verification Steps
- [ ] Template has When Stuck with the protocol
- [ ] Escalation ladder (1st/2nd/3rd failure) is documented
- [ ] Ralph Wiggum Rule named and explained
- [ ] task021 failure taxonomy includes `approach_exhausted`

## When Stuck (meta)
- This is documentation of a protocol — just write the markdown
- Cross-reference task021 for failure_reason values — use consistent terminology
