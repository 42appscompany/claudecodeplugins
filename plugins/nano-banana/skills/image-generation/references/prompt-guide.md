# Nano Banana Pro Prompting Guide

## Core Philosophy

Write prompts like a **Creative Director**, not a search engine. Describe your vision with intent and purpose, not as a list of disconnected keywords.

## The Prompt Formula

```
[STYLE] + [SUBJECT] + [COMPOSITION] + [LIGHTING] + [ATMOSPHERE] + [TECHNICAL]
```

### Style
Define the artistic approach:
- Photography: "cinematic photography", "product photography", "street photography"
- 3D: "3D render", "isometric 3D", "low-poly 3D"
- Illustration: "digital illustration", "watercolor", "vector art"
- Design: "flat design", "neumorphic", "glassmorphism"

### Subject
Describe what's in the image with specifics:
- Use descriptive adjectives
- Include relevant details
- Be specific about materials, textures, colors

### Composition
Guide the framing:
- Camera angle: "eye level", "bird's eye view", "worm's eye view"
- Lens simulation: "85mm portrait lens", "wide angle 24mm", "macro close-up"
- Framing: "rule of thirds", "centered composition", "asymmetric balance"
- Depth: "shallow depth of field", "deep focus", "tilt-shift"

### Lighting
Set the mood through light:
- Setup: "three-point lighting", "Rembrandt lighting", "split lighting"
- Quality: "soft diffused light", "hard dramatic shadows", "rim lighting"
- Source: "golden hour sunlight", "overcast ambient", "neon glow"
- Color: "warm tungsten", "cool daylight", "colored gel lighting"

### Atmosphere
Define the emotional quality:
- Mood: "serene", "energetic", "mysterious", "nostalgic"
- Color palette: describe specific colors
- Ambiance: "misty", "clear", "dusty", "ethereal"

### Technical
Quality markers:
- "photorealistic", "hyper-detailed", "studio quality"
- "8K resolution", "RAW photograph quality"
- "octane render", "unreal engine quality"

## Good vs Bad Prompts

### Bad (Tag Soup)
```
cat, cute, fluffy, 4k, beautiful, amazing, trending, artstation, detailed
```

### Good (Creative Direction)
```
Elegant Persian cat lounging on velvet cushion, soft cream-colored fur catching
afternoon window light, shallow depth of field with 85mm f/1.4 bokeh effect,
warm golden tones with hints of burgundy from the fabric, intimate portrait
composition, peaceful domestic atmosphere, studio photography quality
```

## Prompts by Use Case

### App Icons
```
Modern 3D app icon design, [main visual element] rendered with soft shadows,
[primary color] to [secondary color] gradient background, rounded superellipse
container, centered composition, subtle ambient occlusion, clean iOS aesthetic
```

### Website Headers
```
[Style] hero image, [main subject] with [action/state], wide 16:9 composition,
[position] focal point leaving space for text overlay, [lighting description],
[color palette] color scheme, professional web design aesthetic
```

### Product Photography
```
Professional product shot of [product], floating against [background color]
infinity backdrop, three-point studio lighting with soft key light,
subtle reflection on surface, commercial photography quality, clean minimal
composition
```

### Social Media
```
Eye-catching [style] for social media, [engaging subject], square 1:1
composition optimized for feeds, vibrant [colors] that pop on mobile screens,
[mood] atmosphere, scroll-stopping visual impact
```

### Marketing Materials
```
Commercial [photography/illustration] of [product/concept], [action or context],
professional lighting with [specific setup], [brand colors] color palette,
space for copy on [left/right/top], persuasive marketing aesthetic
```

## Technical Specifications

### Camera/Lens References
- Portrait: "85mm f/1.4", "135mm f/2"
- Wide: "24mm f/2.8", "16mm ultra-wide"
- Macro: "100mm macro lens"
- Cinematic: "anamorphic lens flare", "35mm film grain"

### Lighting Setups
- Product: "three-point lighting with soft boxes"
- Portrait: "butterfly lighting", "loop lighting"
- Dramatic: "chiaroscuro", "single hard light source"
- Natural: "golden hour", "blue hour", "overcast soft light"

### Render Quality
- Photorealistic: "photorealistic render", "hyperrealistic"
- 3D specific: "octane render", "redshift", "unreal engine 5"
- Traditional: "oil painting texture", "watercolor wash"

## Style Transfer Tips

When matching a reference image style:

1. **Analyze the reference first**
   - What colors dominate?
   - What's the artistic technique?
   - How is light handled?
   - What's the overall mood?

2. **Use preservation directives**
   ```
   Maintain exact style consistency with reference:
   - Preserve color palette: [specific colors from reference]
   - Preserve technique: [identified style]
   - Preserve lighting: [lighting characteristics]
   - Preserve mood: [emotional quality]
   ```

3. **Be specific about what to keep**
   ```
   Keep all visual elements consistent with reference while changing only the subject matter
   ```

## Common Mistakes to Avoid

1. **Too vague**: "beautiful landscape" → Be specific about type, time, mood
2. **Contradictory**: "bright dark moody cheerful" → Pick one direction
3. **Overloaded**: Too many competing elements → Focus on key aspects
4. **Keyword spam**: Random trending terms → Write coherent descriptions
5. **Missing context**: No purpose stated → Include use case when relevant

## Aspect Ratio Selection

| Ratio | Best For |
|-------|----------|
| 1:1 | App icons, profile pictures, Instagram posts |
| 16:9 | Website headers, presentations, YouTube thumbnails |
| 9:16 | Mobile screens, Instagram/TikTok stories |
| 4:3 | Photos, UI mockups, traditional displays |
| 3:2 | Photography standard, print materials |
| 21:9 | Cinematic banners, ultra-wide displays |
