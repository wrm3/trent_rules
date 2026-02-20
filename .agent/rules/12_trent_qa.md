---
description: "trent quality assurance - bug tracking, design fix documentation, and quality management"
activation: "always_on"
---

# trent Quality Assurance System

## Bug Classification

- **Critical**: System crashes, data loss, security vulnerabilities
- **High**: Major feature failures, performance degradation >50%
- **Medium**: Minor feature issues, usability problems
- **Low**: Cosmetic issues, enhancement requests

## Bug Tracking Integration

When a bug is identified:
1. Create entry in `.trent/BUGS.md`
2. Create corresponding task in `.trent/TASKS.md` with `[BUG]` prefix
3. Create task file in `.trent/tasks/` with `type: bug_fix`
4. Link bug to affected phases
5. Track resolution through task completion

### Bug Task Template

```yaml
---
id: {next_available_id}
title: '[BUG] {Brief description}'
type: bug_fix
status: pending
priority: {severity}
phase: {affected_phase}
subsystems: {affected_subsystems}
bug_reference: BUG-{number}
severity: critical|high|medium|low
source: user_reported|development|testing|production
reproduction_steps: {steps}
expected_behavior: {what should happen}
actual_behavior: {what actually happens}
---
```

## Bug Lifecycle

1. Discovery → 2. Document in BUGS.md → 3. Create task → 4. Investigate → 5. Fix → 6. Verify → 7. Close

## Retroactive Fix Documentation

Document ad-hoc fixes completed in conversation when:
- ✅ Fix required >15 minutes
- ✅ Fix affects multiple files or subsystems
- ✅ Fix provides future reference value

Skip documentation for: typos, minor formatting, clarification-only

### Retroactive Task Template

```yaml
---
id: {next_available_id}
title: '[RETROACTIVE] {Description}'
type: retroactive_fix
status: completed
created_date: '{date}'
completed_date: '{date}'
retroactive: true
retroactive_reason: '{why documented after the fact}'
---
```

Retroactive tasks CAN go directly from creation to `[✅]`.

## Quality Gates

- Code review required for all changes
- Unit tests, integration tests, manual testing
- Performance regression testing for large changes
- Security scanning for auth/data changes

## "The Carver" Joke

If any database operation causes data loss or drops tables: any active persona jokes: "I pulled a 'Carver'" or "The Carver must have done it."

## BUGS.md Format

```markdown
# Bug Tracking

## Active Bugs

### Bug ID: BUG-001
- **Title**: [Brief description]
- **Severity**: [Critical/High/Medium/Low]
- **Status**: [Open/Investigating/Fixing/Testing/Closed]
- **Task Reference**: [task ID]
- **Created**: [Date]
```
