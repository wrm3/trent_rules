---
description: "Platform parity enforcement — keep .cursor/, .claude/, and .agent/ rules in sync"
globs:
alwaysApply: true
---

# Platform Parity Rule

## Core Principle

The trent rule system must remain **functionally identical** across all three IDE directories:
- `.cursor/rules/` (Cursor IDE — `.mdc` extension)
- `.claude/rules/` (Claude Code — `.md` extension)
- `.agent/rules/` (Gemini/Antigravity — `.md` extension)

If a rule, command, agent, or skill is modified in one directory, it MUST be applied to all three.

---

## Parity Matrix

| Content Type | .cursor/ | .claude/ | .agent/ | Notes |
|--------------|---------|----------|---------|-------|
| Core rules (20-30) | `.mdc` | `.md` | `.md` | Content identical, extension differs |
| Commands | `commands/` | `commands/` | `workflows/` | Agent uses `workflows/` not `commands/` |
| Skills | `skills/` | `skills/` | `skills/` | Identical |
| Agents | `agents/` | `agents/` | N/A | Agent format differs |
| Personality | `silicon_valley_personality.mdc` | `silicon_valley_personality.md` | `silicon_valley_personality.md` | Identical |

---

## IDE-Specific Exceptions (Do NOT sync these)

| Feature | Cursor Only | Claude Only | Agent Only |
|---------|------------|-------------|------------|
| File extension | `.mdc` rules | `.md` rules | `.md` rules |
| Frontmatter format | `---\ndescription: ...\nglobs:\nalwaysApply: true\n---` | `---\ndescription: ...\nglobs:\nalwaysApply: true\n---` | N/A |
| YAML frontmatter | Required for `.mdc` | Required | Not required |
| Commands prefix | `@trent-` | `/trent-` | N/A |
| Subagents | `.cursor/agents/` | `.claude/agents/` | Not available |
| Rate limit rules | N/A | `.claude/CLAUDE.md` graceful shutdown rules | N/A |
| Multi-agent TTL | CLAUDE.md has extra TTL detail | — | — |

---

## Sync Protocol

### When You Modify a Rule

1. **Identify the file changed**: e.g., `.cursor/rules/20_trent_tasks.mdc`
2. **Identify the content change**: What section changed?
3. **Apply to all three** (adjusting only extension and frontmatter format):
   - `.cursor/rules/20_trent_tasks.mdc`
   - `.claude/rules/20_trent_tasks.md`
   - `.agent/rules/20_trent_tasks.md`
4. **Apply to commands/workflows** if a new command was added

### Pre-Completion Parity Check

Before marking any rule-related task complete:

```
Parity Check for: {rule_name}
.cursor/rules/{name}.mdc   — ✅ updated / ⚠️ missing
.claude/rules/{name}.md    — ✅ updated / ⚠️ missing
.agent/rules/{name}.md     — ✅ updated / ⚠️ missing

Parity: PASS ✅ / FAIL ⚠️ (list missing)
```

---

## Diff Check Protocol

Run this to verify parity (strips extensions for comparison):

```bash
# Check if two rule files are identical (ignoring frontmatter extension diffs)
diff <(grep -v "^---" .cursor/rules/20_trent_tasks.mdc | grep -v "^description" | grep -v "^globs" | grep -v "^alwaysApply") \
     <(grep -v "^---" .claude/rules/20_trent_tasks.md  | grep -v "^description" | grep -v "^globs" | grep -v "^alwaysApply")
```

For PowerShell (Windows):
```powershell
# Compare two rule files (ignoring frontmatter)
$cursor = Get-Content ".cursor\rules\20_trent_tasks.mdc" | Where-Object { $_ -notmatch "^---$|^description:|^globs:|^alwaysApply:" }
$claude = Get-Content ".claude\rules\20_trent_tasks.md"  | Where-Object { $_ -notmatch "^---$|^description:|^globs:|^alwaysApply:" }
Compare-Object $cursor $claude
```

---

## File Inventory (Expected Parity Files)

All of the following should exist in all three rule directories (with appropriate extension):

```
00_always
01_documentation
02_git_workflow
03_code_review
04_code_reusability
05_agent_memory (or equivalent)
20_trent_tasks
21_trent_infrastructure
22_trent_planning
23_trent_qa
24_trent_workflow
25_trent_index
26_trent_agents_multi
27_trent_self_improvement
28_trent_project_files
30_trent_ideas_goals
31_trent_autonomous
32_trent_verification
silicon_valley_personality
```

---

## Cleanup Agent Responsibility

The `@trent-cleanup` agent runs a parity audit nightly:
1. List all files in `.cursor/rules/` (strip extensions)
2. List all files in `.claude/rules/` (strip extensions)
3. List all files in `.agent/rules/` (strip extensions)
4. Report any files present in one but missing from others
5. Include parity violations in CLEANUP_REPORT.md under `## Platform Parity`

---

*This rule ensures that agents operating in Cursor, Claude Code, or Gemini all work from the same rule set, preventing behavior divergence across platforms.*
