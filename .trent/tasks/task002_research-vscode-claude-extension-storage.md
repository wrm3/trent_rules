---
id: 2
title: 'Research VS Code + Claude extension session storage'
type: research
status: completed
priority: high
phase: 0
subsystems: [vscode_adapter]
project_context: 'Unblocks Phase 5 VS Code adapter. Cursor is a VS Code fork — this storage may be reusable.'
dependencies: []
---

# Task 002: Research VS Code + Claude Extension Storage

## Objective
Determine where the Anthropic Claude VS Code extension stores conversation data.
Since Cursor is a VS Code fork, the structure may be identical to cursor_adapter.py
with just a different path.

## Acceptance Criteria
- [ ] Confirmed VS Code globalStorage path for Claude extension
- [ ] Confirmed whether it uses state.vscdb (SQLite) like Cursor, or different format
- [ ] If SQLite: confirmed table/key structure (same as Cursor? different?)
- [ ] Python snippet confirmed to read a session
- [ ] Decision: can reuse cursor_adapter.py with different path, or need new adapter?

## Investigation Steps

### Step 1: Find Claude extension globalStorage path
```powershell
# VS Code extension global storage
$vsCodePath = "$env:APPDATA\Code\User\globalStorage"
Get-ChildItem $vsCodePath | Where-Object { $_.Name -like "*anthropic*" -or $_.Name -like "*claude*" }

# Also check VS Code Insiders
$vsCodeInsidersPath = "$env:APPDATA\Code - Insiders\User\globalStorage"
Get-ChildItem $vsCodeInsidersPath -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "*anthropic*" -or $_.Name -like "*claude*" }
```

### Step 2: Find extension ID
```powershell
# List all VS Code extensions looking for Anthropic/Claude
code --list-extensions 2>$null | Where-Object { $_ -like "*claude*" -or $_ -like "*anthropic*" }
```

### Step 3: Check if state.vscdb exists and has cursorDiskKV
```python
import sqlite3
path = r"C:\Users\FSTrent\AppData\Roaming\Code\User\globalStorage\anthropic.claude-vscode\state.vscdb"
conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
print([row[0] for row in cursor])
```

### Step 4: If different format, document the format
- What tables exist?
- What keys contain conversation data?
- Is the key pattern similar to Cursor's composerData: prefix?

## Output
Document findings in docs/20260301_Cursor_VSCODE_CLAUDE_STORAGE_RESEARCH.md
Update phase5_vscode-adapter.md with confirmed paths and approach.
Note: if storage is identical to Cursor, vscode_adapter.py may simply be cursor_adapter.py
with a different path constant — which saves significant implementation work.
