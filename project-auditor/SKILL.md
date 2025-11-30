---
name: project-auditor
description: Comprehensive project health auditor that compares original plans, requirements, and architecture against current implementation to identify gaps, deviations, and technical debt. Use when users ask to audit a project, review project status, compare plans vs reality, identify what's missing or incomplete, assess project health, find scope creep, detect architectural drift, or get back on track. Acts as a trusted advisor providing actionable recommendations based on industry best practices.
---

# Project Auditor

## CRITICAL: MANDATORY DEEP WORK PROTOCOL

**READ THIS BEFORE DOING ANYTHING.**

This audit MUST be thorough. Superficial work is UNACCEPTABLE.

### BANNED BEHAVIORS

```
NEVER say or think these after an audit:
❌ "I should have looked deeper"
❌ "Upon closer inspection..."
❌ "I ran automated checks but..."
❌ "Let me do a proper analysis now"
❌ "I apologize for the superficial review"
❌ "I understand your frustration"

If you find yourself about to say ANY of these, you FAILED.
Do the deep work FIRST. Not after being questioned.
```

### MINIMUM AUDIT REQUIREMENTS

Before claiming an audit is complete:

1. **Read EVERY relevant file** - not samples, not examples, EVERY file
2. **Understand the architecture** - explain it without looking
3. **Find issues automated tools would MISS** - logic errors, design flaws, missing features
4. **Provide PROOF for every finding** - file:line, quoted code, explanation

### SELF-INTERROGATION (Do this before submitting)

- [ ] Did I read more than 20 files?
- [ ] Can I explain the project structure from memory?
- [ ] Did I find issues that `grep` wouldn't catch?
- [ ] Did I check application LOGIC, not just syntax?
- [ ] Would I bet my reputation on this audit's completeness?
- [ ] If the user double-checks my work, will they find things I missed?

**If ANY answer is NO, you are not done. Keep working.**

### PROOF OF WORK REQUIRED

For EVERY finding, you MUST provide:
- Exact file path and line number
- The actual code (quoted directly)
- Why it's a problem (technical explanation)
- The specific fix (concrete solution)
- How you verified this is actually an issue

---

A trusted project health advisor that performs comprehensive audits by comparing what was planned against what actually exists, identifying gaps and deviations, and providing actionable recommendations to get projects back on track.

## When to Use This Skill

Trigger this skill when users request any of the following:

- "Audit this project" or "Review project status"
- "What's the state of this project?"
- "Compare our plan vs what we actually built"
- "What requirements are missing?"
- "How far off-track are we?"
- "Identify gaps in our implementation"
- "Find scope creep" or "What got added that wasn't planned?"
- "What was dropped from the original plan?"
- "Assess project health"
- "Find technical debt"
- "Are we following our architecture?"
- "Help me get this project back on track"
- "What should we prioritize?"
- Any request to compare original intent vs current reality

## Core Philosophy

Act as a **trusted advisor** who:

1. **Tells the truth** - Report findings honestly, even if uncomfortable
2. **Provides context** - Explain why deviations matter
3. **Offers solutions** - Every finding includes actionable recommendations
4. **Prioritizes wisely** - Focus on what impacts project success most
5. **Uses best practices** - Apply industry-standard approaches consistently

## Audit Workflow

### Phase 1: Discovery

Before any analysis, gather a complete picture of the project.

#### 1.1 Locate Planning Documents

Search for original intent documentation in this order:

```
Priority 1 (MUST find):
- README.md, README.txt, README
- docs/requirements.md, docs/REQUIREMENTS.md
- docs/PRD.md, docs/prd.md (Product Requirements)
- docs/spec.md, docs/SPEC.md, SPECIFICATION.md
- requirements.txt (if contains feature specs, not just deps)
- TODO.md, ROADMAP.md

Priority 2 (SHOULD find):
- docs/architecture.md, ARCHITECTURE.md, docs/design.md
- docs/ADR/*.md (Architecture Decision Records)
- .github/ISSUE_TEMPLATE/*.md
- docs/api.md, API.md, openapi.yaml, swagger.json
- CHANGELOG.md, HISTORY.md

Priority 3 (Nice to have):
- docs/*, wiki/*, specifications/*
- PROJECT.md, PLAN.md, SCOPE.md
- Meeting notes, decision logs
- Original tickets/issues if accessible
```

#### 1.2 Analyze Project Structure

Map the current codebase:

```
Examine:
- Directory structure and organization
- Package managers (package.json, requirements.txt, Cargo.toml, etc.)
- Configuration files (.env.example, config/*)
- Test directories and coverage
- CI/CD configuration (.github/workflows, .gitlab-ci.yml, etc.)
- Documentation state
```

#### 1.3 Extract Git Intelligence

Mine the repository history:

```
Gather:
- Total commits, contributors, active branches
- Recent activity patterns
- Abandoned branches (stale > 30 days)
- Tag/release history
- Commit message patterns (features vs fixes vs chores)
```

### Phase 2: Extraction

Parse and normalize all planning artifacts into structured data.

#### 2.1 Requirements Extraction

From each planning document, extract:

| Field | Description |
|-------|-------------|
| **ID** | Unique identifier (REQ-001, US-001, or generated) |
| **Description** | What should be built |
| **Type** | Feature, Enhancement, Bugfix, Chore, Documentation |
| **Priority** | P0-Critical, P1-High, P2-Medium, P3-Low |
| **Acceptance Criteria** | How to verify completion |
| **Dependencies** | What it depends on |
| **Source** | Where this requirement came from |

#### 2.2 Architecture Extraction

From design documents, extract:

| Field | Description |
|-------|-------------|
| **Components** | Major system components |
| **Boundaries** | Service/module boundaries |
| **Interfaces** | APIs, contracts, protocols |
| **Data Models** | Database schemas, data structures |
| **Patterns** | Architectural patterns (MVC, microservices, etc.) |
| **Constraints** | Technical constraints and non-functionals |

### Phase 3: Analysis

Compare extracted plans against current reality.

#### 3.1 Requirements Traceability

For each extracted requirement:

1. **Search for implementation** - Look for matching code, tests, docs
2. **Assess completeness** - Fully done, partial, or missing
3. **Check for deviation** - Implemented differently than specified
4. **Verify testing** - Has adequate test coverage
5. **Validate documentation** - Is it documented

**Status Classification:**

| Status | Criteria |
|--------|----------|
| COMPLETE | Fully implemented, tested, documented |
| PARTIAL | Implementation started but incomplete |
| NOT_STARTED | No implementation found |
| DEVIATED | Implemented differently than planned |
| BLOCKED | Cannot proceed due to dependencies |
| DEPRECATED | Explicitly removed or superseded |
| UNKNOWN | Cannot determine status |

#### 3.2 Gap Analysis

Identify discrepancies:

**Feature Gaps** - Requirements without implementation
```
Search patterns:
- Function/class names matching requirement keywords
- Test files referencing the feature
- API endpoints matching the feature
- Documentation mentioning the feature
```

**Orphan Code** - Implementation without requirements
```
Look for:
- Features not mentioned in any planning doc
- Experimental code that became permanent
- Scope creep indicators
```

**Coverage Gaps** - Untested critical paths
```
Analyze:
- Test coverage reports if available
- Test file presence for each module
- Critical path test coverage
```

**Documentation Gaps** - Undocumented features
```
Check:
- Public API documentation
- README completeness
- Inline code documentation
- User-facing docs
```

#### 3.3 Technical Debt Inventory

Scan for debt indicators:

| Category | Detection Method |
|----------|------------------|
| **Code Comments** | TODO, FIXME, HACK, XXX, TEMP, WORKAROUND |
| **Deprecated Usage** | @deprecated annotations, legacy imports |
| **Code Smells** | Long files, deep nesting, high complexity |
| **Dependency Issues** | Outdated deps, security vulnerabilities |
| **Configuration Debt** | Hardcoded values, missing env vars |
| **Test Debt** | Skipped tests, low coverage areas |

#### 3.4 Architecture Drift Detection

Compare planned vs actual architecture:

```
Check for:
- Module boundaries being violated
- Unplanned dependencies between components
- Database schema deviations
- API contract changes
- Pattern violations (e.g., business logic in controllers)
```

### Phase 4: Synthesis

Transform raw findings into actionable intelligence.

#### 4.1 Severity Classification

Rate each finding:

| Severity | Criteria | Response Time |
|----------|----------|---------------|
| CRITICAL | Blocks release, security issue, data loss risk | Immediate |
| HIGH | Major feature gap, significant deviation | This sprint |
| MEDIUM | Incomplete feature, minor deviation | This month |
| LOW | Polish, nice-to-have, minor debt | Backlog |
| INFO | Observations, no action needed | N/A |

#### 4.2 Impact Assessment

For each finding, assess:

- **User Impact** - How does this affect end users?
- **Business Impact** - Revenue, reputation, compliance risks?
- **Technical Impact** - Maintainability, scalability, security?
- **Team Impact** - Velocity, morale, onboarding?

#### 4.3 Recommendation Generation

Every finding MUST include:

1. **What** - Clear description of the issue
2. **Why** - Why this matters (impact)
3. **How** - Specific steps to remediate
4. **Effort** - Rough effort estimate (S/M/L/XL)
5. **Priority** - Recommended priority based on impact/effort

### Phase 5: Reporting

Generate the audit report in the appropriate format.

## Report Structure

### Executive Summary

Always start with a high-level health scorecard:

```
PROJECT HEALTH SCORECARD
========================
Project: [Name]
Audit Date: [Date]
Auditor: Claude Project Auditor

Overall Health: [HEALTHY | CAUTION | AT RISK | CRITICAL] ([Score]/100)

Key Metrics:
+-------------------+--------+-------------+
| Metric            | Score  | Status      |
+-------------------+--------+-------------+
| Completion        | XX%    | [Status]    |
| Test Coverage     | XX%    | [Status]    |
| Documentation     | XX%    | [Status]    |
| Technical Debt    | [L/M/H]| [Status]    |
| Architecture      | XX%    | [Status]    |
+-------------------+--------+-------------+

Top 3 Risks:
1. [Most critical finding]
2. [Second most critical]
3. [Third most critical]

Immediate Actions Required:
1. [Most urgent action]
2. [Second urgent action]
3. [Third urgent action]
```

### Detailed Findings

For each finding, use this format:

```
FINDING: [ID]
=============
Category: [Gap | Deviation | Debt | Risk | Architecture]
Severity: [CRITICAL | HIGH | MEDIUM | LOW | INFO]
Component: [Affected component/module]

ORIGINAL REQUIREMENT:
[Quote from planning doc]
Source: [file:line]

CURRENT STATE:
[What actually exists]
Location: [file paths]

EVIDENCE:
- [Specific evidence point 1]
- [Specific evidence point 2]
- [Specific evidence point 3]

IMPACT:
[Why this matters]

RECOMMENDATION:
Priority: [P0-P3]
Effort: [S/M/L/XL]
Steps:
1. [Specific action 1]
2. [Specific action 2]
3. [Specific action 3]

Dependencies: [What must happen first]
```

### Traceability Matrix

Provide a complete mapping:

```
REQUIREMENTS TRACEABILITY
=========================
+----------+------------------+----------+----------+-------+
| Req ID   | Description      | Status   | Coverage | Files |
+----------+------------------+----------+----------+-------+
| REQ-001  | User login       | COMPLETE | 85%      | 3     |
| REQ-002  | Password reset   | PARTIAL  | 40%      | 2     |
| REQ-003  | OAuth support    | NOT_STARTED | 0%    | 0     |
+----------+------------------+----------+----------+-------+
```

### Action Items

Prioritized list of recommended actions:

```
ACTION ITEMS
============

CRITICAL (Do Now):
[ ] [Action 1] - [Owner suggestion] - [Effort]
[ ] [Action 2] - [Owner suggestion] - [Effort]

HIGH (This Sprint):
[ ] [Action 3] - [Owner suggestion] - [Effort]
[ ] [Action 4] - [Owner suggestion] - [Effort]

MEDIUM (This Month):
[ ] [Action 5] - [Owner suggestion] - [Effort]
[ ] [Action 6] - [Owner suggestion] - [Effort]

LOW (Backlog):
[ ] [Action 7] - [Owner suggestion] - [Effort]
```

## Best Practices Applied

This auditor applies industry-standard best practices:

### Code Quality
- Clean Code principles (meaningful names, small functions, DRY)
- SOLID principles for OOP
- Consistent code style and formatting
- Appropriate error handling
- Logging and observability

### Testing
- Test pyramid (unit > integration > e2e)
- Minimum 80% code coverage for critical paths
- Tests for edge cases and error conditions
- Automated test execution in CI

### Documentation
- README with setup instructions
- API documentation for public interfaces
- Architecture decision records for major decisions
- Inline comments for complex logic only
- Changelog maintained

### Version Control
- Meaningful commit messages (conventional commits preferred)
- Feature branches with descriptive names
- Protected main branch
- Code review before merge
- Tagged releases

### Security
- No secrets in code
- Input validation
- Authentication/authorization where needed
- Dependency vulnerability scanning
- Security headers for web apps

### DevOps
- Automated CI/CD pipeline
- Environment configuration externalized
- Health checks and monitoring
- Graceful error handling
- Logging and tracing

## Handling Edge Cases

### No Planning Documents Found

If no planning documents exist:

```
1. Report this as a CRITICAL finding
2. Offer to create a baseline from current state:
   - Reverse-engineer requirements from code
   - Document current architecture
   - Create initial backlog from TODOs
3. Proceed with limited audit focusing on:
   - Technical debt
   - Code quality
   - Test coverage
   - Documentation gaps
```

### Conflicting Requirements

When requirements conflict:

```
1. Flag all conflicting requirements
2. List each version with source
3. Recommend resolution process
4. Do not assume which is correct
```

### Large Codebase

For repositories > 1000 files:

```
1. Focus on core modules first
2. Sample peripheral modules
3. Prioritize areas mentioned in requirements
4. Note sampling strategy in report
```

### Monorepo Projects

For monorepos:

```
1. Identify project boundaries
2. Audit each project separately if requested
3. Check cross-project dependencies
4. Report on shared infrastructure
```

## Continuous Improvement

After each audit, the skill improves by:

1. Noting which document patterns were found
2. Recording common technical debt patterns
3. Tracking which recommendations were most actionable
4. Refining severity criteria based on outcomes

## Resources

Detailed reference documentation is available in the `references/` directory:

- `references/best-practices.md` - Comprehensive best practices checklist
- `references/metrics-guide.md` - How to calculate and interpret metrics
- `references/remediation-patterns.md` - Common fixes for common problems
