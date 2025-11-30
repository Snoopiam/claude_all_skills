# Remediation Patterns

Common problems found during project audits and proven solutions to fix them.

## Requirements & Planning Gaps

### Problem: No Requirements Documentation

**Symptoms:**
- No PRD, spec, or requirements files found
- Features exist without documented purpose
- Team relies on tribal knowledge

**Remediation:**
1. **Immediate (This Sprint):**
   - Create `docs/requirements.md` with current features
   - Interview team members to capture known requirements
   - Document the "as-is" state

2. **Short-term (This Month):**
   - Establish requirement template
   - Retroactively document top 10 features
   - Create user story backlog

3. **Long-term (Ongoing):**
   - Require requirements before development
   - Link commits to requirements (e.g., "Implements REQ-001")
   - Regular requirement review sessions

**Template:**
```markdown
# Requirements

## REQ-001: [Feature Name]
**Priority:** P1
**Status:** Implemented

**Description:**
[What the feature does]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Implementation:** `src/feature/`
**Tests:** `tests/feature/`
```

---

### Problem: Scope Creep Detected

**Symptoms:**
- Features exist that weren't in original plan
- Codebase is larger than expected
- Deadlines are missed

**Remediation:**
1. **Immediate:**
   - Document all unplanned features
   - Categorize: Essential vs Nice-to-Have
   - Get stakeholder acknowledgment

2. **Short-term:**
   - Implement change request process
   - Create scope document with in/out sections
   - Establish approval workflow for new features

3. **Long-term:**
   - Regular scope reviews
   - Track scope changes in changelog
   - Include scope impact in estimates

**Process Template:**
```markdown
# Change Request: [Feature Name]

**Requested by:** [Name]
**Date:** [Date]
**Priority:** [P0-P3]

**Description:**
[What is being requested]

**Justification:**
[Why this is needed]

**Impact Assessment:**
- Timeline: [Impact]
- Resources: [Impact]
- Existing features: [Impact]

**Decision:** [ ] Approved [ ] Rejected [ ] Deferred
**Decided by:** [Name]
**Date:** [Date]
```

---

## Code Quality Issues

### Problem: High Technical Debt (TODO/FIXME accumulation)

**Symptoms:**
- Numerous TODO/FIXME comments
- Code contains HACK/WORKAROUND markers
- Developers afraid to touch certain areas

**Remediation:**
1. **Immediate:**
   - Catalog all debt markers with `grep -rn "TODO\|FIXME\|HACK" src/`
   - Categorize by severity and effort
   - Create tracking issues for each

2. **Short-term:**
   - Adopt "Boy Scout Rule" (leave code better than found)
   - Dedicate 20% of sprint capacity to debt
   - Establish debt budget (max allowed TODOs)

3. **Long-term:**
   - Add debt limits to CI (fail if > threshold)
   - Track debt metrics over time
   - Celebrate debt reduction

**Debt Tracking Template:**
```markdown
## Technical Debt Register

| ID | Location | Type | Description | Effort | Priority | Owner |
|----|----------|------|-------------|--------|----------|-------|
| TD-001 | src/api.js:45 | FIXME | Error handling incomplete | S | High | - |
| TD-002 | src/db.js:123 | TODO | Add connection pooling | M | Medium | - |
```

---

### Problem: Low Test Coverage

**Symptoms:**
- Coverage below 60%
- Critical paths untested
- Bugs regress frequently

**Remediation:**
1. **Immediate:**
   - Identify coverage gaps: `npm test -- --coverage`
   - List top 10 untested critical files
   - Add tests to next sprint

2. **Short-term:**
   - Require tests for all new code (PR requirement)
   - Add coverage gates in CI (e.g., fail if < 60%)
   - Pair program on test writing

3. **Long-term:**
   - Adopt TDD for new features
   - Regular testing workshops
   - Test coverage as team metric

**Coverage Improvement Plan:**
```markdown
## Test Coverage Improvement

### Current: 45%
### Target: 80%
### Timeline: 3 sprints

### Sprint 1 Focus:
- [ ] src/auth/ (critical) - 0% -> 80%
- [ ] src/payment/ (critical) - 20% -> 80%

### Sprint 2 Focus:
- [ ] src/api/ - 40% -> 80%
- [ ] src/services/ - 35% -> 75%

### Sprint 3 Focus:
- [ ] Remaining modules to 60%+
- [ ] Integration tests for critical flows
```

---

### Problem: No Error Handling

**Symptoms:**
- Try-catch blocks missing
- Errors not logged
- Application crashes on edge cases

**Remediation:**
1. **Immediate:**
   - Add global error handler
   - Implement logging for all catch blocks
   - Fix critical crash points

2. **Short-term:**
   - Define error handling standards
   - Create error handling utilities
   - Add error tests

3. **Long-term:**
   - Error monitoring (Sentry, etc.)
   - Error budget tracking
   - Graceful degradation patterns

**Error Handling Pattern:**
```javascript
// Bad
async function getUser(id) {
  const user = await db.query(`SELECT * FROM users WHERE id = ${id}`);
  return user;
}

// Good
async function getUser(id) {
  try {
    const user = await db.query('SELECT * FROM users WHERE id = ?', [id]);
    if (!user) {
      throw new NotFoundError(`User ${id} not found`);
    }
    return user;
  } catch (error) {
    logger.error('Failed to get user', { userId: id, error });
    if (error instanceof NotFoundError) {
      throw error;
    }
    throw new DatabaseError('Failed to retrieve user', { cause: error });
  }
}
```

---

## Documentation Gaps

### Problem: Missing or Incomplete README

**Symptoms:**
- README is empty or boilerplate
- New team members struggle to onboard
- Setup instructions are outdated

**Remediation:**
1. **Immediate:**
   - Create minimum viable README
   - Include setup instructions
   - Add quick start example

2. **Short-term:**
   - Expand with configuration details
   - Add troubleshooting section
   - Include contribution guidelines

**README Template:**
```markdown
# Project Name

Brief description of what this project does.

## Prerequisites

- Node.js 18+
- PostgreSQL 14+

## Installation

```bash
git clone [repo]
cd [project]
npm install
cp .env.example .env
# Edit .env with your values
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| DATABASE_URL | PostgreSQL connection | - |
| API_KEY | External API key | - |

## Running

```bash
# Development
npm run dev

# Production
npm run build && npm start
```

## Testing

```bash
npm test
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT
```

---

### Problem: No API Documentation

**Symptoms:**
- Consumers don't know how to use API
- Frequent questions about endpoints
- Integration errors are common

**Remediation:**
1. **Immediate:**
   - List all public endpoints
   - Document request/response formats
   - Add authentication details

2. **Short-term:**
   - Implement OpenAPI/Swagger
   - Generate docs from code
   - Add examples for each endpoint

3. **Long-term:**
   - Auto-generate from code comments
   - Keep in sync with implementation
   - Include in CI validation

**API Documentation Template:**
```markdown
## POST /api/users

Create a new user.

### Authentication
Requires `Authorization: Bearer <token>`

### Request Body
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user"
}
```

### Response

**201 Created**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "name": "John Doe",
  "createdAt": "2024-01-01T00:00:00Z"
}
```

**400 Bad Request**
```json
{
  "error": "VALIDATION_ERROR",
  "message": "Email is required"
}
```

**409 Conflict**
```json
{
  "error": "DUPLICATE_EMAIL",
  "message": "Email already exists"
}
```
```

---

## Architecture Issues

### Problem: Architecture Drift

**Symptoms:**
- Implementation doesn't match design docs
- Unexpected dependencies between modules
- "It evolved organically" explanations

**Remediation:**
1. **Immediate:**
   - Document current architecture (as-is)
   - Identify critical violations
   - Create Architecture Decision Records for changes

2. **Short-term:**
   - Update design docs to match reality (or fix code)
   - Add architecture tests (dependency checks)
   - Review architecture in PRs

3. **Long-term:**
   - Regular architecture reviews
   - Architectural fitness functions
   - Living documentation

**ADR Template:**
```markdown
# ADR-001: [Decision Title]

## Status
Accepted | Superseded | Deprecated

## Context
What is the issue that we're seeing that is motivating this decision?

## Decision
What is the change that we're proposing/doing?

## Consequences
What becomes easier or more difficult because of this change?

## Alternatives Considered
What other options were evaluated?
```

---

### Problem: Circular Dependencies

**Symptoms:**
- Import cycles detected
- Module A imports B, B imports A
- Difficult to understand code flow

**Remediation:**
1. **Immediate:**
   - Map all circular dependencies
   - Identify dependency direction violations
   - Prioritize by impact

2. **Short-term:**
   - Extract shared code to new module
   - Use dependency injection
   - Invert dependencies where needed

3. **Long-term:**
   - Add cycle detection to CI
   - Define module boundaries clearly
   - Regular dependency analysis

**Pattern to Fix:**
```
Before (circular):
A -> B -> A

After (extracted):
A -> C
B -> C

Or (inverted):
A -> Interface
B implements Interface
```

---

## Security Issues

### Problem: Secrets in Code

**Symptoms:**
- API keys hardcoded
- Passwords in config files
- Secrets visible in git history

**Remediation:**
1. **Immediate (URGENT):**
   - Rotate ALL exposed secrets
   - Remove from code
   - Add to .gitignore

2. **Short-term:**
   - Use environment variables
   - Implement secrets management
   - Add secret scanning to CI

3. **Long-term:**
   - Regular secret rotation
   - Audit secret access
   - Use vault solutions

**Secrets Cleanup Checklist:**
```markdown
## Secret Remediation

### Exposed Secrets Found:
- [ ] AWS_SECRET_KEY in src/config.js
- [ ] DATABASE_PASSWORD in docker-compose.yml
- [ ] API_KEY in .env (committed)

### Rotation Status:
- [ ] AWS credentials rotated
- [ ] Database password changed
- [ ] API key regenerated

### Prevention Measures:
- [ ] Added pre-commit hook for secret detection
- [ ] Updated .gitignore
- [ ] Added secret scanning to CI
- [ ] Documented secrets management process
```

---

### Problem: Missing Input Validation

**Symptoms:**
- SQL injection possible
- XSS vulnerabilities
- Malformed data causes errors

**Remediation:**
1. **Immediate:**
   - Audit all user inputs
   - Add validation to critical endpoints
   - Parameterize all SQL queries

2. **Short-term:**
   - Implement validation library
   - Add input schemas
   - Security testing in CI

3. **Long-term:**
   - Regular security audits
   - Penetration testing
   - Security training for developers

**Validation Pattern:**
```javascript
// Bad
app.post('/users', (req, res) => {
  db.query(`INSERT INTO users (email) VALUES ('${req.body.email}')`);
});

// Good
const { z } = require('zod');

const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
});

app.post('/users', (req, res) => {
  const result = createUserSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error });
  }
  db.query('INSERT INTO users (email, name) VALUES (?, ?)',
    [result.data.email, result.data.name]);
});
```

---

## Process Issues

### Problem: No CI/CD Pipeline

**Symptoms:**
- Manual deployments
- "Works on my machine" issues
- Inconsistent builds

**Remediation:**
1. **Immediate:**
   - Set up basic CI (build + test)
   - Add linting to pipeline
   - Block merges on failure

2. **Short-term:**
   - Add deployment automation
   - Include security scanning
   - Add coverage reporting

3. **Long-term:**
   - Full CD with staging environments
   - Automated rollbacks
   - Infrastructure as code

**Starter GitHub Actions:**
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm run build
```

---

### Problem: No Code Review Process

**Symptoms:**
- Direct commits to main
- Bugs slip through
- Knowledge silos

**Remediation:**
1. **Immediate:**
   - Enable branch protection
   - Require at least 1 review
   - Document review expectations

2. **Short-term:**
   - Create review checklist
   - Establish review SLA (24 hours)
   - Add automated checks

3. **Long-term:**
   - Review metrics tracking
   - Pair programming sessions
   - Knowledge sharing rotations

**Review Checklist:**
```markdown
## Code Review Checklist

### Correctness
- [ ] Code does what it's supposed to do
- [ ] Edge cases handled
- [ ] Error cases handled

### Quality
- [ ] Code is readable
- [ ] No unnecessary complexity
- [ ] Follows project conventions

### Testing
- [ ] Tests added/updated
- [ ] Tests are meaningful
- [ ] Coverage adequate

### Security
- [ ] No hardcoded secrets
- [ ] Input validated
- [ ] No obvious vulnerabilities

### Documentation
- [ ] Public APIs documented
- [ ] Complex logic explained
- [ ] README updated if needed
```

---

## Quick Reference: Common Fixes

| Problem | Quick Fix |
|---------|-----------|
| No README | Copy template, fill in basics |
| Missing tests | Add tests for bug fixes first |
| Hardcoded config | Extract to .env |
| No linting | Add ESLint/Prettier with defaults |
| No CI | Add GitHub Actions starter |
| Old dependencies | Run `npm update` carefully |
| No error handling | Add global error handler |
| Missing docs | Generate from code comments |
| Architecture drift | Document as-is, then plan changes |
| Scope creep | Document, get approval, track |
