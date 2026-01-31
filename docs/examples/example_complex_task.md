# Example: Complex Task with Sub-Tasks

**This example demonstrates how a complex task is broken down into sub-tasks using the trent workflow system.**

---

## Parent Task

```yaml
---
id: 142
title: 'Implement User Authentication System'
type: task
status: pending
priority: high
phase: 1
subsystems: [auth, database, api, frontend]
project_context: 'Enables secure user access to the application, required for all user-specific features. Supports project goal of multi-user collaboration.'
dependencies: [100, 101]
estimated_effort: '5-7 days'
complexity_score: 8
---

# Task 142: Implement User Authentication System

## Objective
Implement a complete user authentication system including registration, login, password reset, and session management. The system must be secure, scalable, and provide a foundation for role-based access control.

## Complexity Assessment
**Score: 8/10** - Requires expansion into sub-tasks

**Scoring Breakdown:**
- Estimated Effort: 4 points (5-7 days > 2-3 days)
- Cross-Subsystem Impact: 3 points (affects auth, database, api, frontend)
- Multiple Components: 3 points (registration, login, password reset, sessions)
- High Uncertainty: 1 point (security best practices need research)
- Multiple Outcomes: 2 points (registration, login, reset, sessions)
- **Total: 13 points** → **MANDATORY EXPANSION**

## Acceptance Criteria
- [ ] Users can register with email and password
- [ ] Users can login with credentials
- [ ] Users can reset forgotten passwords via email
- [ ] Sessions are securely managed
- [ ] Password requirements are enforced
- [ ] Authentication is integrated with API
- [ ] Frontend login/register UI is complete
- [ ] Security best practices are followed

## Sub-Tasks

This task has been expanded into the following sub-tasks:

1. **task142.1_setup_auth_database.md** - Database schema for users and sessions
2. **task142.2_implement_password_hashing.md** - Secure password storage
3. **task142.3_create_auth_api_endpoints.md** - Registration, login, reset APIs
4. **task142.4_build_frontend_auth_ui.md** - Login and registration forms
5. **task142.5_implement_session_management.md** - Secure session handling
6. **task142.6_add_password_reset_flow.md** - Email-based password reset
7. **task142.7_integrate_auth_with_api.md** - Protect API endpoints
8. **task142.8_security_testing.md** - Security audit and testing

## Implementation Notes
- Use bcrypt for password hashing (industry standard)
- Implement JWT tokens for session management
- Follow OWASP security guidelines
- Add rate limiting to prevent brute force attacks
- Use HTTPS for all authentication endpoints
- Store sessions in Redis for scalability (future)

## Dependencies
- Task 100: Database schema design (must complete first)
- Task 101: API framework setup (required for endpoints)

## Testing Plan
- Unit tests for password hashing
- Integration tests for auth flows
- Security testing (OWASP ZAP)
- Load testing for login endpoints
- Manual testing of all user flows
```

---

## Sub-Task Example: task142.1_setup_auth_database.md

```yaml
---
id: "142.1"
title: 'Setup Authentication Database Schema'
type: task
status: pending
priority: high
phase: 1
parent_task: 142
dependencies: [100]
subsystems: [database, auth]
project_context: 'Creates the database foundation for user authentication, storing user accounts, password hashes, and session data.'
---

# Task 142.1: Setup Authentication Database Schema

## Objective
Design and implement database tables for user authentication including users table, sessions table, and password reset tokens table.

## Acceptance Criteria
- [ ] Users table created with required fields (id, email, password_hash, created_at, updated_at)
- [ ] Sessions table created (id, user_id, token, expires_at, created_at)
- [ ] Password reset tokens table created (id, user_id, token, expires_at, used, created_at)
- [ ] Appropriate indexes created for performance
- [ ] Foreign key constraints established
- [ ] Database migrations written and tested
- [ ] Schema documented

## Implementation Notes
- Use UUID for primary keys
- Email must be unique and indexed
- Password hash field should be VARCHAR(255) for bcrypt
- Session tokens should expire after 24 hours
- Reset tokens should expire after 1 hour
- Add soft delete support for users (deleted_at field)

## Database Schema

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP NULL
);

CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE password_reset_tokens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_sessions_token ON sessions(token);
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_reset_tokens_token ON password_reset_tokens(token);
```

## Testing Plan
- Verify table creation
- Test foreign key constraints
- Test unique constraints
- Verify indexes are created
- Test migration rollback
```

---

## Sub-Task Example: task142.3_create_auth_api_endpoints.md

```yaml
---
id: "142.3"
title: 'Create Authentication API Endpoints'
type: task
status: pending
priority: high
phase: 1
parent_task: 142
dependencies: [142.1, 142.2, 101]
subsystems: [api, auth]
project_context: 'Provides REST API endpoints for user registration, login, logout, and password reset. Enables frontend to interact with authentication system.'
---

# Task 142.3: Create Authentication API Endpoints

## Objective
Implement REST API endpoints for user authentication: POST /api/auth/register, POST /api/auth/login, POST /api/auth/logout, POST /api/auth/reset-password, POST /api/auth/reset-password/confirm.

## Acceptance Criteria
- [ ] POST /api/auth/register endpoint created
- [ ] POST /api/auth/login endpoint created
- [ ] POST /api/auth/logout endpoint created
- [ ] POST /api/auth/reset-password endpoint created
- [ ] POST /api/auth/reset-password/confirm endpoint created
- [ ] Input validation on all endpoints
- [ ] Error handling with appropriate HTTP status codes
- [ ] Rate limiting implemented
- [ ] API documentation updated
- [ ] Unit tests written

## Implementation Notes
- Use Flask-RESTful for endpoint structure
- Validate email format and password strength
- Return JWT token on successful login
- Implement rate limiting (5 requests per minute per IP)
- Use proper HTTP status codes (200, 201, 400, 401, 429)
- Log authentication attempts for security monitoring

## API Endpoints

### POST /api/auth/register
**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (201):**
```json
{
  "user_id": "uuid",
  "email": "user@example.com",
  "message": "User registered successfully"
}
```

### POST /api/auth/login
**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "token": "jwt_token_here",
  "user_id": "uuid",
  "expires_at": "2026-01-28T12:00:00Z"
}
```

## Testing Plan
- Test successful registration
- Test registration with invalid email
- Test registration with weak password
- Test successful login
- Test login with wrong credentials
- Test rate limiting
- Test token expiration
```

---

**This example demonstrates:**
1. **Complexity Assessment**: Task scored 13/10, triggering mandatory expansion
2. **Sub-Task Breakdown**: Logical, sequential sub-goals
3. **Dependency Management**: Sub-tasks depend on each other and parent dependencies
4. **Detailed Implementation**: Each sub-task has clear acceptance criteria and notes
