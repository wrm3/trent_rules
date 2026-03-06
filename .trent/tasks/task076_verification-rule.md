---
id: 76
title: 'Create new rule: verification and cross-agent review workflow'
type: feature
status: pending
priority: high
phase: 0
subsystems: [agent-rules, verification]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [30, 31, 32, 33, 34]
project_context: 'Verification deserves its own rule file — the cross-agent verification workflow, adversarial review persona, evidence checking protocol, and solo exception are complex enough to consolidate separately from the main tasks rule'
---

# Task 076: Create new rule: verification and cross-agent review workflow

## Objective
Create `template_v2/.cursor/rules/32_trent_verification.mdc` — a dedicated rule file for the complete verification workflow, consolidating all verification protocols from tasks 030-034.

## Rule Content Summary

```markdown
# Verification and Cross-Agent Review

## The Core Rule
A task CANNOT reach [✅] without being verified by a DIFFERENT agent than the one that implemented it.

This is not optional. This is not waivable by the implementing agent.

## Status Flow
[🔄] (implementing) → (done) → fill evidence_of_completion → [🔍] (awaiting verification)
                                                                    ↓ (different agent)
[✅] (approved)  ←←← APPROVED ←←← verify evidence + criteria
[🔄] (returned)  ←←← RETURNED ←←← evidence fails

## Implementing Agent Responsibilities
Before setting status: awaiting_verification, you MUST:
1. Complete Pre-Mortem (task034)
2. Complete all acceptance criteria  
3. Fill evidence_of_completion with independently checkable artifacts (task031)
4. Commit: "impl(task-{id}): complete — awaiting verification"

## Verification Agent Persona (MANDATORY)
[reference task033 adversarial persona instruction]
"You are the most skeptical senior engineer on the team..."

## Verification Review Format
[reference task033 review template]

## What Verifiers Check
[reference task031 evidence types]
[reference task032 acceptance criteria check]

## Verification Outcomes
**APPROVED**: Set verified_by, verified_at, status: completed, [🔍] → [✅]
**RETURNED**: Document failure, set status: in_progress, [🔍] → [🔄]

## Solo Exception
[reference task032 solo exception rules]

## Human Override
[reference task032 human override rules]
```

## Acceptance Criteria
- [ ] New rule file `32_trent_verification.mdc` in template_v2 (all 3 IDEs)
- [ ] Core rule (different agent) stated explicitly
- [ ] Status flow diagram
- [ ] Implementing + verifying agent responsibilities
- [ ] Adversarial persona instruction
- [ ] Solo exception + human override

## Verification Steps
- [ ] Rule exists in all 3 IDE directories (parity compliant)
- [ ] "different agent" rule is explicit
- [ ] Adversarial persona instruction present

## When Stuck
- Assembly task from tasks 030-034 — pull each section from those specs
