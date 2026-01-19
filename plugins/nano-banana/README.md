# Nano Banana Pro

AI image generation plugin for Claude Code using **Nano Banana Pro** (Gemini 3 Pro Image).

## Features

- **Smart Prompt Generation** - Automatically transforms simple requests into optimized prompts
- **Style Transfer** - Generate images matching the style of reference images
- **Context-Aware** - Understands your project context to create appropriate visuals
- **Multiple Providers** - Works with Google API or OpenRouter API
- **Multiple Formats** - Support for various aspect ratios and resolutions

## Setup

### 1. Install Dependencies

```bash
# For Google API (recommended)
pip install google-genai Pillow

# For OpenRouter API
pip install openai Pillow
```

### 2. Choose and Configure Provider

#### Option A: Google API (Recommended)

Best for full image generation features.

1. Go to https://aistudio.google.com
2. Sign in with your Google account
3. Click "Get API Key" -> "Create API Key"
4. Add to `~/.zshrc` or `~/.bashrc`:

```bash
export GEMINI_API_KEY="your-key-here"
export NANO_BANANA_PROVIDER="google"
```

#### Option B: OpenRouter API

Alternative unified API provider.

1. Go to https://openrouter.ai
2. Sign in and go to Keys section
3. Create a new API key
4. Add to `~/.zshrc` or `~/.bashrc`:

```bash
export OPENROUTER_API_KEY="your-key-here"
export NANO_BANANA_PROVIDER="openrouter"
```

### 3. Apply Configuration

```bash
source ~/.zshrc
```

## Usage

### Slash Commands

```
/generate-image "app icon for fitness tracker"
/generate-image "website hero banner" aspect=16:9 resolution=4K
/style-transfer reference=/path/to/style.png subject="company logo"
/nano-banana-help
```

### Natural Language

Just describe what you want:
- "Create an image of a sunset over mountains"
- "Make me an app icon for a todo list"
- "Generate a banner for my website, 16:9"
- "Create something in the style of that image"

### CLI Usage

```bash
# Basic generation
python3 scripts/generate.py "A serene mountain landscape"

# With options
python3 scripts/generate.py "Website hero" --aspect-ratio 16:9 --resolution 4K

# Style transfer
python3 scripts/generate.py "Logo" --reference style.png

# Specify provider
python3 scripts/generate.py "Image" --provider openrouter
```

## Provider Comparison

| Feature | Google API | OpenRouter |
|---------|------------|------------|
| Image Generation | Full support | Limited |
| Style Transfer | Up to 14 refs | Limited |
| Aspect Ratios | Native support | Via prompt hints |
| Resolution Control | 1K/2K/4K | Via prompt hints |
| Free Tier | Yes | Yes (limited) |

**Recommendation:** Use Google API for best image generation results.

## Options

### Aspect Ratios

| Ratio | Best For |
|-------|----------|
| 1:1 | App icons, social media posts |
| 16:9 | Website headers, presentations |
| 9:16 | Mobile screens, stories |
| 4:3 | Photos, UI mockups |
| 3:2 | Photography |
| 21:9 | Cinematic banners |

### Resolutions

| Size | Use Case |
|------|----------|
| 1K | Quick drafts, smaller files |
| 2K | Balanced quality (default) |
| 4K | Maximum quality |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `NANO_BANANA_PROVIDER` | Provider: `google` (default) or `openrouter` |
| `GEMINI_API_KEY` | API key for Google provider |
| `OPENROUTER_API_KEY` | API key for OpenRouter provider |

## Style Transfer

Provide a reference image and describe what you want in that style:

```
/style-transfer reference=./my-style.png subject="logo for coffee shop"
```

Works best with:
- Distinctive art styles
- High-quality reference images
- Up to 14 reference images (Google API)

## Troubleshooting

### "API_KEY not set"
Add the appropriate key to your shell profile and restart terminal.

### "Package not installed"
```bash
pip install google-genai Pillow   # for Google
pip install openai Pillow         # for OpenRouter
```

### "No image generated"
- Prompt may have triggered safety filters - try rephrasing
- Check API quota
- Try switching providers

## Plugin Structure

```
nano-banana/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── generate-image.md
│   ├── style-transfer.md
│   └── help.md
├── skills/
│   └── image-generation/
│       ├── SKILL.md
│       └── references/
│           ├── prompt-guide.md
│           ├── prompt-templates.md
│           └── style-transfer.md
├── scripts/
│   └── generate.py
├── README.md
└── requirements.txt
```

## License

MIT

---

Made with love by [42apps](mailto:hello@42apps.ai)
