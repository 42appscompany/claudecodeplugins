---
name: style-transfer
description: Generate an image in the style of a reference image. Provide a reference image and describe what you want.
arguments:
  - name: reference
    description: Path to the reference image to match the style of
    required: true
  - name: subject
    description: What to create in the reference style (e.g., "a logo for coffee shop", "portrait of a cat")
    required: true
  - name: aspect
    description: Aspect ratio (1:1, 16:9, 9:16, 4:3, 3:2)
    required: false
  - name: resolution
    description: Resolution (1K, 2K, 4K)
    required: false
---

# Style Transfer with Nano Banana Pro

You are performing style transfer using Nano Banana Pro (Gemini 3 Pro Image).

## User Request
**Reference Image:** $ARGUMENTS.reference
**New Subject:** $ARGUMENTS.subject
**Aspect Ratio:** ${ARGUMENTS.aspect:-1:1}
**Resolution:** ${ARGUMENTS.resolution:-2K}

## Your Task

1. **Analyze the Reference Image**
   First, read and analyze the reference image to understand its style:
   - Color palette (dominant colors, temperature, saturation)
   - Artistic technique (photography, illustration, painting, 3D, etc.)
   - Lighting characteristics (direction, quality, mood)
   - Texture and detail level
   - Composition patterns
   - Overall aesthetic and mood

2. **Extract Style Markers**
   Document the key style elements:
   - Art style/genre
   - Color scheme description
   - Lighting type
   - Edge treatment (sharp/soft)
   - Surface quality
   - Any distinctive stylistic features

3. **Construct Style-Matched Prompt**
   Create a prompt that:
   - Describes the new subject clearly
   - Includes explicit preservation directives
   - References the extracted style markers

   Example structure:
   ```
   Create [new subject] in the exact artistic style of the reference image.

   Subject: [detailed description of new subject]

   Style preservation:
   - Match color palette: [extracted colors]
   - Match technique: [identified style]
   - Match lighting: [lighting characteristics]
   - Match atmosphere: [mood and ambiance]
   - Maintain visual consistency with the reference aesthetic
   ```

4. **Execute Generation with Reference**
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/generate.py" "YOUR_STYLE_TRANSFER_PROMPT" \
     --reference "$ARGUMENTS.reference" \
     --aspect-ratio "${ARGUMENTS.aspect:-1:1}" \
     --resolution "${ARGUMENTS.resolution:-2K}"
   ```

5. **Present and Compare**
   - Show the generated image
   - Explain how the style was transferred
   - Note which elements were preserved
   - Offer refinements if needed

## Example

**Reference:** A watercolor painting with soft pastels and dreamy blur

**Subject:** "a logo for coffee shop"

**Generated Prompt:**
```
Create a coffee shop logo in the exact artistic style of the reference image.

Subject: Elegant coffee cup with rising steam forming a subtle heart shape,
stylized coffee bean motif, warm inviting cafe aesthetic.

Style preservation:
- Match color palette: soft pastels with warm cream, dusty rose, and sage green
- Match technique: watercolor with visible brush strokes and soft edges
- Match lighting: diffused, dreamy ambient light
- Match atmosphere: romantic, nostalgic, handcrafted feeling
- Maintain the gentle blur and organic imperfections of the reference
```

## Tips for Better Results

- Provide high-quality reference images
- Be specific about which style elements matter most
- The more distinctive the reference style, the better the transfer
- You can use multiple reference images (up to 14) for complex styles
