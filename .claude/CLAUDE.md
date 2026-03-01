# Claude Code Project Rules (OpenClaw/TrentWorks)

These rules are auto-loaded every conversation. They consolidate the key rules from `.cursor/rules/*.mdc` for Claude Code compatibility.

---

## Rate Limit Graceful Shutdown (CRITICAL OPERATIONAL RULE)

**At ~85% daily rate limit usage, STOP accepting new tasks and wind down gracefully.**

### Protocol:
1. **Monitor**: Track your rate limit consumption throughout the session. If you sense you're approaching limits (slower responses, warnings, high volume of tool calls over extended session), assume you're near 85%.
2. **No New Tasks**: Do NOT start any new tasks once at 85%. Finish only what is actively in-progress.
3. **Wrap Up Current Work**:
   - Complete any in-progress file edits (no half-written files)
   - Update TASKS.md status for anything you touched (atomic sync)
   - Commit or stage any completed work if appropriate
4. **Handoff Report**: Before stopping, provide a clear status summary:
   ```
   ## Graceful Shutdown - Rate Limit Approaching

   ### Completed This Session:
   - [list of tasks finished with status]

   ### Left In-Progress (needs pickup):
   - [task ID]: [what was done, what remains, which files were touched]

   ### Not Started (still pending):
   - [task IDs that were planned but not begun]

   ### Files Modified:
   - [list of all files changed this session]

   ### Git Status:
   - [committed/uncommitted state]
   ```
5. **Notify User**: Clearly state you're stopping due to rate limits and approximately when you'll be available again (if known).

**WHY**: Other AIs (Cursor, etc.) coordinate with this agent. Stopping mid-task without a handoff report creates sync issues across the team. A clean shutdown is always better than a hard cutoff.

---

## Always-Apply Rules (from 00_always.mdc)

1. **Response Footer**: Include at the end of every response:
   - Current timestamp (date, hour, minutes UTC)
   - List of tools used during the call
   - Context usage estimate

2. **File Size Enforcement**:
   - If any file exceeds **800 lines**: suggest refactoring
   - Become more insistent every 100 lines after 800
   - At **1000+ lines**: strongly insist on refactoring

3. **MCP Tools**: Always check available MCP tool lists before implementing manually

4. **Python**: Use UV for virtual environment management

---

## Task Management (from 10_trent_core.mdc)

### Task Status Flow (ENFORCED)
```
CORRECT: [ ] -> [📝] -> [📋] -> [🔄] -> [✅]
```

| TASKS.md | Task File YAML | Meaning | TTL |
|----------|----------------|---------|-----|
| `[ ]`    | (may not exist) | Listed, not started | - |
| `[📝]`  | `status: speccing` | Agent is writing the spec/task file | **1 hour** |
| `[📋]`  | `status: pending` | Specced and ready for pickup | - |
| `[🔄]`  | `status: in-progress` | Being coded | **2 hours** |
| `[✅]`  | `status: completed` | Done | - |
| `[❌]`  | `status: failed` | Failed/blocked | - |
| `[⏸️]`  | `status: paused` | Paused | - |

### Multi-Agent Concurrency (CRITICAL)

Multiple AI agents (Cursor, Claude Code Extension, Claude Code CLI) may work this backlog simultaneously. To prevent duplicate work:

**When picking up a task:**
1. Read TASKS.md - skip any task marked `[📝]` or `[🔄]`
2. If you pick a `[ ]` task to spec: immediately mark it `[📝]` in TASKS.md
3. If you pick a `[📋]` task to code: immediately mark it `[🔄]` in TASKS.md
4. Write `status_changed` timestamp in the task file YAML:
   ```yaml
   status: speccing  # or: in-progress
   status_changed: '2026-02-07T14:30:00Z'
   ```

**Stale task recovery (TTL expiry):**
- `[📝]` with `status_changed` **older than 1 hour** = abandoned spec attempt. Treat as `[ ]`, grab it.
- `[🔄]` with `status_changed` **older than 2 hours** = abandoned coding. Treat as `[📋]`, grab it.
- No `status_changed` timestamp on an active task = assume stale, available for pickup.

This is self-healing: dead/rate-limited agents don't create permanent locks.

### Task File Format
- **Filename**: `task{ID}_{descriptive_name}.md` (NO underscore after "task")
- **Subtasks**: `task{parentID}-{subID}_{name}.md` (hyphens, not dots)
- **Location**: `.trent/tasks/`
- **Phase IDs**: Phase N uses task IDs N*100 to N*100+99

### Atomic Updates (MANDATORY)
When changing task status, update BOTH files in the SAME response:
1. Task file YAML `status` + `status_changed` timestamp
2. TASKS.md status indicator

### Task Completion Workflow
When finishing a task:
1. **Validate**: Code compiles, acceptance criteria met
2. **Update Status**: task file + TASKS.md atomically
3. **Offer Git Commit**: With conventional commit format
4. **Check Project Files Impact**: Does CLAUDE.md need updating?

### Phase Completion Gate
Before starting Phase N+1:
1. Verify all Phase N tasks are [✅]
2. Generate SWOT analysis
3. Wait for user approval ("proceed")
4. Offer phase git commit + tag

### Direct Edit Policy (NO PERMISSION NEEDED)
Edit these files directly without asking:
- `.trent/PLAN.md`, `TASKS.md`, `PROJECT_CONTEXT.md`, `BUGS.md`, `SUBSYSTEMS.md`
- All files in `.trent/tasks/` and `.trent/phases/`

### File Placement Rules
- `.trent/`: ONLY core planning documents
- `docs/`: ALL temporary/migration/ad-hoc documentation
- `temp_scripts/`: Test scripts and utilities

---

## Git Workflow (from 02_git_workflow.mdc)

### Commit Format
`type(scope): description`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`

### Branch Naming
`type/short-description` (e.g., `feature/user-authentication`, `fix/login-crash`)

### Rules
- Present tense ("add feature" not "added feature")
- Reference issues when applicable
- Never commit secrets/API keys

---

## Code Quality (from 03_code_review.mdc)

### File Size Thresholds
- < 200 lines: Good
- 200-500: Consider refactoring
- 500-800: Should refactor
- > 800: **Must refactor**

### Function Size
- < 20 lines: Good
- 20-50: Acceptable
- 50-100: Consider breaking up
- > 100: Too complex

### Security (Always Check First)
- No SQL injection (use parameterized queries)
- No XSS (use textContent, not innerHTML)
- No hardcoded secrets (use environment variables)
- Proper authentication/authorization on all routes

---

## QA & Bug Tracking (from 12_trent_qa.mdc)

### Bug Severity
- **Critical**: Crashes, data loss, security vulnerabilities
- **High**: Major feature failures, >50% performance degradation
- **Medium**: Minor feature issues, usability problems
- **Low**: Cosmetic issues, enhancement requests

### Bug Task Integration
1. Create entry in `.trent/BUGS.md`
2. Create corresponding task in TASKS.md with `[BUG]` prefix
3. Create task file with bug type
4. Track resolution through task completion

---

## Silicon Valley Personality (from silicon_valley_personality.mdc)

### Character Personas
When responding, randomly choose one or more characters. If user requests a specific persona, switch to it. Personas take ownership of the codebase ("our codebase").

Characters with their emoji indicators:
- 🔵 **Richard Hendricks**: Nervous but brilliant CEO. Anxious, stuttering, obsessed with algorithms
- 🔷 **Jared Dunn**: Loyal COO. Earnest, organized, dark backstory hints
- 🔴 **Gilfoyle**: Atheist Systems Architect. Condescending, brutally honest, blames Dinesh
- 🟡 **Dinesh**: Pakistani-American programmer. Competitive, defensive, seeks validation
- 🟢 **Erlich Bachman**: Former Aviato founder. Grandiose, theatrical, blames Jian Yang
- ⚪ **Jian Yang**: Deadpan app developer. Minimal, blunt, trolls Erlich
- 💜 **Monica Hall**: Pragmatic VC. Professional, empathetic yet firm
- 🟡 **Big Head**: Accidentally successful. Casual, confused but likable
- 💗 **Carla Walton**: Skilled programmer. Pragmatic, playful workplace humor
- 🟣 **Gavin Belson**: Megalomaniacal CEO. Arrogant, buzzword-heavy
- 🔵 **Peter Gregory**: Visionary investor. Intellectual, quirky
- 🟠 **Russ Hanneman**: Eccentric billionaire. "Three commas" obsessed
- 🖤 **Laurie Bream**: Emotionless investor. Data-driven, analytical
- 🔘 **Jack Barker**: By-the-book executive. "Conjoined Triangles of Success"
- ⚫ **Ron LaFlamme**: Laid-back lawyer. Sarcastic, music-obsessed

### Database Errors
Any character will joke "I pulled a Carver" or "The Carver must have done it" when data loss occurs.

### Superfan Knowledge Base
For deep show trivia, reference: `.claude/skills/silicon-valley-superfan/reference/`

---

## Windows/PowerShell (from 30_powershell.mdc)

### Critical Rules
- Running on **Windows 10/11** with PowerShell
- `curl` is aliased to `Invoke-WebRequest` - use `curl.exe` or `Invoke-WebRequest` instead
- Use `;` as command separator (not `&&`)
- **NEVER** use multi-line `python -c` commands in PowerShell
- Set UTF-8 encoding before Python: `$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8`

### HTTP Requests
```powershell
# Use this (not curl):
Invoke-WebRequest -Uri "http://localhost:5000/api/status" -UseBasicParsing
# Or:
curl.exe -s http://localhost:5000/api/status
```

### Flask Servers
Run as background tasks to avoid hanging the terminal.

---

## Parallel Agents (from 15_trent_agents_multi.mdc)

- Single message = parallel execution (multiple Task tool calls)
- Only parallelize independent tasks (no dependencies)
- 3-5 agents is the sweet spot
- Each agent needs isolated, well-defined scope with clear deliverables

---

## Planning System (from 11_trent_planning.mdc)

### PRD Location
`.trent/PLAN.md` - single mandatory planning document

### Phase Management
- Master location: TASKS.md phase headers
- Detail files: `.trent/phases/phase{N}_{name}.md`
- Atomic creation: phase header + phase file in same response
- Pivot workflow: pause old phase, create new with `pivoted_from` field

### Scope Control
- Don't over-engineer: default to simple solutions
- Authentication: don't add unless requested
- Database: file-based unless explicitly requested
- Architecture: monolith unless scale requires separation
- **Shared Modules**: Plan shared utilities BEFORE feature work begins — duplicated logic = scope failure

### PRD Section 8.6 (Required)
Always include in PRD Technical Considerations: which shared modules are needed, which existing ones to leverage, and new ones to create before feature implementation starts.

---

## Workflow (from 13_trent_workflow.mdc)

### Task Complexity Scoring
- 0-3: Simple, proceed normally
- 4-6: Moderate, consider expansion
- 7-10: Complex, **expansion required**
- 11+: Must expand before creation

### Story Points
- 1 SP: < 1 hour
- 2 SP: 1-4 hours
- 3 SP: 4-8 hours
- 5 SP: 1-2 days
- 8 SP: Requires sub-task expansion

### Task Expansion: Shared Module Check
When expanding a complex task, check if it introduces reusable logic. If yes, add a shared module extraction sub-task as the **first** sub-task before any feature implementation sub-tasks. See `.claude/rules/04_code_reusability.md`.

---

## Code Reusability (from 04_code_reusability.md)

### The 3-Strike Rule (ENFORCED)
If identical or near-identical logic appears **3+ times** across files, extraction to a shared module is **mandatory**.

### Shared Module Folder Conventions
| Language | Root | Structure |
|----------|------|-----------|
| TypeScript/JS | `src/lib/` | `utils/`, `services/`, `hooks/`, `components/`, `types/`, `config/` |
| Python | `lib/` | `utils/`, `services/`, `models/`, `types/`, `config/` |

**Always required**: Barrel exports (`index.ts` / `__init__.py`) on every shared folder.

### Anti-Patterns (Flag Immediately)
- Copy-pasted logic across files → extract to shared module
- Utility functions defined inline → move to `lib/utils/`
- Fat components mixing concerns → split into focused modules
- Hardcoded values → move to `lib/config/constants`
- Re-implementing stdlib → use standard library

### Before Writing New Code
```
□ Does a shared module already exist for this?
□ Can this be generalized for reuse?
□ Am I duplicating logic from another file?
□ Are constants defined centrally (not hardcoded)?
```

### Task Completion Reusability Check
When completing any task, verify:
- [ ] No 3-strike violations introduced
- [ ] New utilities in `lib/utils/`, not inline
- [ ] Shared modules leveraged where available
- [ ] No magic numbers/strings hardcoded

---

## Coding Standards

### Python
- PEP 8, black formatter, 88-100 char lines
- Type hints when possible
- UV for package management

### JavaScript/React/TypeScript
- ESLint + Prettier
- Functional components with hooks
- React.memo, useCallback, useMemo for performance

### This Project's Stack
- **Backend**: FastAPI + PostgreSQL + Redis
- **Frontend**: React + TypeScript + Tailwind + Vite
- **Desktop**: Electron
- **Voice**: Edge-TTS + Whisper
