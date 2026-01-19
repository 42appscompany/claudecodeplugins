---
name: nano-banana-help
description: Show help and usage information for Nano Banana Pro image generation
---

# Nano Banana Pro - Help

Display comprehensive help information for the Nano Banana Pro image generation plugin.

## Response

Provide the following help information:

---

## Nano Banana Pro Image Generator

Generate high-quality AI images using Nano Banana Pro (Gemini 3 Pro Image).

### Commands

| Command | Description |
|---------|-------------|
| `/generate-image <description>` | Generate an image from a description |
| `/style-transfer <reference> <subject>` | Create image in the style of a reference |
| `/nano-banana-help` | Show this help |

### Quick Examples

```
/generate-image "modern app icon for meditation app"

/generate-image "website hero for AI startup" aspect=16:9 resolution=4K

/style-transfer reference=/path/to/style.png subject="company logo"
```

### Natural Language

You can also just describe what you want naturally:
- "Create an image of a sunset over mountains"
- "Make me an app icon for a todo list app"
- "Generate a banner for my website, 16:9"
- "Create something in the style of that image I showed you"

### Supported Options

**Providers:**
- `google` - Google AI Studio API (recommended, full features)
- `openrouter` - OpenRouter API (alternative)

**Aspect Ratios:**
- `1:1` - Square (app icons, profile pictures)
- `16:9` - Widescreen (website headers, presentations)
- `9:16` - Vertical (mobile screens, stories)
- `4:3` - Classic (photos, UI mockups)
- `3:2` - Photo standard
- `21:9` - Ultra-wide (cinematic banners)

**Resolutions:**
- `1K` - Fast generation, smaller file
- `2K` - Balanced quality (default)
- `4K` - Maximum quality, larger file

### Provider Setup

The plugin supports two API providers:

**Google API (Recommended)**
```bash
export GEMINI_API_KEY="your-key-here"
export NANO_BANANA_PROVIDER="google"
```
Get key at: https://aistudio.google.com

**OpenRouter API**
```bash
export OPENROUTER_API_KEY="your-key-here"
export NANO_BANANA_PROVIDER="openrouter"
```
Get key at: https://openrouter.ai

### Provider Comparison

| Feature | Google | OpenRouter |
|---------|--------|------------|
| Image Gen | Full | Limited |
| Style Transfer | 14 refs | Limited |
| Aspect Ratio | Native | Prompt hints |
| Resolution | 1K-4K | Prompt hints |

### Style Transfer Tips

1. Use clear, high-quality reference images
2. Works best with distinctive art styles
3. Can use up to 14 reference images (Google API)
4. Combine multiple references for complex styles

### Dependencies

```bash
# For Google API
pip install google-genai Pillow

# For OpenRouter API
pip install openai Pillow
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `NANO_BANANA_PROVIDER` | `google` (default) or `openrouter` |
| `GEMINI_API_KEY` | Key for Google provider |
| `OPENROUTER_API_KEY` | Key for OpenRouter provider |

### Troubleshooting

**"API_KEY not set"**
- Add the key to your ~/.zshrc and run `source ~/.zshrc`

**"Package not installed"**
- Run: `pip install google-genai Pillow` or `pip install openai Pillow`

**"Image not generated"**
- The prompt may have triggered safety filters
- Try rephrasing the request
- Check API quota
- Try switching providers

---

Need more help? Check the [prompt guide](${CLAUDE_PLUGIN_ROOT}/skills/image-generation/references/prompt-guide.md) for detailed prompting tips.
