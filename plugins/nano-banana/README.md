# Nano Banana Pro

AI image generation plugin for Claude Code using **Nano Banana Pro** (Gemini 3 Pro Image).

## Features

- **Smart Prompt Generation** - Automatically transforms simple requests into optimized prompts
- **Style Transfer** - Generate images matching the style of reference images
- **Context-Aware** - Understands your project context to create appropriate visuals
- **Multiple Providers** - Works with Google API or OpenRouter API
- **Multiple Formats** - Support for various aspect ratios and resolutions
- **Flexible Configuration** - Per-project settings file or global environment variables

## Setup

### 1. Install Dependencies

```bash
# For Google API (recommended)
pip install google-genai Pillow

# For OpenRouter API
pip install openai Pillow
```

### 2. Configure API (Choose One Method)

#### Method 1: Interactive Setup (Recommended)

Run the setup command in Claude Code:

```
/nano-banana:setup
```

This will guide you through choosing a provider and entering your API key.

#### Method 2: Project Settings File

Create `.claude/nano-banana.local.md` in your project:

```markdown
---
provider: openrouter
api_key: "sk-or-v1-your-api-key-here"
---

# Nano Banana Pro Settings
```

**For Google API:**
```markdown
---
provider: google
api_key: "your-gemini-api-key-here"
---
```

> **Note:** Add `.claude/*.local.md` to your `.gitignore` to avoid committing API keys.

#### Method 3: Environment Variables

Add to `~/.zshrc` or `~/.bashrc`:

**For Google API (Recommended):**
```bash
export GEMINI_API_KEY="your-key-here"
export NANO_BANANA_PROVIDER="google"
```

**For OpenRouter API:**
```bash
export OPENROUTER_API_KEY="your-key-here"
export NANO_BANANA_PROVIDER="openrouter"
```

Then run: `source ~/.zshrc`

### Configuration Priority

Settings are loaded in this order (first found wins):
1. `.claude/nano-banana.local.md` (project-specific)
2. Environment variables (global)

### Get API Keys

- **Google AI Studio:** https://aistudio.google.com → Get API Key → Create API Key (Free tier available)
- **OpenRouter:** https://openrouter.ai → Keys → Create Key

## Usage

### Slash Commands

```
/nano-banana:setup                                    # Configure API settings
/generate-image "app icon for fitness tracker"
/generate-image "website hero banner" aspect=16:9 resolution=4K
/style-transfer reference=/path/to/style.png subject="company logo"
/nano-banana:help
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
│   ├── setup.md              # NEW: Interactive setup command
│   └── help.md
├── skills/
│   └── image-generation/
│       ├── SKILL.md
│       └── references/
│           ├── prompt-guide.md
│           ├── prompt-templates.md
│           └── style-transfer.md
├── scripts/
│   └── generate.py           # Supports .local.md settings
├── README.md
└── requirements.txt

# Per-project settings (not in git)
.claude/
└── nano-banana.local.md      # API provider and key
```

## License

MIT

---

Made with love by [42apps](mailto:hello@42apps.ai)
