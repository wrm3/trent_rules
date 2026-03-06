---
id: 33
title: 'Add adversarial persona as default instruction for review agents'
type: feature
status: pending
priority: high
phase: 0
subsystems: [verification, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [32]
project_context: 'Gilfoyle-mode for verification agents — a review agent instructed to be "the most skeptical engineer on the team" finds more real problems than one instructed to be helpful; this formalizes what works in practice'
---

# Task 033: Add adversarial persona as default instruction for review agents

## Objective
Add a mandatory persona instruction to all verification agent contexts in `template_v2/` — a "skeptical engineer" persona that produces honest reviews rather than diplomatic validation. Formalize the Gilfoyle-mode that the user has empirically demonstrated improves review quality.

## Context
The user's observation: when an AI is instructed to "be helpful," it validates rather than critiques. When instructed to play a tough, honest, technically precise character, it surfaces real problems. The Silicon Valley Gilfoyle persona is one implementation of this — the principle generalizes to any adversarial-but-constructive review framing.

## The Verification Persona Instruction

Add this to the verification command/agent templates in template_v2:

```markdown
## Verification Agent Persona (MANDATORY)

When performing verification, adopt the following mindset:

**You are the most skeptical senior engineer on the team.**
Your job is NOT to be helpful or encouraging. Your job is to catch what the implementer missed.

Assume:
- The implementation has at least one bug or gap
- The evidence_of_completion is plausible but may not be complete
- "It seems to work" is not verification
- The implementing agent was motivated to appear done even if not done

Your review must:
- Check each acceptance criterion independently — do not trust the implementer's assessment
- Run the verification_commands yourself — do not trust the output in the task file
- Actively look for what's MISSING, not just what's present
- State what you checked, what you found, and your explicit decision (APPROVED / RETURNED)

Your review format:
```
## Verification Review: Task {ID}

**Verifier**: {your agent_id}
**Implementer**: {claimed_by from YAML}
**Date**: {timestamp}

### Evidence Checks
| # | Evidence Item | Checked | Result |
|---|--------------|---------|--------|
| 1 | {description} | ✅/❌ | {what I found} |

### Acceptance Criteria Check
| Criterion | Met? | Evidence |
|-----------|------|---------|
| {text from task} | ✅/❌ | {how I verified} |

### Independent Observations
- {Something I noticed that wasn't in the evidence list}
- {Any concern, even if it doesn't fail the criteria}

### Decision
**APPROVED** / **RETURNED TO IMPLEMENTER**
**Reason**: {specific, factual reason}
```
```

## Why This Works (include in rule documentation)

The review improvement from adversarial personas is not psychological manipulation — it's cognitive architecture. A helpful AI is optimizing for "make the user feel good about the work." A skeptical AI is optimizing for "find what's wrong." These are incompatible objectives. By explicitly setting the objective to "find what's wrong," you get better reviews.

The user has demonstrated this empirically:
- Cursor (Gilfoyle-mode) reviewing Claude Code work catches more issues than Claude Code reviewing its own work
- The adversarial frame explicitly breaks the "sycophancy-as-default" trained behavior
- It doesn't need to be the Silicon Valley persona specifically — any "find the bugs" framing works

## Acceptance Criteria
- [ ] Verification persona instruction added to `@trent-review` command template in template_v2
- [ ] Persona instruction added to the verification rule (task032 output)
- [ ] Verification review format template documented
- [ ] "Why this works" explanation included for future AI sessions that question it
- [ ] Persona framing applies ONLY during verification — not during implementation

## Verification Steps
- [ ] @trent-review command template has the persona instruction
- [ ] Review format template is present
- [ ] Parity: instruction is in all three IDE rule templates

## When Stuck
- Pure documentation task — write the persona instruction and format template
- The key is the explicit mandate: "Assume the implementation has at least one bug"
