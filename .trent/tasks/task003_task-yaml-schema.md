---
id: 3
title: 'Create Updated Task YAML Schema with All vNext Fields'
type: feature
status: pending
priority: critical
phase: 0
subsystem: template-core
ai_safe: true
requires_solo_agent: false
blast_radius: low
requires_verification: true
verified_by: null
spec_version: 1
spec_last_verified: "2026-03-05"
allow_spec_update: false
estimated_duration_minutes: 60
claim_ttl_minutes: 120
dependencies: [1]
---

# Task 003: Create Updated Task YAML Schema with All vNext Fields

## Objective
Create the definitive task file template in `template_v2/.trent/templates/task_template.md`
with all new YAML fields from the vNext design. This schema is the source of truth for
all task files in vNext projects.

## Acceptance Criteria
- [ ] Full YAML schema documented with all new fields
- [ ] Every field has inline comment explaining purpose
- [ ] Required vs optional fields clearly distinguished
- [ ] Example values provided for every field
- [ ] Status progression documented in the template
- [ ] "When Stuck" section included in template body
- [ ] Saved to `template_v2/.trent/templates/task_template.md`
- [ ] Git commit: `feat(template-v2): add vNext task YAML schema`

## Full Schema to Implement

```yaml
---
# === IDENTITY ===
id: {number or SUBSYSTEM-NNN}
title: 'Task Title'
type: feature | bug_fix | refactor | documentation | research | retroactive_fix
status: pending | in-progress | awaiting-verification | completed | failed | harvested | paused | resource-gated

# === PRIORITY & PHASE ===
priority: critical | high | medium | low
phase: 0
subsystem: subsystem-name        # Primary subsystem (stable identifier)
milestone: milestone-name        # Optional: delivery target (temporal)
concern: feature | bug | refactor | experiment | maintenance

# === AUTONOMY FLAGS ===
ai_safe: true | false            # Safe for unattended autonomous execution
requires_solo_agent: true | false  # No other agents may touch this subsystem simultaneously
blast_radius: low | medium | high
blast_radius_reason: "Why this blast radius"
affected_files_estimate: 3       # Agent's estimate before starting
actual_files_changed: null       # Filled on completion

# === CLAIM / TTL (Resilience) ===
claimed_by: null                 # Agent ID that claimed this task
claimed_at: null                 # ISO-8601 timestamp
estimated_duration_minutes: 60
claim_ttl_minutes: 90            # Auto: estimated_duration * 1.5
claim_expires_at: null           # Auto: claimed_at + claim_ttl_minutes
last_heartbeat: null             # Updated by agent every N minutes on long tasks

# === VERIFICATION ===
requires_verification: true      # Default true for all code tasks
verified_by: null                # Must be different agent from implementing agent
verified_date: null
evidence_of_completion:
  type: null                     # test_output | compile_log | runtime_log | manual_check
  path: null                     # .trent/logs/task{id}_evidence.log

# === SPEC MANAGEMENT ===
spec_version: 1
spec_last_verified: "YYYY-MM-DD"
allow_spec_update: true          # Agent may update spec if approach is outdated
spec_dependencies: []
# spec_dependencies format:
# - name: library-name
#   pinned_version: "1.2.3"
#   last_verified: "YYYY-MM-DD"

# === FAILURE HISTORY ===
failure_history: []
# failure_history entry format:
# - attempt: 1
#   date: "YYYY-MM-DD"
#   agent: agent-id
#   failure_reason: compilation_error | test_failure | resource_unavailable | spec_outdated | approach_wrong | dependencies_missing | escalation_needed | timeout | agent_timeout
#   failure_note: "Human readable description"
#   failure_log: ".trent/logs/task{id}_attempt{N}.log"

# === PROGRESS CHECKPOINTING ===
execution_progress:
  last_checkpoint: null
  checkpoint_date: null
  completed_steps: []
  remaining_steps: []
  checkpoint_note: null

# === COST TRACKING ===
execution_cost:
  model_used: null
  input_tokens: null
  output_tokens: null
  estimated_cost_usd: null
  review_cost_usd: null
  total_cost_usd: null

# === STANDARD FIELDS ===
project_context: "How this task connects to project goals"
dependencies: []                 # Task IDs that must complete first
tags: []
created_date: "YYYY-MM-DD"
completed_date: null
rules_version: null              # Rules version when task was completed
---

# Task {id}: {title}

## Objective
[Clear, actionable goal — what will be true when this task is done]

## Context
[Why this task exists, what problem it solves, links to related docs]

## Acceptance Criteria
- [ ] [Specific, verifiable outcome]
- [ ] [Specific, verifiable outcome]
- [ ] [All criteria must be independently testable]

## Implementation Notes
[Technical details, approach, gotchas, links to relevant code]

## Verification
[What the reviewer should check — independent of implementer's self-assessment]
- [ ] [What to verify]
- [ ] Run: `[command to test]`

## When Stuck

### If [specific error/problem]:
[Specific diagnostic step]

### If approach fails after 2 attempts:
[Fallback approach or alternative]

### Escalation trigger:
[What specifically should cause this task to be escalated to human review]

### Safe to skip if:
[Conditions under which this task can be deferred]
```
