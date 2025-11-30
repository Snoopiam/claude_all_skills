# Best Practices Checklist

Comprehensive checklist of industry best practices for evaluating project health. Use this reference when assessing findings and generating recommendations.

## Code Quality Best Practices

### Naming Conventions
- [ ] Variables and functions have meaningful, descriptive names
- [ ] Names reveal intent (what, not how)
- [ ] Consistent naming style throughout codebase (camelCase, snake_case, etc.)
- [ ] No abbreviations unless universally understood
- [ ] Boolean variables/functions start with is/has/can/should
- [ ] Classes are nouns, functions are verbs

### Functions and Methods
- [ ] Functions do one thing (Single Responsibility)
- [ ] Functions are small (ideally < 20 lines)
- [ ] Maximum 3-4 parameters per function
- [ ] No side effects in functions that return values
- [ ] Early returns to reduce nesting
- [ ] Guard clauses for validation

### Code Organization
- [ ] Related code is grouped together
- [ ] Clear module/file boundaries
- [ ] Consistent file structure across similar modules
- [ ] No circular dependencies
- [ ] Dependency injection for loose coupling
- [ ] Configuration separated from code

### Error Handling
- [ ] All errors are handled appropriately
- [ ] Specific error types, not generic catches
- [ ] Errors contain useful context
- [ ] Errors are logged with appropriate level
- [ ] User-facing errors are friendly
- [ ] Critical errors trigger alerts

### Comments and Documentation
- [ ] Code is self-documenting where possible
- [ ] Comments explain WHY, not WHAT
- [ ] No commented-out code
- [ ] Public APIs have documentation
- [ ] Complex algorithms are explained
- [ ] TODOs have owners and dates

## Testing Best Practices

### Test Coverage
- [ ] Critical paths have 80%+ coverage
- [ ] All public APIs have tests
- [ ] Edge cases are covered
- [ ] Error paths are tested
- [ ] Integration points have tests
- [ ] Performance-critical code has benchmarks

### Test Quality
- [ ] Tests are independent (no shared state)
- [ ] Tests are deterministic (no flaky tests)
- [ ] Tests are fast (unit tests < 100ms each)
- [ ] Test names describe the scenario
- [ ] Arrange-Act-Assert pattern used
- [ ] Mocks are used appropriately

### Test Organization
- [ ] Tests are colocated with code OR in parallel structure
- [ ] Clear distinction between unit/integration/e2e
- [ ] Test utilities are shared and maintained
- [ ] Test data is managed (fixtures, factories)
- [ ] CI runs all tests on every push
- [ ] Test failures block merges

## Documentation Best Practices

### README
- [ ] Project description and purpose
- [ ] Prerequisites and requirements
- [ ] Installation instructions
- [ ] Configuration guide
- [ ] Quick start example
- [ ] How to run tests
- [ ] How to contribute
- [ ] License information
- [ ] Contact/support information

### API Documentation
- [ ] All endpoints documented
- [ ] Request/response formats shown
- [ ] Error codes listed
- [ ] Authentication explained
- [ ] Rate limits documented
- [ ] Examples for each endpoint
- [ ] Versioning policy stated

### Architecture Documentation
- [ ] System overview diagram
- [ ] Component descriptions
- [ ] Data flow diagrams
- [ ] Integration points documented
- [ ] Technology stack listed
- [ ] Deployment architecture
- [ ] Security model

### Decision Records
- [ ] Major decisions documented (ADRs)
- [ ] Context and constraints captured
- [ ] Alternatives considered
- [ ] Trade-offs explained
- [ ] Decision date and authors
- [ ] Superseded decisions linked

## Version Control Best Practices

### Commit Hygiene
- [ ] Atomic commits (one logical change)
- [ ] Meaningful commit messages
- [ ] Conventional commits format (optional)
- [ ] No large binary files committed
- [ ] Sensitive data never committed
- [ ] .gitignore properly configured

### Branching Strategy
- [ ] Main branch always deployable
- [ ] Feature branches for new work
- [ ] Branch names are descriptive
- [ ] Branches are short-lived (< 1 week ideal)
- [ ] Stale branches cleaned up
- [ ] Protected branches configured

### Code Review
- [ ] All changes reviewed before merge
- [ ] Review checklist exists
- [ ] Constructive feedback culture
- [ ] Reviews completed within 24 hours
- [ ] CI passes before review
- [ ] No self-merges on critical code

### Release Management
- [ ] Semantic versioning used
- [ ] Releases are tagged
- [ ] Changelog maintained
- [ ] Release notes written
- [ ] Rollback procedure documented
- [ ] Feature flags for risky changes

## Security Best Practices

### Authentication & Authorization
- [ ] Strong password requirements
- [ ] Multi-factor authentication available
- [ ] Session management is secure
- [ ] JWT tokens expire appropriately
- [ ] Permissions follow least privilege
- [ ] OAuth implemented correctly (if used)

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] Data encrypted in transit (HTTPS)
- [ ] PII is identified and protected
- [ ] Data retention policy exists
- [ ] Backup and recovery tested
- [ ] GDPR/compliance requirements met

### Input Validation
- [ ] All user input validated
- [ ] SQL injection prevented (parameterized queries)
- [ ] XSS prevented (output encoding)
- [ ] CSRF protection enabled
- [ ] File uploads restricted and scanned
- [ ] API rate limiting implemented

### Secrets Management
- [ ] No secrets in code
- [ ] Environment variables for secrets
- [ ] Secrets rotated regularly
- [ ] Access to secrets audited
- [ ] Different secrets per environment
- [ ] Secret scanning in CI

### Dependency Security
- [ ] Dependencies audited regularly
- [ ] Known vulnerabilities patched
- [ ] Dependency updates automated
- [ ] Lock files committed
- [ ] Minimal dependencies used
- [ ] Licenses are compatible

## DevOps Best Practices

### CI/CD Pipeline
- [ ] Automated builds on every push
- [ ] Automated tests in pipeline
- [ ] Static analysis in pipeline
- [ ] Security scanning in pipeline
- [ ] Deployment is automated
- [ ] Pipeline is fast (< 10 min ideal)

### Environment Management
- [ ] Environments are identical (dev/staging/prod)
- [ ] Configuration is externalized
- [ ] Infrastructure as Code
- [ ] Environments are disposable
- [ ] Database migrations are automated
- [ ] Secrets differ per environment

### Monitoring & Observability
- [ ] Health check endpoints exist
- [ ] Application metrics collected
- [ ] Logs are centralized
- [ ] Distributed tracing enabled
- [ ] Alerts configured for issues
- [ ] Dashboards for key metrics

### Incident Management
- [ ] On-call rotation exists
- [ ] Runbooks for common issues
- [ ] Incident response process defined
- [ ] Post-mortems conducted
- [ ] SLOs/SLAs defined
- [ ] Status page maintained

## Project Management Best Practices

### Requirements Management
- [ ] Requirements are documented
- [ ] Acceptance criteria defined
- [ ] Requirements are prioritized
- [ ] Requirements are traceable
- [ ] Changes are managed
- [ ] Stakeholders are identified

### Task Management
- [ ] Work is tracked in a system
- [ ] Tasks are small and estimable
- [ ] Progress is visible
- [ ] Blockers are escalated
- [ ] Technical debt is tracked
- [ ] Backlog is groomed

### Communication
- [ ] Regular team syncs
- [ ] Stakeholder updates
- [ ] Decision logs maintained
- [ ] Documentation accessible
- [ ] Onboarding materials exist
- [ ] Knowledge sharing happens

## Scoring Guide

When auditing, score each category:

| Score | Criteria |
|-------|----------|
| 90-100% | Excellent - Best practices fully followed |
| 70-89% | Good - Most practices followed, minor gaps |
| 50-69% | Fair - Significant gaps, improvement needed |
| 30-49% | Poor - Major gaps, urgent improvement needed |
| 0-29% | Critical - Fundamental practices missing |

## Priority Matrix

When recommending improvements, prioritize:

```
                    HIGH IMPACT
                        |
        Quick Wins      |     Major Projects
        (Do First)      |     (Plan Carefully)
                        |
LOW EFFORT -------------|-------------- HIGH EFFORT
                        |
        Fill Ins        |     Thankless Tasks
        (Do When Idle)  |     (Reconsider Need)
                        |
                    LOW IMPACT
```
