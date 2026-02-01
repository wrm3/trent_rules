# Hooks Index

> Quick reference for all available hooks in this system.
> 
> **Location**: `.cursor/hooks/`
> **Usage**: Hooks are lifecycle events that trigger automatically.

---

## Current Hooks

| Hook | Description | Trigger |
|------|-------------|---------|
| *None active* | Hooks directory exists but no active hooks | - |

---

## Hook Concepts

Hooks are automated triggers that run at specific lifecycle events:

### Potential Hook Types

| Hook Type | When It Runs | Use Case |
|-----------|--------------|----------|
| `pre-commit` | Before git commit | Linting, formatting |
| `post-commit` | After git commit | Notifications, CI trigger |
| `pre-task` | Before starting a task | Validation, setup |
| `post-task` | After completing a task | Cleanup, documentation |
| `on-error` | When an error occurs | Logging, recovery |
| `on-file-change` | When files are modified | Auto-formatting, sync |

### Hook File Structure

```markdown
# Hook: hook-name

## Trigger
[When this hook runs]

## Actions
[What this hook does]

## Configuration
[Any settings or options]
```

---

## Why No Active Hooks?

The Trent system currently handles lifecycle events through:

1. **Rules** - Always-applied rules handle most automation
2. **Commands** - User-triggered actions for specific workflows
3. **Skills** - Activated by context/triggers

Hooks would add complexity for scenarios that are already covered.

## When to Add Hooks

Consider adding hooks when you need:

- **Automatic actions** that should ALWAYS run (no user choice)
- **Pre/post processing** around specific events
- **Integration triggers** with external systems

---

## Hook Count Summary

- **Total Hooks**: 0 (intentional)
- **README only**: Documentation placeholder

---

*Last updated: 2026-02-01*
