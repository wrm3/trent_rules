---
description: Idea Board and Project Goals — capture ideas and maintain strategic goals
globs: "**/.trent/IDEA_BOARD.md,**/.trent/PROJECT_GOALS.md"
alwaysApply: true
---

# Idea Board & Project Goals

## IDEA_BOARD.md

### MANDATORY Capture Triggers

**User phrases that ALWAYS trigger an IDEA_BOARD entry:**
- "make a note of that" / "remember this idea" / "note that somewhere"
- "idea: ..." / "what if we..." / "someday..." / "eventually..."
- "for later..." / "we should think about..." / "that's interesting but not now"

**AI-identified triggers (suggest adding):**
- Improvement that would cause scope creep on current task
- Business opportunity mentioned in passing
- Architectural pattern not needed now
- Feature that doesn't fit current phase

### Capture Process (ATOMIC)

1. Add entry to `.trent/IDEA_BOARD.md` under Active Ideas
2. Assign next IDEA-NNN ID
3. Confirm: "Captured as IDEA-{ID}: {title}"
4. Continue current work — do NOT derail session

### Idea Entry Format

```markdown
### IDEA-NNN: [Title]
**Status**: raw | evaluating | accepted | shelved
**Category**: feature | monetization | ux | technical | architecture | business
**Captured**: YYYY-MM-DD
**Description**: [1-3 sentences]
**Potential Value**: [Why worth keeping]
```

### Rules

1. **NEVER auto-promote** ideas to tasks — requires explicit user decision
2. **Capture immediately** when trigger phrases detected
3. When promoting: update IDEA_BOARD status + create task/phase atomically

---

## PROJECT_GOALS.md

### Purpose

Strategic north star. Goals live above tasks — they explain *why* we're building.

### Display at Session Start (when file exists)

```
Goals: G-01: [name] | G-02: [name]
```

Use goals to validate decisions, steer priorities, and alert on conflicts.

### When to Update

- User mentions new business direction, revenue model, or success criteria
- New phase created with different objectives
- User says "our goal is..." / "the point of this is..."
- During `trent-plan` or `trent-setup`

### Goal Entry Format

```markdown
| ID   | Goal          | Target / Metric      | Status |
|------|---------------|----------------------|--------|
| G-01 | [Goal name]   | [Measurable outcome] | active |
```

### Maintenance Rules

1. **Create** during `trent-setup` or `trent-plan` if missing
2. **Update** with Goal Log entry whenever goals change
3. **Reference** relevant goals in architectural/priority decisions
4. **NEVER delete goals** — mark as `complete` or `retired` and log the change

### When Creating Tasks

- Check alignment with PROJECT_GOALS.md
- If misaligned: flag for user, offer IDEA_BOARD entry instead
