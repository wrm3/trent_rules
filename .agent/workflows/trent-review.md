---
description: "Comprehensive code review - security, quality, performance, and maintainability"
---

# Workflow: trent-review

Perform a comprehensive code review covering security, quality, performance, and maintainability.

## Steps

### Step 1: Load Project Context

Read `.trent/PROJECT_CONTEXT.md` and `.trent/SUBSYSTEMS.md` to understand system boundaries and expectations.

### Step 2: Identify Changed Files

// turbo
Run `git diff --name-only HEAD~1` or examine recently modified files.

### Step 3: Security Review

Check each file for:
- Hardcoded secrets, API keys, passwords
- SQL injection vulnerabilities (raw string queries)
- XSS vulnerabilities (unescaped user input)
- Insecure direct object references
- Missing authentication/authorization checks
- Sensitive data in logs

### Step 4: Code Quality Review

Check for:
- Functions/methods exceeding 50 lines (suggest breaking up)
- Duplicate code patterns (DRY violations)
- Missing error handling and edge cases
- Unclear variable/function names
- Missing type hints (Python) or TypeScript types
- Dead code and unused imports
- Files exceeding 800 lines (flag for refactoring)

### Step 5: Performance Review

Check for:
- N+1 query patterns in database code
- Missing database indexes for frequently queried fields
- Large data loaded into memory unnecessarily
- Blocking I/O where async would be appropriate
- Missing caching for expensive computations

### Step 6: Maintainability Review

Check for:
- Missing docstrings on public functions/classes
- Complex logic without explanatory comments
- Tight coupling between components
- Violation of SOLID principles
- Missing or outdated tests

### Step 7: trent Compliance Review

Check:
- Task files have complete YAML frontmatter
- TASKS.md is in sync with task files
- Phase files match TASKS.md headers
- Documentation files are in `docs/` folder (not root)

### Step 8: Generate Review Report

Present findings organized by severity:

```markdown
## 🔍 Code Review Report

### 🚨 Critical Issues (must fix)
{list}

### ⚠️ High Priority Issues
{list}

### 💡 Suggestions (optional improvements)
{list}

### ✅ What's Working Well
{list}

### 📋 Next Steps
1. {action items in priority order}
```
