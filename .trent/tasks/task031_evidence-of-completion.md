---
id: 31
title: 'Add evidence_of_completion field to task YAML schema'
type: feature
status: pending
priority: high
phase: 0
subsystems: [verification]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 30]
project_context: 'AI agents claim tasks complete without verifiable proof — evidence_of_completion forces agents to provide checkable artifacts (test output, file hash, screenshot) that the verification agent can independently confirm'
---

# Task 031: Add evidence_of_completion field to task YAML

## Objective
Add `evidence_of_completion` field to the task YAML schema in `template_v2/`, requiring the implementing agent to provide specific, independently checkable proof that the task is complete before it can be moved to `[🔍]` (Awaiting Verification).

## Context
The core of the "AI lying" problem: an agent marks a task done because it *believes* it's done, not because it can *prove* it. A verifying agent checking `evidence_of_completion` is doing objective verification, not just reading the implementing agent's opinion. This is the "show your work" requirement.

## YAML Field to Add

```yaml
evidence_of_completion:
  # Implementing agent fills this in BEFORE setting status: awaiting_verification
  provided_by: ''           # agent_id that provided this evidence
  provided_at: ''           # ISO timestamp
  evidence_items:           # At least 1 required — must be independently checkable
    - type: file_exists      # See evidence types below
      path: ''
      description: ''
    - type: test_output
      command: ''
      expected_output: ''
      actual_output: ''
    - type: grep_result
      command: ''
      expected: ''
    - type: file_content_match
      path: ''
      contains: ''
  verification_commands:    # Commands the verifier should run to check
    - ''
  notes: ''                 # Anything the verifier should know
```

## Evidence Types

| Type | Description | Example |
|------|-------------|---------|
| `file_exists` | File was created at path | `template_v2/.trent/SPRINT.md` |
| `file_not_exists` | File was deleted | `template_v2/.trent/PLAN.md` |
| `file_content_match` | File contains specific text | SPRINT.md contains "Sprint Rules" |
| `grep_result` | grep command produces expected output | `grep -r "PLAN.md" template_v2/` returns empty |
| `test_output` | Command runs and produces expected result | python test.py returns "PASSED" |
| `linter_clean` | No linter errors in specified files | `pylint plugin.py` returns 0 errors |
| `yaml_valid` | YAML parses without error | task YAML is valid |
| `git_commit_exists` | Specific commit was made | commit with message matching pattern |
| `directory_structure` | Directory has expected contents | `ls template_v2/.trent/` shows expected files |

## Verification Agent Protocol

When picking up a `[🔍]` (Awaiting Verification) task:
1. Read `evidence_of_completion.evidence_items`
2. Run each `verification_commands` independently
3. For each evidence_item: verify it matches reality
4. If ALL evidence checks pass:
   - Update task YAML: `verified_by: {your_agent_id}`, `verified_at: {timestamp}`
   - Set `status: completed`
   - Update TASKS.md: `[🔍]` → `[✅]`
5. If ANY evidence check fails:
   - Document which check failed and how
   - Add to `failure_history`
   - Set `status: in_progress` (sends back to implementer)
   - Update TASKS.md: `[🔍]` → `[🔄]`
   - Git commit: `"verify-fail(task-{id}): evidence check {n} failed — {reason}"`

## Acceptance Criteria
- [ ] `evidence_of_completion:` YAML block added to task003 schema
- [ ] Evidence types table documented
- [ ] Verification agent protocol documented
- [ ] Task file template has empty `evidence_of_completion:` section
- [ ] Rule that implementing agent MUST fill evidence_of_completion before setting `awaiting_verification`
- [ ] Rule that verifying agent MUST check evidence, not just read the task

## Verification Steps
- [ ] task003 schema has `evidence_of_completion` block
- [ ] Evidence types listed with descriptions
- [ ] Verification agent protocol (pass/fail paths) documented
- [ ] Task file template has the empty evidence section

## When Stuck
- Pure schema + documentation task
- The key principle: evidence must be checkable by a DIFFERENT agent independently
- "I checked it myself" is not evidence
