---
description: "Git workflow standards for commit messages, branching, and collaboration"
activation: "model_decision"
---

# Git Workflow Standards

These standards apply to ALL git operations in this project.

## Commit Message Format

**Format:** `type(scope): description`

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, semicolons, etc.)
- **refactor**: Code refactoring (no functional changes)
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, dependencies, build config
- **perf**: Performance improvements

### Examples

```bash
feat(auth): add OAuth2 login support
fix(api): resolve null pointer in user endpoint
docs(readme): update installation instructions
refactor(database): simplify query builder logic
test(user): add integration tests for registration
chore(deps): update dependencies to latest versions
```

## Branching Strategy

### Branch Naming

**Format:** `type/short-description`

**Examples:**
```
feature/user-authentication
fix/login-button-crash
docs/api-documentation
refactor/database-layer
```

### Main Branches

- **main**: Production-ready code
- **develop**: Integration branch (if using GitFlow)

## Best Practices

### DO

✅ **Write clear, concise commit messages**
✅ **Commit logical units of work**
✅ **Use present tense** ("add feature" not "added feature")
✅ **Reference issues when applicable** (`fix(api): resolve timeout issue (#123)`)

### DON'T

❌ **Vague messages** (e.g., "fix stuff", "updates", "wip")
❌ **Commit sensitive data** (passwords, API keys, secrets)
❌ **Commit large binary files** (use Git LFS if necessary)

## Pull Request Guidelines

### PR Title Format

Same as commit message format: `feat(auth): add OAuth2 login support`

### Before Creating PR

1. ✅ Rebase on latest main
2. ✅ Resolve any conflicts
3. ✅ Ensure all tests pass
4. ✅ Update documentation
5. ✅ Self-review your changes
