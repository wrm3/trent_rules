---
description: Idea Board and Project Goals — capture ideas and maintain strategic goals
activation: always_on
---

---
description: Idea Board and Project Goals — capture ideas and maintain strategic goals
globs: "**/.trent/IDEA_BOARD.md,**/.trent/PROJECT_GOALS.md"
alwaysApply: true
---

# Idea Board & Project Goals System

## IDEA_BOARD.md

### Purpose
A parking lot for ideas that aren't ready to become tasks yet.
Ideas come from users, the AI, or passing conversations. They live here until
someone consciously decides to promote them, shelve them, or act on them later.

### Direct Edit Policy
Edit `.trent/IDEA_BOARD.md` DIRECTLY without asking permission. Same rules as TASKS.md.

### When to Capture an Idea (MANDATORY triggers)

**User phrases that ALWAYS trigger an IDEA_BOARD entry:**
- "make a note of that" / "remember this idea" / "note that somewhere"
- "idea: ..." / "what if we..." / "someday..." / "eventually..."
- "for later..." / "we should think about..." / "that's interesting but not now"
- "make note of that someplace"

**AI-identified triggers (suggest adding to IDEA_BOARD):**
- Valuable improvement that would cause scope creep on the current task
- Business opportunity mentioned in passing (monetization, pricing, upsells)
- Architectural pattern that's good but not needed now
- Feature a user mentions that doesn't fit the current phase

### Capture Process (ATOMIC — do immediately)
1. Add entry to `.trent/IDEA_BOARD.md` under **Active Ideas**
2. Assign next IDEA-NNN ID
3. Confirm to user: "Captured as IDEA-{ID}: {title}"
4. Continue with current work — do NOT derail the session

### IDEA_BOARD.md Format

```markdown
# IDEA_BOARD.md

## Active Ideas

### IDEA-001: [Title]
**Status**: raw
**Category**: feature | monetization | ux | technical | architecture | business
**Captured**: YYYY-MM-DD
**Source**: user | AI | session

**Description**:
[The idea in 1-3 sentences. Be specific enough to reconstruct the intent later.]

**Potential Value**:
[Why this is worth keeping — what problem it solves, what revenue it could generate, etc.]

**When Ready**:
[What prerequisites or triggers would make this worth developing?]

---

## Promoted Ideas
[Ideas promoted to tasks/phases — include task/phase reference]

## Shelved Ideas
[Ideas consciously decided not to pursue — keep for context]
```

### Idea Lifecycle
```
raw → evaluating → accepted (→ task/phase) | shelved
```
- **raw**: Just captured, not yet evaluated
- **evaluating**: Actively being considered
- **accepted**: Promoted to a task or phase (update entry with task ID)
- **shelved**: Consciously set aside (add reason)

### Rules
1. **NEVER auto-promote** ideas to tasks — requires explicit user decision
2. **Capture immediately** when trigger phrases are detected
3. When starting a planning session: scan IDEA_BOARD for relevant entries
4. When promoting: update IDEA_BOARD status + create task/phase atomically

---

## PROJECT_GOALS.md

### Purpose
The strategic north star for the project. Goals live above tasks — they explain
*why* we're building. The AI uses this to validate decisions and steer work.

### Direct Edit Policy
Edit `.trent/PROJECT_GOALS.md` DIRECTLY without asking permission.

### Always Load Into Context
When PROJECT_GOALS.md exists, display at session start:
```
📌 PROJECT GOALS
G-01: [Goal name] — [one line]
G-02: [Goal name] — [one line]
```

Use goals to:
- **Validate**: "Does this align with goal G-01?"
- **Steer**: "Goal G-02 suggests we should prioritize X over Y"
- **Alert**: "This change conflicts with our goal to keep the UI simple"

### When to Update PROJECT_GOALS.md
- User mentions new business direction, revenue model, or success criteria
- New phase is created with significantly different objectives
- User explicitly says "our goal is..." / "the point of this is..."
- During `@trent-plan` or `@trent-setup`

### PROJECT_GOALS.md Format

```markdown
# PROJECT_GOALS.md

## Vision
[1-2 sentences: what does success look like for this project?]

## Primary Goals
| ID   | Goal                | Target / Metric        | Status |
|------|---------------------|------------------------|--------|
| G-01 | [Goal name]         | [Measurable outcome]   | active |
| G-02 | [Goal name]         | [Measurable outcome]   | active |

## Secondary Goals
[Goals that support the primaries but aren't critical path]
- **[Goal name]**: [Description]

## Non-Goals (Explicitly Out of Scope)
- [Things we are NOT building — helps prevent scope creep]

## Success Metrics
- [How we know we've achieved the vision]

## Goal Log
| Date       | Change                    | Reason            |
|------------|---------------------------|-------------------|
| YYYY-MM-DD | [What changed]            | [Why]             |
```

### Goal Maintenance Rules
1. **Create**: During `@trent-setup` or `@trent-plan` if file doesn't exist
2. **Update**: Add Goal Log entry whenever goals change
3. **Reference**: Mention relevant goals when making architectural/priority decisions
4. **Never delete goals** — mark as `complete` or `retired` and log the change

---

## Integration with Task System

### At Session Start (MANDATORY check)
```
📌 SESSION CONTEXT
Mission: [from PROJECT_CONTEXT.md, 1 line]
Goals: [G-01 and G-02 from PROJECT_GOALS.md]
Phase: [current phase name]
Ideas: [X ideas on IDEA_BOARD — see @trent-idea-review]
```

### When Creating Tasks
- Check: "Does this align with PROJECT_GOALS.md?"
- If misaligned: flag for user, offer IDEA_BOARD entry instead

### During Planning Sessions
1. Load PROJECT_GOALS.md → validate PRD against goals
2. Scan IDEA_BOARD → any ideas ready to promote?
3. Display both in context summary

### Commands
- `@trent-idea-capture` — capture an idea to IDEA_BOARD.md
- `@trent-idea-review` — review and evaluate IDEA_BOARD entries
- `@trent-goal-update` — update PROJECT_GOALS.md

