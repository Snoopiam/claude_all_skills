---
name: logo-prompt-generator
description: Generates optimized prompts for AI logo generation tools (Midjourney, DALL-E, Stable Diffusion, ComfyUI). Transforms brand requirements into effective AI prompts with style parameters, negative prompts, and technical specifications.
license: Apache-2.0
---

# Logo Prompt Generator

## CRITICAL: MANDATORY DEEP WORK PROTOCOL

**READ THIS BEFORE GENERATING ANY PROMPTS.**

Generic prompts produce generic logos. UNACCEPTABLE.

### BANNED BEHAVIORS

```
NEVER say or think these after generating prompts:
❌ "These prompts might produce generic results"
❌ "Let me add more specificity..."
❌ "I should have included better negative prompts"
❌ "I apologize for the AI-looking outputs"
❌ "I understand your frustration"
❌ "Let me create more distinctive prompts"

If you find yourself about to say ANY of these, you FAILED.
Create distinctive prompts FIRST. Not after seeing generic results.
```

### MINIMUM PROMPT REQUIREMENTS

Before claiming prompts are complete:

1. **Understand the brand deeply** - not just the name
2. **Include STRONG negative prompts** - exclude all AI clichés
3. **Specify unusual colors** - never purple/blue gradients
4. **Reference specific styles** - not generic "modern"
5. **Add anti-generic terms** - explicitly ban AI aesthetics

### SELF-INTERROGATION (Do this before submitting)

- [ ] Did I include comprehensive negative prompts?
- [ ] Did I ban purple, blue-purple gradients, and neon colors?
- [ ] Did I specify colors by HEX code?
- [ ] Did I reference specific art movements (not just "modern")?
- [ ] Would these prompts produce unique, non-AI-looking results?
- [ ] Did I avoid all terms from the BANNED list?
- [ ] If the user generates 10 logos, will they ALL be distinctive?

**If ANY answer is wrong, you are not done. Keep working.**

### PROOF OF WORK REQUIRED

For EVERY prompt set, you MUST provide:
- Explanation of why this won't produce generic results
- The specific negative prompts included
- Why you chose these colors/styles (not AI defaults)
- What AI clichés you specifically excluded

---

A specialized skill for creating highly optimized AI prompts for logo generation. Transforms brand briefs and design requirements into effective prompts for Midjourney, DALL-E, Stable Diffusion, ComfyUI, and other AI image generation tools.

## Purpose

This skill helps designers, marketers, and entrepreneurs:
- Generate effective AI prompts for logo creation
- Translate brand requirements into AI-friendly language
- Optimize prompts for specific AI platforms (Midjourney, DALL-E, SD, ComfyUI)
- Include proper negative prompts to avoid common AI logo failures
- Specify technical parameters for best results
- Iterate and refine prompts based on outputs

## Core Philosophy

**AI Logo Generation is a Tool, Not a Replacement:**
- AI creates concepts and inspiration rapidly
- Human designers refine, vectorize, and polish
- Final logos require professional refinement
- AI excels at exploration, humans excel at execution

**The Prompt is Everything:**
- Quality of prompt = Quality of output
- Specificity > Vagueness
- Negative prompts are as important as positive
- Technical parameters drastically affect results

## Understanding AI Logo Generation

### What AI Does Well
✓ **Concept exploration**: Generate 20 variations in minutes
✓ **Style transfer**: "Art Deco typography" or "Minimalist geometric"
✓ **Inspiration**: Break creative blocks with unexpected combinations
✓ **Rapid iteration**: Test multiple directions quickly
✓ **Abstract symbols**: Geometric patterns, organic shapes

### What AI Struggles With
❌ **Text rendering**: Gibberish text, misspellings, distorted letters
❌ **Vector precision**: Outputs are raster (pixels), not scalable vectors
❌ **Subtle refinement**: Optical corrections, kerning, spacing
❌ **Brand strategy**: No understanding of market positioning, audience psychology
❌ **Trademark originality**: May generate similar to existing logos
❌ **Consistency**: Variations differ significantly across generations

### Recommended Workflow
1. **AI Generation**: Create 10-20 concept variations with this skill's prompts
2. **Selection**: Choose 2-3 strongest directions
3. **Human Refinement**: Designer recreates in vector, refines proportions, typography
4. **Iteration**: Generate more AI variations based on refined direction
5. **Final Polish**: Professional designer finalizes, creates variations, brand guidelines

## AI Platform Comparison

### Midjourney
**Strengths:**
- Best aesthetic quality and artistic interpretation
- Strong at abstract symbols, minimalist designs
- Excellent color palettes and composition
- Version 6+ handles text better (but still imperfect)

**Weaknesses:**
- Text rendering still problematic
- Less control over exact output
- Subscription required
- No local generation

**Best For:** Abstract symbols, iconic marks, visual inspiration, mood boards

**Prompt Style:** Natural language with style keywords, parameters at end

### DALL-E 3 (OpenAI)
**Strengths:**
- Better text rendering than Midjourney
- Good at following specific instructions
- Understands complex compositional requests
- Accessible via ChatGPT Plus

**Weaknesses:**
- More literal, less artistic interpretation
- Can look "AI-generated" (too perfect, soulless)
- Limited control parameters
- Censorship filters can block legitimate requests

**Best For:** Combination marks (symbol + text), wordmarks with simple text, literal concepts

**Prompt Style:** Detailed natural language descriptions, conversational

### Stable Diffusion / ComfyUI
**Strengths:**
- Full control over every parameter
- Local generation (privacy, unlimited)
- LoRA models for specific styles (e.g., "flat logo design")
- ControlNet for guided composition
- Negative prompts for precise exclusions

**Weaknesses:**
- Steeper learning curve
- Requires technical setup
- Base models struggle with logos without fine-tuning
- Need to find/train specialized logo models

**Best For:** High-volume iteration, specific style control, designers with technical skills

**Prompt Style:** Keyword-heavy, technical parameters, negative prompts critical

### Adobe Firefly
**Strengths:**
- Commercially safe (trained on Adobe Stock)
- Good integration with Adobe suite
- Decent text rendering

**Weaknesses:**
- Less creative than Midjourney
- Smaller model, less capable
- Limited to Adobe ecosystem

**Best For:** Commercial projects requiring copyright safety, Adobe users

**Prompt Style:** Natural language, similar to DALL-E

## Prompt Components Breakdown

### 1. Logo Type Declaration
**Always start with logo type to set context:**

**For Symbol/Icon Marks:**
```
"minimalist logo icon, abstract symbol, [concept], simple geometric design"
"flat logo design, iconic symbol of [concept], clean and modern"
```

**For Wordmarks/Logotypes:**
```
"typography logo, wordmark design for '[BRAND NAME]', custom lettering"
"lettermark logo, '[INITIALS]' monogram, elegant typography"
```

**For Combination Marks:**
```
"logo design combining symbol and text, '[BRAND NAME]' with [symbol description]"
"brand mark with icon and wordmark, [symbol] + '[BRAND NAME]' typography"
```

**For Emblems:**
```
"circular emblem logo, badge design with '[BRAND NAME]', traditional seal"
"vintage badge logo, emblem containing [elements], classic style"
```

### 2. Visual Style Keywords

**Minimalist/Modern:**
```
minimalist, clean, simple, geometric, flat design, negative space,
contemporary, sleek, modern, streamlined, uncluttered
```

**Vintage/Retro:**
```
vintage, retro, art deco, mid-century, classic, timeless, heritage,
traditional, nostalgic, [decade: 1920s, 1950s, 1970s, etc.]
```

**Luxury/Premium:**
```
elegant, sophisticated, refined, luxurious, premium, upscale,
high-end, exclusive, prestigious, opulent
```

**Playful/Friendly:**
```
playful, friendly, approachable, whimsical, fun, cheerful,
energetic, youthful, vibrant, dynamic
```

**Tech/Futuristic:**
```
futuristic, tech, digital, cyber, sci-fi, innovative, cutting-edge,
high-tech, electronic, modern tech
```

**Organic/Natural:**
```
organic, natural, handcrafted, artisanal, rustic, earthy,
botanical, nature-inspired, flowing, hand-drawn
```

**Bold/Powerful:**
```
bold, strong, powerful, impactful, confident, assertive,
dynamic, energetic, striking, commanding
```

**Professional/Corporate:**
```
professional, corporate, authoritative, trustworthy, established,
credible, serious, formal, institutional
```

### 3. Industry/Concept Keywords

**Technology:**
```
tech, digital, innovation, connectivity, network, circuit, data,
cloud, AI, software, algorithm, code
```

**Food/Restaurant:**
```
culinary, gourmet, artisan, fresh, farm-to-table, chef, kitchen,
dining, flavor, taste, organic, homemade
```

**Health/Wellness:**
```
health, wellness, vitality, balance, harmony, healing, natural,
holistic, mindful, care, fitness, nutrition
```

**Fashion/Beauty:**
```
fashion, style, beauty, elegance, chic, glamour, couture,
cosmetics, skincare, luxury, trendy
```

**Finance/Law:**
```
financial, trust, stability, authority, justice, equity, growth,
wealth, security, professional, credible
```

**Real Estate:**
```
property, home, architecture, building, residential, shelter,
foundation, space, location, modern living
```

**Education:**
```
learning, knowledge, education, academic, growth, development,
teaching, wisdom, discovery, literacy
```

**Creative/Agency:**
```
creative, design, innovation, imagination, artistic, visionary,
studio, craft, conceptual, expressive
```

### 4. Color Specifications

**Format:**
```
"[primary color] and [secondary color] color scheme"
"monochrome [color] design"
"black and white with [accent color] accent"
```

**Examples:**
```
"navy blue and gold color palette, premium feel"
"vibrant orange and deep purple combination"
"forest green monochrome, natural aesthetic"
"black and white with electric cyan accents"
```

**Specific Color Terms:**
```
Primary colors: red, blue, yellow
Secondary: orange, green, purple
Tertiary: teal, coral, burgundy, navy, sage, etc.

Descriptors: vibrant, muted, pastel, deep, rich, bright, dark,
light, neon, metallic, earthy, warm, cool
```

### 5. Composition & Layout

**Symmetry:**
```
"symmetrical composition, balanced design, centered layout"
"radial symmetry, circular balance"
```

**Asymmetry:**
```
"dynamic asymmetrical layout, off-center composition"
"modern asymmetric design, visual tension"
```

**Geometric:**
```
"geometric shapes, circles and triangles, angular composition"
"hexagonal structure, modular grid system"
```

**Organic:**
```
"flowing organic forms, natural curves, fluid shapes"
"hand-drawn feel, organic linework"
```

### 6. Typography Specifications (for text-based logos)

**For Wordmarks:**
```
"bold sans-serif typography, modern letterforms"
"elegant serif lettering, classical proportions"
"custom geometric font, architectural letters"
"flowing script lettering, calligraphic style"
"condensed uppercase typography, vertical emphasis"
```

**Avoid (in negative prompt):**
```
"gibberish text, misspelled words, distorted letters,
unreadable typography, corrupted text"
```

### 7. Negative Prompts (CRITICAL)

**Always include to avoid common AI failures:**

**Universal Negative Prompts:**
```
realistic, photographic, 3D render, detailed illustration,
complex details, gradient effects, drop shadow, emboss,
bevels, too many colors, cluttered, busy, text errors,
multiple versions, watermark, blurry, low quality
```

**For Minimalist Logos:**
```
ornate, decorative, intricate patterns, excessive details,
multiple elements, complex composition, textured
```

**For Text-Based Logos:**
```
gibberish text, misspelled words, wrong letters, distorted text,
unreadable, corrupted font, random characters
```

**For Professional/Corporate:**
```
playful, whimsical, cartoonish, childish, informal,
handwritten, messy, unprofessional
```

**For Vintage/Classic:**
```
modern, futuristic, tech, digital, minimalist, stark,
contemporary, trendy
```

### 8. Technical Parameters

**Midjourney Parameters:**
```
--v 6.1                    (version 6.1, best for logos)
--style raw                (less artistic interpretation, more literal)
--s 50                     (stylization 0-1000, lower = more literal)
--ar 1:1                   (aspect ratio, square for most logos)
--ar 3:2                   (horizontal logos)
--ar 2:3                   (vertical logos)
--no [elements]            (negative prompt inline)
--q 2                      (quality, higher = more detail)
--chaos 0                  (consistency, 0 = most consistent)
```

**DALL-E (via ChatGPT):**
```
No special parameters, use natural language and be explicit:
"Create a square composition, 1024x1024, centered, white background"
```

**Stable Diffusion / ComfyUI:**
```
Sampler: DPM++ 2M Karras or Euler a
Steps: 25-40
CFG Scale: 7-9 (logo prompts work well at 7-8)
Resolution: 1024x1024 (SD 1.5), 1024x1024 (SDXL)
Negative prompt: (see detailed negative prompts above)
LoRA: "Flat Logo Design" or similar logo-specific models
ControlNet: Edge detection or scribble for guided composition
```

## Prompt Templates by Logo Type

### Template 1: Minimalist Symbol/Icon Mark

**Platform: Midjourney**
```
minimalist logo icon of [CONCEPT], simple geometric design,
flat vector style, [COLOR SCHEME], clean and modern,
negative space, professional, white background --v 6.1 --s 50 --ar 1:1
```

**Example:**
```
minimalist logo icon of a mountain peak, simple geometric design,
flat vector style, navy blue and slate gray, clean and modern,
negative space, professional, white background --v 6.1 --s 50 --ar 1:1
```

**Negative Prompt (SD/ComfyUI):**
```
realistic, photographic, 3D render, detailed illustration, gradient,
drop shadow, complex details, multiple colors, cluttered, watermark,
text, letters, words
```

---

### Template 2: Modern Tech Logo (Abstract Symbol)

**Platform: Midjourney**
```
abstract tech logo, [CONCEPT], geometric minimalist design,
[COLOR] and [COLOR] color palette, futuristic, innovation,
connectivity concept, flat vector, clean lines, white background
--v 6.1 --style raw --s 40 --ar 1:1
```

**Example:**
```
abstract tech logo, neural network nodes, geometric minimalist design,
electric blue and cyan color palette, futuristic, innovation,
connectivity concept, flat vector, clean lines, white background
--v 6.1 --style raw --s 40 --ar 1:1
```

**Negative Prompt:**
```
realistic, photographic, 3D, gradient mesh, complex illustration,
ornate details, vintage, retro, text, letters, organic shapes,
irregular forms
```

---

### Template 3: Vintage/Retro Badge/Emblem

**Platform: Midjourney**
```
vintage badge logo, circular emblem, [INDUSTRY/CONCEPT],
[ERA: art deco/1950s/Victorian] style, [COLOR] and [COLOR],
classic typography, traditional design, seal of quality,
detailed linework, white background --v 6.1 --s 70 --ar 1:1
```

**Example:**
```
vintage badge logo, circular emblem, coffee roasting company,
1920s art deco style, brown and cream, classic typography,
traditional design, seal of quality, detailed linework,
white background --v 6.1 --s 70 --ar 1:1
```

**Negative Prompt:**
```
modern, minimalist, tech, futuristic, flat design, simple,
geometric only, sans-serif only, digital, photographic
```

---

### Template 4: Wordmark/Typography Logo

**Platform: DALL-E 3 (better text rendering)**
```
typography logo design for "[BRAND NAME]", [STYLE] lettering,
[FONT STYLE: bold sans-serif/elegant serif/custom geometric],
[COLOR] color, minimal, professional, clean wordmark,
white background, vector style, no additional graphics
```

**Example:**
```
typography logo design for "NEXUS", bold geometric sans-serif lettering,
modern architectural font, navy blue color, minimal, professional,
clean wordmark, white background, vector style, no additional graphics
```

**Negative Prompt:**
```
symbol, icon, illustration, decorative elements, complex design,
gradient, 3D effects, shadow, multiple fonts, script, handwriting
```

---

### Template 5: Lettermark/Monogram

**Platform: Midjourney**
```
lettermark logo, "[INITIALS]" monogram, [STYLE] design,
interlocking letters, [FONT STYLE], [COLOR SCHEME],
sophisticated, professional, balanced composition,
white background --v 6.1 --s 50 --ar 1:1
```

**Example:**
```
lettermark logo, "HC" monogram, art deco design,
interlocking letters, geometric serif font, black and gold,
sophisticated, professional, balanced composition,
white background --v 6.1 --s 50 --ar 1:1
```

**Negative Prompt:**
```
full words, complete text, realistic, photographic, illustration,
complex details, decorative borders, multiple colors, gradient
```

---

### Template 6: Organic/Natural Symbol

**Platform: Stable Diffusion with Nature LoRA**
```
organic logo design, [NATURAL ELEMENT: leaf/tree/water/etc.],
flowing natural forms, [COLOR PALETTE], botanical illustration style,
simple elegant linework, minimalist, earthy, white background
```

**Example:**
```
organic logo design, olive branch and leaves, flowing natural forms,
sage green and forest green palette, botanical illustration style,
simple elegant linework, minimalist, earthy, white background
```

**Negative Prompt:**
```
geometric, angular, tech, futuristic, mechanical, industrial,
complex patterns, realistic rendering, photographic, 3D,
text, letters, multiple elements
```

---

### Template 7: Playful/Friendly Icon

**Platform: Midjourney**
```
playful logo icon, [CONCEPT], friendly rounded shapes,
[COLOR SCHEME], cheerful, approachable, simple character design,
flat vector illustration, clean outlines, white background
--v 6.1 --s 60 --ar 1:1
```

**Example:**
```
playful logo icon, smiling coffee cup character, friendly rounded shapes,
warm brown and cream colors, cheerful, approachable, simple character design,
flat vector illustration, clean outlines, white background
--v 6.1 --s 60 --ar 1:1
```

**Negative Prompt:**
```
serious, corporate, minimalist, geometric only, angular,
realistic, detailed, complex, dark colors, professional corporate
```

---

### Template 8: Luxury/Premium Brand Mark

**Platform: Midjourney**
```
luxury logo design, [CONCEPT], elegant minimalist symbol,
[PREMIUM COLORS: gold/black/navy], sophisticated, refined,
high-end brand, timeless design, balanced composition,
white background --v 6.1 --style raw --s 40 --ar 1:1
```

**Example:**
```
luxury logo design, diamond geometry with crown element, elegant minimalist symbol,
black and gold color scheme, sophisticated, refined, high-end brand,
timeless design, balanced composition, white background
--v 6.1 --style raw --s 40 --ar 1:1
```

**Negative Prompt:**
```
playful, casual, bright colors, childish, informal, busy,
complex details, realistic, photographic, gradient, 3D effects
```

---

## Industry-Specific Prompt Examples

### Technology Startup
```
minimalist tech logo, abstract connectivity symbol,
geometric nodes and lines, electric blue and cyan gradient,
modern innovation, digital network concept, flat vector design,
clean professional, white background --v 6.1 --style raw --s 45 --ar 1:1

Negative: realistic, 3D render, complex illustration, vintage,
ornate, text, multiple colors, cluttered
```

### Organic Bakery
```
artisanal bakery logo, wheat sheaf icon, hand-drawn organic style,
warm brown and cream colors, rustic elegant, natural linework,
circular composition, traditional craft, white background
--v 6.1 --s 65 --ar 1:1

Negative: modern tech, geometric only, minimalist, futuristic,
bright colors, photographic, 3D, complex details
```

### Law Firm
```
professional law firm logo, classical pillar symbol,
elegant serif typography "[FIRM NAME]", navy blue and gold,
authoritative, trustworthy, timeless traditional design,
balanced symmetrical, white background --v 6.1 --s 50 --ar 1:1

Negative: playful, modern tech, colorful, informal, abstract,
organic shapes, handwritten, casual
```

### Fitness Brand
```
dynamic fitness logo, abstract human in motion symbol,
bold angular geometric design, energetic red and black,
powerful athletic, modern strong, movement concept,
flat vector, white background --v 6.1 --style raw --s 50 --ar 1:1

Negative: delicate, soft, pastel colors, vintage, ornate,
complex details, realistic, photographic, text heavy
```

### Children's Education
```
playful education logo, colorful learning symbol,
friendly rounded shapes, rainbow color palette, cheerful,
approachable, simple illustration, fun bright design,
white background --v 6.1 --s 70 --ar 1:1

Negative: serious corporate, minimal, monochrome, sophisticated,
luxury, complex, realistic, dark colors, professional formal
```

### Real Estate Luxury
```
luxury real estate logo, modern architectural symbol,
elegant geometric house/building design, black and gold,
sophisticated minimal, premium upscale, clean refined,
white background --v 6.1 --style raw --s 40 --ar 1:1

Negative: playful, casual, colorful, vintage ornate, busy,
realistic rendering, photographic, 3D detailed
```

## Advanced Prompt Techniques

### 1. Style Fusion
Combine two distinct styles for unique results:
```
"minimalist logo combining Japanese zen aesthetics with
Bauhaus geometric principles, [concept], [colors]"

"art deco elegance meets modern tech minimalism,
[concept] logo design, [colors]"
```

### 2. Artist/Movement References
Reference specific art movements or designers (use ethically, for style inspiration only):
```
"logo in the style of Swiss modernism, [concept],
geometric precision, limited color palette"

"Bauhaus-inspired logo design, [concept],
form follows function, primary colors"

Note: Don't copy specific living artists' work directly
```

### 3. Material/Texture Implications (for style, not literal texture)
```
"brushed metal aesthetic logo, [concept], industrial modern"
"paper-cut style logo, layered minimalist design, [concept]"
"neon sign inspired logo, [concept], glowing outline style"
```

### 4. Negative Space Emphasis
```
"clever negative space logo, [concept] with hidden [element],
minimalist dual-image design, [colors]"

Example: "clever negative space logo, coffee cup with
hidden steam forming bird shape, black and white"
```

### 5. Geometric Construction Specification
```
"logo based on golden ratio proportions, [concept],
circular geometry, perfect mathematical balance"

"hexagonal grid logo system, modular [concept] design,
geometric precision, [colors]"
```

### 6. Cultural/Regional Style Influences
```
"Scandinavian minimalist logo, [concept], clean simple,
muted Nordic color palette"

"Japanese minimalism meets [concept], zen simplicity,
balanced negative space, [colors]"
```

## Iteration & Refinement Strategy

### Round 1: Exploration (Generate 10-20 variations)
- Use broad prompts with varied styles
- Test different logo types (symbol, wordmark, combination)
- Explore color palettes
- Try multiple AI platforms

### Round 2: Direction Selection (Narrow to 2-3 directions)
- Choose strongest concepts
- Identify what works (composition, colors, style)
- Identify what to improve

### Round 3: Refinement (Generate focused variations)
- Adjust prompts based on Round 1 learnings
- Add more specific negative prompts to eliminate unwanted elements
- Fine-tune colors, composition, style keywords
- Test variations: "make it more [bold/subtle/modern/classic]"

### Round 4: Final Candidates (Generate print-ready concepts)
- Lock in best prompt formulas
- Generate multiple seeds/variations of top concepts
- Prepare for designer handoff (vectorization, refinement)

## Common Prompt Problems & Fixes

### Problem: Too Complex/Cluttered Output
**Fix:**
- Add "minimalist, simple, clean" to prompt
- Negative prompt: "complex details, busy, cluttered, ornate"
- Reduce concept elements to 1-2 maximum
- Use "--s 30" (lower stylization) in Midjourney

### Problem: Text is Gibberish
**Fix:**
- Switch to DALL-E 3 (better text rendering)
- Use shorter text (2-3 letters max)
- Negative prompt: "text errors, misspelled, gibberish, wrong letters"
- Consider symbol-only logos, add text manually later

### Problem: Too Generic/Looks Like Other Logos
**Fix:**
- Add unique concept combinations
- Reference specific styles: "Bauhaus meets organic forms"
- Use unexpected color combinations
- Add distinctive element: "with hidden [element] in negative space"

### Problem: Colors Are Wrong/Muddy
**Fix:**
- Specify exact colors: "navy blue (#1E3A8A) and gold (#FFD700)"
- Use "flat color design, solid colors, no gradients"
- Negative prompt: "gradient, blended colors, multiple shades"
- Monochrome first, add color later manually

### Problem: Not Professional Enough
**Fix:**
- Add "professional, corporate, clean, polished"
- Negative prompt: "amateur, messy, rough, sketchy"
- Use "vector style, logo design, brand identity"
- Reference: "as seen on corporate brand guidelines"

### Problem: Too "AI-Looking"
**Fix:**
- Use "--style raw" in Midjourney (less AI interpretation)
- Add "hand-crafted feel, artisanal, human-designed"
- Reference traditional design: "Swiss modernism, classic design principles"
- Plan for human refinement (AI is concept, human is execution)

## Integration with SnoopLabs Projects

### ComfyUI Workflow Builder
Use this skill with ComfyUI:
- **Generate prompts** for ComfyUI text-to-image nodes
- **Reference AI MODELS directory**: Use logo-specific LoRAs
- **Workflow**: Prompt generation → ComfyUI batch processing → Selection → Vectorization

**Example ComfyUI Workflow:**
1. Load SDXL checkpoint
2. Load "Flat Logo Design" LoRA (strength 0.8)
3. CLIP Text Encode (positive): [Generated prompt from this skill]
4. CLIP Text Encode (negative): [Generated negative prompt]
5. Empty Latent Image (1024x1024)
6. KSampler (25 steps, DPM++ 2M Karras, CFG 7)
7. VAE Decode
8. Save Image (batch of 4-8 variations)

### Logo Designer Skill
Complementary workflow:
- **Logo Prompt Generator**: Creates AI concepts for exploration
- **Logo Designer Skill**: Human-refined final logos with brand strategy

**Combined Process:**
1. Use Logo Prompt Generator → Generate 20 AI concepts
2. Select top 3 directions
3. Use Logo Designer Skill → Refine strategy, vectorize, create guidelines

### AgentLabs AI Toolkit
Generate supporting materials:
- **Presentation Builder**: Show AI-generated concepts to clients
- **Notes Generator**: Document prompt iterations and learnings
- **Factsheet Generator**: Create brand identity presentations

## Prompt Library by Platform

### Midjourney Prompt Collection

**Minimalist Tech:**
```
abstract tech logo, geometric neural network, electric blue and cyan,
minimalist modern, connectivity symbol, flat vector, clean lines,
white background --v 6.1 --style raw --s 40 --ar 1:1
```

**Vintage Badge:**
```
vintage circular badge logo, 1920s art deco, coffee roastery,
brown and cream, ornate classic typography, traditional seal,
detailed linework, white background --v 6.1 --s 70 --ar 1:1
```

**Luxury Minimal:**
```
luxury minimalist logo, elegant geometric symbol, black and gold,
sophisticated refined, premium brand, timeless design,
balanced composition, white background --v 6.1 --style raw --s 35 --ar 1:1
```

**Organic/Natural:**
```
organic logo design, flowing leaf symbol, botanical style,
sage green and forest green, natural elegant linework,
minimalist earthy, white background --v 6.1 --s 60 --ar 1:1
```

**Bold/Athletic:**
```
bold athletic logo, abstract motion symbol, dynamic angular design,
powerful red and black, energetic sports concept, flat vector,
white background --v 6.1 --style raw --s 50 --ar 1:1
```

### DALL-E 3 Prompt Collection

**Wordmark:**
```
Clean typography logo for "BRAND NAME", bold modern sans-serif,
navy blue color, minimal professional wordmark, vector style,
centered on white background, no additional graphics or symbols
```

**Monogram:**
```
Elegant monogram logo with letters "AB", interlocking design,
classical serif font, black and gold color scheme, symmetrical
balanced composition, luxury feel, white background
```

**Combination Mark:**
```
Logo combining mountain peak icon with "SUMMIT" text below,
minimalist geometric design, forest green and slate gray colors,
clean modern style, balanced vertical composition, white background
```

### Stable Diffusion Prompt Collection

**Positive Prompt:**
```
flat logo design, minimalist geometric symbol, [concept],
[color] and [color] color scheme, simple clean vector style,
professional brand identity, centered composition, white background
```

**Negative Prompt:**
```
realistic, photographic, 3D render, photograph, detailed illustration,
gradient effects, drop shadow, emboss, bevel, texture, complex details,
too many colors, cluttered, busy, ornate, decorative, multiple versions,
watermark, text, letters, words, signature, blurry, low quality,
oversaturated, noisy
```

## Resources & Tools

### AI Platforms
- **Midjourney**: Discord-based, best aesthetics
- **DALL-E 3**: Via ChatGPT Plus or API
- **Stable Diffusion**: Automatic1111, ComfyUI (local generation)
- **Adobe Firefly**: Commercially safe, Adobe integration

### Logo-Specific Resources
- **LoRA Models** (Stable Diffusion): Search "logo design" on Civitai
- **Prompt Databases**: PromptHero, Lexica (Stable Diffusion prompts)
- **Style References**: Collect logo styles you like, reverse-engineer prompts

### Post-AI Tools
- **Vectorization**: Adobe Illustrator Image Trace, Inkscape, Vector Magic
- **Refinement**: Figma, Adobe Illustrator, Affinity Designer
- **Color Extraction**: Coolors.co, Adobe Color

## BANNED: AI-Generated Aesthetic Clichés

**CRITICAL**: Never include these in prompts as they produce generic, obviously AI-generated results:

### BANNED COLOR TERMS (Never use in prompts)

```
PURPLE/VIOLET (The #1 AI cliché):
- "purple", "violet", "lavender", "amethyst"
- "purple and blue gradient"
- "cyan and purple"
- "neon purple"

OVERUSED COMBINATIONS:
- "blue to purple gradient"
- "pink and purple"
- "electric blue and cyan"
- "synthwave colors"
- "aurora colors"
- "cosmic colors"
- "galaxy palette"

GENERIC TECH:
- "tech blue"
- "startup colors"
- "modern gradient"
```

### BANNED STYLE TERMS (Remove from prompts)

```
OVERUSED AESTHETICS:
- "glassmorphism"
- "3D floating"
- "neon glow"
- "holographic"
- "iridescent"
- "chrome effect"
- "mesh gradient"

CLICHÉ DESCRIPTORS:
- "futuristic tech"
- "modern startup"
- "innovative digital"
- "cutting-edge"
- "next-generation"
```

### BANNED SYMBOLS (Exclude from concepts)

```
OVERUSED ICONS:
- "light bulb" (for ideas)
- "globe" (for global)
- "arrow pointing up" (for growth)
- "rocket ship" (for startups)
- "brain" or "neural network" (for AI/tech)
- "infinity symbol"
- "hexagon with nodes"
- "abstract swoosh"
- "geometric lion/wolf/eagle made of triangles"
- "letter with hidden arrow"
```

### ENHANCED NEGATIVE PROMPTS

**Add these to EVERY logo prompt:**
```
purple, violet, lavender, purple gradient, blue to purple,
cyan and purple, neon glow, holographic, iridescent,
glassmorphism, 3D floating, chrome effect, rainbow gradient,
generic tech, startup cliché, light bulb, globe symbol,
rocket ship, brain icon, neural network, infinity symbol,
hexagon nodes, abstract swoosh, generic minimalist
```

### INSTEAD USE: Distinctive Alternatives

**COLOR ALTERNATIVES:**
```
Instead of purple/blue:
- "terracotta and cream"
- "forest green and mustard"
- "burgundy and gold"
- "charcoal and coral"
- "navy and peach"
- "olive and blush"
- "rust and sage"
- "midnight green and warm gray"

Specify exact colors when possible:
- "deep burgundy (#722F37)"
- "warm terracotta (#C2703E)"
- "prussian blue (#003153)"
```

**STYLE ALTERNATIVES:**
```
Instead of generic modern:
- "Swiss modernism, Bauhaus principles"
- "Japanese minimalism, zen simplicity"
- "art deco geometric precision"
- "mid-century modern warmth"
- "Scandinavian clean design"
- "editorial typography focus"
- "architectural precision"
- "hand-crafted artisanal feel"
```

**SYMBOL ALTERNATIVES:**
```
Instead of cliché icons:
- "abstract form derived from [specific concept]"
- "negative space creating [hidden meaning]"
- "custom letterform based on [brand name]"
- "geometric abstraction of [real object]"
- "typographic solution only"
- "cultural symbol from [specific origin]"
```

### EXAMPLE: Fixing AI-Generic Prompts

**BAD (Generic AI look):**
```
minimalist tech logo, abstract symbol, blue and purple gradient,
modern innovation, futuristic, clean design
```

**GOOD (Distinctive):**
```
minimalist logo, abstract form inspired by architectural arches,
midnight green (#004953) and warm gray (#9B9B8F),
Swiss modernism influence, geometric precision,
Bauhaus principles, white background
--no purple, violet, gradient, neon, glow, tech cliché
```

**BAD (Generic AI look):**
```
startup logo, rocket ship, innovation, blue cyan colors,
modern tech, dynamic
```

**GOOD (Distinctive):**
```
brand mark, abstract ascending form (NOT rocket),
terracotta (#C2703E) and charcoal (#36454F),
editorial precision, architectural influence,
balanced asymmetry, white background
--no rocket, arrow, swoosh, purple, blue gradient, generic tech
```

---

## Best Practices Summary

1. **Start Simple**: Minimalist prompts often produce better logos than complex ones
2. **Negative Prompts Matter**: Spend as much time on negatives as positives
3. **Iterate Rapidly**: Generate 10-20 before committing to a direction
4. **Platform-Specific**: Use Midjourney for symbols, DALL-E for text, SD for control
5. **Human Refinement**: AI is concept exploration, designers create final logos
6. **Trademark Search**: Check originality before finalizing (even AI-generated logos can infringe)
7. **Vector Always**: Plan to recreate raster AI outputs in vector formats
8. **Test at Small Sizes**: Best logos work at 50px width
9. **Monochrome First**: Test in black and white before adding color
10. **Document Prompts**: Save successful prompts for future refinement
11. **AVOID AI CLICHÉS**: Never use purple, gradients, or generic tech symbols

## Ethical Considerations

### Copyright & Originality
- AI-generated logos are starting points, not final products
- Always check for similarity to existing logos (Google Image Search, TinEye)
- Recreate in vector to add originality and human craftsmanship
- Trademark search before commercial use

### Artist Attribution
- Don't prompt "in the style of [living artist]" to copy their work directly
- Art movements/eras are fair (Bauhaus, Art Deco), specific artists less so
- Use for inspiration, not replication
- Add human creativity and refinement

### AI Disclosure
- Be transparent with clients if using AI in design process
- Position as "AI-assisted concept exploration + professional refinement"
- Final deliverable should be human-refined, vectorized, professional

## Version History

- v1.0 (2025-01) - Initial release
- Optimized for Midjourney, DALL-E, Stable Diffusion, ComfyUI
- Integration with SnoopLabs logo-designer and comfyui-workflow-builder skills
- Comprehensive prompt templates for all logo types and industries

---

*This skill generates AI logo prompts for rapid concept exploration. Final logos should always be professionally refined, vectorized, and validated for originality. AI is a powerful tool for ideation, but human design expertise creates ownable, strategic brand identities.*
