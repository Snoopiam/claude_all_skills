---
name: image-optimizer
description: Compress, resize, and convert images for web/mobile. Handles PNG, JPG, WebP, SVG optimization. Use when user needs to optimize images for performance or convert formats.
---

# Image Optimizer

You are an expert at optimizing images for web, mobile, and production use.

## When to Use This Skill

- User wants to reduce image file size
- User needs to convert between formats
- User wants to optimize for web performance
- User needs responsive images
- User wants to batch process images

## Quick Reference: Best Format for Use Case

| Use Case | Best Format | Why |
|----------|-------------|-----|
| Photos (web) | WebP, JPEG | Good compression, wide support |
| Photos (fallback) | JPEG | Universal support |
| Transparency needed | PNG, WebP | Alpha channel support |
| Icons/Logos | SVG | Scalable, tiny file size |
| Animations | WebP, GIF | Animated support |
| Print | TIFF, PNG | Lossless quality |
| Stickers (digital) | WebP, PNG | Transparency + compression |

## Optimization Commands

### Using Sharp (Node.js)

```bash
# Install
npm install sharp

# Resize and compress
npx sharp -i input.png -o output.webp --width 800 --quality 80

# Batch convert to WebP
npx sharp -i "*.png" -o ./output/ -f webp --quality 80
```

### Using ImageMagick

```bash
# Resize maintaining aspect ratio
magick input.png -resize 800x800 output.png

# Convert to WebP
magick input.png -quality 80 output.webp

# Compress JPEG
magick input.jpg -quality 85 -strip output.jpg

# Batch resize
magick mogrify -resize 50% *.png
```

### Using Squoosh CLI

```bash
# Install
npm install -g @squoosh/cli

# Optimize PNG
squoosh-cli --oxipng '{"level":3}' input.png

# Convert to WebP
squoosh-cli --webp '{"quality":80}' input.png
```

### Using SVGO (SVG only)

```bash
# Install
npm install -g svgo

# Optimize SVG
svgo input.svg -o output.svg

# Batch optimize
svgo -f ./svg-folder/ -o ./optimized/
```

## Optimization Settings by Use Case

### Web Images (General)
```
Format: WebP (with JPEG fallback)
Quality: 75-85%
Max width: 1920px (desktop), 1080px (mobile)
Strip metadata: Yes
```

### Thumbnails
```
Format: WebP or JPEG
Quality: 70-80%
Size: 150x150 to 400x400 px
Strip metadata: Yes
```

### Stickers (Digital)
```
Format: WebP or PNG
Quality: 85-95% (need crisp edges)
Size: 512x512 px (standard)
Transparency: Preserve
```

### Icons/Logos
```
Format: SVG (preferred) or PNG
PNG sizes: 16, 32, 64, 128, 256, 512 px
Optimize SVG: Remove metadata, simplify paths
```

### Social Media
```
Format: JPEG or PNG
Quality: 85-90%
Sizes vary by platform (see below)
```

## Platform-Specific Sizes

### Social Media
| Platform | Image Size |
|----------|------------|
| Instagram Post | 1080x1080 |
| Instagram Story | 1080x1920 |
| Facebook Post | 1200x630 |
| Twitter Post | 1200x675 |
| LinkedIn Post | 1200x627 |

### App Icons
| Platform | Sizes Needed |
|----------|--------------|
| iOS | 20, 29, 40, 58, 60, 76, 80, 87, 120, 152, 167, 180, 1024 |
| Android | 48, 72, 96, 144, 192, 512 |
| Favicon | 16, 32, 48, 64, 128, 256 |

## Responsive Images (HTML)

```html
<!-- Modern approach with srcset -->
<img
  src="image-800.webp"
  srcset="
    image-400.webp 400w,
    image-800.webp 800w,
    image-1200.webp 1200w
  "
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  alt="Description"
  loading="lazy"
>

<!-- With fallback -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="Description" loading="lazy">
</picture>
```

## Node.js Script for Batch Optimization

```javascript
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function optimizeImages(inputDir, outputDir, options = {}) {
  const {
    width = 1200,
    quality = 80,
    format = 'webp'
  } = options;

  const files = fs.readdirSync(inputDir);

  for (const file of files) {
    if (!/\.(jpg|jpeg|png|gif)$/i.test(file)) continue;

    const inputPath = path.join(inputDir, file);
    const outputName = file.replace(/\.[^.]+$/, `.${format}`);
    const outputPath = path.join(outputDir, outputName);

    await sharp(inputPath)
      .resize(width, null, { withoutEnlargement: true })
      .toFormat(format, { quality })
      .toFile(outputPath);

    console.log(`Optimized: ${file} → ${outputName}`);
  }
}

// Usage
optimizeImages('./input', './output', {
  width: 800,
  quality: 80,
  format: 'webp'
});
```

## Size Reduction Targets

| Original | Target | Reduction |
|----------|--------|-----------|
| 5MB+ | < 500KB | 90%+ |
| 1-5MB | < 200KB | 80-95% |
| 500KB-1MB | < 100KB | 80-90% |
| < 500KB | < 50KB | 70-90% |

## Checklist Before Optimizing

```
□ Determine target use (web, mobile, print)
□ Choose appropriate format
□ Set maximum dimensions
□ Set quality level
□ Preserve transparency if needed
□ Strip unnecessary metadata
□ Test visual quality after optimization
□ Verify file size reduction
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Over-compression | Keep quality above 70% |
| Wrong format | Use WebP for web, PNG for transparency |
| Upscaling images | Never enlarge, only reduce |
| Ignoring metadata | Strip EXIF for privacy/size |
| No fallbacks | Provide JPEG fallback for WebP |

## Process

1. **Identify** source images and target use
2. **Choose** optimal format and settings
3. **Resize** to appropriate dimensions
4. **Compress** with recommended quality
5. **Test** visual quality and file size
6. **Generate** multiple sizes if responsive needed
7. **Implement** with proper HTML/CSS
