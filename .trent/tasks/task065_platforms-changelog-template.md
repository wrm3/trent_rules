---
id: 65
title: 'Create .platforms/CHANGELOG.md template and update format'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [platform-docs, template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1]
project_context: '.platforms/CHANGELOG.md is the human-readable history of platform changes detected by Firecrawl — when an agent notices a platform changed behavior, it can quickly check here for the most recent known changes'
---

# Task 065: Create .platforms/CHANGELOG.md template

## Objective
Create `template_v2/.platforms/CHANGELOG.md` — the template for tracking significant platform documentation changes detected by the Firecrawl service. Also define the format for how the scheduler writes to this file.

## Template Content

```markdown
# Platform Documentation Changelog

This file tracks significant changes to platform APIs and documentation
detected by the weekly Firecrawl crawl.

**Auto-updated by**: Firecrawl scheduler (weekly, Sundays)
**Manual additions**: Acceptable — use the same format

---

## {YYYY-MM-DD} — Weekly Update

### Cursor IDE
**Changed Pages**: {n}
**New Pages**: {n}

Significant changes:
- **{Page Title}** (`{url}`): {brief description of what changed}
- No significant changes detected

### Claude / Anthropic
**Changed Pages**: {n}
**New Pages**: {n}

Significant changes:
- **{Page Title}** (`{url}`): {brief description of what changed}

### Gemini API
**Changed Pages**: {n}
**New Pages**: {n}

Significant changes:
- None detected

---

## {Previous date} — Weekly Update

[older entries...]

---

## Manual Entries

### {YYYY-MM-DD} — {Brief Title}
**Platform**: {cursor | claude | gemini | anthropic}
**Type**: breaking_change | new_feature | deprecation | correction
**Discovered By**: human | firecrawl | {agent_id}

**Change**:
{Description of the change and its impact on trent system}

**Action Required**:
- [ ] Update `.platforms/{platform}.md` reference file
- [ ] Update relevant rules if behavior changed
- [ ] Check if any tasks have outdated specs based on this

---
```

## Scheduler Write Format

The Firecrawl scheduler updates this file weekly:
1. Read existing CHANGELOG.md
2. Prepend new dated entry at top (after header)
3. Keep last 3 months of entries, archive older to `.platforms/archive/CHANGELOG_{YYYY}.md`

## Acceptance Criteria
- [ ] `template_v2/.platforms/CHANGELOG.md` exists
- [ ] Template has weekly update format with platform sections
- [ ] Manual entry format included
- [ ] `Action Required` checklist in manual entries
- [ ] Archive strategy described in comments

## Verification Steps
- [ ] File exists at correct path
- [ ] Both auto-generated and manual entry formats present
- [ ] Platform sections: Cursor, Claude, Gemini

## When Stuck
- Pure template task
- The key is the "Action Required" checklist — forces humans to update rules when platforms change
