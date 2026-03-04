---
description: "Task expansion, complexity scoring, story points, sub-task creation"
globs:
alwaysApply: true
---

# Task Expansion & Workflow

## Complexity Scoring (1-10+ scale)

| Criterion | Points |
|-----------|--------|
| Estimated Effort >2-3 days | 4 |
| Cross-Subsystem Impact | 3 |
| Multiple Unrelated Components | 3 |
| High Uncertainty | 2 |
| Multiple Distinct Outcomes | 2 |
| Dependency Blocking | 2 |
| Exceptionally Long Requirements | 1 |
| >5 Story Points | 1 |

### Complexity Matrix

| Score | Level | Action |
|-------|-------|--------|
| 0-3 | Simple | Proceed normally |
| 4-6 | Moderate | SHOULD expand (recommended) |
| 7-10 | Complex | **Expansion MANDATORY** |
| 11+ | High Complex | **MUST expand before creation** |

---

## Sub-Task Creation

**Filename**: `task{parent_id}-{sub_id}_name.md` (hyphens, not dots)

```yaml
---
id: "42-1"
title: 'Setup Database'
type: task
status: pending
priority: high
parent_task: 42
dependencies: []
---
```

### Expansion Workflow

1. Score complexity using criteria above
2. **Shared Module Check**: If task introduces reusable logic, add extraction sub-task as FIRST sub-task (see `04_code_reusability.md`)
3. Break into logical, sequential sub-goals aligned with subsystem boundaries
4. Create sub-task files directly (no approval prompts needed)
5. Update parent task to reference expansion

---

## Story Points

| SP | Effort | Guidance |
|----|--------|----------|
| 1 | < 1 hour | Minor fixes |
| 2 | 1-4 hours | Small features |
| 3 | 4-8 hours | Medium complexity |
| 5 | 1-2 days | Complex features |
| 8 | 2+ days | **Requires sub-task expansion** |

See `trent-workflow` skill for sprint planning, kanban, and visualization templates.
