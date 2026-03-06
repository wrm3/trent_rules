---
description: Rules for coordinating multiple SubAgents in parallel execution
globs:
alwaysApply: false
---

# Parallel SubAgents Workflow

## Core Principles (ALL MANDATORY)

1. **Single Message = Parallel Execution**: Multiple agents in ONE message run in parallel
2. **Different Agent Types Only**: NEVER run same agent type simultaneously
3. **Independent Tasks Only**: NEVER parallelize tasks with dependencies
4. **Clear Boundaries**: Each agent MUST have isolated scope with defined deliverables
5. **Optimal Count**: 3-5 agents in parallel

## Agent Substitutions

When you need multiple similar agents:
- **Backend work**: backend-developer, full-stack-developer, api-designer
- **Frontend work**: frontend-developer, full-stack-developer
- **Database work**: database-expert, full-stack-developer, backend-developer
- **Documentation**: technical-writer, api-designer

## Dependency Check (BLOCKING)

Before parallelizing, verify ALL are false:
- Does Task B need output from Task A?
- Do tasks modify the same files?
- Do tasks require each other's completion?

**If ANY is true → Run sequentially. No exceptions.**

## Boundary Definition (REQUIRED per agent)

Each agent MUST have:
- Exact deliverables (files to create/modify)
- Input requirements
- Success criteria
- File scope (which files agent will touch)

## Git Worktrees for Parallel Agents

| Scenario | Worktrees? |
|----------|------------|
| Agents touch **different files** | Recommended |
| Agents touch **same subsystem** | REQUIRED |
| Agents touch **same files** | REQUIRED |

**Workflow**: Create worktree per agent → agents work in isolation → merge branches → cleanup worktrees.

### Orchestrator Integration

When using the `orchestrator` agent:
1. Orchestrator creates worktrees before spawning agents
2. Each agent receives its worktree path
3. Orchestrator merges results after completion
4. Orchestrator cleans up worktrees
