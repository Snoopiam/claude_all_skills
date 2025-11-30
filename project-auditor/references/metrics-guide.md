# Metrics Guide

How to calculate, interpret, and act on project health metrics.

## Core Metrics

### 1. Completion Rate

**What it measures:** Percentage of planned requirements that are fully implemented.

**Calculation:**
```
Completion Rate = (Completed Requirements / Total Requirements) x 100
```

**Status thresholds:**
| Score | Status | Interpretation |
|-------|--------|----------------|
| 90-100% | HEALTHY | On track for delivery |
| 70-89% | CAUTION | Minor gaps, monitor closely |
| 50-69% | AT RISK | Significant gaps, action needed |
| < 50% | CRITICAL | Major concerns, reassess scope |

**How to improve:**
- Prioritize completing partial implementations
- Descope non-essential requirements
- Add resources to critical path items
- Break large requirements into smaller deliverables

---

### 2. Test Coverage

**What it measures:** Percentage of code covered by automated tests.

**Calculation:**
```
Test Coverage = (Lines Covered by Tests / Total Lines) x 100
```

**Status thresholds:**
| Score | Status | Interpretation |
|-------|--------|----------------|
| 80-100% | HEALTHY | Well-tested codebase |
| 60-79% | CAUTION | Adequate but could improve |
| 40-59% | AT RISK | Significant testing gaps |
| < 40% | CRITICAL | High regression risk |

**Important nuances:**
- Coverage quantity != coverage quality
- Focus on critical path coverage first
- Integration tests matter as much as unit tests
- 100% coverage is not the goal; meaningful coverage is

**How to improve:**
- Start with untested critical paths
- Add tests when fixing bugs
- Require tests in code reviews
- Use TDD for new features
- Set coverage gates in CI

---

### 3. Documentation Score

**What it measures:** Completeness of project documentation.

**Calculation:**
```
Documentation Score = (Documented Items / Total Required Items) x 100

Required Items:
- README with setup instructions (10 points)
- API documentation (15 points)
- Architecture overview (15 points)
- Configuration guide (10 points)
- Contribution guide (10 points)
- Changelog (10 points)
- Public function/class docs (30 points)
```

**Status thresholds:**
| Score | Status | Interpretation |
|-------|--------|----------------|
| 80-100% | HEALTHY | Well-documented project |
| 60-79% | CAUTION | Usable but gaps exist |
| 40-59% | AT RISK | Onboarding will be difficult |
| < 40% | CRITICAL | Knowledge is tribal |

**How to improve:**
- Start with README essentials
- Document as you develop
- Use documentation generators
- Include documentation in Definition of Done
- Review docs in code reviews

---

### 4. Technical Debt Index

**What it measures:** Accumulated shortcuts and quality compromises.

**Calculation:**
```
Technical Debt Score = Weighted sum of debt indicators

Indicators (with weights):
- TODO/FIXME comments: 1 point each
- HACK/WORKAROUND comments: 2 points each
- Deprecated code still in use: 3 points each
- Known security vulnerabilities: 5 points each
- Outdated dependencies (major version behind): 2 points each
- Skipped tests: 2 points each
- High complexity functions (cyclomatic > 10): 2 points each
- Very long files (> 500 lines): 1 point each
- Duplicated code blocks: 1 point each
```

**Status thresholds:**
| Score | Status | Interpretation |
|-------|--------|----------------|
| 0-20 | LOW | Well-maintained codebase |
| 21-50 | MEDIUM | Normal debt, plan to address |
| 51-100 | HIGH | Debt impacting velocity |
| > 100 | CRITICAL | Debt causing failures |

**How to improve:**
- Dedicate 20% of sprint to debt reduction
- Address debt when touching related code
- Track debt in backlog with visibility
- Set thresholds and enforce in CI
- Celebrate debt paydown

---

### 5. Architecture Compliance

**What it measures:** How well implementation follows planned architecture.

**Calculation:**
```
Architecture Compliance = (Compliant Decisions / Total Architectural Decisions) x 100

Check each decision:
- Module boundaries respected?
- Dependency directions correct?
- Patterns implemented correctly?
- Data models match design?
- APIs match contracts?
```

**Status thresholds:**
| Score | Status | Interpretation |
|-------|--------|----------------|
| 90-100% | HEALTHY | Architecture is maintained |
| 70-89% | CAUTION | Some drift, course correct |
| 50-69% | AT RISK | Significant deviations |
| < 50% | CRITICAL | Architecture abandoned |

**How to improve:**
- Update ADRs when decisions change
- Review architecture in code reviews
- Use automated architecture tests
- Regular architecture review sessions
- Make architecture visible (diagrams)

---

## Composite Metrics

### Overall Health Score

**Calculation:**
```
Health Score = (
    Completion Rate x 0.25 +
    Test Coverage x 0.20 +
    Documentation Score x 0.15 +
    (100 - Technical Debt Index) x 0.20 +
    Architecture Compliance x 0.20
)
```

**Interpretation:**
| Score | Rating | Description |
|-------|--------|-------------|
| 90-100 | EXCELLENT | Project is in great shape |
| 75-89 | GOOD | Healthy with minor concerns |
| 60-74 | FAIR | Needs attention in some areas |
| 40-59 | POOR | Significant problems exist |
| < 40 | CRITICAL | Urgent intervention needed |

---

### Velocity Trend

**What it measures:** How project progress is trending over time.

**Calculation:**
```
Track completed items per time period (sprint/week/month)
Calculate moving average
Compare current to average

Trend = (Current Period / Average) - 1
```

**Interpretation:**
| Trend | Status | Action |
|-------|--------|--------|
| > +20% | Accelerating | Maintain, but watch for burnout |
| +5% to +20% | Improving | Good trajectory, sustain |
| -5% to +5% | Stable | Normal, no action needed |
| -20% to -5% | Slowing | Investigate blockers |
| < -20% | Stalling | Urgent: identify and remove blockers |

---

### Risk Score

**What it measures:** Aggregate project risk level.

**Calculation:**
```
Risk Score = Sum of (Finding Severity x Finding Count)

Severity weights:
- CRITICAL: 10 points
- HIGH: 5 points
- MEDIUM: 2 points
- LOW: 1 point
- INFO: 0 points
```

**Interpretation:**
| Score | Risk Level | Recommended Action |
|-------|------------|-------------------|
| 0-10 | LOW | Monitor normally |
| 11-30 | MODERATE | Address high items |
| 31-50 | ELEVATED | Sprint focus on risk |
| 51-100 | HIGH | Dedicated risk sprint |
| > 100 | SEVERE | Stop feature work, fix issues |

---

## Metric Collection Methods

### Automated Collection

**For Test Coverage:**
```bash
# JavaScript/TypeScript (Jest)
jest --coverage

# Python (pytest-cov)
pytest --cov=src --cov-report=html

# Go
go test -cover ./...

# Java (JaCoCo)
mvn jacoco:report
```

**For Technical Debt:**
```bash
# Count TODO/FIXME
grep -rn "TODO\|FIXME\|HACK\|XXX" src/

# Check outdated dependencies
npm outdated        # Node
pip list --outdated # Python
cargo outdated      # Rust

# Security vulnerabilities
npm audit           # Node
safety check        # Python
cargo audit         # Rust
```

**For Code Complexity:**
```bash
# JavaScript (complexity-report)
cr src/

# Python (radon)
radon cc src/ -a

# General (SonarQube)
sonar-scanner
```

### Manual Collection

For metrics requiring human judgment:

1. **Documentation Score**
   - Review README sections
   - Check API docs completeness
   - Verify architecture docs accuracy

2. **Architecture Compliance**
   - Compare code to design docs
   - Review dependency graphs
   - Check pattern implementation

3. **Requirements Traceability**
   - Map each requirement to code
   - Verify implementation matches spec
   - Check for undocumented features

---

## Metric Reporting

### Trend Charts

Track metrics over time to identify patterns:

```
Health Score Trend
100|
 90|----*----*
 80|         *----*
 70|              *----*
 60|
   +----+----+----+----+
   W1   W2   W3   W4   W5
```

### Heat Maps

Show risk concentration:

```
Module Risk Heat Map
+------------+--------+--------+--------+
|            | Low    | Medium | High   |
+------------+--------+--------+--------+
| auth/      |        |        |   X    |
| api/       |        |   X    |        |
| utils/     |   X    |        |        |
| models/    |        |   X    |        |
+------------+--------+--------+--------+
```

### Comparison Tables

Track progress between audits:

```
Metric Comparison: Audit 1 vs Audit 2
+-------------------+--------+--------+--------+
| Metric            | Before | After  | Change |
+-------------------+--------+--------+--------+
| Completion        | 65%    | 78%    | +13%   |
| Test Coverage     | 45%    | 62%    | +17%   |
| Documentation     | 30%    | 55%    | +25%   |
| Tech Debt         | 85     | 52     | -33    |
+-------------------+--------+--------+--------+
```

---

## Setting Targets

### Recommended Minimums

| Metric | Minimum | Target | Stretch |
|--------|---------|--------|---------|
| Completion | 80% | 90% | 95% |
| Test Coverage | 60% | 80% | 90% |
| Documentation | 50% | 75% | 90% |
| Tech Debt Index | < 75 | < 40 | < 20 |
| Architecture | 70% | 85% | 95% |
| Health Score | 60 | 75 | 85 |

### Improvement Cadence

Realistic improvement rates per sprint:

| Metric | Achievable Improvement |
|--------|----------------------|
| Completion | +5-10% per sprint |
| Test Coverage | +10-15% initially, slows to +5% |
| Documentation | +10-20% with focused effort |
| Tech Debt | -10-20 points per sprint |
| Architecture | +5-10% when actively addressed |
