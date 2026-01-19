---
name: generate-image
description: Generate an AI image with Nano Banana Pro. Provide a description and Claude will create an optimized prompt.
arguments:
  - name: description
    description: What image to generate (e.g., "app icon for fitness tracker", "hero banner for tech startup")
    required: true
  - name: aspect
    description: Aspect ratio (1:1, 16:9, 9:16, 4:3, 3:2)
    required: false
  - name: resolution
    description: Resolution (1K, 2K, 4K)
    required: false
---

# Generate Image with Nano Banana Pro

You are generating an image using Nano Banana Pro (Gemini 3 Pro Image).

## User Request
**Description:** $ARGUMENTS.description
**Aspect Ratio:** ${ARGUMENTS.aspect:-1:1}
**Resolution:** ${ARGUMENTS.resolution:-2K}

## Your Task

1. **Analyze the Request**
   - Understand what type of image is needed
   - Consider the likely use case
   - Determine appropriate style

2. **Generate Optimized Prompt**
   Transform the user's simple description into a detailed, professional prompt following this structure:
   - Style (photography, 3D, illustration, etc.)
   - Subject with descriptive details
   - Composition and framing
   - Lighting setup
   - Color palette and atmosphere
   - Technical quality markers

3. **Execute Generation**
   Run the generation script:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/generate.py" "YOUR_OPTIMIZED_PROMPT" \
     --aspect-ratio "${ARGUMENTS.aspect:-1:1}" \
     --resolution "${ARGUMENTS.resolution:-2K}"
   ```

4. **Present Result**
   - Show the generated image
   - Explain what was created
   - Offer to refine if needed

## Example Transformation

**Input:** "app icon for fitness tracker"

**Optimized Prompt:**
"Modern 3D app icon design, stylized running figure silhouette emerging from circular gradient,
dynamic motion lines suggesting speed and energy, vibrant gradient from electric orange to magenta,
centered composition within rounded superellipse container, soft studio lighting with rim highlights,
health and fitness aesthetic, clean vector-like quality with subtle depth"

Remember: Write prompts like a Creative Director, not as keyword lists. Describe the intent and vision clearly.
