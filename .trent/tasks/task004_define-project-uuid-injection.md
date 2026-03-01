---
id: 4
title: 'Define project_uuid format and .trent injection point'
type: design
status: completed
priority: high
phase: 0
subsystems: [trent_install, identity]
project_context: 'Stable project identity that survives renames/moves — the key improvement over OneContext.'
dependencies: [3]
---

# Task 004: Define project_uuid Injection

## Objective
Define exactly where project_uuid lives in .trent/ files and how it's injected
by trent_install. Must be stable (never changes), discoverable (hooks can read it),
and backward-compatible (does not break existing .trent/ installs).

## Acceptance Criteria
- [ ] project_uuid field location decided (which file, which line/field)
- [ ] Format decided (proj_{uuid} vs plain UUID)
- [ ] Hook read logic documented (how agent-complete.ps1 finds the ID)
- [ ] Idempotency confirmed (second trent_install does not regenerate UUID)
- [ ] Backward compat: projects without project_uuid still work (default to path hash)

## Proposed Approach

### Option A: Add to PROJECT_CONTEXT.md (recommended)
The file already exists in every trent install. Add one YAML-like line:
```markdown
project_id: proj_a1b2c3d4
```

Pros: already in every project, easy to find, tracked by git
Cons: slightly pollutes a Markdown doc with a machine-generated value

### Option B: Dedicated .trent/.project_id file
```
proj_a1b2c3d4
```
Single-line file. Clean separation of concerns.
Pros: can't accidentally edit it, trivially readable
Cons: one more file in .trent/

### Option C: In PLAN.md frontmatter
Not recommended — PLAN.md may be regenerated.

## Recommendation: Option B (.trent/.project_id)
- Trivial to read in PowerShell: `$projectId = Get-Content .trent/.project_id`
- Trivial to read in Python: `project_id = open('.trent/.project_id').read().strip()`
- Cannot be accidentally overwritten by PRD regeneration
- Git-tracked (follows project through renames/clones)

## Hook Read Logic (PowerShell)
```powershell
# In agent-complete.ps1
$projectIdFile = ".trent/.project_id"
$projectId = if (Test-Path $projectIdFile) { Get-Content $projectIdFile } else { "unknown" }
```

## Hook Read Logic (Python/shell, for Claude Code / Gemini hooks)
```bash
PROJECT_ID=$(cat .trent/.project_id 2>/dev/null || echo "unknown")
```

## Generation (in trent_install.py)
```python
def ensure_project_id(trent_dir):
    id_file = os.path.join(trent_dir, '.project_id')
    if os.path.exists(id_file):
        return open(id_file).read().strip()  # idempotent
    
    project_id = f"proj_{uuid.uuid4().hex[:8]}"
    open(id_file, 'w').write(project_id)
    return project_id
```

## Output
Decision documented here. Implementation in Task 600.
