---
id: 1
title: 'Research Gemini CLI session storage location'
type: research
status: completed
priority: high
phase: 0
subsystems: [gemini_adapter]
project_context: 'Unblocks Phase 4 Gemini adapter. Without this, we cannot build the Gemini capture layer.'
dependencies: []
---

# Task 001: Research Gemini CLI Session Storage

## Objective
Determine where Gemini CLI (and Antigravity) stores session/conversation data on disk.
Produce a concrete file path, format description, and sample file if possible.

## Acceptance Criteria
- [ ] Confirmed file path(s) where Gemini CLI stores session data
- [ ] Format documented (JSONL? SQLite? JSON? Other?)
- [ ] Sample file or schema captured to docs/
- [ ] Python snippet confirmed to read a session (or confirmed inaccessible)
- [ ] Decision: can we build a gemini_adapter.py, or does Gemini not expose session data?

## Investigation Steps

### Step 1: Check known Gemini CLI locations on Windows
```powershell
# Gemini CLI / Google AI Studio CLI paths
Get-ChildItem "$env:APPDATA\Google" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
Get-ChildItem "$env:LOCALAPPDATA\Google" -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.Extension -in '.jsonl','.json','.db','.sqlite' } | Select-Object FullName
Get-ChildItem "$env:USERPROFILE\.gemini" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
Get-ChildItem "$env:USERPROFILE\.config\gemini" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

### Step 2: Check Antigravity-specific paths
```powershell
# Antigravity / Google Agent Framework
Get-ChildItem "$env:USERPROFILE\.agent" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
Get-ChildItem "$env:APPDATA\Antigravity" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

### Step 3: Check if Gemini has hooks documentation
- Review Antigravity docs for hook/event system
- Check: does Gemini CLI have a --hook or --on-complete flag?
- Check: does GEMINI.md in this repo describe any hook mechanism?

### Step 4: Read a session file if found
```python
# If JSONL found:
import json
with open(path) as f:
    for line in f:
        obj = json.loads(line)
        print(obj.get('type'), obj.get('role'))
```

## Output
Document findings in docs/20260301_Cursor_GEMINI_SESSION_STORAGE_RESEARCH.md
Update phase4_gemini-adapter.md with confirmed paths.
