---
phase: 7
name: 'Quality, Polish & Documentation'
status: planning
subsystems: [all]
task_range: '700-799'
prerequisites: [0, 1, 2, 3, 4, 5, 6]
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 7: Quality, Polish & Documentation

## Overview
Production hardening. All adapters work individually — this phase ensures the system
is reliable at scale, handles edge cases gracefully, and is fully documented.

## Key Concerns
1. **Performance**: With 1000+ turns in PostgreSQL, does memory_search() stay fast?
2. **Deduplication**: What happens when the same conversation is ingested twice?
3. **Token budget**: Does memory_context() respect the max_tokens limit reliably?
4. **Documentation**: Are all 4 new MCP tools documented in AGENTS.md and CLAUDE.md?

## Deliverables
- [ ] Performance test results with large dataset
- [ ] Deduplication verified working (content hash in agent_turns)
- [ ] AGENTS.md updated with memory tools
- [ ] CLAUDE.md updated with memory tools
- [ ] MCP_TOOLS_INVENTORY.md updated
