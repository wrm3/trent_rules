---
id: 47
title: 'Add Ralph Wiggum prevention rule (N failures → research-mode retry)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [autonomous, resilience, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [21, 23]
project_context: 'Ralph Wiggum loop = AI repeating the same failed approach until token limit — prevention requires explicit counting, mandatory approach change, and hard stop after 3 attempts; prevents the most expensive failure mode in autonomous operation'
---

# Task 047: Add Ralph Wiggum prevention rule

## Objective
Add the Ralph Wiggum Prevention Rule to the task rules in `template_v2/` — an explicit, numbered counter that forces approach changes after failures and mandates escalation after 3 total failures on the same task.

## Context
"Ralph Wiggum loop" (named for the Simple Minds song "Don't You Forget About Me" / Ralph's obliviousness in The Simpsons): an AI agent that keeps trying the same failed approach because it doesn't recognize it's in a loop. The fix is an explicit counter, not a warning — warnings get ignored, numbers don't.

## The Ralph Wiggum Prevention Rule

Add to `20_trent_tasks` rule in template_v2:

```markdown
## 🔄 Ralph Wiggum Prevention Rule (MANDATORY)

### The Rule
Count your failures. After 3 failures on the same task: STOP and escalate.

### Failure Counter Location
In the task YAML `failure_history` array (from task021). Count entries where `task_id` matches.

### What Counts as a Failure
- Code you wrote doesn't compile
- Acceptance criterion was not met after implementation  
- Evidence check fails during verification (counted as implementer failure)
- Resource was unavailable (NOT a Ralph Wiggum failure — these are environmental)
- Spec was outdated (NOT a failure — update spec and try once)

### The Three-Strike Protocol

**Strike 1**: Failure detected
→ Document in failure_history
→ Change approach — do NOT retry the same way
→ Web search for current best practice
→ Check git log for how similar work was done before
→ Continue with modified approach

**Strike 2**: Second failure
→ Document in failure_history
→ Change approach AGAIN — completely different method
→ Check SYSTEM_EXPERIMENTS.md for prior attempts
→ Consider: is the spec itself wrong? If so, update it (see task027)
→ Continue with new approach

**Strike 3**: Third failure
→ Document in failure_history (failure_reason: approach_exhausted)
→ Set status: failed
→ Update TASKS.md: [🔄] → [❌]
→ Add AI-IDEA entry to IDEA_BOARD.md with full context
→ git commit: "fail(task-{id}): Ralph Wiggum rule — 3 strikes, approach exhausted"
→ STOP. Do not attempt again.

### The Rule for Verifiers
If you are verifying a task and see failure_history.length >= 2:
→ Be extra skeptical — this task has already failed twice
→ Apply adversarial persona even harder than usual
→ Do NOT give benefit of the doubt

### The Rule for Cleanup Agent
Tasks with failure_history.length >= 3: 
→ Do NOT include in SPRINT.md
→ Flag in CLEANUP_REPORT.md as "needs human review"
→ Add to "Actions Required" section
```

## failure_history Entry Format (from task021)

```yaml
failure_history:
  - failure_number: 1
    failure_date: ''
    failure_reason: compilation_error | test_failure | approach_wrong | spec_outdated | resource_unavailable | approach_exhausted
    failed_approach: ''     # Brief description of what was tried
    error_details: ''       # Exact error message
    agent_id: ''            # Which agent hit this failure
    ralph_wiggum_count: 1   # Current count at time of failure
```

## Acceptance Criteria
- [ ] Ralph Wiggum Prevention Rule added to `20_trent_tasks` template rule
- [ ] Three-strike protocol documented (strike 1, 2, 3 actions)
- [ ] `ralph_wiggum_count` field in failure_history entry
- [ ] Cleanup agent exclusion rule for 3+ failure tasks documented
- [ ] Verifier skepticism rule for 2+ failure history documented

## Verification Steps
- [ ] Rule present in template_v2 rule files
- [ ] Three-strike protocol is explicit (not just "stop after failures")
- [ ] `ralph_wiggum_count` in task021 failure_history schema

## When Stuck
- Cross-reference task021 (failure taxonomy) — ralph_wiggum_count goes in that schema
- Cross-reference task023 (When Stuck protocol) — that's the tactical escape route this feeds into
