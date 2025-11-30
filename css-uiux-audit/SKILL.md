---
name: css-uiux-audit
description: Comprehensive CSS and UI/UX code review, issue identification, and automated fixing with documentation. Use when reviewing stylesheets, analyzing UI/UX patterns, auditing frontend code quality, fixing CSS issues, or documenting style improvements. Triggers on requests like "review my CSS", "audit UI/UX", "fix styling issues", "improve my styles", or "document CSS fixes".
---

# CSS & UI/UX Audit Skill

## CRITICAL: MANDATORY DEEP WORK PROTOCOL

**READ THIS BEFORE AUDITING ANYTHING.**

Superficial CSS audits are UNACCEPTABLE. Running automated tools and calling it done is UNACCEPTABLE.

### BANNED BEHAVIORS

```
NEVER say or think these after an audit:
❌ "I ran automated checks and made incremental CSS/HTML fixes"
❌ "I didn't do a proper deep-dive audit"
❌ "Upon closer inspection, there are more issues..."
❌ "I should have checked the application logic"
❌ "I apologize for the superficial review"
❌ "I understand your frustration"
❌ "Let me do a proper audit now"

If you find yourself about to say ANY of these, you FAILED.
Do the deep audit FIRST. Not after being questioned.
```

### MINIMUM AUDIT REQUIREMENTS

Before claiming an audit is complete:

1. **Read EVERY CSS file** - not samples, EVERY file
2. **Test the ACTUAL UI** - don't just read code, verify it works
3. **Check APPLICATION LOGIC** - CSS affects behavior, not just appearance
4. **Verify at ALL breakpoints** - mobile, tablet, desktop
5. **Test interactions** - hover, focus, active, disabled states

### SELF-INTERROGATION (Do this before submitting)

- [ ] Did I read EVERY CSS file, not just run a scanner?
- [ ] Did I understand what each style rule actually DOES?
- [ ] Did I check how CSS affects JavaScript behavior?
- [ ] Did I test the UI at mobile sizes (320px)?
- [ ] Did I verify all interactive states work?
- [ ] Did I find issues that automated tools CANNOT find?
- [ ] Did I check for logic issues, not just syntax?
- [ ] If the user double-checks my audit, will they find things I missed?

**If ANY answer is NO, you are not done. Keep working.**

### PROOF OF WORK REQUIRED

For EVERY audit finding, you MUST provide:
- Exact file path and line number
- The actual CSS code (quoted)
- What the visual/behavioral problem is
- How you verified this is actually an issue
- The specific fix (not just "improve this")
- How the fix resolves the problem

### WHAT "DEEP AUDIT" ACTUALLY MEANS

```
SUPERFICIAL (WRONG):
- Run a linter
- Report syntax errors
- Suggest generic improvements
- "Your CSS looks mostly fine with a few issues"

DEEP (CORRECT):
- Read every file line by line
- Understand the component architecture
- Test the actual rendered output
- Verify at multiple breakpoints
- Check how CSS interacts with JS
- Find logic bugs, not just style issues
- Provide file:line references for everything
- Explain WHY each issue matters
```

---

Systematic review, fix, and documentation workflow for CSS files and UI/UX patterns.

## Workflow

### Phase 1: Discovery

1. Scan project for CSS/style files:
   ```bash
   find . -type f \( -name "*.css" -o -name "*.scss" -o -name "*.sass" -o -name "*.less" -o -name "*.styled.ts" -o -name "*.styled.js" -o -name "*.module.css" \) 2>/dev/null | head -50
   ```

2. Identify framework (Tailwind, Bootstrap, MUI, styled-components, CSS Modules, vanilla CSS)

3. Run analysis script on each file:
   ```bash
   python scripts/css_analyzer.py <file_path>
   ```

### Phase 2: Analysis

Review each file against these categories. See [references/audit-checklist.md](references/audit-checklist.md) for detailed criteria.

**Critical Issues** (must fix):
- Accessibility violations (contrast, focus states)
- Layout breaking bugs (overflow, z-index conflicts)
- Mobile responsiveness failures
- Specificity wars (!important abuse)

**Major Issues** (should fix):
- Inconsistent spacing/sizing (no design tokens)
- Duplicate/redundant rules
- Missing hover/active/focus states
- Poor naming conventions
- Hardcoded values instead of variables

**Minor Issues** (consider fixing):
- Suboptimal selectors
- Missing vendor prefixes (if no autoprefixer)
- Commented-out code
- Empty rules or unused styles

### Phase 3: Fixes

For each identified issue:

1. **Document the issue** in the audit report (see Phase 4)
2. **Apply the fix** directly to the file
3. **Validate** the fix doesn't break other styles

**Fix Priority Order:**
1. Critical → 2. Major → 3. Minor

**Fix Patterns:**

```css
/* BEFORE: Hardcoded values */
.card { margin: 16px; padding: 24px; }

/* AFTER: CSS variables */
.card { margin: var(--spacing-md); padding: var(--spacing-lg); }
```

```css
/* BEFORE: Specificity issue */
div.container .wrapper .card .title { color: red; }

/* AFTER: Clean selector */
.card-title { color: var(--color-primary); }
```

```css
/* BEFORE: Missing states */
.button { background: blue; }

/* AFTER: Complete interaction states */
.button { 
  background: var(--btn-bg);
  transition: background 0.2s ease;
}
.button:hover { background: var(--btn-bg-hover); }
.button:focus { outline: 2px solid var(--focus-ring); outline-offset: 2px; }
.button:active { background: var(--btn-bg-active); }
.button:disabled { opacity: 0.5; cursor: not-allowed; }
```

### Phase 4: Documentation

Generate `CSS_AUDIT_REPORT.md` in project root:

```markdown
# CSS/UI-UX Audit Report
Generated: [timestamp]

## Summary
- Files analyzed: X
- Critical issues: X (fixed: X)
- Major issues: X (fixed: X)  
- Minor issues: X (fixed: X)

## Files Reviewed

### [filename.css]
**Issues Found:**
| # | Severity | Issue | Line | Fix Applied |
|---|----------|-------|------|-------------|
| 1 | Critical | Missing focus state on buttons | 42 | Added :focus with outline |
| 2 | Major | Hardcoded color #333 | 15 | Replaced with var(--text-primary) |

**Before/After:**
[code snippets showing changes]

## Design System Recommendations
- [List of suggested CSS variables]
- [Spacing scale recommendation]
- [Color palette standardization]

## Next Steps
- [ ] Outstanding issues requiring manual review
- [ ] Suggested refactors beyond scope
```

## Quick Commands

**Full audit with fixes:**
```bash
python scripts/css_analyzer.py --dir . --fix --report
```

**Analyze single file:**
```bash
python scripts/css_analyzer.py path/to/file.css
```

**Generate report only (no fixes):**
```bash
python scripts/css_analyzer.py --dir . --report-only
```

## Framework-Specific Notes

**Tailwind CSS**: Check for conflicting utility classes, custom CSS overriding utilities, missing dark mode variants

**CSS Modules**: Verify proper scoping, check for global leaks via :global

**Styled Components**: Look for missing theme usage, inline style objects, prop interpolation issues

**SCSS/Sass**: Check nesting depth (<4 levels), mixin usage, variable organization
