---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

---

## Frontend Aesthetics Guidelines

### Typography
Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial, Inter, Roboto, and system fonts. Opt instead for distinctive choices that elevate the frontend's aesthetics with unexpected, characterful font choices. Pair a distinctive display font with a refined body font.

**Font Pairing Examples** (vary these, never repeat across projects):
- Display + Body: Syne + Outfit, Clash Display + Satoshi, Space Grotesk + DM Sans
- Mono accents: IBM Plex Mono, JetBrains Mono, Fira Code
- Editorial: Playfair Display + Source Serif, Fraunces + Work Sans
- Geometric: Archivo + Inter (only if paired distinctively), Unbounded + Manrope

### Color & Theme
Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.

**Color System Requirements**:
```css
:root {
  /* Define a complete system, not ad-hoc colors */
  --color-bg-primary: ...;
  --color-bg-secondary: ...;
  --color-bg-elevated: ...;
  --color-text-primary: ...;
  --color-text-secondary: ...;
  --color-text-muted: ...;
  --color-accent-primary: ...;
  --color-accent-secondary: ...;
  --color-border: ...;
  --color-border-hover: ...;
}
```

### Motion & Animation
Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.

**Animation Best Practices**:
- Define timing variables: `--transition-fast: 150ms`, `--transition-smooth: 300ms`
- Use `cubic-bezier` for natural easing, not just `ease` or `linear`
- Stagger animations with `animation-delay` for orchestrated reveals
- Always provide `prefers-reduced-motion` alternatives

### Spatial Composition
Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.

### Backgrounds & Visual Details
Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

---

## Responsive Design (REQUIRED)

Design mobile-first, then enhance for larger screens. Every interface must work across all device sizes.

### Breakpoint Strategy
```css
/* Mobile-first approach */
/* Base styles for mobile (320px+) */

@media (min-width: 640px) { /* sm: Tablet portrait */ }
@media (min-width: 768px) { /* md: Tablet landscape */ }
@media (min-width: 1024px) { /* lg: Desktop */ }
@media (min-width: 1280px) { /* xl: Large desktop */ }
@media (min-width: 1536px) { /* 2xl: Extra large */ }
```

### Responsive Requirements
- **Typography**: Use fluid scaling with `clamp()` for headings
  ```css
  font-size: clamp(1.5rem, 4vw, 3rem);
  ```
- **Touch Targets**: Minimum 44x44px for all interactive elements on mobile
- **Grid Collapse**: Multi-column layouts must stack on mobile
- **Spacing**: Reduce padding/margins proportionally on smaller screens
- **Images**: Use responsive images with srcset or CSS object-fit
- **Navigation**: Provide mobile-friendly navigation (hamburger, bottom nav, etc.)

### Testing Checklist
- [ ] 320px (small mobile)
- [ ] 375px (iPhone SE/standard)
- [ ] 768px (tablet)
- [ ] 1024px (small desktop)
- [ ] 1440px (standard desktop)
- [ ] 1920px+ (large monitors)

---

## Accessibility (A11y) Standards (REQUIRED)

Accessibility is not optional. All interfaces must meet WCAG 2.1 AA standards minimum.

### Focus States
- All interactive elements MUST have visible focus states
- Focus indicators should use the accent color with sufficient contrast
- Never use `outline: none` without a visible alternative
```css
:focus-visible {
  outline: 2px solid var(--color-accent-primary);
  outline-offset: 2px;
}
```

### Semantic HTML
- Use proper heading hierarchy (h1 → h2 → h3, no skipping)
- Use semantic elements: `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`
- **ALWAYS wrap page content in `<main>`** - this is required for screen readers
- Use `<button>` for actions, `<a>` for navigation
- Form inputs must have associated `<label>` elements

```tsx
// ✅ CORRECT - Semantic page structure
<div className="min-h-screen">
  <header>...</header>
  <main className="container mx-auto">
    {/* Page content here */}
  </main>
  <footer>...</footer>
</div>
```

### ARIA Requirements
- Icon-only buttons MUST have `aria-label`
```tsx
<button aria-label="Copy to clipboard">
  <CopyIcon />
</button>
```
- Dynamic content updates need `role="status"` or `aria-live`
- Modal dialogs need proper `role="dialog"` and focus trapping
- Loading states need `aria-busy="true"`

### Toast/Notification Pattern
Toasts and notifications MUST be accessible:
```tsx
// ✅ CORRECT - Accessible toast component
<div
  role="status"
  aria-live="polite"
  aria-atomic="true"
  className={`fixed bottom-8 ... ${visible ? 'opacity-100' : 'opacity-0'}`}
>
  <span className="sr-only">Notification:</span>
  {message}
</div>
```

Key requirements:
- `role="status"` announces to screen readers without interrupting
- `aria-live="polite"` waits for user to finish current task
- `aria-atomic="true"` reads the entire content, not just changes
- Include visually hidden context with `.sr-only` if needed

### Color Contrast
- Text contrast ratio: 4.5:1 minimum (AA standard)
- Large text (18px+ bold or 24px+ regular): 3:1 minimum
- UI components and graphical objects: 3:1 minimum
- Use tools: WebAIM Contrast Checker, Stark plugin

### Reduced Motion
Always provide alternatives for users who prefer reduced motion:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Keyboard Navigation
- All functionality must be accessible via keyboard
- Tab order must be logical (follows visual order)
- Provide skip links for main content
- Escape key should close modals/dropdowns

---

## Performance Optimization

### CSS Performance
- Avoid fixed-position overlays that render off-screen constantly
- Use CSS `contain` property for complex animated elements
```css
.complex-animation {
  contain: layout style paint;
}
```
- Prefer CSS animations over JavaScript animations
- Use `will-change` sparingly and only when needed

### Rendering Optimization
- Lazy-load heavy visual effects and below-fold content
- Use `loading="lazy"` for images
- Avoid layout thrashing (batch DOM reads/writes)
- Use CSS transforms instead of top/left for animations

### Bundle Considerations
- Prefer system fonts or subset custom fonts
- Use modern image formats (WebP, AVIF) with fallbacks
- Minimize third-party dependencies for visual effects

---

## Code Quality Standards

### CSS/Tailwind Syntax
NEVER use broken arbitrary value syntax. These patterns are INVALID:
```tsx
// ❌ WRONG - Cannot append opacity to CSS variable in Tailwind
className="border-[var(--accent)]30"
className="bg-[var(--color)]20"

// ❌ WRONG - Cannot append opacity in template literals either
style={{ background: `${config.color}20` }}  // "20" is just appended as text!
style={{ border: `1px solid ${color}30` }}   // Invalid color value

// ✅ CORRECT - Use rgba() with explicit values
className="border-[rgba(0,245,212,0.3)]"
className="border-accent/30"  // Tailwind opacity modifier (if configured)

// ✅ CORRECT - Use CSS color-mix() for dynamic opacity
style={{ background: `color-mix(in srgb, ${config.color} 20%, transparent)` }}

// ✅ CORRECT - Define opacity variants in CSS
.bg-accent-20 { background: rgba(var(--accent-rgb), 0.2); }

// ✅ CORRECT - Use hex with alpha channel
style={{ background: `${config.color}33` }} // Only works if color is hex AND you add valid alpha (33 = 20%)
// But prefer color-mix() for clarity
```

### Opacity Utility Classes
When using dynamic colors with opacity, define utility classes in CSS:
```css
/* Define RGB versions of your colors for rgba() usage */
:root {
  --accent-primary: #00f5d4;
  --accent-primary-rgb: 0, 245, 212;
  --accent-secondary: #7b61ff;
  --accent-secondary-rgb: 123, 97, 255;
}

/* Create opacity utility classes */
.bg-accent-primary-10 { background: rgba(var(--accent-primary-rgb), 0.1); }
.bg-accent-primary-20 { background: rgba(var(--accent-primary-rgb), 0.2); }
.border-accent-primary-30 { border-color: rgba(var(--accent-primary-rgb), 0.3); }
```

### Design Tokens
Define all design values as CSS variables or Tailwind config:
```css
:root {
  /* Colors */
  --color-*: ...;

  /* Spacing */
  --space-unit: 8px;
  --space-xs: calc(var(--space-unit) * 0.5);
  --space-sm: var(--space-unit);
  --space-md: calc(var(--space-unit) * 2);
  --space-lg: calc(var(--space-unit) * 3);
  --space-xl: calc(var(--space-unit) * 4);

  /* Typography */
  --font-display: 'Syne', sans-serif;
  --font-body: 'Outfit', sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;

  /* Transitions */
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-smooth: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-spring: 500ms cubic-bezier(0.34, 1.56, 0.64, 1);

  /* Shadows */
  --shadow-sm: ...;
  --shadow-md: ...;
  --shadow-lg: ...;

  /* Border radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-xl: 24px;
}
```

### Component Architecture
- Keep components focused on single responsibilities
- Extract reusable UI primitives (Button, Input, Card, etc.)
- Use TypeScript with proper prop types
- Document complex components with comments

---

## Edge Cases & States

Every interface must handle these states gracefully:

### Loading States
```tsx
// Skeleton loaders, spinners, or progressive loading
<div aria-busy="true" aria-label="Loading content">
  <Skeleton />
</div>
```

### Empty States
Design meaningful empty states with:
- Clear illustration or icon
- Helpful message explaining why it's empty
- Call-to-action to resolve (if applicable)

### Error States
- Clear error messages in plain language
- Visual indication (color, icon) without relying solely on color
- Recovery action when possible

### Content Extremes
Test with:
- Very long text (truncation, wrapping)
- Very short text (minimum widths)
- Missing optional content (graceful fallbacks)
- Large data sets (pagination, virtualization)

---

## Anti-Patterns to Avoid

### BANNED: Generic AI Aesthetics

This is **CRITICAL**. The following are explicitly forbidden because they scream "AI generated":

#### BANNED COLORS (Never use as primary/accent):
```
PURPLE/VIOLET FAMILY (The #1 AI cliché):
- #8B5CF6, #7C3AED, #6D28D9 (Violet/Purple - massively overused)
- #A855F7, #9333EA, #7E22CE (Purple variants)
- #C084FC, #A78BFA, #818CF8 (Light purples/lavenders)

BLUE-PURPLE GRADIENTS (The signature AI look):
- Any gradient from blue (#3B82F6) to purple (#8B5CF6)
- Any gradient from cyan (#06B6D4) to purple
- Any "aurora" or "cosmic" gradient

NEON/ELECTRIC COMBINATIONS:
- #00F5D4 (Mint/Cyan) + #7B61FF (Purple) - overused combo
- #FF006E (Hot pink) + #3A86FF (Blue)
- Any "synthwave" palette

SAFE BUT BORING:
- Pure #3B82F6 blue as primary (Tailwind blue-500)
- Pure #10B981 green as primary (Tailwind emerald-500)
- #6366F1 indigo (Tailwind indigo-500)
```

#### BANNED FONTS (Never use):
```
OVERUSED BY AI:
- Inter (the #1 AI default - NEVER use)
- Roboto (Google's generic choice)
- Open Sans (too safe, too common)
- Poppins (trendy but now AI cliché)
- Montserrat (overused in every AI design)
- Lato (generic and forgettable)
- Source Sans Pro (Adobe's boring default)
- Nunito (AI loves this too much)

SYSTEM FONTS AS PRIMARY:
- Arial, Helvetica (only as fallback, never primary)
- -apple-system, BlinkMacSystemFont (fallback only)
```

#### BANNED EFFECTS & STYLES:
```
GRADIENTS:
- Purple-to-blue gradients (THE AI signature)
- Rainbow/spectrum gradients
- "Glassmorphism" with purple/blue tints
- Gradient text on everything

SHADOWS:
- Colored shadows matching the element (purple shadow on purple button)
- Excessive blur shadows (blur-3xl everywhere)
- "Glow" effects on everything

PATTERNS:
- Grid dot patterns (every AI uses these)
- Blob/organic shapes as backgrounds (the "blobby" look)
- Floating geometric shapes (circles, triangles)
- "Mesh gradient" backgrounds

ANIMATIONS:
- Elements floating up and down endlessly
- Pulsing/breathing animations on everything
- Gradient animations cycling through colors
- Particles floating in background

LAYOUTS:
- Centered hero with gradient heading
- 3-column feature grid with icons
- Purple CTA buttons
- Cards with purple/blue gradient borders
```

#### BANNED COMPONENT PATTERNS:
```
- Cards with gradient borders
- Buttons with gradient backgrounds
- "Glassmorphism" cards with blur backdrop
- Icons in gradient circles
- Testimonials with star ratings in purple
- Pricing tables with "popular" badge in purple
- Feature lists with checkmark icons in circles
- Hero sections with floating 3D elements
```

### INSTEAD USE: Distinctive Alternatives

#### COLORS - Use Unexpected Palettes:
```css
/* Earthy & Warm */
--terracotta: #C2703E;
--ochre: #CC7722;
--rust: #A54A2A;
--sage: #9CAF88;

/* Deep & Moody */
--midnight-green: #004953;
--prussian-blue: #003153;
--wine: #722F37;
--charcoal: #36454F;

/* Bright & Bold (but not AI-cliché) */
--vermillion: #E34234;
--chartreuse: #DFFF00;
--electric-lime: #CCFF00;
--coral: #FF6F61;

/* Sophisticated Neutrals */
--warm-gray: #9B9B8F;
--greige: #B2AA9E;
--taupe: #8B8378;
--graphite: #383838;

/* Unexpected Combinations */
--forest + --peach
--navy + --mustard
--burgundy + --cream
--teal + --terracotta
```

#### FONTS - Use Distinctive Choices:
```css
/* Display/Headlines */
--font-display: 'Syne', 'Clash Display', 'Space Grotesk', 'Outfit';
--font-editorial: 'Fraunces', 'Libre Baskerville', 'Playfair Display';
--font-geometric: 'Archivo', 'DM Sans', 'Satoshi', 'Cabinet Grotesk';
--font-expressive: 'Unbounded', 'Righteous', 'Chillax';

/* Body */
--font-body: 'Outfit', 'Satoshi', 'General Sans', 'Switzer';
--font-readable: 'Source Serif 4', 'Literata', 'Charter';

/* Mono */
--font-mono: 'IBM Plex Mono', 'JetBrains Mono', 'Fira Code';
```

#### EFFECTS - Use With Purpose:
```css
/* Shadows - Subtle and Natural */
--shadow-natural: 0 4px 20px rgba(0, 0, 0, 0.08);
--shadow-elevated: 0 10px 40px rgba(0, 0, 0, 0.12);
/* NOT colored glows, NOT excessive blur */

/* Borders - Visible and Intentional */
border: 1px solid var(--color-border);
/* NOT gradient borders, NOT glowing borders */

/* Backgrounds - Texture Over Gradients */
background: var(--bg-primary);
background-image: url('/noise.png'); /* subtle grain */
/* NOT mesh gradients, NOT floating blobs */
```

NEVER use generic AI-generated aesthetics:
- ❌ Overused fonts: Inter, Roboto, Arial, system fonts (as primary)
- ❌ Clichéd color schemes: purple gradients on white, blue-purple tech gradients
- ❌ Predictable layouts: centered hero + 3-column features + footer
- ❌ Cookie-cutter components without context-specific character
- ❌ Generic placeholder content ("Lorem ipsum", "John Doe")

NEVER ship broken code:
- ❌ Invalid CSS/Tailwind syntax
- ❌ Missing responsive breakpoints
- ❌ Inaccessible interactive elements
- ❌ Hardcoded values that should be variables
- ❌ Uncommented complex logic

---

## Quality Checklist

Before considering the design complete, verify:

### Visual
- [ ] Typography hierarchy is clear and distinctive
- [ ] Color palette is cohesive with proper contrast
- [ ] Spacing is consistent and rhythmic
- [ ] Animations are smooth and purposeful
- [ ] Design has a memorable, distinctive quality

### Technical
- [ ] All CSS/Tailwind syntax is valid
- [ ] CSS variables are used for all design tokens
- [ ] No hardcoded magic numbers
- [ ] Components are properly typed (TypeScript)

### Responsive
- [ ] Works on mobile (320px)
- [ ] Works on tablet (768px)
- [ ] Works on desktop (1024px+)
- [ ] Touch targets are 44px+ on mobile

### Accessibility
- [ ] Focus states are visible
- [ ] Color contrast meets AA standards
- [ ] Icon buttons have aria-labels
- [ ] Keyboard navigation works
- [ ] Reduced motion is respected

### Edge Cases
- [ ] Loading states designed
- [ ] Empty states designed
- [ ] Error states designed
- [ ] Long/short content tested

---

## Final Note

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

Remember: Claude is capable of extraordinary creative work. Don't hold back—show what can truly be created when thinking outside the box and committing fully to a distinctive vision.
