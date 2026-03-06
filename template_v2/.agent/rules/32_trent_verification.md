---
description: Cross-agent verification workflow — implementer cannot self-verify, adversarial persona, evidence requirements
globs: 
alwaysApply: true
---
# Trent Verification Protocol (Rule 32)

Tasks do NOT complete when the implementer says they're done. Completion requires a **different agent** to verify the work.

This rule defines the full verification workflow.

---

## The Core Rule

```
IMPLEMENTER → status: awaiting-verification → VERIFIER → status: completed
```

**The agent that implemented a task CANNOT set it to `completed`.**

---

## Verification Workflow

### Step 1: Implementation Complete
Implementer:
1. Fills all acceptance criteria checkboxes in the task file
2. Creates evidence file at `.trent/logs/task{id}_evidence.log`
3. Fills `evidence_of_completion` in task YAML:
   ```yaml
   evidence_of_completion:
     type: test_output | compile_log | runtime_log | manual_check
     path: ".trent/logs/task{id}_evidence.log"
   ```
4. Sets `status: awaiting-verification`
5. Updates TASKS.md: `[🔄]` → `[🔍]`
6. Commits and pushes:
   ```bash
   git add .trent/tasks/task{id}_*.md .trent/logs/task{id}_evidence.log
   git commit -m "impl(task-{id}): implementation complete, awaiting verification"
   git push
   ```

### Step 2: Verifier Takes Over
Verifier (different agent):
1. Reads the task file — specifically `## Verification` section
2. Does NOT read the implementer's commentary — verifies independently
3. Runs the verification steps
4. Checks every acceptance criterion
5. Reviews evidence file

### Step 3: Verification Decision

**Pass** — all criteria met:
```yaml
verified_by: "{verifier_agent_id}"  # MUST differ from claimed_by
verified_date: "{today}"
status: completed
```
Update TASKS.md: `[🔍]` → `[✅]`

**Fail** — criteria not met:
```yaml
status: pending  # Reset for reimplementation
verified_by: null
```
Add failure_history entry with `reason: verification_rejected`.
Update TASKS.md: `[🔍]` → `[📋]`

---

## Adversarial Verification Persona (MANDATORY)

When verifying, the agent MUST adopt a skeptical stance. Default inner voice:

> "The implementer claims this works. I will try to prove it doesn't."

Verification checklist mindset:
- [ ] **Does it actually work, or does it just look like it works?**
- [ ] **What happens in the error case?** (implementer likely only tested happy path)
- [ ] **Is the evidence authentic?** (not just a screenshot of code, but actual output)
- [ ] **Do the acceptance criteria actually match what was built?**
- [ ] **Could this regress something existing?**

Do NOT rubber-stamp. A fast "LGTM" is a verification violation.

---

## Evidence File Standards

### Evidence File Format (`.trent/logs/task{id}_evidence.log`)

```
=== TASK {id} VERIFICATION EVIDENCE ===
Date: {ISO timestamp}
Implementer: {agent_id}
Rules-Version: {version}

=== ACCEPTANCE CRITERIA CHECKLIST ===
[✅] Criterion 1: {what was done to verify}
[✅] Criterion 2: {what was done to verify}

=== EVIDENCE ===
Type: test_output | compile_log | runtime_log | manual_check

{Actual output here — command run, result, or step-by-step walkthrough}

=== SIGN-OFF ===
Verified By: {verifier_agent_id}
Date: {ISO date}
Status: PASS | FAIL
```

---

## Evidence Type Requirements

| Type | What's Required |
|------|----------------|
| `test_output` | Full output from `pytest` / `jest` / `go test` showing pass count and zero failures |
| `compile_log` | Full build output with zero errors and zero warnings |
| `runtime_log` | Application started, relevant endpoint or function invoked, expected response shown |
| `manual_check` | Step-by-step walkthrough against each acceptance criterion with observed result |

**Lazy evidence examples (REJECT these):**
- "Code looks correct" — not evidence
- A screenshot of the code file — not evidence
- "Tested locally" with no output — not evidence
- A passing test for a different scenario than the acceptance criteria — not evidence

---

## Rules for Documentation-Only Tasks

Tasks with `type: documentation` and `requires_verification: false` may skip cross-agent verification.

They STILL require:
- Acceptance criteria checked off
- A manual check evidence entry confirming the docs are accurate
- `verified_by` set to the same agent (self-verify is permitted for docs-only)

---

## Verification Timeouts

If a task remains in `[🔍]` for more than 4 hours:
- Cleanup agent logs it in CLEANUP_REPORT.md
- Sprint agent will NOT attempt verification on a task already in `[🔍]` — that's stuck
- After 8 hours: cleanup agent resets to `[📋]` and adds a `failure_history` entry with `reason: verification_timeout`

---

## Self-Check (Before Ending Any Response)

```
□ Did I complete implementation for a task?
  → Set evidence_of_completion YAML
  → Set status: awaiting-verification
  → Update TASKS.md to [🔍]
  → Commit and push

□ Did I verify a task I also implemented?
  → VIOLATION: cannot self-verify non-documentation tasks
  → Reset to awaiting-verification, request different agent

□ Is there a task in [🔍] I can verify right now?
  → If I did NOT implement it: proceed with verification
  → If I DID implement it: skip, flag in response
```
