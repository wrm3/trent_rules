---
id: 46
title: 'Add cost_per_task tracking fields + subsystem cost aggregation'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [autonomous, template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 41]
project_context: 'AI bills are $3000-4000/month — knowing which subsystems and tasks consume the most cost helps prioritize what to automate with cheaper local models vs expensive paid APIs'
---

# Task 046: Add cost_per_task tracking fields + subsystem cost aggregation

## Objective
Add `execution_cost` tracking fields to the task YAML schema in `template_v2/`, and add cost aggregation to the CLEANUP_REPORT.md template and health score calculation.

## YAML Fields to Add

```yaml
execution_cost:
  model_used: ''           # e.g., "claude-sonnet-4-5", "local-llama-3", "claude-opus-4"
  estimated_cost_usd: 0.0  # Estimated cost (agent fills in based on token usage)
  actual_cost_usd: 0.0     # Actual cost if available from API response
  input_tokens: 0
  output_tokens: 0
  api_calls: 0             # Number of API calls made
  duration_minutes: 0      # Wall clock time
  cost_tier: free | low | medium | high  # free: local LLM, low: <$0.10, medium: $0.10-1.00, high: >$1.00
```

## Cost Aggregation (add to CLEANUP_REPORT.md template)

```markdown
### Cost Report (Last 7 Days)

| Subsystem | Total Cost | Tasks | Avg Cost/Task | Most Expensive Task |
|-----------|------------|-------|---------------|---------------------|
| {name} | ${total} | {n} | ${avg} | task-{id} (${cost}) |

**Project Total (7 days)**: ${total}
**Escalation Savings**: {n} tasks run on local LLM = ~${saved} saved vs paid model

### Model Usage Breakdown
| Model | Tasks | Cost | Use Case |
|-------|-------|------|----------|
| local-llama | {n} | $0.00 | Simple template tasks |
| claude-sonnet | {n} | ${} | Standard implementation |
| claude-opus | {n} | ${} | Complex/escalated tasks |
```

## Escalation Ladder Cost Tracking

When an agent escalates to a more expensive model (task047/048), it should:
1. Log the escalation: `escalation_model_change: "local → sonnet"` in execution_cost
2. Record why: `escalation_reason: "local model failed 2x at task complexity"`
3. This data helps optimize: which task types should START on which model

## Health Score Impact

Add to health score calculation:
- Subsystem with avg_cost_per_task > $2.00: flag as "expensive subsystem" in CLEANUP_REPORT
- Tasks with cost_tier: high that are `ai_safe: true`: suggest review (paying a lot for unattended work)

## Acceptance Criteria
- [ ] `execution_cost:` YAML block added to task003 schema
- [ ] `cost_tier` enum documented (free/low/medium/high)
- [ ] Cost aggregation table added to task041 CLEANUP_REPORT template
- [ ] Escalation cost tracking fields defined
- [ ] Health score impact from cost documented

## Verification Steps
- [ ] task003 schema has `execution_cost` block
- [ ] task041 CLEANUP_REPORT template has cost report section
- [ ] cost_tier enum defined with dollar ranges

## When Stuck
- Pure schema + documentation task
- The agent filling in `estimated_cost_usd` uses the token counts × model pricing from the response headers
