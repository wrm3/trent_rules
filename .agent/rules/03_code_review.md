---
description: "Comprehensive code review guidelines for security, quality, performance, and maintainability"
activation: "model_decision"
---

# Code Review Guidelines

Perform thorough code reviews following these standardized procedures.

## Review Types

**Quick Review** (< 100 lines):
- Security scan
- Style check
- Basic quality

**Standard Review** (100-500 lines):
- Full security scan
- Quality analysis
- Performance check

**Comprehensive Review** (> 500 lines):
- In-depth security
- Architecture review
- Performance profiling

## Security Checklist (CRITICAL - Always First)

### SQL Injection
```python
# ❌ VULNERABLE
query = f"SELECT * FROM users WHERE id={user_id}"

# ✅ SAFE
query = "SELECT * FROM users WHERE id=%s"
cursor.execute(query, (user_id,))
```

### XSS (Cross-Site Scripting)
```javascript
// ❌ VULNERABLE
div.innerHTML = user_input;

// ✅ SAFE
div.textContent = user_input;
```

### Authentication/Authorization
```python
# ❌ MISSING AUTH
@app.route('/admin/users')
def admin_users():
    return render_template('users.html')

# ✅ PROPER AUTH
@app.route('/admin/users')
@require_admin
def admin_users():
    if not current_user.is_admin:
        abort(403)
    return render_template('users.html')
```

### Secrets Exposure
```python
# ❌ HARDCODED
API_KEY = "sk-1234567890"

# ✅ FROM ENVIRONMENT
API_KEY = os.getenv('API_KEY')
```

## Code Quality Standards

### File Size
- < 200 lines: ✅ Good
- 200-500 lines: ⚠️ Consider refactoring
- 500-800 lines: ⚠️ Should refactor
- > 800 lines: ❌ Must refactor

### Function Size
- < 20 lines: ✅ Good
- 20-50 lines: ⚠️ Acceptable
- 50-100 lines: ⚠️ Consider breaking up
- > 100 lines: ❌ Too complex

### Naming Conventions

**Python:**
```python
# ✅ GOOD
user_count = 10
USER_API_KEY = "..."
class UserManager:
    def get_user_by_id(self, user_id):
        pass
```

**JavaScript/TypeScript:**
```javascript
// ✅ GOOD
const userCount = 10;
const USER_API_KEY = "...";
class UserManager {
    getUserById(userId) {}
}
```

## Performance Checks

### N+1 Query Problem
```python
# ❌ BAD (N+1 queries)
users = User.query.all()
for user in users:
    print(user.profile.bio)

# ✅ GOOD (2 queries total)
users = User.query.options(joinedload(User.profile)).all()
for user in users:
    print(user.profile.bio)
```

### Missing Indexes
```python
# Check if frequently queried fields are indexed
class User(db.Model):
    email = db.Column(db.String, index=True)  # ✅
```

## Reusability Checklist (HIGH - Check Every Review)

See `04_code_reusability.md` for full DRY standards and folder conventions.

### Duplication Detection
- [ ] No copy-pasted logic across files (3-strike rule: 3+ occurrences → extract MANDATORY)
- [ ] Utility functions placed in `lib/utils/` or `shared/`, not defined inline
- [ ] Existing shared modules used where applicable (checked `lib/`, `shared/`, `utils/`)
- [ ] No magic numbers/strings hardcoded (should be in `lib/config/constants`)

### Shared Module Quality
- [ ] New shared modules have clear, single responsibility
- [ ] Barrel exports (`index.ts` / `__init__.py`) used for clean import paths
- [ ] Shared modules are documented (docstrings/JSDoc on public functions)
- [ ] New shared modules have 2+ consumers (not premature abstraction)

## Review Output Format

```markdown
# Code Review: [Feature Name]

## Summary
**Recommendation:** [Approve / Request Changes / Comment]

## Security Issues
### CRITICAL
- [Issue with fix]

### HIGH
- [Issue with fix]

## Quality Issues
- [File size warnings]
- [Complexity warnings]

## Performance Concerns
- [With recommendations]

## Reusability Issues
- [Duplicated logic that should be extracted]
- [Inline utilities that belong in lib/utils/]
- [Missing shared module usage]

## Action Items
1. [ ] Fix CRITICAL issue X
2. [ ] Refactor large file Y
3. [ ] Add tests for Z
4. [ ] Extract duplicated logic to shared module (if applicable)
```

## Integration with fstrent-spec-tasks

Create tasks for:
- 🔴 CRITICAL/HIGH security issues → Immediate task
- ⚠️ Files > 800 lines → Refactoring task
- 📝 Missing tests → Improvement task

---

**For full details, see `.cursor/skills/trent-code-reviewer/rules.md`**
