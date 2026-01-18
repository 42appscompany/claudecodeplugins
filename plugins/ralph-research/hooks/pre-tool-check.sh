#!/bin/bash

# Ralph Research PreToolUse Hook
# Checks if research was cancelled and blocks further tool execution

RESEARCH_FILE=".claude/ralph-research.local.md"

if [[ ! -f "$RESEARCH_FILE" ]]; then
  exit 0  # No file - allow tool execution
fi

# Check active flag in frontmatter
ACTIVE=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$RESEARCH_FILE" | grep '^active:' | sed 's/active: *//')

if [[ "$ACTIVE" == "false" ]]; then
  # Research was cancelled - block tool and notify
  echo '{"systemMessage": "⛔ Ralph Research was cancelled. Stopping all operations."}' >&2
  exit 2  # Block tool execution
fi

exit 0
