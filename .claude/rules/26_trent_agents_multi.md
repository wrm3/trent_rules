---
description: Rules for coordinating multiple SubAgents in parallel execution
globs:
alwaysApply: false
---

# Parallel SubAgents Workflow Rules

**Purpose**: Define rules for coordinating multiple SubAgents in parallel execution

## Core Principles

1. **Single Message = Parallel Execution**: Multiple agents in ONE message run in parallel
2. **Different Agent Types Only**: Cannot run same agent type on multiple tasks simultaneously
3. **Independent Tasks Only**: Parallelize tasks with no dependencies
4. **Clear Boundaries**: Each agent needs isolated, well-defined scope
5. **Optimal Count**: 3-5 agents in parallel is the sweet spot

## Rule 1: Single Message, Multiple Task Calls

To run agents in parallel, MUST send **single message** with **multiple Task tool calls**.

### ❌ Wrong (Sequential Execution)
```
Message 1: "Use backend-developer to implement Task A"
[Wait for completion]
Message 2: "Use frontend-developer to implement Task B"
```

### ✅ Correct (Parallel Execution)
```
Message 1: "Run these in parallel:
- Use backend-developer to implement Task A
- Use frontend-developer to implement Task B"
```

## Rule 2: Different Agent Types Only

Cannot run the SAME agent type on multiple tasks simultaneously.

### Agent Substitutions
When you need multiple similar agents:
- **Backend work**: backend-developer, full-stack-developer, api-designer
- **Frontend work**: frontend-developer, full-stack-developer
- **Database work**: database-expert, full-stack-developer, backend-developer
- **Documentation**: technical-writer, api-designer

## Rule 3: Independent Tasks Only

Only parallelize tasks that have NO dependencies on each other.

### Dependency Analysis Checklist
- ✓ Does Task B need output/artifacts from Task A?
- ✓ Do tasks modify the same files?
- ✓ Do tasks require each other's completion?

If YES to any → Run sequentially, not in parallel

## Rule 4: Clear Task Boundaries

Each agent must have an isolated, well-defined task with clear scope and deliverables.

### Boundary Definition Checklist
- ✓ Exact deliverables (files to create/modify)
- ✓ Input requirements (what agent needs to start)
- ✓ Output artifacts (what agent produces)
- ✓ Success criteria (how to know it's done)
- ✓ File scope (which files agent will touch)

## Rule 5: Optimal Agent Count (3-5)

Run 3-5 agents in parallel for optimal performance.

### Scaling Guidelines
- **Simple tasks (1-2 days)**: 2-3 agents
- **Medium tasks (3-5 days)**: 3-4 agents
- **Complex tasks (1-2 weeks)**: 4-5 agents
- **Very complex (2+ weeks)**: Multiple phases of 3-5 agents each

## Rule 6: Git Worktrees for Parallel Agents

When running multiple agents in parallel, use **Git worktrees** to prevent file conflicts.

### What Are Git Worktrees?

Git worktrees allow multiple working directories from the same repository, each on a different branch, simultaneously. Each agent works in isolation.

### Setup Workflow

```bash
# 1. Create worktree for each parallel agent
git worktree add ../project-agent1 -b task-101
git worktree add ../project-agent2 -b task-102
git worktree add ../project-agent3 -b task-103

# 2. Each agent works in its own directory
# Agent 1 → ../project-agent1 (branch: task-101)
# Agent 2 → ../project-agent2 (branch: task-102)
# Agent 3 → ../project-agent3 (branch: task-103)

# 3. No collision - completely separate directories!
```

### Merge Workflow (After Agents Complete)

```bash
# Return to main branch
git checkout main

# Merge each agent's work
git merge task-101 -m "Merge task-101: {task_title}"
git merge task-102 -m "Merge task-102: {task_title}"
git merge task-103 -m "Merge task-103: {task_title}"

# Clean up worktrees
git worktree remove ../project-agent1
git worktree remove ../project-agent2
git worktree remove ../project-agent3

# Clean up branches (optional)
git branch -d task-101 task-102 task-103
```

### When to Use Worktrees

| Scenario | Use Worktrees? |
|----------|----------------|
| Agents touch **different files** | Optional (low conflict risk) |
| Agents touch **same subsystem** | ✅ Recommended |
| Agents touch **same files** | ✅ Required |
| Quick, small tasks | Optional (overhead may not be worth it) |
| Long-running parallel tasks | ✅ Recommended |

### Orchestrator Integration

When using the `orchestrator` agent to spawn parallel workers:
1. Orchestrator creates worktrees before spawning agents
2. Each agent receives its worktree path as working directory
3. Orchestrator merges results after all agents complete
4. Orchestrator cleans up worktrees

## Benefits of Following Rules

When rules are followed correctly:
- ✅ **30-50% time savings** through parallelization
- ✅ **Zero conflicts** from proper planning
- ✅ **Clear accountability** with defined boundaries
- ✅ **Easy monitoring** with independent tracking
- ✅ **Clean git history** with worktree isolation
