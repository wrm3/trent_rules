---
id: 201
title: 'Update trent_install to deploy from template_v2/'
type: feature
status: pending
priority: critical
phase: 2
subsystem: installation
blast_radius: medium
blast_radius_reason: "Changes install behavior for all new projects — existing projects unaffected"
ai_safe: true
requires_solo_agent: false
dependencies: [200]
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "New installs should get vNext rules by default; existing projects upgraded on next trent_install call"
---

# Task 201: Update trent_install to deploy from template_v2/

## Objective
Update `trent_install.py` (and the platform-specific variants) to use `RULES_MANIFEST_V2` and `TRENT_MANIFEST_V2` instead of the v1 manifests, making template_v2 the default for all new installs.

## Acceptance Criteria
- [ ] `trent_install.py` imports `RULES_MANIFEST_V2` and `TRENT_MANIFEST_V2` from `_trent_shared`
- [ ] Uses V2 manifests by default
- [ ] Accepts `use_v2: bool = True` parameter to allow opt-out (backwards compat)
- [ ] Tool description updated to mention vNext
- [ ] Platform-specific installs (`trent_install_cursor.py` etc.) also updated if they exist

## Implementation Notes
In `trent_install.py`:
1. Import `RULES_MANIFEST_V2`, `TRENT_MANIFEST_V2` alongside existing imports
2. In `execute()`, select manifest based on `use_v2` param:
   ```python
   rules_manifest = RULES_MANIFEST_V2 if use_v2 else RULES_MANIFEST
   trent_manifest = TRENT_MANIFEST_V2 if use_v2 else TRENT_MANIFEST
   ```
3. Pass `template_prefix="template_v2/"` to `run_install()` when using V2
4. Update `TOOL_DESCRIPTION` to note vNext

Check if `run_install()` / `extract_manifest_from_zip()` needs a `template_prefix` param threaded through — verify in `_trent_shared.py`.
