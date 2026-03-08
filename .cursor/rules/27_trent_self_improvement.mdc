---
description: Self-improvement protocol for identifying and reporting issues in the trent system, integrated with SYSTEM_EXPERIMENTS.md
globs: 
alwaysApply: true
---
# Trent System Self-Improvement Protocol (vNext)

This rule defines the protocol for identifying, reporting, and resolving issues within the trent task management system itself.

## SYSTEM_EXPERIMENTS.md Integration (NEW)

Before proposing any system improvement, **always do two things first:**

1. **Read `.trent/SYSTEM_EXPERIMENTS.md`** — check Rejected Ideas before proposing
2. **Call `memory_search`** to check if a similar experiment was tried in a previous session:
   ```
   memory_search(query="experiment: {brief description of proposed change}", project_id="{project_id}")
   ```
   If results show a previous attempt, surface them before proposing again.

### Why?
- Prevents re-proposing rejected experiments
- Provides context on what was already tried (even across sessions)
- Tracks active experiments that may still be in monitoring phase

### AI Contribution Protocol (Autonomous Sessions)
During unattended sprint or cleanup runs, AI agents MAY add proposals to SYSTEM_EXPERIMENTS.md:

```markdown
### EXP-NNN: [Experiment Title]
**Status**: proposed
**Started**: YYYY-MM-DD
**Proposed By**: {agent_id}
**Hypothesis**: [What this change is expected to improve]
**Change Made**: Not yet applied
**Monitoring**: Pending human approval
**experiment_result**:
  outcome: null
  measured_by: []
  task_failure_rate_before: null
  task_failure_rate_after: null
  notes: ""
  closed_date: null
```

AI agents MUST NOT:
- Apply system-level rule changes without human approval
- Modify `.cursor/rules/`, `.claude/rules/`, or `.agent/rules/` during autonomous operation
- Increment `rules_version` without human review

### Human Decision Flow
When a user reviews SYSTEM_EXPERIMENTS.md at session start:
1. `proposed` → `active` = human approves; AI may implement
2. `proposed` → `rejected` = human declines; AI must never re-propose
3. `active` → `completed` = outcome confirmed after monitoring
4. `active` → `rejected` = experiment failed or unwanted

### Closing an Experiment (MANDATORY memory capture)
When moving an experiment to `completed` or `rejected`, **call `memory_capture_insight`**:
```
memory_capture_insight(
    project_id  = "{project_id}",
    category    = "system_experiment",
    topic       = "EXP-NNN: {title}",
    insight     = "{outcome summary — what worked, what didn't, lessons learned}",
    platform    = "{cursor|claude_code|gemini_antigravity}"
)
```
This enables future sessions to find experiment outcomes via `memory_search`
even when SYSTEM_EXPERIMENTS.md has been reset or the project has been reinstalled.

---

## Purpose

The trent system should continuously improve. When the AI assistant identifies inconsistencies, weak enforcement, missing features, or documentation gaps in the trent system, it MUST report them to the user with proposed solutions.

## Issue Categories

### Category 1: Inconsistencies
- Naming convention conflicts between rules/skills
- Status indicator mismatches
- Template format differences
- Documentation contradictions

### Category 2: Weak Enforcement
- Rules that say "should" but have no enforcement mechanism
- Missing self-checks in workflows
- Optional steps that should be mandatory
- Gaps in validation logic

### Category 3: Missing Features
- Referenced features that don't exist
- Documented capabilities without implementation
- Incomplete tool coverage
- Missing commands or skills

### Category 4: Documentation Gaps
- Undocumented features
- Outdated references
- Missing examples
- Incomplete templates

### Category 5: Redundancy
- Duplicate content across rules/skills
- Overlapping functionality
- Unnecessary complexity
- Context bloat

## 🚨 MANDATORY: Issue Reporting Protocol

**When you identify ANY issue with the trent system, you MUST:**

### Step 1: Identify and Document

```markdown
## 🔧 Trent System Issue Detected

**Category**: [Inconsistency/Weak Enforcement/Missing Feature/Documentation Gap/Redundancy]

**Location(s)**: 
- [File 1]: [specific line or section]
- [File 2]: [specific line or section]

**Issue Description**:
[Clear description of what's wrong]

**Impact**:
[How this affects system usage or AI behavior]
```

### Step 2: Propose Solution

```markdown
**Proposed Solution**:
[Specific, actionable fix]

**Files to Modify**:
- [File 1]: [what to change]
- [File 2]: [what to change]

**Estimated Complexity**: [Easy/Medium/Complex]
```

### Step 3: Request User Decision

```markdown
**Options**:
1. ✅ **Accept** - Implement the proposed solution
2. ❌ **Decline** - Keep current behavior (explain why if possible)
3. 🔄 **Alternative** - Provide a different solution

Please respond with your choice (1, 2, or 3).
```

## Issue Detection Triggers

### Automatic Detection (Check During Normal Operations)

**During Task Operations:**
- [ ] Naming conventions match across all references
- [ ] Status indicators are consistent
- [ ] Templates are complete and accurate
- [ ] Workflows have enforcement mechanisms

**During Planning Operations:**
- [ ] Phase conventions are consistent
- [ ] PRD templates are complete
- [ ] Subsystem references are valid

**During System Setup:**
- [ ] All referenced directories exist
- [ ] All documented features are implemented
- [ ] All skills/agents are listed in agents.md

### Manual Detection (User-Triggered)

When user asks:
- "Check the trent system for issues"
- "Audit the trent rules"
- "Are there any problems with the system?"
- "Review trent for improvements"

Run comprehensive audit:
1. Cross-reference all naming conventions
2. Verify all referenced files exist
3. Check for duplicate content
4. Validate all enforcement mechanisms
5. Confirm documentation accuracy

## Issue Tracking

### Session-Level Tracking

When issues are identified during a session:

```markdown
## 📋 Trent System Issues (This Session)

| # | Category | Location | Status |
|---|----------|----------|--------|
| 1 | Inconsistency | 20_trent_tasks.md | Pending User Decision |
| 2 | Missing Feature | agents.md | Fixed |
| 3 | Weak Enforcement | 25_trent_index.md | Declined |
```

### Resolution Workflow

1. **Issue Identified** → Report to user with solution
2. **User Accepts** → Implement fix immediately
3. **User Declines** → Document reason, move on
4. **User Provides Alternative** → Implement alternative
5. **Fix Implemented** → Confirm completion

## Self-Check Questions

**Before ending any session that touched trent system files:**

```
□ Did I notice any inconsistencies in the trent system?
  → If yes, report using Issue Reporting Protocol
□ Did I find any weak enforcement rules?
  → If yes, propose strengthening
□ Did I reference any features that don't exist?
  → If yes, flag as missing feature
□ Did I find duplicate content?
  → If yes, propose consolidation
```

## Example Issue Reports

### Example 1: Naming Inconsistency

```markdown
## 🔧 Trent System Issue Detected

**Category**: Inconsistency

**Location(s)**: 
- `22_trent_planning.md`: Line 160 - `phase{N}_{kebab-case-name}.md`
- `trent-planning/SKILL.md`: Line 81 - `{phaseN-name}.md`

**Issue Description**:
Phase file naming convention differs between the planning rule and planning skill.

**Impact**:
AI may create phase files with inconsistent naming, causing sync validation failures.

**Proposed Solution**:
Standardize on `phase{N}_{kebab-case-name}.md` (e.g., `phase0_setup.md`, `phase1_foundation.md`)

**Files to Modify**:
- `trent-planning/SKILL.md`: Update line 81 to match rule convention

**Estimated Complexity**: Easy

**Options**:
1. ✅ **Accept** - Implement the proposed solution
2. ❌ **Decline** - Keep current behavior
3. 🔄 **Alternative** - Provide a different solution
```

### Example 2: Weak Enforcement

```markdown
## 🔧 Trent System Issue Detected

**Category**: Weak Enforcement

**Location(s)**: 
- `20_trent_tasks.md`: Task Completion Workflow section

**Issue Description**:
Git commit step says "offer git commit" but there's no self-check to ensure this actually happens.

**Impact**:
AI may forget to offer git commit, leaving work uncommitted.

**Proposed Solution**:
Add explicit self-check at end of task completion workflow:
```
**Before ending response:**
□ Did I offer git commit? If not, offer it now.
```

**Files to Modify**:
- `20_trent_tasks.md`: Add self-check after Step 4 of Task Completion Workflow

**Estimated Complexity**: Easy

**Options**:
1. ✅ **Accept** - Implement the proposed solution
2. ❌ **Decline** - Keep current behavior
3. 🔄 **Alternative** - Provide a different solution
```

### Example 3: Missing Feature

```markdown
## 🔧 Trent System Issue Detected

**Category**: Missing Feature

**Location(s)**: 
- `agents.md`: Line 38 - References `.cursor/hooks/`

**Issue Description**:
The agents.md file references a hooks directory that doesn't exist.

**Impact**:
Users may look for hooks functionality that isn't implemented.

**Proposed Solution**:
Remove the hooks reference from agents.md until hooks are implemented.

**Files to Modify**:
- `agents.md`: Remove line 38 (`├── hooks/`)

**Estimated Complexity**: Easy

**Options**:
1. ✅ **Accept** - Remove the reference
2. ❌ **Decline** - Keep reference for future implementation
3. 🔄 **Alternative** - Create empty hooks directory with README
```

## Integration with Other Rules

### Link to Core Rules (20_trent_tasks.md)
- Issues with task management → Report and fix
- Issues with file organization → Report and fix
- Issues with coding standards → Report and fix

### Link to Planning Rules (22_trent_planning.md)
- Issues with PRD templates → Report and fix
- Issues with phase management → Report and fix
- Issues with subsystems → Report and fix

### Link to QA Rules (23_trent_qa.md)
- Issues with bug tracking → Report and fix
- Issues with quality workflows → Report and fix

### Link to Workflow Rules (24_trent_workflow.md)
- Issues with task expansion → Report and fix
- Issues with sprint planning → Report and fix

## Continuous Improvement Metrics

Track over time:
- **Issues Identified**: Count of issues found
- **Issues Fixed**: Count of issues resolved
- **Issues Declined**: Count of issues user chose not to fix
- **Categories**: Distribution of issue types
- **Complexity**: Distribution of fix complexity

## Best Practices

1. **Report Immediately**: Don't wait until end of session
2. **Be Specific**: Include exact file locations and line numbers
3. **Propose Concrete Solutions**: Don't just identify problems
4. **Respect User Decision**: If declined, don't re-raise same issue
5. **Batch Related Issues**: Group similar issues together
6. **Prioritize Impact**: Report high-impact issues first

---

*This self-improvement protocol ensures the trent system evolves and improves over time through systematic issue identification and resolution.*
