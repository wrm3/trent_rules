---
id: 66
title: 'Create platform parity enforcement rule (cross-IDE rule diff check)'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [platform-docs, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1]
project_context: 'Rules in .cursor/, .claude/, .agent/ must stay in sync — when one is updated, all must be updated; the parity rule is the enforcement mechanism that catches drift before it causes inconsistent behavior across IDEs'
---

# Task 066: Create platform parity enforcement rule

## Objective
Create a platform parity enforcement rule in `template_v2/` that mandates cross-IDE synchronization of rules, agents, skills, and commands — preventing the drift that causes different AI tools to behave differently on the same project.

## The Parity Rule

Add to `template_v2/.cursor/rules/` (and .claude, .agent):

```markdown
## 🔄 Platform Parity Enforcement (MANDATORY)

### The Rule
If you modify a rule, command, agent, or skill in ANY IDE directory, you MUST apply the same change to ALL three IDE directories in the same response.

### Three IDE Directories That Must Stay in Sync
- `.cursor/rules/*.mdc` — Cursor IDE (Markdown Cursor format)
- `.claude/rules/*.md` — Claude Code (standard markdown)
- `.agent/rules/*.md` — Gemini/other agents (standard markdown)

### What Must Stay in Parity

| File Type | Location Pattern | Parity Required |
|-----------|-----------------|-----------------|
| Core rules (00-09) | `*/rules/0*_*.md` | ✅ YES — identical content |
| Trent rules (20-29) | `*/rules/2*_*.md` | ✅ YES — identical content |
| Silicon Valley persona | `*/rules/silicon_valley*.md` | ✅ YES |
| IDE-specific features | `.cursor/rules/cursor_*.mdc` | ❌ NO — cursor only |
| Agent definitions | `*/agents/*.md` | ✅ YES — identical |
| Skills | `*/skills/*/SKILL.md` | ✅ YES — identical |
| Commands | `*/commands/*.md` | ⬜ VERIFY — may differ by IDE prefix |

### Parity Check Protocol

When completing any rule/agent/skill modification task:

```bash
# Check for differences between cursor and claude rules
diff .cursor/rules/20_trent_tasks.mdc .claude/rules/20_trent_tasks.md

# List all rule files that exist in cursor but not claude (or vice versa)
# (run these commands manually or via cleanup agent)
```

**Verify before marking task [🔍]:**
- [ ] `.cursor/rules/` change applied to `.claude/rules/`
- [ ] `.cursor/rules/` change applied to `.agent/rules/`
- [ ] Note: .cursor uses `.mdc` extension, .claude and .agent use `.md`
- [ ] Content is identical (only extension differs)

### Cleanup Agent Parity Check

During nightly cleanup, the cleanup agent SHOULD:
1. Compare rule files between .cursor, .claude, .agent
2. Report mismatches in CLEANUP_REPORT.md: `rule_parity_violations: {n}`
3. List which files are out of sync

### When Parity Cannot Be Achieved

IDE-specific features (cursor-only rules, claude-only capabilities):
- Create the rule only in the relevant IDE directory
- Add a comment in the other IDEs' rule directories: `# NOTE: {rule_name} is {cursor}-specific — no equivalent here`
- Document in SUBSYSTEMS.md which features are IDE-exclusive

### Commands Parity

Command names differ by IDE prefix convention:
- Cursor: `@trent-task-new`
- Claude Code: `/trent-task-new`
- Agent: may use different invocation

But command CONTENT (what they instruct the AI to do) must be identical.
```

## Acceptance Criteria
- [ ] Platform parity rule created in `template_v2/` rule files (all 3 IDEs)
- [ ] Parity matrix table (what requires parity, what doesn't)
- [ ] Parity check protocol with diff commands
- [ ] Cleanup agent parity check behavior documented
- [ ] Exception handling (IDE-specific features)
- [ ] Command parity rule (same content, different prefix)

## Verification Steps
- [ ] Rule exists in all 3 IDE rule directories (self-referential — must be parity compliant itself)
- [ ] Parity matrix table present
- [ ] Diff commands documented
- [ ] Exception handling for IDE-specific features documented

## When Stuck
- This rule must itself demonstrate parity — create it in all 3 directories at once
- The key difference: .cursor uses .mdc extension; .claude and .agent use .md
