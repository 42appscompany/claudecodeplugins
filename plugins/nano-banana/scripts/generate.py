#!/usr/bin/env python3
"""
Nano Banana Pro Image Generator CLI
Generates images using Gemini 3 Pro Image via Google API or OpenRouter.

Supports two providers:
- google: Direct Google AI Studio API (requires GEMINI_API_KEY)
- openrouter: OpenRouter API (requires OPENROUTER_API_KEY)

Set NANO_BANANA_PROVIDER environment variable to choose (default: google)
"""

import argparse
import base64
import io
import os
import sys
from datetime import datetime
from pathlib import Path

# Provider constants
PROVIDER_GOOGLE = "google"
PROVIDER_OPENROUTER = "openrouter"
DEFAULT_PROVIDER = PROVIDER_GOOGLE

# Model names
GOOGLE_MODEL = "gemini-3-pro-image-preview"
OPENROUTER_MODEL = "google/gemini-3-pro-image-preview"  # Paid model with native image generation

VALID_ASPECT_RATIOS = ["1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3", "21:9"]
VALID_RESOLUTIONS = ["1K", "2K", "4K"]

# OpenRouter API URL
OPENROUTER_API_URL = "https://openrouter.ai/api/v1"


def get_provider() -> str:
    """Get the configured provider."""
    provider = os.environ.get("NANO_BANANA_PROVIDER", DEFAULT_PROVIDER).lower()
    if provider not in [PROVIDER_GOOGLE, PROVIDER_OPENROUTER]:
        print(f"Warning: Unknown provider '{provider}'. Using '{DEFAULT_PROVIDER}'.")
        return DEFAULT_PROVIDER
    return provider


def get_google_api_key() -> str:
    """Get Gemini API key from environment."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("\nTo get an API key:")
        print("1. Go to https://aistudio.google.com")
        print("2. Sign in with your Google account")
        print("3. Click 'Get API Key' → 'Create API Key'")
        print("4. Add to ~/.zshrc or ~/.bashrc:")
        print('   export GEMINI_API_KEY="your-key-here"')
        print("5. Restart terminal or run: source ~/.zshrc")
        sys.exit(1)
    return api_key


def get_openrouter_api_key() -> str:
    """Get OpenRouter API key from environment."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.")
        print("\nTo get an API key:")
        print("1. Go to https://openrouter.ai")
        print("2. Sign in and go to Keys section")
        print("3. Create a new API key")
        print("4. Add to ~/.zshrc or ~/.bashrc:")
        print('   export OPENROUTER_API_KEY="your-key-here"')
        print("5. Restart terminal or run: source ~/.zshrc")
        sys.exit(1)
    return api_key


def load_image_as_base64(path: str) -> tuple[str, str]:
    """Load image and return as base64 with media type."""
    from PIL import Image

    img = Image.open(path)

    # Determine format
    format_map = {
        "JPEG": ("image/jpeg", "jpeg"),
        "JPG": ("image/jpeg", "jpeg"),
        "PNG": ("image/png", "png"),
        "GIF": ("image/gif", "gif"),
        "WEBP": ("image/webp", "webp"),
    }

    img_format = img.format or "PNG"
    media_type, ext = format_map.get(img_format.upper(), ("image/png", "png"))

    # Convert to bytes
    buffer = io.BytesIO()
    img.save(buffer, format=ext.upper())
    img_bytes = buffer.getvalue()

    return base64.b64encode(img_bytes).decode("utf-8"), media_type


def generate_with_google(
    prompt: str,
    reference_images: list[str] | None = None,
    aspect_ratio: str = "1:1",
    resolution: str = "2K",
) -> bytes:
    """Generate image using Google AI Studio API."""
    try:
        from google import genai
        from google.genai import types
        from PIL import Image
    except ImportError as e:
        print(f"Error: Required package not installed: {e}")
        print("Install with: pip install google-genai Pillow")
        sys.exit(1)

    api_key = get_google_api_key()
    client = genai.Client(api_key=api_key)

    contents = [prompt]

    if reference_images:
        for path in reference_images:
            try:
                img = Image.open(path)
                contents.append(img)
                print(f"Loaded reference: {path}")
            except Exception as e:
                print(f"Warning: Could not load {path}: {e}")
        print(f"Using {len(contents) - 1} reference image(s) for style transfer")

    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
            image_size=resolution,
        ),
    )

    print(f"Generating with Google API (model: {GOOGLE_MODEL})...")

    try:
        response = client.models.generate_content(
            model=GOOGLE_MODEL,
            contents=contents,
            config=config,
        )
    except Exception as e:
        print(f"Error calling Google API: {e}")
        sys.exit(1)

    # Extract image from response
    for part in response.candidates[0].content.parts:
        if hasattr(part, "inline_data") and part.inline_data:
            return base64.b64decode(part.inline_data.data)
        elif hasattr(part, "text") and part.text:
            print(f"Model response: {part.text}")

    return None


def generate_with_openrouter(
    prompt: str,
    reference_images: list[str] | None = None,
    aspect_ratio: str = "1:1",
    resolution: str = "2K",
) -> bytes:
    """Generate image using OpenRouter API."""
    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai package not installed.")
        print("Install with: pip install openai")
        sys.exit(1)

    api_key = get_openrouter_api_key()

    client = OpenAI(
        base_url=OPENROUTER_API_URL,
        api_key=api_key,
    )

    # Build message content
    content = []

    # Add reference images first if provided
    if reference_images:
        for path in reference_images:
            try:
                img_base64, media_type = load_image_as_base64(path)
                content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{media_type};base64,{img_base64}"
                    }
                })
                print(f"Loaded reference: {path}")
            except Exception as e:
                print(f"Warning: Could not load {path}: {e}")
        print(f"Using {len(content)} reference image(s) for style transfer")

    # Add aspect ratio and resolution hints to prompt
    enhanced_prompt = f"{prompt}\n\n[Technical: aspect ratio {aspect_ratio}, {resolution} resolution]"
    content.append({
        "type": "text",
        "text": enhanced_prompt
    })

    print(f"Generating with OpenRouter API (model: {OPENROUTER_MODEL})...")

    # Map resolution to OpenRouter image_size format
    resolution_map = {
        "1K": "1024x1024",
        "2K": "2048x2048",
        "4K": "4096x4096",
    }
    image_size = resolution_map.get(resolution, "2048x2048")

    try:
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ],
            extra_headers={
                "HTTP-Referer": "https://github.com/42apps/nano-banana",
                "X-Title": "Nano Banana Pro"
            },
            extra_body={
                "modalities": ["text", "image"],
                "image_config": {
                    "aspect_ratio": aspect_ratio,
                    "image_size": image_size,
                }
            }
        )
    except Exception as e:
        print(f"Error calling OpenRouter API: {e}")
        sys.exit(1)

    # Extract response - OpenRouter returns images in content array
    if response.choices and response.choices[0].message:
        message = response.choices[0].message

        # Check for image in response
        if hasattr(message, "content") and message.content:
            content = message.content

            # Handle list of content blocks (multimodal response)
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict):
                        # Check for image_url type
                        if block.get("type") == "image_url":
                            image_url = block.get("image_url", {})
                            url = image_url.get("url", "")
                            if url.startswith("data:image"):
                                base64_start = url.find("base64,") + 7
                                if base64_start > 7:
                                    return base64.b64decode(url[base64_start:])
                        # Check for inline_data (Gemini format)
                        elif block.get("type") == "image":
                            if "data" in block:
                                return base64.b64decode(block["data"])
                            elif "image" in block and "data" in block["image"]:
                                return base64.b64decode(block["image"]["data"])
                        # Check for text response
                        elif block.get("type") == "text":
                            text = block.get("text", "")
                            if text:
                                print(f"Model text: {text[:200]}...")
                    # Handle object with attributes
                    elif hasattr(block, "type"):
                        if block.type == "image_url" and hasattr(block, "image_url"):
                            url = block.image_url.url if hasattr(block.image_url, "url") else block.image_url.get("url", "")
                            if url.startswith("data:image"):
                                base64_start = url.find("base64,") + 7
                                if base64_start > 7:
                                    return base64.b64decode(url[base64_start:])

            # Handle string content (legacy format)
            elif isinstance(content, str):
                # Check if it's a base64 image data URL
                if content.startswith("data:image"):
                    base64_start = content.find("base64,") + 7
                    if base64_start > 7:
                        return base64.b64decode(content[base64_start:])

                # Otherwise it's just text response
                print(f"Model response: {content[:500]}...")
                print("\nNote: Model returned text instead of image.")

    return None


def generate_image(
    prompt: str,
    reference_images: list[str] | None = None,
    aspect_ratio: str = "1:1",
    resolution: str = "2K",
    output_path: str | None = None,
    output_dir: str | None = None,
    provider: str | None = None,
) -> str:
    """
    Generate an image using configured provider.

    Args:
        prompt: Text prompt for image generation
        reference_images: List of paths to reference images for style transfer
        aspect_ratio: Image aspect ratio (1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 21:9)
        resolution: Image resolution (1K, 2K, 4K)
        output_path: Full path for output file (optional)
        output_dir: Directory for output (optional, defaults to current dir)
        provider: API provider to use (google or openrouter)

    Returns:
        Path to the generated image
    """
    if aspect_ratio not in VALID_ASPECT_RATIOS:
        print(f"Warning: Invalid aspect ratio '{aspect_ratio}'. Using '1:1'.")
        aspect_ratio = "1:1"

    if resolution not in VALID_RESOLUTIONS:
        print(f"Warning: Invalid resolution '{resolution}'. Using '2K'.")
        resolution = "2K"

    # Determine provider
    if provider is None:
        provider = get_provider()

    print(f"Provider: {provider}")
    print(f"Aspect ratio: {aspect_ratio}")
    print(f"Resolution: {resolution}")
    print(f"Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
    print()

    # Generate based on provider
    if provider == PROVIDER_GOOGLE:
        image_data = generate_with_google(prompt, reference_images, aspect_ratio, resolution)
    elif provider == PROVIDER_OPENROUTER:
        image_data = generate_with_openrouter(prompt, reference_images, aspect_ratio, resolution)
    else:
        print(f"Error: Unknown provider '{provider}'")
        sys.exit(1)

    if not image_data:
        print("Error: No image was generated in the response.")
        print("This might happen if:")
        print("  - The prompt was blocked by safety filters")
        print("  - The API quota was exceeded")
        print("  - The model doesn't support image generation")
        print("  - There was a temporary API issue")
        sys.exit(1)

    # Determine output path
    if output_path:
        final_path = output_path
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"nano_banana_{timestamp}.png"
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            final_path = os.path.join(output_dir, filename)
        else:
            final_path = filename

    # Save image
    with open(final_path, "wb") as f:
        f.write(image_data)

    print(f"Image saved to: {final_path}")
    return final_path


def main():
    parser = argparse.ArgumentParser(
        description="Generate images with Nano Banana Pro (Gemini 3 Pro Image)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "A serene mountain landscape at sunset"
  %(prog)s "Modern app icon for notes app" --aspect-ratio 1:1
  %(prog)s "Website hero banner" --aspect-ratio 16:9 --resolution 4K
  %(prog)s "Logo in this style" --reference style1.png style2.png
  %(prog)s "Product photo" -o product_shot.png
  %(prog)s "AI visualization" --provider openrouter

Providers:
  google      Google AI Studio API (default, requires GEMINI_API_KEY)
  openrouter  OpenRouter API (requires OPENROUTER_API_KEY)

Environment:
  NANO_BANANA_PROVIDER   Provider to use: google (default) or openrouter
  GEMINI_API_KEY         Required for google provider
  OPENROUTER_API_KEY     Required for openrouter provider
        """,
    )

    parser.add_argument(
        "prompt",
        help="Text prompt describing the image to generate",
    )

    parser.add_argument(
        "-p", "--provider",
        choices=[PROVIDER_GOOGLE, PROVIDER_OPENROUTER],
        help="API provider to use (default: from NANO_BANANA_PROVIDER or 'google')",
    )

    parser.add_argument(
        "-r", "--reference",
        nargs="+",
        metavar="IMAGE",
        help="Reference image(s) for style transfer (up to 14 images)",
    )

    parser.add_argument(
        "-a", "--aspect-ratio",
        default="1:1",
        choices=VALID_ASPECT_RATIOS,
        help="Aspect ratio (default: 1:1)",
    )

    parser.add_argument(
        "-s", "--resolution",
        default="2K",
        choices=VALID_RESOLUTIONS,
        help="Image resolution (default: 2K)",
    )

    parser.add_argument(
        "-o", "--output",
        metavar="PATH",
        help="Output file path (default: nano_banana_<timestamp>.png)",
    )

    parser.add_argument(
        "-d", "--output-dir",
        metavar="DIR",
        help="Output directory (default: current directory)",
    )

    args = parser.parse_args()

    output_path = generate_image(
        prompt=args.prompt,
        reference_images=args.reference,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        output_path=args.output,
        output_dir=args.output_dir,
        provider=args.provider,
    )

    print(f"\nGeneration complete: {output_path}")


if __name__ == "__main__":
    main()
