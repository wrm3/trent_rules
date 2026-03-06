---
id: 200
title: 'Update _trent_shared.py manifests for template_v2'
type: feature
status: pending
priority: critical
phase: 2
subsystem: installation
blast_radius: medium
blast_radius_reason: "Changes the manifest used by trent_install — affects all new installs"
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "trent_install currently deploys from template/ — must deploy from template_v2/ for vNext"
---

# Task 200: Update _trent_shared.py manifests for template_v2

## Objective
Add `TEMPLATE_V2_PREFIX` and `FULL_MANIFEST_V2` (plus cursor/claude/gemini/rules variants) to `_trent_shared.py` so `trent_install` can deploy template_v2 files.

## Acceptance Criteria
- [ ] `TEMPLATE_V2_PREFIX = "template_v2/"` constant defined
- [ ] `FULL_MANIFEST_V2` list mirrors `FULL_MANIFEST` but points to `template_v2/` paths
- [ ] `CURSOR_MANIFEST_V2`, `CLAUDE_MANIFEST_V2`, `GEMINI_MANIFEST_V2` defined
- [ ] `RULES_MANIFEST_V2` and `TRENT_MANIFEST_V2` defined
- [ ] Old `template/` manifests unchanged (backward compatibility)
- [ ] No functional changes to existing install paths

## Implementation Notes
In `_trent_shared.py`, after line ~141 (`TRENT_MANIFEST`), add:

```python
# ── template_v2 manifests (vNext — autonomous multi-agent support) ────────────
TEMPLATE_V2_PREFIX = "template_v2/"

FULL_MANIFEST_V2: List[str] = [
    'template_v2/.agent',
    'template_v2/.claude',
    'template_v2/.cursor',
    'template_v2/.platforms',
    'template_v2/docs',
    'template_v2/research',
    'template_v2/temp_scripts',
    'template_v2/agents.md',
    'template_v2/CLAUDE.md',
    'template_v2/GEMINI.md',
    'template_v2/GUARDRAILS.md',
    'template_v2/LICENSE',
    'template_v2/NOTICE',
    'template_v2/.trent',
]

CURSOR_MANIFEST_V2: List[str] = [
    'template_v2/.cursor',
    'template_v2/.platforms',
    'template_v2/docs',
    'template_v2/research',
    'template_v2/temp_scripts',
    'template_v2/agents.md',
    'template_v2/GUARDRAILS.md',
    'template_v2/LICENSE',
    'template_v2/NOTICE',
]

CLAUDE_MANIFEST_V2: List[str] = [
    'template_v2/.claude',
    'template_v2/.platforms',
    'template_v2/docs',
    'template_v2/research',
    'template_v2/temp_scripts',
    'template_v2/agents.md',
    'template_v2/CLAUDE.md',
    'template_v2/GUARDRAILS.md',
    'template_v2/LICENSE',
    'template_v2/NOTICE',
]

GEMINI_MANIFEST_V2: List[str] = [
    'template_v2/.agent',
    'template_v2/.platforms',
    'template_v2/docs',
    'template_v2/research',
    'template_v2/temp_scripts',
    'template_v2/agents.md',
    'template_v2/GEMINI.md',
    'template_v2/GUARDRAILS.md',
    'template_v2/LICENSE',
    'template_v2/NOTICE',
]

RULES_MANIFEST_V2: List[str] = [i for i in FULL_MANIFEST_V2 if i != 'template_v2/.trent']
TRENT_MANIFEST_V2: List[str] = ['template_v2/.trent']
```

The `extract_manifest_from_zip` function already handles arbitrary `TEMPLATE_PREFIX` values via the `template_prefix` parameter — just ensure that parameter is threaded through when using V2 manifests.
