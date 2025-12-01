---
name: comfyui-workflow-builder
description: Generates optimized ComfyUI workflows for image generation, editing, and enhancement. Creates JSON workflow files using available models and provides step-by-step setup instructions.
license: Apache-2.0
---

# ComfyUI Workflow Builder

## CRITICAL: MANDATORY DEEP WORK PROTOCOL

**READ THIS BEFORE CREATING ANY WORKFLOW.**

Broken workflows are UNACCEPTABLE. Missing nodes is UNACCEPTABLE.

### BANNED BEHAVIORS
```
NEVER say these after delivering a workflow:
❌ "I should have checked the node connections"
❌ "Let me fix that missing node..."
❌ "I understand your frustration"
❌ "Upon testing, there's an error..."
❌ "I apologize for the broken workflow"

If you're about to say ANY of these, you FAILED.
Create working workflows FIRST. Not after errors.
```

### SELF-INTERROGATION (Before submitting)
- [ ] Are ALL node connections valid?
- [ ] Did I verify the workflow structure is correct?
- [ ] Are the model names accurate?
- [ ] Did I include all required nodes?
- [ ] Would this workflow execute without errors?

**If ANY answer is NO, keep working.**

---

A specialized skill for creating, optimizing, and troubleshooting ComfyUI workflows. Generates production-ready workflow JSON files for image generation, editing, upscaling, and creative AI tasks using Stable Diffusion and other generative models.

## Purpose

This skill helps AI artists, photographers, and developers:
- Generate ComfyUI workflow JSON files from text descriptions
- Optimize workflows for specific hardware (GPU VRAM, CPU)
- Select appropriate models from available checkpoints
- Create custom node configurations
- Troubleshoot workflow errors
- Build production pipelines for batch processing

## Capabilities

### 1. Workflow Generation
Create workflows for common tasks:
- **Text-to-Image**: Basic SD generation with prompts
- **Image-to-Image**: Style transfer, variations, img2img
- **Inpainting**: Object removal, selective editing
- **Outpainting**: Canvas extension, scene expansion
- **Upscaling**: Super-resolution, detail enhancement
- **ControlNet**: Pose, depth, edge-guided generation
- **LoRA Stacking**: Multiple LoRA model combinations
- **Face Restoration**: Portrait enhancement, face swap
- **Background Removal**: Subject isolation, transparency
- **Batch Processing**: Multiple image generation

### 2. Model Selection & Management
Optimize model usage based on SnoopLabs AI MODELS directory:

**Available Model Categories:**
```
AI MODELS/
├── checkpoints/          # Main SD models (SD 1.5, SDXL, custom)
├── loras/               # LoRA models for style/character
├── controlnet/          # ControlNet models (pose, depth, canny)
├── vae/                 # VAE models for encoding/decoding
├── clip/                # CLIP text encoders
├── clip_vision/         # CLIP vision models
├── upscale_models/      # Super-resolution models (ESRGAN, RealESRGAN)
├── embeddings/          # Textual inversions
├── style_models/        # Style transfer models
└── ipadapter/          # IP-Adapter models
```

### 3. Hardware Optimization
Adjust workflows for available resources:
- **High VRAM (12GB+)**: SDXL, batch processing, high resolution
- **Medium VRAM (6-10GB)**: SD 1.5, standard resolution, VAE tiling
- **Low VRAM (<6GB)**: Optimized settings, model offloading, reduced batch
- **CPU Fallback**: Slower but functional workflows

### 4. Custom Node Integration
Support for popular ComfyUI custom nodes:
- **ControlNet Preprocessors**: Canny, depth, pose detection
- **Face Detectors**: RetinaFace, MediaPipe
- **Upscaler Nodes**: Ultimate SD Upscale, iterative upscaling
- **Image Processing**: Color correction, filters, compositing
- **Video Nodes**: Frame interpolation, animation
- **Utility Nodes**: Batch processing, file operations

## Workflow Templates

### Template 1: Basic Text-to-Image (SD 1.5)
**Use Case**: Simple image generation from text prompts

**Required Models:**
- Checkpoint: `checkpoints/v1-5-pruned-emaonly.safetensors` (or similar SD 1.5)
- VAE: `vae/vae-ft-mse-840000-ema-pruned.safetensors` (optional, improves quality)

**Workflow Description:**
```
1. Load Checkpoint (SD 1.5)
2. CLIP Text Encode (Positive Prompt)
3. CLIP Text Encode (Negative Prompt)
4. Empty Latent Image (512x512)
5. KSampler (20 steps, euler, normal CFG 7)
6. VAE Decode
7. Save Image
```

**Parameters:**
- Resolution: 512x512 (SD 1.5 native)
- Steps: 20-30
- CFG Scale: 7-9
- Sampler: euler, euler_a, dpmpp_2m
- Scheduler: normal, karras

### Template 2: SDXL High Quality Generation
**Use Case**: Photorealistic or high-detail image generation

**Required Models:**
- Base: `checkpoints/sd_xl_base_1.0.safetensors`
- Refiner: `checkpoints/sd_xl_refiner_1.0.safetensors` (optional)
- VAE: `vae/sdxl_vae.safetensors`

**Workflow Description:**
```
1. Load SDXL Base Checkpoint
2. CLIP Text Encode (Positive) - Both CLIP-L and CLIP-G
3. CLIP Text Encode (Negative)
4. Empty Latent Image (1024x1024)
5. KSampler (Base: 25 steps, switch at step 20)
6. Load SDXL Refiner
7. KSampler (Refiner: 5 steps, denoise 0.4)
8. VAE Decode
9. Save Image
```

**Parameters:**
- Resolution: 1024x1024 (SDXL native)
- Base Steps: 20-25
- Refiner Steps: 5-10
- CFG: 7-8
- Sampler: dpmpp_2m_sde, dpmpp_3m_sde

### Template 3: ControlNet Pose-Guided Generation
**Use Case**: Generate images matching reference pose/composition

**Required Models:**
- Checkpoint: SD 1.5 or SDXL
- ControlNet: `controlnet/control_v11p_sd15_openpose.pth`
- Preprocessor: OpenPose detector

**Workflow Description:**
```
1. Load Image (Reference for pose)
2. OpenPose Preprocessor → Extract pose skeleton
3. Load Checkpoint
4. Apply ControlNet (strength 1.0)
5. CLIP Text Encode (Positive)
6. CLIP Text Encode (Negative)
7. KSampler (with ControlNet conditioning)
8. VAE Decode
9. Preview Image (pose skeleton)
10. Save Image (generated)
```

**Use Cases:**
- Portrait generation matching reference pose
- Character illustration with specific posture
- Product photography with consistent composition

### Template 4: Real Estate Image Enhancement
**Use Case**: Enhance property photos with AI upscaling and correction

**Required Models:**
- Upscaler: `upscale_models/RealESRGAN_x4plus.pth`
- Optional: `checkpoints/sd_v1.5_inpainting.safetensors` (for object removal)

**Workflow Description:**
```
1. Load Image (Property photo)
2. Upscale Image (RealESRGAN 4x)
3. Image Resize (to target resolution)
4. Color Correction (optional: exposure, vibrance)
5. Sharpen (subtle: 0.3-0.5 strength)
6. Save Image (High-res output)

Optional Enhancement Path:
7. Load Inpainting Model
8. Draw Mask (remove unwanted objects)
9. Inpaint (replace with AI-generated fill)
10. Save Enhanced Image
```

### Template 5: LoRA Style Mixing
**Use Case**: Apply multiple LoRA styles for custom aesthetics

**Required Models:**
- Base: Any SD 1.5 or SDXL checkpoint
- LoRAs: 2-4 from `loras/` directory

**Workflow Description:**
```
1. Load Checkpoint
2. Load LoRA #1 (strength 0.7)
3. Load LoRA #2 (strength 0.5)
4. Load LoRA #3 (strength 0.3)
5. CLIP Text Encode with LoRA triggers
6. KSampler
7. VAE Decode
8. Save Image
```

**Best Practices:**
- Stack 2-4 LoRAs maximum
- Reduce strengths for each additional LoRA
- Total combined strength ≤ 2.0
- Test combinations before batch processing

### Template 6: Background Removal & Replacement
**Use Case**: Isolate subjects and replace backgrounds

**Required Models:**
- Background Removal: RMBG or similar (custom node)
- Optional: SD Inpainting for new backgrounds

**Workflow Description:**
```
1. Load Image
2. Background Removal Node → Alpha mask
3. Save Image (Subject with transparency)

For Background Replacement:
4. Create Inverted Mask (background only)
5. Load Inpainting Model
6. CLIP Text Encode (new background description)
7. Inpaint Background
8. Composite Subject + New Background
9. Save Image
```

## Usage Examples

### Example 1: Generate Product Photography Workflow
```
User: Create a ComfyUI workflow for generating professional product photos on white backgrounds

Claude:
# Product Photography Workflow (SD 1.5 + ControlNet)

## Workflow Summary
Generates product photos with consistent lighting and clean white backgrounds using ControlNet depth guidance.

## Required Models
- `checkpoints/realisticVisionV51_v51VAE.safetensors` (photorealistic SD 1.5)
- `controlnet/control_v11f1p_sd15_depth.pth` (depth ControlNet)
- `vae/vae-ft-mse-840000-ema-pruned.safetensors`

## Node Configuration

**1. Load Image**
- Input: Reference product photo or 3D render

**2. Depth Preprocessor (MiDaS)**
- Generates depth map from input image
- Ensures consistent perspective

**3. Load Checkpoint**
- Model: realisticVisionV51_v51VAE.safetensors

**4. Apply ControlNet**
- ControlNet: control_v11f1p_sd15_depth.pth
- Strength: 0.9 (high adherence to depth)

**5. CLIP Text Encode (Positive)**
Prompt:
"professional product photography, [PRODUCT TYPE], studio lighting,
white background, commercial photo, high detail, 8k, sharp focus"

**6. CLIP Text Encode (Negative)**
Prompt:
"shadows, gradient background, cluttered, low quality, blurry,
distorted, watermark, text"

**7. Empty Latent Image**
- Width: 768
- Height: 768
- Batch: 4 (generate 4 variations)

**8. KSampler**
- Steps: 25
- CFG: 7.5
- Sampler: dpmpp_2m
- Scheduler: karras
- Denoise: 1.0

**9. VAE Decode**
- VAE: From checkpoint

**10. Save Image**
- Prefix: product_photo_
- Format: PNG (lossless)

## Expected Output
- 768x768px product images
- Clean white background
- Consistent lighting
- Professional studio quality
- 4 variations per generation

## Hardware Requirements
- VRAM: 6GB minimum
- Generation Time: ~30 seconds per batch (RTX 3060)

## JSON Export
[Would provide actual ComfyUI JSON workflow here]
```

### Example 2: Real Estate Virtual Staging
```
User: I need to virtually stage empty rooms. Create a workflow that keeps the room structure but adds furniture

Claude:
# Virtual Staging Workflow (ControlNet + Inpainting)

## Workflow Concept
Uses ControlNet depth/canny to preserve room geometry while inpainting furniture into empty spaces.

## Required Models
- `checkpoints/sd_v1.5_inpainting.safetensors`
- `controlnet/control_v11p_sd15_canny.pth` (edge preservation)
- `loras/interior_design_lora.safetensors` (if available)

## Workflow Steps

**1. Load Room Image**
- Input: Empty room photo

**2. Canny Edge Detector**
- Threshold Low: 100
- Threshold High: 200
- Preserves wall lines, windows, architectural features

**3. Create Mask**
- Use Image Editor or Mask Editor node
- Draw mask over areas to add furniture
- Example: Center of living room for sofa

**4. Load Inpainting Checkpoint**

**5. Apply ControlNet (Canny)**
- Strength: 0.7 (preserve architecture, allow furniture)

**6. CLIP Text Encode (Positive)**
"modern furnished living room, contemporary sofa, coffee table,
rug, professional interior design, realistic lighting, cohesive style,
[STYLE: modern/traditional/minimalist]"

**7. CLIP Text Encode (Negative)**
"empty room, distorted furniture, unrealistic perspective,
floating objects, mismatched colors"

**8. Inpaint KSampler**
- Steps: 30
- CFG: 8
- Denoise: 0.85 (high for adding new content)

**9. VAE Decode**

**10. Save Image**

## Tips for Best Results
- Keep original lighting in prompt ("natural window light", "warm evening light")
- Match existing style ("complement hardwood floors", "match wall color")
- Use lower denoise (0.6-0.7) for subtle additions
- Use higher denoise (0.8-0.95) for full room staging

## Batch Processing Option
Add "Batch Image Load" node to process multiple room photos with same furniture style.

## Output
- Realistically staged room photos
- Preserves original architecture
- Consistent with existing lighting
- Professional interior design quality
```

### Example 3: Face Restoration for Old Photos
```
User: Create workflow to restore and enhance old family photos with damaged faces

Claude:
# Face Restoration Workflow (CodeFormer + GFPGAN)

## Workflow Purpose
Restores and enhances facial details in old, damaged, or low-quality photos.

## Required Models
- `facerestore_models/GFPGANv1.4.pth` (face enhancement)
- `upscale_models/RealESRGAN_x4plus.pth` (general upscaling)
- Optional: `facerestore_models/codeformer.pth` (alternative face restorer)

## Workflow Configuration

**1. Load Image**
- Input: Old/damaged photo

**2. Face Detector**
- Model: RetinaFace or MediaPipe
- Detects all faces in image
- Returns bounding boxes and landmarks

**3. Upscale Image (4x)**
- Model: RealESRGAN_x4plus
- Upscales entire image first
- Provides more data for face restoration

**4. Face Restore (GFPGAN)**
- Strength: 0.8-1.0
- Applies to detected faces only
- Enhances facial features, skin texture

**5. Blend Original + Restored**
- Blend Factor: 0.7 (70% restored, 30% original)
- Preserves likeness while improving quality

**6. Color Correction (Optional)**
- Auto Levels
- Slight saturation boost
- Remove color cast from aging

**7. Sharpen**
- Strength: 0.4
- Enhances restored details

**8. Save Image**

## Alternative Path (CodeFormer)
If GFPGAN over-smooths faces:
- Use CodeFormer instead (Step 4)
- Adjust fidelity ratio: 0.5-0.9
- Lower = more face enhancement
- Higher = more fidelity to original

## Handling Multiple Faces
- Workflow automatically processes all detected faces
- Can set different restoration strengths per face
- Useful for group photos with varying damage

## Expected Results
- Clearer facial features
- Reduced noise and damage
- Enhanced skin texture
- Preserved facial likeness
- Improved overall image quality

## Limitations
- Severely damaged faces may not restore perfectly
- Very low resolution sources (<100px face) have limits
- Works best on frontal or 3/4 view faces
```

## Best Practices

### 1. Prompt Engineering
- **Positive prompts**: Specific, detailed descriptions
- **Negative prompts**: Common defects to avoid
- **LoRA triggers**: Use activation words when loading LoRAs
- **Weighting**: Use (emphasis:1.2) or [de-emphasis:0.8]

### 2. Sampling Parameters
- **Steps**: 20-30 for most cases, 40+ for fine detail
- **CFG Scale**: 7-9 for balance, <7 for creative freedom, >9 for strict prompt adherence
- **Denoise**: 1.0 for txt2img, 0.4-0.8 for img2img, 0.85+ for inpainting

### 3. Resolution Guidelines
- **SD 1.5**: Native 512x512, maximum 768x768 without upscaling
- **SDXL**: Native 1024x1024, can go to 1536x1536
- **Custom**: Maintain aspect ratio, use multiples of 64

### 4. VRAM Management
- Enable VAE tiling for large images
- Use model offloading for low VRAM
- Reduce batch size if OOM errors
- Clear cache between generations

### 5. Quality Control
- Generate multiple seeds (batch size 4-8)
- Use consistent seeds for A/B testing
- Save successful prompts and parameters
- Document model combinations that work well

## Troubleshooting

### Common Issues

**1. Out of Memory (OOM) Errors**
Solutions:
- Reduce image resolution
- Enable VAE tiling
- Lower batch size
- Use model offloading
- Close other GPU applications

**2. Poor Image Quality**
Causes:
- Too few sampling steps
- Wrong VAE or missing VAE
- CFG too high or too low
- Incompatible model + LoRA combination

Solutions:
- Increase steps to 30-40
- Add VAE node with correct model
- Adjust CFG to 7-9 range
- Test LoRAs individually

**3. Anatomy/Structure Problems**
Causes:
- Model limitations
- Conflicting LoRAs
- Poor prompt

Solutions:
- Use ControlNet for structure guidance
- Reduce LoRA strengths
- Add negative prompts for common issues
- Try different base models

**4. Style Not Matching**
Causes:
- LoRA not loaded correctly
- Missing trigger words
- LoRA strength too low

Solutions:
- Verify LoRA path and loading
- Check LoRA documentation for triggers
- Increase strength to 0.8-1.0

**5. Workflow Won't Run**
Causes:
- Missing custom nodes
- Incorrect model paths
- Node connection errors

Solutions:
- Install required custom nodes
- Verify model files exist in AI MODELS directory
- Check all node connections in UI

## Integration with SnoopLabs Projects

### RapidRAW Integration
Export edited RAW images to ComfyUI for:
- AI-based noise reduction (better than traditional)
- Super-resolution upscaling beyond lens limits
- Creative style transfer
- Background replacement
- Object removal

**Workflow**: RapidRAW → Export TIFF → ComfyUI → Enhanced Output

### AgentLabs AI Toolkit
Generate real estate imagery:
- Virtual staging workflows
- Property photo enhancement
- Marketing material creation
- Presentation visuals

### AI MODELS Directory Reference
Workflow builder automatically checks:
- `C:\SnoopLabs\AI MODELS\checkpoints\` for base models
- `C:\SnoopLabs\AI MODELS\loras\` for style models
- `C:\SnoopLabs\AI MODELS\controlnet\` for control models
- Other subdirectories for specialized models

## Advanced Features

### Batch Processing Setup
```
1. Load Image Batch (folder input)
2. [Standard workflow nodes]
3. Save Image Batch (output folder)
4. Add filename prefix/suffix
5. Preserve metadata
```

### Conditional Workflows
Use Switch nodes to:
- Select model based on image type
- Apply different LoRAs per category
- Adjust parameters per input
- Route to different processors

### API Integration
Generate workflows that can be:
- Called from Python scripts
- Integrated into web applications
- Automated with file watchers
- Scheduled for batch jobs

## JSON Workflow Format

ComfyUI workflows are JSON with this structure:
```json
{
  "1": {
    "class_type": "CheckpointLoaderSimple",
    "inputs": {
      "ckpt_name": "v1-5-pruned-emaonly.safetensors"
    }
  },
  "2": {
    "class_type": "CLIPTextEncode",
    "inputs": {
      "text": "positive prompt",
      "clip": ["1", 1]
    }
  }
  // ... more nodes
}
```

This skill can generate complete JSON workflows on request.

## Resources & Documentation

### Model Sources
- **Checkpoints**: Civitai, HuggingFace
- **LoRAs**: Civitai, LoRA library
- **ControlNet**: lllyasviel GitHub
- **Upscalers**: ESRGAN, RealESRGAN official

### Custom Nodes
- ComfyUI Manager (install custom nodes easily)
- ControlNet Preprocessors
- WAS Node Suite
- Impact Pack
- Ultimate SD Upscale

### Learning Resources
- ComfyUI Examples Wiki
- Workflow sharing communities
- Model documentation on Civitai
- YouTube tutorials

## Version History

- v1.0 (2025-01) - Initial release
- Optimized for SnoopLabs AI MODELS directory structure
- Templates for real estate, portrait, and product workflows
- Integration guides for RapidRAW and AgentLabs
