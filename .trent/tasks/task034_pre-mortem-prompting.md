---
id: 34
title: 'Add pre-mortem prompting as mandatory pre-implementation step to task template'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [verification, template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 23]
project_context: 'Pre-mortem prompting asks the agent "how will this fail?" BEFORE starting — surfaces known risks, prevents blindly following a doomed approach, and creates a written record of anticipated failure modes'
---

# Task 034: Add pre-mortem prompting to task template

## Objective
Add a mandatory `## Pre-Mortem` section to the task file template in `template_v2/`, and document the pre-mortem prompting protocol that implementing agents run before writing any code.

## Context
From the agent honesty research: agents that explicitly reason about "how could this fail?" before starting find more edge cases and produce more robust implementations than agents that go straight to coding. The pre-mortem is also a commitment device — the agent writes down anticipated failure modes, which makes it harder to later pretend those modes weren't foreseeable.

## Pre-Mortem Template Section

Add to each task file:

```markdown
## Pre-Mortem

**Implementing agent fills this in BEFORE writing code.**
*Prompt: "Imagine you have already implemented this task and it failed. What went wrong?"*

### Anticipated Failure Modes
- [ ] **{Failure mode 1}**: {How likely? What would I do to prevent it?}
- [ ] **{Failure mode 2}**: {How likely? What would I do to prevent it?}

### Dangerous Assumptions
- Assuming {X} is true — if it's not, the implementation will break because {Y}
- Assuming {X} exists/is available — verify before proceeding

### Riskiest Part
**The single most likely point of failure**: {specific component or operation}
**Mitigation**: {what I'll do to reduce that risk}

### Pre-Implementation Checks
- [ ] I have read the ARCHITECTURE_CONSTRAINTS.md
- [ ] I have checked git log for context on how similar work was done
- [ ] I have verified spec_dependencies are completed and current
- [ ] I have confirmed required resources are available
```

## Pre-Mortem Prompt (for agents)

When starting any task, run this internal reasoning before coding:

```
"Imagine it's tomorrow morning. You implemented this task last night and it failed.
The task is marked [❌]. What happened?

List 3-5 things that could have gone wrong:
1. ...
2. ...
3. ...

Now, what would you do differently knowing those risks?
Write those mitigations into the Pre-Mortem section of the task file."
```

## Why Pre-Mortems Work

Include in rule documentation:

> A pre-mortem is a prospective hindsight exercise. Research shows that imagining a failure HAS occurred (vs. might occur) increases the ability to identify failure causes by up to 30% (Klein, 2007). For AI agents, the additional benefit is: it breaks the default "let's get started" momentum that causes agents to skip edge case analysis. The pre-mortem creates a written commitment to the failure modes identified — making it harder to rationalize away problems during implementation.

## Acceptance Criteria
- [ ] Task file template has `## Pre-Mortem` section
- [ ] Pre-mortem prompt text is included in the template
- [ ] "Dangerous Assumptions" subsection present
- [ ] "Riskiest Part" field present
- [ ] Pre-implementation checklist present
- [ ] Brief explanation of why pre-mortems work included in rule documentation

## Verification Steps
- [ ] Task file template has the Pre-Mortem section
- [ ] All four subsections present (Failure Modes, Dangerous Assumptions, Riskiest Part, Checklist)
- [ ] Pre-mortem prompt is actionable (clear what the agent should imagine)

## When Stuck
- Pure template/documentation task
- The key phrasing: "Imagine you have ALREADY implemented this task and it FAILED" — past tense, not future
- The past-tense framing is what makes the exercise work psychologically
