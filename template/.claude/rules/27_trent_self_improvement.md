---
description: Self-improvement protocol for identifying and reporting issues in the trent system
globs:
alwaysApply: true
---

# Trent System Self-Improvement Protocol

## Purpose

When the AI identifies inconsistencies, weak enforcement, missing features, or documentation gaps in the trent system, it MUST report them with proposed solutions.

## Issue Categories

1. **Inconsistencies**: Naming conflicts, status mismatches, template differences, contradictions
2. **Weak Enforcement**: Rules saying "should" without enforcement, missing self-checks, optional steps that MUST be mandatory
3. **Missing Features**: Referenced features that don't exist, documented capabilities without implementation
4. **Documentation Gaps**: Undocumented features, outdated references, incomplete templates
5. **Redundancy**: Duplicate content across rules/skills, overlapping functionality, context bloat

## MANDATORY: Issue Reporting Protocol

**When you identify ANY issue, you MUST report using this format:**

```markdown
## Trent System Issue Detected

**Category**: [1-5 from above]
**Location(s)**: [File]: [section/line]
**Issue**: [What's wrong]
**Impact**: [How it affects behavior]
**Proposed Fix**: [Specific, actionable change]
**Files to Modify**: [list]
**Complexity**: [Easy/Medium/Complex]

**Options**:
1. Accept — Implement fix
2. Decline — Keep current behavior
3. Alternative — User provides different fix
```

## Detection Triggers

### Automatic (during normal operations)
- Naming conventions mismatch across references
- Status indicators inconsistent
- Templates incomplete or inaccurate
- Workflows missing enforcement mechanisms

### Manual (user-triggered phrases)
- "Check the trent system for issues" / "Audit the trent rules" / "Review trent for improvements"
- Run comprehensive audit: cross-reference naming, verify files exist, check for duplicates, validate enforcement

## Resolution Workflow

1. **Issue Identified** → Report with solution
2. **User Accepts** → Implement fix immediately
3. **User Declines** → Document reason, move on. Do NOT re-raise.
4. **User Provides Alternative** → Implement alternative

## Self-Check (before ending sessions touching trent files)

```
□ Did I notice any inconsistencies? → Report using protocol above
□ Did I find weak enforcement rules? → Propose strengthening
□ Did I reference features that don't exist? → Flag as missing
□ Did I find duplicate content? → Propose consolidation
```

## Example Issue Report

```markdown
## Trent System Issue Detected

**Category**: Inconsistency
**Location(s)**: `22_trent_planning.md` line 160, `trent-planning/SKILL.md` line 81
**Issue**: Phase file naming convention differs (`phase{N}_{name}.md` vs `{phaseN-name}.md`)
**Impact**: AI may create inconsistently named phase files, causing sync failures
**Proposed Fix**: Standardize on `phase{N}_{kebab-case-name}.md`
**Files to Modify**: `trent-planning/SKILL.md` line 81
**Complexity**: Easy
```
