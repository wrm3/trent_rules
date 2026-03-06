# Bug Tracking

## Active Bugs

### BUG-001: scheduler.py — Duplicate `CrawlTarget` import
- **Severity**: High
- **Source**: Development (found during code review of template_v2 / docker changes)
- **Phase Impact**: Phase 1 (Docker Integration)
- **Status**: Closed
- **Task Reference**: Task 062 (Create Firecrawl scheduler.py)
- **Created**: 2026-03-06
- **Fixed**: 2026-03-06 — Removed duplicate `CrawlTarget` from import line
- **File**: `docker/firecrawl/scheduler.py` line 20

---

### BUG-002: scheduler.py — `psycopg2.extras` used but not imported
- **Severity**: High
- **Source**: Development (found during code review of template_v2 / docker changes)
- **Phase Impact**: Phase 1 (Docker Integration)
- **Status**: Closed
- **Task Reference**: Task 062 (Create Firecrawl scheduler.py)
- **Created**: 2026-03-06
- **Fixed**: 2026-03-06 — Added `import psycopg2.extras` to import block
- **File**: `docker/firecrawl/scheduler.py` line 17-19

---

### BUG-003: platform_docs_search.py — `execute()` not async
- **Severity**: Medium
- **Source**: Development (found during code review of template_v2 / docker changes)
- **Phase Impact**: Phase 1 (Docker Integration)
- **Status**: Closed
- **Task Reference**: Task 064 (Create platform_docs_search MCP tool)
- **Created**: 2026-03-06
- **Fixed**: 2026-03-06 — Changed `def execute(` to `async def execute(`
- **File**: `docker/trent/tools/plugins/platform_docs_search.py` line 34

---

### BUG-004: trent_health_report.py — [🔍] awaiting-verification status not tracked
- **Severity**: Medium
- **Source**: Development (found during code review of template_v2 / docker changes)
- **Phase Impact**: Phase 1 (Docker Integration)
- **Status**: Closed
- **Task Reference**: Task 101 (Add trent_health_report MCP tool)
- **Created**: 2026-03-06
- **Fixed**: 2026-03-06 — Added `r"\[🔍\]": "awaiting_verification"` to STATUS_PATTERNS and `awaiting_verification` to task_counts return dict
- **File**: `docker/trent/tools/plugins/trent_health_report.py`

---

### BUG-005: template_v2 platform parity — 5 .claude rules truncated
- **Severity**: High
- **Source**: Development (found during parity audit post code review)
- **Phase Impact**: Phase 0 (Template Core)
- **Status**: Closed
- **Task Reference**: Task 066 (Platform parity), Task 077 (Rule 66 platform parity enforcement)
- **Created**: 2026-03-06
- **Fixed**: 2026-03-06 — Copied canonical .cursor versions to .claude for rules 23, 24, 26, 28, 29, 30
- **File**: `template_v2/.claude/rules/` — rules 23_trent_qa, 24_trent_workflow, 26_trent_agents_multi, 28_trent_project_files, 29_trent_codebase_analysis, 30_trent_ideas_goals were truncated (2,518–2,798 chars vs 4,892–12,313 chars in .cursor)
- **Note**: README.md differences across platforms are intentional (platform-specific content)

## Resolved Bugs
(None yet)

---

## Bug Template

When adding a bug, use this format:

### BUG-XXX: [Brief Title]
- **Severity**: [Critical/High/Medium/Low]
- **Source**: [User Reported/Development/Testing/Production]
- **Phase Impact**: [Affected phases]
- **Status**: [Open/Investigating/Fixing/Testing/Closed]
- **Task Reference**: [Link to task if applicable]
- **Created**: [Date]
- **Description**: [What's wrong]
- **Steps to Reproduce**: [How to reproduce]
- **Expected Behavior**: [What should happen]
- **Actual Behavior**: [What actually happens]

---

**Legend:**
- **Critical**: System crashes, data loss, security vulnerabilities
- **High**: Major feature failures, performance degradation >50%
- **Medium**: Minor feature issues, usability problems
- **Low**: Cosmetic issues, enhancement requests
