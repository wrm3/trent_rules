---
id: 77
title: 'Ensure .cursor/rules/, .claude/rules/, .agent/rules/ are in sync (parity check for template_v2)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [agent-rules]
ai_safe: true
blast_radius: low
requires_verification: true
requires_solo_agent: false
dependencies: [70, 71, 72, 73, 74, 75, 76]
project_context: 'After all rule updates are done, do a final parity check across all three IDE directories in template_v2 — this is the QA gate before any deployment'
---

# Task 077: Final parity check — all rule files in template_v2

## Objective
Perform a comprehensive parity audit across all three IDE rule directories in `template_v2/` — confirming that all rule files are present in all three locations and content is identical where required.

## Audit Process

```bash
# List files in each directory
ls template_v2/.cursor/rules/
ls template_v2/.claude/rules/
ls template_v2/.agent/rules/

# For each shared rule file, diff cursor vs claude
diff template_v2/.cursor/rules/20_trent_tasks.mdc template_v2/.claude/rules/20_trent_tasks.md

# Repeat for each rule file
```

## Expected File Inventory (template_v2)

| Rule File | Cursor (.mdc) | Claude (.md) | Agent (.md) | Notes |
|-----------|---------------|--------------|-------------|-------|
| `00_always` | ✅ | ✅ | ✅ | Identical content |
| `01_documentation` | ✅ | ✅ | ✅ | Identical |
| `02_git_workflow` | ✅ | ✅ | ✅ | Identical |
| `03_code_review` | ✅ | ✅ | ✅ | Identical |
| `04_code_reusability` | ✅ | ✅ | ✅ | Identical |
| `05_agent_memory` | ✅ | ✅ | ✅ | Identical |
| `20_trent_tasks` | ✅ | ✅ | ✅ | Identical |
| `21_trent_infrastructure` | ✅ | ✅ | ✅ | Identical |
| `22_trent_planning` | ✅ | ✅ | ✅ | Identical |
| `23_trent_qa` | ✅ | ✅ | ✅ | Identical |
| `24_trent_workflow` | ✅ | ✅ | ✅ | Identical |
| `25_trent_index` | ✅ | ✅ | ✅ | Identical |
| `26_trent_agents_multi` | ✅ | ✅ | ✅ | Identical |
| `27_trent_self_improvement` | ✅ | ✅ | ✅ | Identical |
| `28_trent_project_files` | ✅ | ✅ | ✅ | Identical |
| `29_trent_codebase_analysis` | ✅ | ✅ | ✅ | Identical |
| `30_trent_ideas_goals` | ✅ | ✅ | ✅ | Identical |
| `31_trent_autonomous` | ✅ | ✅ | ✅ | Identical (NEW) |
| `32_trent_verification` | ✅ | ✅ | ✅ | Identical (NEW) |
| `silicon_valley_personality` | ✅ | ✅ | ✅ | Identical |

## Acceptance Criteria
- [ ] All rule files exist in all 3 IDE directories
- [ ] Diff between cursor and claude versions returns no content differences
- [ ] Diff between cursor and agent versions returns no content differences
- [ ] Any IDE-specific files are documented as exceptions

## Evidence of Completion
```yaml
evidence_of_completion:
  evidence_items:
    - type: grep_result
      command: "ls template_v2/.cursor/rules/ | wc -l"
      expected: "matches ls template_v2/.claude/rules/ | wc -l"
    - type: grep_result
      command: "diff -r template_v2/.cursor/rules/ template_v2/.claude/rules/ --include='*.md' (ignoring extensions)"
      expected: "no content differences"
```

## When Stuck
- This is a verification/audit task — no new content creation needed
- Run the diff commands and fix whatever they find
- It's OK to create missing files by copying from the existing version
