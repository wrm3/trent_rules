# trent Agent Memory System — Task List

## Phase 0: Research & Foundation [✅]
*Goal: Confirm all unknowns before writing production code. No Phase 1 until all research tasks complete.*

- [✅] **Task 001**: Research Gemini CLI session storage location
- [✅] **Task 002**: Research VS Code + Claude extension session storage
- [✅] **Task 003**: Design user_config.json spec & generation logic
- [✅] **Task 004**: Define project_uuid format & .trent injection point
- [✅] **Task 005**: Write 05_agent_memory.sql PostgreSQL schema

## Phase 1: Core Infrastructure [🔄]
*Goal: PostgreSQL schema live, all 5 MCP tools operational, testable with sample data.*

- [✅] **Task 100**: Add 05_agent_memory.sql to docker/init_db/ and rebuild container
- [✅] **Task 101**: Create _agent_memory_shared.py + 5 plugin files
- [✅] **Task 102**: Implement memory_ingest_session() tool (Tier 1: passive)
- [✅] **Task 103**: Implement memory_capture_session() tool (Tier 2: active, agent-reported)
- [✅] **Task 104**: Implement memory_search() tool
- [✅] **Task 105**: Implement memory_sessions() tool
- [✅] **Task 106**: Implement memory_context() tool
- [✅] **Task 107**: Unit test all 5 tools with injected sample data — LIVE in Docker, confirmed via trent_server_status
- [ ] **Task 108**: Integration test memory_context token budget management

## Phase 2: Cursor Adapter [  ]
*Goal: Full end-to-end capture from real Cursor session → PostgreSQL.*

- [ ] **Task 200**: Implement cursor_adapter.py (state.vscdb reader, cursorDiskKV)
- [ ] **Task 201**: Integration test cursor_adapter against live state.vscdb
- [ ] **Task 202**: Extend agent-complete.ps1 — background call to memory_ingest_session
- [ ] **Task 203**: Extend session-start.ps1 — call memory_context, inject into context
- [ ] **Task 204**: End-to-end test: run Cursor session → verify turns in PostgreSQL

## Phase 3: Claude Code Adapter [  ]
*Goal: Full end-to-end capture from real Claude Code session → PostgreSQL.*

- [ ] **Task 300**: Implement claude_adapter.py (~/.claude/projects/*.jsonl reader)
- [ ] **Task 301**: Create Claude Code stop hook (shell script, cross-platform)
- [ ] **Task 302**: Integration test claude_adapter against real .jsonl session file
- [ ] **Task 303**: End-to-end test: run Claude Code session → verify turns in PostgreSQL

## Phase 4: Gemini/Antigravity Adapter [  ]
*Research complete. Conversations stored as ENCRYPTED .pb files — cannot read passively.*
*Approach: Active MCP tool call (agent self-reports via memory_capture_session)*

- [ ] **Task 400**: Add memory_capture_session() MCP tool (if not done in Phase 1)
- [ ] **Task 401**: Write GEMINI.md session rule: "call memory_capture_session before ending"
- [ ] **Task 402**: Test: run Antigravity session with rule → verify capture in PostgreSQL
- [ ] **Task 403**: Add Antigravity installation_id as machine_id source in identity.py

## Phase 5: VS Code + Claude Extension Adapter [  ]
*Research complete. VS Code chat sessions stored as JSON (emptyWindowChatSessions format).*
*Approach: Active MCP as primary. Passive JSON reader as stretch goal once ext confirmed installed.*

- [ ] **Task 500**: Write VS Code session rule for Claude extension (same as Gemini rule)
- [ ] **Task 501**: Document VS Code stable machine IDs (devDeviceId from storage.json)
- [ ] **Task 502**: Stretch: implement vscode_adapter.py once Claude ext storage confirmed
- [ ] **Task 503**: End-to-end test with VS Code

## Phase 6: trent_install Integration [  ]
*Goal: Every new project installed with trent gets memory system automatically.*

- [ ] **Task 600**: Add project_uuid generation to trent_install.py
- [ ] **Task 601**: Add user_config.json creation to trent_install.py
- [ ] **Task 602**: Deploy extended Cursor hooks (agent-complete, session-start) via trent_install
- [ ] **Task 603**: Deploy Claude Code stop hook via trent_install
- [ ] **Task 604**: Deploy Gemini hooks via trent_install
- [ ] **Task 605**: Update AGENTS.md template — document 4 new MCP memory tools
- [ ] **Task 606**: Update CLAUDE.md template — document memory tools + session-start usage
- [ ] **Task 607**: Inject memory_context call pattern into trent session-start rule (00_always.mdc)

## Phase 7: Quality, Polish & Documentation [  ]
*Goal: Production-ready, tested, documented.*

- [ ] **Task 700**: Performance test with 1000+ turns in PostgreSQL
- [ ] **Task 701**: Deduplication edge case testing (identical turns, re-runs)
- [ ] **Task 702**: Update AGENTS.md in trent_rules — new MCP tools section
- [ ] **Task 703**: Update CLAUDE.md in trent_rules — new MCP tools section
- [ ] **Task 704**: Update MCP_TOOLS_INVENTORY.md

## Phase 8: Final Cleanup & Release [  ]
*Goal: Clean commit of completed feature with pristine .trent/ template state.*

- [ ] **Task 800**: Reset .trent/ to pristine template state (copy from .trent_bk/)
- [ ] **Task 801**: Final review — verify all adapters functional, all tools documented
- [ ] **Task 802**: Git commit: agent memory system complete
- [ ] **Task 803**: Git push to remote

---

## Completed Tasks
(None yet)

## Blocked Tasks
- Tasks 400-403: Blocked on Task 001 (Gemini storage research)
- Tasks 500-503: Blocked on Task 002 (VS Code storage research)

---
**Legend:**
- `[ ]` - Pending (no task file yet)
- `[📋]` - Ready (task file created)
- `[🔄]` - In Progress
- `[✅]` - Completed
- `[❌]` - Failed/Blocked
