---
id: 25
title: 'Add requires_solo_agent flag to task YAML'
type: feature
status: pending
priority: high
phase: 0
subsystems: [resilience, autonomous]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 24]
project_context: 'Some tasks (database migrations, schema changes, file system reorganization) must not have other agents touching related code simultaneously — requires_solo_agent enforces exclusive execution'
---

# Task 025: Add requires_solo_agent flag to task YAML

## Objective
Add `requires_solo_agent: true/false` field to the task YAML schema in `template_v2/`, and document the enforcement rules that ensure tasks requiring exclusive execution are never run while other agents are active on the same subsystem.

## Context
Parallel agents can collide when tasks touch shared state (database schemas, configuration files, shared libraries). `requires_solo_agent` is the opt-in flag that says "I need the whole system to myself for this one." The cleanup agent uses this to ensure solo tasks only appear in SPRINT.md when they can be the only task.

## YAML Field to Add

```yaml
# In task YAML frontmatter:
requires_solo_agent: false   # default: false
solo_reason: ''              # if true: explain why exclusive execution is needed
                             # Examples: "database schema migration", "file system restructure",
                             #           "shared library refactor", "config overwrite"
```

## Enforcement Rules

### For cleanup agent (sprint population):
When a `requires_solo_agent: true` task is included in SPRINT.md:
1. It MUST be the ONLY task in the sprint
2. SPRINT.md max_tasks is overridden to 1
3. SPRINT.md header note: "⚠️ SOLO TASK SPRINT — Do not claim any other tasks"
4. All other sprint slots are left empty

### For sprint agents claiming tasks:
Before claiming any task:
1. Check if any active claimed task has `requires_solo_agent: true` in current project
2. If yes: abort all other claims until that task completes or expires
3. If you are claiming a `requires_solo_agent: true` task: immediately commit to git to "announce" sole occupancy

### Announcement Commit (solo task claim)
```bash
git commit -m "solo-claim(task-{id}): {agent_id} claiming exclusive execution
Solo reason: {solo_reason}
Estimated TTL: {claim_ttl_minutes} minutes
Other agents: please stand down until this commit is followed by completion/release"
```

### Release Commit (after solo task)
```bash
git commit -m "solo-release(task-{id}): {agent_id} releasing exclusive claim
Status: completed | failed | released-timeout
Other agents: clear to proceed"
```

## When requires_solo_agent Should Be true

| Scenario | Solo Required | Reason |
|----------|---------------|--------|
| Database schema migration | ✅ yes | Race condition on migration version |
| Shared library refactor | ✅ yes | Other agents import the library mid-change |
| `.trent/TASKS.md` full restructure | ✅ yes | Concurrent writes corrupt the file |
| Architecture constraint update | ✅ yes | Other agents might violate new constraint while it's being written |
| New feature in isolated module | ❌ no | No shared state |
| Template file creation | ❌ no | Isolated file |
| Bug fix in own subsystem | ❌ no | Isolated change |

## Acceptance Criteria
- [ ] `requires_solo_agent:` field added to task003 YAML schema
- [ ] `solo_reason:` field in schema
- [ ] Enforcement rules documented (cleanup agent + sprint agent)
- [ ] Announcement and release commit format defined
- [ ] Table of when to use (yes/no with reason)
- [ ] SPRINT.md template (task004) handles solo task sprint (max 1 task, warning header)

## Verification Steps
- [ ] task003 schema has `requires_solo_agent` and `solo_reason`
- [ ] Enforcement rules cover both cleanup and sprint agents
- [ ] Announcement commit format documented
- [ ] Solo sprint behavior (1 task only) in SPRINT.md template spec

## When Stuck
- Pure schema + documentation task
- The key design decision: solo means ONLY that task runs, nothing parallel
