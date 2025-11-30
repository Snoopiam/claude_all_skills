---
name: error-debugger
description: Systematic debugging approach for any error. Use when user encounters errors, bugs, or unexpected behavior in their code.
---

# Error Debugger

## CRITICAL: MANDATORY DEEP WORK PROTOCOL

**READ THIS BEFORE DEBUGGING ANYTHING.**

Superficial debugging is UNACCEPTABLE. Guessing at fixes is UNACCEPTABLE.

### BANNED BEHAVIORS

```
NEVER say or think these after debugging:
❌ "I should have traced the code path more carefully"
❌ "Upon closer inspection, the real issue is..."
❌ "Let me look deeper at the root cause"
❌ "I apologize - that fix didn't work because..."
❌ "I understand your frustration"
❌ "I made assumptions that were wrong"

If you find yourself about to say ANY of these, you FAILED.
Find the ROOT CAUSE FIRST. Not after your fix doesn't work.
```

### MINIMUM DEBUGGING REQUIREMENTS

Before proposing ANY fix:

1. **Reproduce the error yourself** - don't guess, VERIFY
2. **Trace the ENTIRE code path** - from entry to error
3. **Find the ROOT CAUSE** - not where it appears, where it STARTS
4. **Understand WHY it happens** - not just WHAT is wrong
5. **Verify the fix works** - don't propose, PROVE

### SELF-INTERROGATION (Do this before proposing a fix)

- [ ] Did I reproduce the exact error?
- [ ] Did I trace the complete code path?
- [ ] Did I find where the bug ORIGINATES (not just where it shows)?
- [ ] Do I understand WHY this bug happens?
- [ ] Did I check for this bug in OTHER places?
- [ ] Am I 100% confident my fix will work?
- [ ] Did I verify my fix doesn't break anything else?
- [ ] If this fix fails, will I have to say "let me look deeper"?

**If ANY answer is NO, you are not done. Keep investigating.**

### PROOF OF WORK REQUIRED

For EVERY bug fix, you MUST provide:
- Steps to reproduce (that you actually tried)
- The exact code path from input to error
- The ROOT CAUSE (file:line where bug originates)
- WHY the bug happens (technical explanation)
- The specific fix with before/after code
- How you verified the fix works
- Other places you checked for the same bug

### WHAT "DEEP DEBUGGING" ACTUALLY MEANS

```
SUPERFICIAL (WRONG):
- Look at the error line
- Guess at what might fix it
- Propose a change
- "Try this and see if it works"

DEEP (CORRECT):
- Reproduce the error exactly
- Trace from input to error
- Find where wrong value/state originates
- Understand the logic flaw
- Fix at the source, not the symptom
- Verify the fix works
- Check for related bugs
- "Here's the root cause at file:line, here's why, here's the fix, and I verified it works"
```

---

You are an expert debugger who systematically identifies and resolves code issues.

## When to Use This Skill

- User has an error message
- Code isn't working as expected
- User needs help understanding a bug
- Something "mysteriously" broke

## The DEBUG Process

### D - Define the Problem

Ask these questions:
```
1. What is the exact error message?
2. When does it occur? (build, runtime, specific action)
3. What was the last change before it broke?
4. Can you reproduce it consistently?
5. What is the expected vs actual behavior?
```

### E - Examine the Evidence

Collect information:
```
□ Full error message and stack trace
□ Relevant code snippet
□ Console output / logs
□ Network requests (if applicable)
□ Environment (Node version, browser, OS)
□ Recent changes (git diff)
```

### B - Break It Down

Isolate the problem:
```
1. Which file is the error in?
2. Which function/line?
3. What are the inputs at that point?
4. What should happen vs what does happen?
5. Is it a syntax, logic, or runtime error?
```

### U - Understand Root Cause

Common error categories:

| Category | Examples | Look For |
|----------|----------|----------|
| **Syntax** | Missing bracket, typo | Red squiggles, parse errors |
| **Type** | undefined is not a function | Type mismatches, null checks |
| **Logic** | Wrong output, infinite loop | Conditional logic, loops |
| **Async** | Race conditions, unhandled promises | await, .then(), timing |
| **Import** | Module not found | Paths, exports, node_modules |
| **State** | Stale data, wrong values | useState, props, context |
| **Network** | Failed requests, CORS | fetch, axios, API calls |
| **Environment** | Works locally, fails in prod | Env vars, build config |

### G - Generate Solutions

Fix approaches:
```
1. Direct fix (obvious solution)
2. Workaround (temporary, with TODO)
3. Refactor (if root cause is deeper)
4. Add guards (prevent future occurrence)
```

## Common Error Patterns & Fixes

### JavaScript / TypeScript

| Error | Likely Cause | Fix |
|-------|--------------|-----|
| `Cannot read property 'x' of undefined` | Accessing property on null/undefined | Add null check: `obj?.x` |
| `x is not a function` | Wrong type, not imported | Check import, check type |
| `Maximum call stack exceeded` | Infinite recursion | Check base case, useEffect deps |
| `Cannot find module` | Wrong path, not installed | Check path, npm install |
| `Unexpected token` | Syntax error, wrong file type | Check syntax, file extension |

### React Specific

| Error | Likely Cause | Fix |
|-------|--------------|-----|
| `Invalid hook call` | Hook outside component, wrong React version | Check hook rules, versions |
| `Too many re-renders` | setState in render, infinite loop | Check useEffect deps, conditions |
| `Each child should have unique key` | Missing/duplicate keys in list | Add unique key prop |
| `Cannot update unmounted component` | Async update after unmount | Cleanup in useEffect |
| `Objects are not valid as React child` | Rendering object directly | Stringify or access properties |

### Node.js / Backend

| Error | Likely Cause | Fix |
|-------|--------------|-----|
| `ECONNREFUSED` | Server not running, wrong port | Start server, check port |
| `ENOENT` | File/directory doesn't exist | Check path, create if needed |
| `CORS error` | Missing CORS headers | Add CORS middleware |
| `UnhandledPromiseRejection` | Missing catch | Add .catch() or try/catch |
| `EADDRINUSE` | Port already in use | Kill process, change port |

### Build Errors

| Error | Likely Cause | Fix |
|-------|--------------|-----|
| `Module parse failed` | Wrong loader, syntax error | Check webpack/vite config |
| `Cannot resolve` | Missing dependency, wrong path | npm install, fix import |
| `Type error` (TS) | Type mismatch | Fix types, add assertion |
| `Out of memory` | Too large bundle, memory leak | Increase memory, optimize |

## Debugging Commands

### JavaScript/Node
```bash
# Run with debugger
node --inspect script.js

# Check Node version
node -v

# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules && npm install
```

### React
```bash
# Check for issues
npm run lint

# Build to see errors
npm run build

# Check bundle size
npm run analyze
```

### Git (find when bug introduced)
```bash
# See recent changes
git log --oneline -10

# Find what changed in file
git log -p -- path/to/file.ts

# Binary search for bug
git bisect start
git bisect bad          # current commit is bad
git bisect good abc123  # known good commit
```

## Debugging Checklist

```
□ Read the FULL error message
□ Check the stack trace (first YOUR code, not library)
□ Google the exact error (in quotes)
□ Check recent changes (git diff)
□ Add console.logs at key points
□ Check inputs/outputs at each step
□ Try in isolation (minimal reproduction)
□ Check environment (versions, env vars)
□ Rubber duck it (explain out loud)
□ Take a break if stuck (fresh eyes help)
```

## Console Debugging Tips

```javascript
// Basic log
console.log('value:', value);

// With label and formatting
console.log('%c Important:', 'color: red; font-weight: bold', data);

// Table for arrays/objects
console.table(arrayOfObjects);

// Group related logs
console.group('API Call');
console.log('Request:', request);
console.log('Response:', response);
console.groupEnd();

// Trace call stack
console.trace('How did we get here?');

// Time operations
console.time('operation');
// ... code ...
console.timeEnd('operation');

// Assert (logs only if false)
console.assert(condition, 'Condition failed!');
```

## Process for Users

1. **Share** the exact error message
2. **Show** the relevant code
3. **Explain** what you expected vs what happened
4. **List** any recent changes
5. **Try** the suggested fix
6. **Confirm** if fixed or share new error

## When to Escalate

Move beyond basic debugging when:
```
- Error persists after obvious fixes
- Error only in production
- Intermittent/random failures
- Security-related issues
- Performance problems (not errors)
```

Then consider:
- Memory profiling
- Network analysis
- Production logs
- Database queries
- Third-party service status
