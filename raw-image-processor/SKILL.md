---
name: raw-image-processor
description: Expert guidance for RAW image editing workflows, providing step-by-step processing instructions, adjustment recommendations, and non-destructive editing best practices for professional photography.
license: Apache-2.0
---

# RAW Image Processing Helper

## CRITICAL: MANDATORY DEEP WORK PROTOCOL

**Poor image quality is UNACCEPTABLE. Wrong settings are UNACCEPTABLE.**

### BANNED BEHAVIORS
```
NEVER say these after providing RAW processing guidance:
❌ "I should have considered your specific image"
❌ "Let me adjust those recommendations..."
❌ "I understand your frustration"
❌ "Upon viewing the result, those settings were wrong..."
❌ "I apologize for the generic advice"

Do it right FIRST. Analyze the specific use case before recommending.
```

### SELF-INTERROGATION (Before submitting)
- [ ] Are recommendations specific to the image type?
- [ ] Did I consider the intended output (web, print)?
- [ ] Are values realistic and tested?
- [ ] Did I explain WHY each adjustment is needed?

**If ANY answer is NO, keep working.**

---

A specialized skill for guiding professional RAW image editing workflows, optimized for use with RapidRAW and other RAW processing applications. Provides expert recommendations for exposure, color grading, retouching, and output optimization.

## Purpose

This skill assists photographers and image editors with:
- RAW file processing workflows (CR2, NEF, ARW, DNG, etc.)
- Non-destructive editing guidance
- Exposure and color correction strategies
- Genre-specific processing (portraits, landscapes, real estate, product)
- Batch processing optimization
- Output preparation for different uses

## Core Capabilities

### 1. RAW Processing Workflow Design
Create optimized editing sequences:
- **Import & Organization**: File naming, folder structure, metadata
- **Initial Assessment**: Exposure evaluation, white balance, composition
- **Base Adjustments**: Exposure, contrast, highlights/shadows
- **Color Grading**: White balance, HSL, color calibration
- **Detail Work**: Sharpening, noise reduction, clarity
- **Creative Adjustments**: Tone curves, vignettes, film emulation
- **Export Settings**: Format, color space, resolution, compression

### 2. Adjustment Recommendations
Provide specific values and ranges:
- Exposure compensation guidance (+/- stops)
- White balance Kelvin temperatures
- Highlight/shadow recovery techniques
- Saturation and vibrance balance
- Sharpening radius, amount, masking
- Noise reduction luminance/color balance

### 3. Genre-Specific Processing

#### Portrait Photography
- Skin tone preservation
- Eye enhancement techniques
- Background separation
- Flattering light adjustments
- Blemish removal workflow

#### Landscape Photography
- Dynamic range optimization
- Sky enhancement and recovery
- Foreground/background balance
- Color harmony in nature scenes
- Graduated filter simulation

#### Real Estate Photography
- Vertical line correction
- Interior/exterior exposure blending
- Window recovery techniques
- Room color accuracy
- Wide-angle distortion correction

#### Product Photography
- White background optimization
- Color accuracy for e-commerce
- Reflection control
- Detail preservation
- Consistent lighting across shots

### 4. Problem Solving
Address common RAW challenges:
- Blown highlights recovery
- Shadow detail extraction
- Mixed lighting color casts
- Chromatic aberration correction
- Lens distortion fixes
- Moiré pattern reduction
- Banding in gradients

## RapidRAW Integration

Optimized for RapidRAW's GPU-accelerated workflow:

### Non-Destructive Editing
- All adjustments saved in `.rrdata` sidecar files
- Original RAW files remain untouched
- Unlimited undo/redo capability
- Instant preview with WGSL shaders

### Adjustment Order
Recommended sequence for RapidRAW:
1. **Exposure** - Base brightness correction
2. **Temperature** - White balance (Kelvin)
3. **Tint** - Green/magenta shift
4. **Highlights/Shadows** - Tone recovery
5. **Whites/Blacks** - Endpoint adjustment
6. **Clarity** - Mid-tone contrast
7. **Vibrance/Saturation** - Color intensity
8. **Sharpness** - Edge definition
9. **Noise Reduction** - Grain smoothing
10. **Vignette** - Edge darkening (creative)

### AI Masking Features
Leverage RapidRAW's ONNX-based AI:
- **Subject Detection**: Automatic person/object isolation
- **Sky Masking**: Separate sky adjustments
- **Selective Adjustments**: Apply edits to detected regions
- **Background Blur**: AI-driven depth simulation

### ComfyUI Integration (Optional)
For generative AI enhancements:
- Background replacement workflows
- Object removal
- Style transfer
- Super-resolution upscaling
- Creative AI filters

## Usage Examples

### Example 1: Underexposed Portrait Recovery
```
User: I have an underexposed portrait RAW file. The face is too dark but the background is okay. How should I process this?

Claude:
# Underexposed Portrait Recovery Workflow

## Step 1: Global Exposure Assessment
- Open RAW in RapidRAW
- Check histogram - confirm shadows are clipped
- Identify usable highlight information

## Step 2: Initial Adjustments
1. **Exposure**: +1.5 to +2.0 stops
   - Push until face reaches proper brightness
   - Don't worry about background yet
2. **Shadows**: +40 to +60
   - Recover detail in darkest areas
   - Watch for noise in shadow regions
3. **Highlights**: -20 to -40
   - Pull back overexposed background
   - Protect blown areas

## Step 3: AI Masking (RapidRAW Feature)
1. Enable **Subject Detection**
2. Apply to detected face:
   - Exposure: Additional +0.3 to +0.7 stops
   - Clarity: +10 to +15 (eye emphasis)
   - Shadows: +20 (under-eye area)
3. Invert mask for background:
   - Exposure: -0.5 to -1.0 stops
   - Bring background to balanced level

## Step 4: Skin Tone Refinement
1. **Temperature**: Adjust to 5200-5800K (warm skin)
2. **Tint**: +5 to +10 (reduce green cast)
3. **HSL Adjustments**:
   - Orange Saturation: +5 to +10
   - Orange Luminance: +5 (brighten skin)
   - Red Saturation: -5 (reduce ruddy tones)

## Step 5: Detail & Finishing
1. **Sharpness**: 40-60 (eyes, hair)
2. **Noise Reduction**: 30-50 (needed after exposure boost)
   - Luminance: 40
   - Color: 30
3. **Clarity**: +10 to +20 (overall micro-contrast)

## Step 6: Export
- Format: JPEG (quality 95) or TIFF (16-bit)
- Color Space: sRGB (web/social) or Adobe RGB (print)
- Resolution: Original or resize as needed

Expected Result: Balanced exposure, natural skin tones, preserved detail
```

### Example 2: Real Estate Interior with Bright Windows
```
User: Real estate photo with blown windows. Can I recover them?

Claude:
# Window Recovery for Real Estate Photography

## Challenge
Interior properly exposed → windows blown white
Windows properly exposed → interior too dark

## Solution: Highlight Recovery + Dual Processing

### Method 1: Single RAW Recovery (Try First)
1. **Highlights**: -100 (maximum recovery)
2. **Whites**: -50 to -80
3. **Exposure**: Adjust room to taste (+0.3 to +1.0)
4. **Shadows**: +60 to +80 (lift interior)
5. Check windows - if detail returns, you're done!

### Method 2: Dual Processing (If Method 1 Fails)
Process RAW twice:

**Version A (Interior)**
- Exposure: +1.0 to +1.5
- Shadows: +70
- Optimize for room detail

**Version B (Windows)**
- Exposure: -2.0 to -3.0
- Highlights: -100
- Recover outdoor view

Then composite in external editor or use RapidRAW masking

### Method 3: ComfyUI Integration (Advanced)
Use RapidRAW → ComfyUI workflow:
1. Export underexposed version (windows visible)
2. Load into ComfyUI
3. Use "Interior Lighting Enhancement" workflow
4. AI brightens interior while preserving windows
5. Import result back to RapidRAW for final tweaks

## Real Estate Best Practices
- Straighten vertical lines (keystone correction)
- Color temperature: 5000-5500K (neutral, inviting)
- Vibrance: +10 to +20 (make rooms pop)
- Clarity: +15 to +25 (detail in textures)
- Slight vignette: -10 (focus on room center)
```

### Example 3: Landscape with Dramatic Sky
```
User: Create a dramatic landscape edit with enhanced sky

Claude:
# Dramatic Landscape Processing Workflow

## Step 1: Base Exposure
- Evaluate histogram for dynamic range
- Exposure: Adjust for foreground (-0.5 to +0.5)
- Don't worry about sky yet

## Step 2: Tone Separation
1. **Highlights**: -60 to -100 (sky recovery)
2. **Shadows**: +40 to +70 (foreground lift)
3. **Whites**: +20 (cloud definition)
4. **Blacks**: -15 (depth in dark areas)

## Step 3: AI Sky Masking (RapidRAW)
1. Enable **Sky Detection**
2. Sky-specific adjustments:
   - Exposure: -0.5 to -1.0 (darken)
   - Clarity: +30 to +50 (cloud drama)
   - Vibrance: +20 to +40 (blue intensity)
   - Temperature: -500K to -1000K (cooler blue)

## Step 4: Foreground Enhancement
1. Invert sky mask
2. Foreground adjustments:
   - Exposure: +0.3 to +0.7 (brighten)
   - Clarity: +15 (detail)
   - Vibrance: +10 (color depth)
   - Temperature: +200K to +500K (warmer)

## Step 5: Color Grading
1. **HSL Adjustments**:
   - Blue Saturation: +15 to +25 (sky)
   - Blue Luminance: -10 to -20 (deeper blue)
   - Green Saturation: +10 (foliage)
   - Yellow/Orange: +5 (warmth in grass/rocks)

## Step 6: Finishing Touches
1. **Tone Curve**: Subtle S-curve for contrast
2. **Vignette**: -15 to -25 (draw eye to center)
3. **Sharpness**: 50-70 (crisp details)
4. **Saturation**: -5 to +5 (fine-tune intensity)

## Alternative: Film Emulation
For classic landscape look:
- Slight green tint (+3 to +5)
- Faded blacks (lift toe of curve)
- Reduced saturation (-10 to -15)
- Grain: Low amount for texture
```

## Adjustment Guidelines by Scenario

### High Dynamic Range Scenes
- Use graduated filters/masks
- Process multiple versions if needed
- Avoid "HDR look" (halos, over-saturation)
- Target natural eye perception

### Low Light / High ISO
- Noise reduction priority
- Preserve luminance detail
- Reduce color noise aggressively
- Avoid over-sharpening
- Consider B&W conversion

### Mixed Lighting
- Custom white balance per light source
- HSL adjustments for color casts
- Consider split-toning
- Selective color correction

### Flat/Low Contrast
- S-curve in tone adjustments
- Clarity boost (+20 to +40)
- Increased vibrance
- Endpoint adjustments (whites/blacks)

### Overexposed Highlights
- Highlights slider to -100
- Whites reduction
- Check highlight warning (clipping indicator)
- Accept some lost detail if severely blown

## Best Practices

### 1. Always Shoot RAW
- Maximum editing flexibility
- 12-14 bit color depth
- Recoverable highlights/shadows
- Non-destructive white balance

### 2. Expose to the Right (ETTR)
- Maximize RAW data capture
- Avoid shadow noise
- Protect highlights
- Adjust downward in post

### 3. Non-Destructive Workflow
- Use sidecar files (.rrdata in RapidRAW)
- Preserve original RAW files
- Document adjustment values
- Create preset snapshots

### 4. Calibrated Display
- Use color-accurate monitor
- Regular calibration
- Appropriate brightness
- Neutral viewing environment

### 5. Batch Consistency
- Create presets for similar shots
- Match exposures in series
- Consistent color grading
- Note settings for reference

## Technical Specifications

### Color Spaces
- **sRGB**: Web, social media, most displays
- **Adobe RGB**: Print, professional work (wider gamut)
- **ProPhoto RGB**: Maximum editing space (later convert)

### Export Formats
- **JPEG**: Compressed, 8-bit, universal compatibility
- **TIFF**: Lossless, 16-bit option, large files
- **PNG**: Lossless, 8/16-bit, good for graphics
- **DNG**: Adobe RAW format, archival

### Resolution Guidelines
- **Web/Social**: 2048px long edge (72-150 DPI)
- **Print 8x10**: 2400x3000px minimum (300 DPI)
- **Large Print**: Original resolution (300-600 DPI)
- **Commercial**: Consult client specs

### Sharpening by Output
- **Screen**: Radius 0.5-1.0, Amount 80-120
- **Print**: Radius 1.5-2.0, Amount 60-100
- **Web (resized)**: Radius 0.3-0.5, Amount 100-150

## Common Mistakes to Avoid

1. **Over-processing**: Natural > dramatic in most cases
2. **Excessive clarity**: Creates unnatural halos
3. **Over-saturation**: Especially skin tones, skies
4. **Heavy vignettes**: Distracting if too strong
5. **Noise reduction**: Don't eliminate all texture
6. **Sharpening**: Halos and artifacts from excess
7. **Contrast**: Blocked shadows, blown highlights

## Integration with SnoopLabs Projects

### AgentLabs AI Toolkit
- Generate processing notes for client delivery
- Create factsheets for photography services
- Document editing workflows

### RapidRAW
- This skill is optimized for RapidRAW's interface
- Leverages GPU-accelerated preview
- Utilizes AI masking features
- Integrates with ComfyUI workflows

### AI MODELS Directory
Reference models for advanced processing:
- Super-resolution upscaling models
- Noise reduction AI models
- Style transfer checkpoints
- Background removal models

## Advanced Techniques

### Frequency Separation (Skin Retouching)
1. Duplicate layer concept in RapidRAW
2. Low-frequency: Color/tone
3. High-frequency: Texture/detail
4. Edit separately, recombine

### Dodge & Burn
- Selective brightness adjustments
- Use luminance masks
- Subtle (+/- 0.3 to 0.7 stops)
- Build dimension and depth

### Color Grading Styles
- **Teal & Orange**: Cool shadows, warm highlights
- **Faded Film**: Lifted blacks, muted colors
- **High Key**: Bright, airy, minimal shadows
- **Low Key**: Dark, moody, dramatic

### Focus Stacking (Multi-Shot)
- Import multiple RAW files
- Align frames
- Blend sharpest regions
- Export combined result

## Resources & Learning

### Histogram Reading
- Left: Shadows/blacks
- Center: Mid-tones
- Right: Highlights/whites
- Height: Pixel quantity
- Clipping: Data loss warning

### White Balance Reference
- Daylight: 5000-5500K
- Shade: 7000-8000K
- Cloudy: 6000-6500K
- Tungsten: 2700-3200K
- Fluorescent: 4000-5000K
- Flash: 5500-6000K

### Keyboard Shortcuts (Suggest for RapidRAW)
- E: Exposure adjustment
- T: Temperature
- H: Highlights
- S: Shadows
- C: Clarity
- Space: Before/After toggle
- Ctrl+Z: Undo
- Ctrl+Y: Redo

## Version History

- v1.0 (2025-01) - Initial release
- Optimized for RapidRAW integration
- Designed for SnoopLabs photography workflows
- Covers residential real estate, portraits, landscapes, product
