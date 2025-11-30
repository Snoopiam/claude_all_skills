# CSS/UI-UX Audit Checklist

## Critical Issues

### Accessibility
- [ ] Color contrast ratio ≥4.5:1 for normal text, ≥3:1 for large text
- [ ] Focus indicators visible on all interactive elements
- [ ] No `outline: none` without alternative focus styling
- [ ] Touch targets minimum 44x44px on mobile
- [ ] No seizure-inducing animations (>3 flashes/second)
- [ ] `prefers-reduced-motion` respected for animations

### Layout Breaking
- [ ] No horizontal overflow causing scroll
- [ ] Z-index values managed (no arbitrary large numbers like 9999)
- [ ] Flexbox/Grid items don't overflow containers
- [ ] Position: fixed/absolute elements don't overlap critical content
- [ ] No negative margins breaking layout flow

### Mobile Responsiveness
- [ ] Viewport meta tag present: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Media queries cover: 320px, 768px, 1024px, 1280px breakpoints
- [ ] No fixed widths breaking small screens
- [ ] Font sizes readable on mobile (≥16px body text)
- [ ] Tap targets adequately spaced

## Major Issues

### Design Tokens & Variables
- [ ] Colors defined as CSS variables
- [ ] Spacing uses consistent scale (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px)
- [ ] Typography scale defined (font-size, line-height, font-weight)
- [ ] Border-radius consistent
- [ ] Shadows use variables
- [ ] No magic numbers (unexplained arbitrary values)

### Selector Quality
- [ ] No IDs for styling (use classes)
- [ ] Selector specificity ≤3 levels
- [ ] No `!important` except for utility overrides
- [ ] No element selectors for component styling (avoid `div`, `span`)
- [ ] BEM or consistent naming convention used

### Interactive States
- [ ] `:hover` states for clickable elements
- [ ] `:active` states for buttons
- [ ] `:focus` and `:focus-visible` states
- [ ] `:disabled` styles for form elements
- [ ] Loading/skeleton states for async content
- [ ] Error states for form validation

### Code Organization
- [ ] Logical property ordering (positioning → display → box model → typography → visual)
- [ ] No duplicate selectors
- [ ] Related styles grouped
- [ ] Comments for non-obvious code
- [ ] No inline styles in HTML (except dynamic values)

## Minor Issues

### Performance
- [ ] No overly complex selectors (avoid descendant selectors 4+ deep)
- [ ] Animations use `transform` and `opacity` (GPU-accelerated)
- [ ] Large background images optimized
- [ ] No unused CSS (check with PurgeCSS or similar)
- [ ] `will-change` used sparingly

### Browser Compatibility
- [ ] Vendor prefixes present (or autoprefixer configured)
- [ ] CSS Grid fallbacks for older browsers (if supporting IE11)
- [ ] Custom properties fallbacks (if supporting older browsers)
- [ ] Modern features have `@supports` checks

### Code Quality
- [ ] No empty rule sets
- [ ] No commented-out code blocks
- [ ] Consistent formatting (indentation, spacing)
- [ ] File size reasonable (<50KB per file)
- [ ] No redundant properties (e.g., setting both `margin` and `margin-top`)

## UI/UX Patterns

### Visual Hierarchy
- [ ] Clear heading hierarchy (h1 > h2 > h3)
- [ ] Primary actions visually prominent
- [ ] Consistent visual weight across similar elements
- [ ] Adequate whitespace (not cramped)
- [ ] Logical reading order (F-pattern or Z-pattern)

### Feedback & Affordance
- [ ] Buttons look clickable (proper affordance)
- [ ] Links distinguishable from body text
- [ ] Form fields have clear boundaries
- [ ] Error messages visually distinct (color + icon)
- [ ] Success states confirmed visually

### Consistency
- [ ] Same component styled identically across pages
- [ ] Consistent spacing rhythm
- [ ] Unified color palette (max 5-7 colors + neutrals)
- [ ] Typography limited to 2-3 font families
- [ ] Icon style consistent (filled vs outlined)

## Common Anti-Patterns to Fix

```css
/* ❌ Magic numbers */
margin-top: 37px;
/* ✅ Use variables or explain */
margin-top: var(--spacing-lg); /* 32px + 5px visual adjustment for icon */

/* ❌ Overly specific selector */
body div.container > section.main article.post p.intro span.highlight { }
/* ✅ Simple class */
.post-highlight { }

/* ❌ Important abuse */
.button { color: red !important; }
/* ✅ Fix specificity issue at source */
.button { color: var(--btn-color); }

/* ❌ Hardcoded colors */
.card { background: #f5f5f5; border: 1px solid #e0e0e0; }
/* ✅ Semantic variables */
.card { background: var(--surface-secondary); border: 1px solid var(--border-default); }

/* ❌ Missing states */
.link { color: blue; }
/* ✅ Complete state coverage */
.link { 
  color: var(--link-color);
  text-decoration: underline;
  text-underline-offset: 2px;
}
.link:hover { color: var(--link-color-hover); }
.link:visited { color: var(--link-color-visited); }
.link:focus { outline: 2px solid var(--focus-ring); outline-offset: 2px; }
```

## Recommended CSS Variable Structure

```css
:root {
  /* Colors */
  --color-primary: #0066cc;
  --color-primary-hover: #0052a3;
  --color-secondary: #6c757d;
  --color-success: #28a745;
  --color-warning: #ffc107;
  --color-error: #dc3545;
  
  /* Neutrals */
  --color-text: #1a1a1a;
  --color-text-muted: #6b6b6b;
  --color-background: #ffffff;
  --color-surface: #f8f9fa;
  --color-border: #dee2e6;
  
  /* Spacing (4px base) */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  
  /* Typography */
  --font-family-base: system-ui, -apple-system, sans-serif;
  --font-family-mono: 'SF Mono', Consolas, monospace;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --line-height-tight: 1.25;
  --line-height-base: 1.5;
  --line-height-loose: 1.75;
  
  /* Borders */
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 12px;
  --border-radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
  
  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease;
  
  /* Focus */
  --focus-ring: var(--color-primary);
  --focus-ring-offset: 2px;
}
```
