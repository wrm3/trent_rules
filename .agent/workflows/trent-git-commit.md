---
description: "Create a well-structured git commit for completed work"
---

# Workflow: trent-git-commit

Create a well-structured git commit following conventional commit format.

## Steps

### Step 1: Check Status

// turbo
Run `git status` and `git diff` to see what has changed.

### Step 2: Review Recent History

// turbo
Run `git log --oneline -10` to understand the commit style used in this repo.

### Step 3: Identify Completed Tasks

Read `.trent/TASKS.md` to identify which tasks were completed in this session.

### Step 4: Draft Commit Message

Create a commit message following conventional commits format:

```
{type}({scope}): {short description}

Tasks completed:
- #{task_id}: {title}

Phase: {phase_number}
Subsystems: {affected_subsystems}

{longer description if needed}
```

Commit types:
| Task Type | Commit Type |
|-----------|-------------|
| `feature` | `feat` |
| `bug_fix` | `fix` |
| `refactor` | `refactor` |
| `documentation` | `docs` |
| `default` | `feat` |

### Step 5: Show Preview

Show the user the planned commit and ask for approval or edits:

```
📦 PLANNED COMMIT

Files to stage:
{list of changed files}

Commit message:
{message}

Options:
- "commit" or Enter - Run this commit
- "edit: {message}" - Use custom message
- "skip" - Don't commit yet
```

### Step 6: Execute Commit

On approval:
// turbo
Stage and commit the files.

### Step 7: Confirm

Report the commit hash and summary.
