# Style Transfer Guide for Nano Banana Pro

Master the art of transferring visual styles from reference images to new creations.

## How Style Transfer Works

Nano Banana Pro can analyze reference images and apply their visual characteristics to new subjects. The API accepts up to 14 reference images alongside your prompt.

## The Style Transfer Process

### Step 1: Analyze the Reference

Before generating, carefully examine the reference image for:

**Color Analysis**
- Dominant colors (list 3-5 main colors)
- Color temperature (warm/cool/neutral)
- Saturation level (vibrant/muted/desaturated)
- Color harmony type (complementary, analogous, triadic)

**Technique Analysis**
- Medium (photography, digital art, painting, 3D, etc.)
- Texture (smooth, brushed, grainy, clean)
- Edge quality (sharp, soft, blurred, stylized)
- Detail level (minimal, moderate, intricate)

**Lighting Analysis**
- Light direction (front, side, back, overhead)
- Light quality (hard, soft, diffused, dramatic)
- Shadows (deep, subtle, colored, absent)
- Highlights (specular, soft glow, rim lighting)

**Composition Analysis**
- Framing style
- Depth treatment
- Focal point handling
- Negative space usage

**Mood Analysis**
- Emotional tone
- Energy level (calm, dynamic, intense)
- Atmosphere (ethereal, grounded, surreal)

### Step 2: Document Style Markers

Create a style profile from your analysis:

```
STYLE PROFILE:
- Art Style: [e.g., watercolor illustration]
- Color Palette: [e.g., soft pastels - dusty pink, sage green, cream]
- Technique: [e.g., visible brushstrokes, soft edges, paper texture]
- Lighting: [e.g., diffused ambient, no harsh shadows]
- Mood: [e.g., dreamy, nostalgic, gentle]
- Distinctive Features: [e.g., organic imperfections, color bleeding]
```

### Step 3: Construct the Prompt

Use this structure for style transfer prompts:

```
Create [new subject with details] in the exact artistic style of the reference image.

Subject Description:
[Detailed description of what you want to create]

Style Preservation Directives:
- Maintain color palette: [extracted colors]
- Preserve technique: [identified technique]
- Match lighting quality: [lighting characteristics]
- Keep atmospheric mood: [mood description]
- Replicate [any distinctive style features]

Ensure complete visual consistency with the reference aesthetic while featuring the new subject matter.
```

### Step 4: Execute with Reference

```bash
python3 generate.py "Your style transfer prompt" --reference /path/to/reference.png
```

## Example Style Transfers

### Example 1: Watercolor Style

**Reference:** Soft watercolor landscape painting

**Style Profile:**
- Art Style: Traditional watercolor
- Colors: Soft blues, greens, warm yellows
- Technique: Wet-on-wet, visible brush strokes, color bleeding
- Lighting: Diffused natural light
- Mood: Serene, contemplative

**Prompt for New Subject (coffee shop logo):**
```
Create a coffee shop logo in the exact artistic style of the reference image.

Subject: Elegant coffee cup with curling steam, coffee bean accent,
warm inviting cafe atmosphere suggested through composition.

Style Preservation:
- Maintain watercolor technique with visible brushstrokes
- Preserve soft, bleeding color transitions
- Match muted, warm color palette with soft blues and creams
- Keep the dreamy, hand-painted quality
- Replicate organic imperfections and paper texture effect

The logo should feel hand-crafted and artisanal while maintaining the
serene, contemplative mood of the reference.
```

### Example 2: Neon Cyberpunk

**Reference:** Cyberpunk city scene with neon lights

**Style Profile:**
- Art Style: Digital art / concept art
- Colors: Deep blacks, electric cyan, hot pink, purple
- Technique: Clean digital rendering, glow effects
- Lighting: Neon sources, wet reflections, fog
- Mood: Futuristic, moody, high-tech

**Prompt for New Subject (music app icon):**
```
Create a music app icon in the exact artistic style of the reference image.

Subject: Stylized headphones with sound wave visualization,
abstract musical elements suggesting rhythm and energy.

Style Preservation:
- Match neon color palette: electric cyan, hot pink, deep purple
- Preserve the dark background with bright glowing accents
- Replicate wet/reflective surface quality
- Maintain atmospheric fog/haze effects
- Keep the cyberpunk futuristic aesthetic

The icon should capture the high-tech, moody atmosphere of the reference
while clearly representing music/audio functionality.
```

### Example 3: Minimalist Japanese

**Reference:** Minimalist Japanese ink drawing

**Style Profile:**
- Art Style: Sumi-e / Japanese ink wash
- Colors: Black ink on white/cream, minimal color
- Technique: Brush strokes, negative space, suggestion over detail
- Lighting: Flat, no cast shadows
- Mood: Zen, contemplative, elegant simplicity

**Prompt for New Subject (meditation app icon):**
```
Create a meditation app icon in the exact artistic style of the reference image.

Subject: Simple seated figure in meditation pose,
subtle lotus flower suggestion, breath or energy visualization.

Style Preservation:
- Maintain traditional Japanese ink brush technique
- Preserve generous negative space and minimal elements
- Match monochromatic palette with possible single accent
- Keep the flat, shadow-free treatment
- Replicate the "suggestion over description" approach

The icon should embody Zen aesthetic and contemplative stillness
while clearly communicating meditation/mindfulness purpose.
```

## Using Multiple References

You can provide up to 14 reference images to capture complex styles:

```bash
python3 generate.py "prompt" \
  --reference style1.png style2.png style3.png
```

**Best uses for multiple references:**
- Combining style elements from different sources
- Showing style consistency across different subjects
- Providing more examples of a unique style
- Capturing both color palette and technique separately

## Tips for Better Style Transfer

### DO
- Use high-quality reference images
- Choose references with distinctive, clear styles
- Be explicit about which elements to preserve
- Describe the new subject in detail
- Include both style AND subject in your prompt

### DON'T
- Use low-resolution or unclear references
- Expect photorealistic results from painterly references
- Skip the analysis step
- Be vague about preservation priorities
- Contradict the reference style in your prompt

## Troubleshooting

**Style not matching well:**
- Add more specific preservation directives
- Use multiple references of the same style
- Be more explicit about the distinctive features

**Subject unclear:**
- Increase detail in subject description
- Simplify the subject if style is complex
- Adjust balance between style and subject emphasis

**Colors not matching:**
- Explicitly list the exact colors to use
- Reference specific color relationships
- Mention color temperature and saturation levels

## Style Categories

Common style types and their key markers:

| Style | Key Markers to Preserve |
|-------|------------------------|
| Watercolor | Bleeding edges, paper texture, soft washes |
| Oil Painting | Impasto texture, rich colors, visible strokes |
| Digital Art | Clean lines, gradient smoothness, glow effects |
| Photography | Lighting quality, depth of field, color grading |
| Flat Design | Solid colors, no gradients, geometric shapes |
| 3D Render | Material quality, lighting setup, perspective |
| Sketch | Line quality, shading technique, paper texture |
| Retro/Vintage | Color palette, grain, period-specific elements |
