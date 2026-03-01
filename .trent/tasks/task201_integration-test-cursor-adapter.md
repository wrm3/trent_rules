---
id: 201
title: 'Integration test cursor_adapter against live state.vscdb'
type: task
status: completed
priority: high
phase: 2
subsystems: [cursor_adapter]
project_context: >
  Verify that cursor_adapter.py can actually read real conversation data
  from Cursor's state.vscdb and successfully POST it to the REST bridge.
dependencies: [200]
---

# Task 201: Integration Test — cursor_adapter vs live state.vscdb

## Objective
Run cursor_adapter.py against the actual state.vscdb to confirm:
1. The file can be located automatically
2. A real conversation_id can be extracted
3. Turns are parsed correctly
4. The REST bridge receives and stores them

## Test Steps

### Step 1 — Health check
```powershell
Invoke-WebRequest -Uri "http://localhost:8082/memory/health" -UseBasicParsing
```
Expected: `{"success":true,"db_connected":true,...}`

### Step 2 — Find a real conversation_id
```powershell
# Check the metrics file for a recent conversation_id
Get-Content ".cursor/metrics\*_completions.csv" | Select-Object -Last 5
```

### Step 3 — Run the adapter manually
```powershell
$projectPath = (Get-Location).Path
$convId = "<REAL-UUID-FROM-METRICS>"
python .cursor/hooks/cursor_adapter.py `
    --conversation-id $convId `
    --project-path $projectPath `
    --status partial
```
Expected: `Ingested N turns for conversation <UUID>`

### Step 4 — Verify in PostgreSQL
```powershell
docker exec trent_rules_postgres psql -U trent -d rag_knowledge -c "
SELECT s.conversation_id, s.platform, COUNT(t.id) AS turns
FROM agent_sessions s
LEFT JOIN agent_turns t ON t.session_id = s.id
GROUP BY s.id, s.conversation_id, s.platform
ORDER BY s.created_at DESC LIMIT 5;"
```

## Acceptance Criteria
- [ ] state.vscdb located automatically (no --vscdb flag needed)
- [ ] At least 1 turn extracted for a real conversation
- [ ] agent_sessions row created with correct conversation_id
- [ ] agent_turns rows created for each extracted turn
- [ ] Graceful failure (exit 1 not 0) when vscdb not found or conv not found
