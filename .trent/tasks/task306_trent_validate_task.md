---
id: 306
title: 'trent_validate_task MCP tool — ARCHITECTURE_CONSTRAINTS hard gate'
type: feature
status: pending
priority: high
phase: 3
subsystem: mcp-tools
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "ARCHITECTURE_CONSTRAINTS.md is currently enforced by prompt only. An autonomous agent under context pressure will skip it. This tool reads the constraints file and validates a task YAML dict against it — returning pass/fail with specific violations listed. The rule 31 autonomous agent calls it before claiming any task."
---

# Task 306: trent_validate_task — constraint validation hard gate

## Objective
Create `docker/trent/tools/plugins/trent_validate_task.py`

The tool:
1. Reads `ARCHITECTURE_CONSTRAINTS.md` from the project (passed as path param)
2. Reads the task YAML fields passed in (subsystems, blast_radius, files_to_modify)
3. Checks each active constraint against the task
4. Returns pass/fail + list of specific violations

## Key design principle: agents CAN still run — but they get a mandatory gate
The tool does NOT prevent the agent from proceeding. It returns a structured
result. The calling rule (31_trent_autonomous) decides what to do with violations:
- WARNINGS → agent logs them, proceeds with extra care
- VIOLATIONS → agent MUST escalate to human before proceeding

This preserves unattended operation for safe tasks while enforcing the constraint
file for risky ones. No manual click required.

## Acceptance Criteria
- [ ] Tool reads ARCHITECTURE_CONSTRAINTS.md from project_path param
- [ ] Parses active constraints (lines starting with `- [ ]` = inactive, `- [x]` = active)
- [ ] Validates: blast_radius vs constraint, subsystem vs locked subsystems, file scope
- [ ] Returns `{"valid": true/false, "warnings": [...], "violations": [...], "constraints_checked": N}`
- [ ] Returns `{"valid": true, "warnings": [], "violations": [], "constraints_checked": 0}` if no constraints file
- [ ] Update 31_trent_autonomous.mdc to call this tool before any task claim
