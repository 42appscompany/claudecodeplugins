---
name: setup
description: Configure Nano Banana Pro API settings (provider and API key) interactively
allowed-tools: ["Read", "Write", "Bash", "AskUserQuestion"]
---

# Setup Nano Banana Pro

Configure the API provider and key for image generation.

## Steps

1. **Check current configuration**

   First, check if `.claude/nano-banana.local.md` exists:
   - If exists, read and show current settings
   - If not, inform user that no settings are configured

2. **Ask for provider**

   Use AskUserQuestion to ask which provider to use:

   ```
   Question: "Which API provider do you want to use for image generation?"
   Options:
   - "Google AI Studio (Recommended)" - Best image generation, native support for all features. Free tier available.
   - "OpenRouter" - Alternative provider with unified API. Supports multiple models.
   ```

3. **Ask for API key**

   Based on the provider chosen, ask for the API key:

   For Google:
   ```
   Question: "Enter your Google AI Studio API key"
   Description: "Get your free API key at https://aistudio.google.com → Get API Key → Create API Key"
   ```

   For OpenRouter:
   ```
   Question: "Enter your OpenRouter API key"
   Description: "Get your API key at https://openrouter.ai → Keys → Create Key"
   ```

4. **Create settings file**

   Create `.claude/` directory if it doesn't exist, then create `.claude/nano-banana.local.md`:

   ```markdown
   ---
   provider: {google|openrouter}
   api_key: "{user's api key}"
   ---

   # Nano Banana Pro Settings

   Configured on {current date}.
   Provider: {provider name}

   To change settings, edit this file or run `/nano-banana:setup` again.
   ```

5. **Add to .gitignore**

   Check if `.gitignore` exists and contains `.claude/*.local.md`:
   - If `.gitignore` doesn't exist or doesn't contain the pattern, add it
   - This prevents accidentally committing API keys

6. **Confirm setup**

   Tell the user:
   - Settings saved to `.claude/nano-banana.local.md`
   - API key will not be committed to git
   - They can now use `/generate-image` command

## Important Notes

- Never show the full API key in output (mask it like `sk-or-...xxx`)
- The settings file has priority over environment variables
- If user already has environment variables set, inform them that the settings file will take priority
