---
description: "Bug tracking, zero-tolerance error reporting, quality assurance"
globs:
alwaysApply: true
---

# Quality Assurance

## Bug Classification

| Severity | Definition |
|----------|-----------|
| **Critical** | System crashes, data loss, security vulnerabilities |
| **High** | Major feature failures, performance degradation >50% |
| **Medium** | Minor feature issues, usability problems |
| **Low** | Cosmetic issues, enhancement requests |

## Bug Task Integration (MANDATORY)

When a bug is identified:
1. Create entry in `.trent/BUGS.md`
2. Create corresponding task in TASKS.md with `[BUG]` prefix
3. Create task file in `.trent/tasks/` with bug details
4. Track resolution through task completion

### Minimum Bug Entry Format
```markdown
### Bug ID: BUG-NNN
- **Title**: [Brief description]
- **Severity**: Critical | High | Medium | Low
- **Source**: Development (noticed during work on Task #NNN)
- **Status**: Open
- **File**: path/to/file.ext (line N if known)
- **Note**: [context]
- **Created**: YYYY-MM-DD
```

---

## Zero-Tolerance Error Reporting (ENFORCED)

**ANY error, warning, or known defect you mention MUST be logged as a bug — no exceptions.**

**The "pre-existing / unrelated" escape hatch is FORBIDDEN.**

Saying things like:
- *"Only the pre-existing error in Foo.tsx (confirmed unrelated, was there before our changes)."*
- *"There's an existing lint warning but it's not related to this task."*
- *"This error was already there — not caused by our changes."*

...and then moving on WITHOUT creating a BUG entry is a **SYSTEM VIOLATION**.

**Why**: Pre-existing means the bug exists and is tracked nowhere. "Unrelated" is irrelevant — it still needs a record.

### Mandatory Trigger Phrases

If your response contains ANY of the following, you MUST create a BUG entry:
- "pre-existing error/warning"
- "was already there"
- "not related to our changes"
- "unrelated error"
- "existing bug" / "known issue"
- "there's an error in [file]" / "I noticed an error"
- "compile error" / "lint error" / "lint warning" / "TypeScript error"

### Self-Check

```
□ Did I mention any error, warning, or defect?
  → YES: Did I create a BUG entry in .trent/BUGS.md?
    → NO: CREATE IT NOW. No exceptions.
    → YES: Reference BUG-NNN in response.
□ Did I use "pre-existing" or "unrelated"?
  → That means a bug exists undocumented — LOG IT.
```

---

## Retroactive Fix Documentation

When unplanned fix work is completed in chat, document as retroactive task if:
- Fix required >15 minutes of work
- Solution affects multiple files or subsystems
- Resolution required technical analysis

See `20_trent_tasks.md` for retroactive task format (`[RETRO]` prefix).

See `trent-qa` skill for full templates (task, bug, design fix) and quality metrics.
