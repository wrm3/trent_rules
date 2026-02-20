---
description: "Self-improvement protocol for identifying and reporting issues in the trent system"
activation: "always_on"
---

# Trent System Self-Improvement Protocol

This rule defines the protocol for identifying, reporting, and resolving issues within the trent task management system itself.

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
| 1 | Inconsistency | 10_trent_core.mdc | Pending User Decision |
| 2 | Missing Feature | agents.md | Fixed |
| 3 | Weak Enforcement | 14_trent_index.mdc | Declined |
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
- `11_trent_planning.mdc`: Line 160 - `phase{N}_{kebab-case-name}.md`
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
- `10_trent_core.mdc`: Task Completion Workflow section

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
- `10_trent_core.mdc`: Add self-check after Step 4 of Task Completion Workflow

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

### Link to Core Rules (10_trent_core.mdc)
- Issues with task management → Report and fix
- Issues with file organization → Report and fix
- Issues with coding standards → Report and fix

### Link to Planning Rules (11_trent_planning.mdc)
- Issues with PRD templates → Report and fix
- Issues with phase management → Report and fix
- Issues with subsystems → Report and fix

### Link to QA Rules (12_trent_qa.mdc)
- Issues with bug tracking → Report and fix
- Issues with quality workflows → Report and fix

### Link to Workflow Rules (13_trent_workflow.mdc)
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
