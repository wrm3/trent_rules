---
id: 304
title: 'memory_setup_user — cross-platform user identity setup tool'
type: feature
status: in-progress
priority: high
phase: 3
subsystem: memory
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "The memory system tracks project sessions by user_id + machine_id, but ~/.trent/user_config.json has never been auto-created. This task builds the MCP tool that creates it, and adds a session-start check to the agent memory rule so users are prompted when the file is missing. Works identically on Windows, macOS, Linux, and shared Docker containers — machine_id is a generated UUID stored in ~/.trent/machine_id, no OS-native ID APIs used."
---

# Task 304: memory_setup_user MCP tool

## Objective
1. Create `docker/trent/tools/plugins/memory_setup_user.py`
2. Update `template_v2/.cursor/rules/` (+ .claude + .agent) `05_agent_memory` rule to add a session-start check
3. Register in `server.py` instructions

## Acceptance Criteria
- [ ] `memory_setup_user(display_name="Alice", user_id="usr_alice")` creates `~/.trent/user_config.json`
- [ ] If `~/.trent/machine_id` exists, reads it; if not, generates UUID and saves it
- [ ] Works on Windows (`C:\Users\...`), macOS (`/Users/...`), Linux (`/home/...`)
- [ ] Works when called from inside Docker (writes to /root/.trent/ in container — acceptable for native installs, documented for shared server)
- [ ] Calling again with same user_id updates display_name but preserves machine_id
- [ ] `memory_whoami()` returns current config (or "not configured" if missing)
- [ ] Rule update: 05_agent_memory rule checks for missing file at session start
- [ ] server.py instructions updated

## user_config.json format
```json
{
  "user_id": "usr_fstrent",
  "display_name": "FSTrent",
  "machine_id": "a1b2c3d4-...",
  "platform": "windows|macos|linux",
  "created_at": "2026-03-06T...",
  "updated_at": "2026-03-06T..."
}
```
