#!/bin/bash

# Ralph Research Stop Hook
# Continues research iterations until plan is complete or max iterations reached

set -euo pipefail

HOOK_INPUT=$(cat)

RESEARCH_FILE=".claude/ralph-research.local.md"

if [[ ! -f "$RESEARCH_FILE" ]]; then
  exit 0
fi

# Parse frontmatter
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$RESEARCH_FILE")
ITERATION=$(echo "$FRONTMATTER" | grep '^iteration:' | sed 's/iteration: *//')
MAX_ITERATIONS=$(echo "$FRONTMATTER" | grep '^max_iterations:' | sed 's/max_iterations: *//')
PHASE=$(echo "$FRONTMATTER" | grep '^phase:' | sed 's/phase: *//')

# Validate
if [[ ! "$ITERATION" =~ ^[0-9]+$ ]] || [[ ! "$MAX_ITERATIONS" =~ ^[0-9]+$ ]]; then
  echo "Warning: Ralph Research state file corrupted, stopping" >&2
  rm "$RESEARCH_FILE"
  exit 0
fi

# Check max iterations
if [[ $MAX_ITERATIONS -gt 0 ]] && [[ $ITERATION -ge $MAX_ITERATIONS ]]; then
  echo "🔬 Ralph Research: Max iterations ($MAX_ITERATIONS) reached."
  echo "   Research file preserved: $RESEARCH_FILE"
  echo "   Review the findings and continue manually if needed."
  # Don't delete - keep research for reference
  # Just remove active flag
  TEMP_FILE="${RESEARCH_FILE}.tmp.$$"
  sed "s/^active: true/active: false/" "$RESEARCH_FILE" > "$TEMP_FILE"
  mv "$TEMP_FILE" "$RESEARCH_FILE"
  exit 0
fi

# Get transcript
TRANSCRIPT_PATH=$(echo "$HOOK_INPUT" | jq -r '.transcript_path')

if [[ ! -f "$TRANSCRIPT_PATH" ]]; then
  echo "Warning: Transcript not found, stopping research" >&2
  exit 0
fi

# Get last assistant output
if ! grep -q '"role":"assistant"' "$TRANSCRIPT_PATH"; then
  exit 0
fi

LAST_LINE=$(grep '"role":"assistant"' "$TRANSCRIPT_PATH" | tail -1)
LAST_OUTPUT=$(echo "$LAST_LINE" | jq -r '
  .message.content |
  map(select(.type == "text")) |
  map(.text) |
  join("\n")
' 2>/dev/null || echo "")

if [[ -z "$LAST_OUTPUT" ]]; then
  exit 0
fi

# Check for completion promise
if echo "$LAST_OUTPUT" | grep -q '<promise>RESEARCH COMPLETE</promise>'; then
  echo "✅ Ralph Research: Analysis complete!"
  echo "   Full research saved to: $RESEARCH_FILE"
  echo ""
  echo "   Next steps:"
  echo "   - Review the implementation plan"
  echo "   - Execute changes following the checklist"
  echo "   - Or use /ralph-loop to implement iteratively"
  # Mark as complete but keep file
  TEMP_FILE="${RESEARCH_FILE}.tmp.$$"
  sed "s/^active: true/active: false/" "$RESEARCH_FILE" > "$TEMP_FILE"
  mv "$TEMP_FILE" "$RESEARCH_FILE"
  exit 0
fi

# Continue research
NEXT_ITERATION=$((ITERATION + 1))

# Determine phase based on iteration progress
# Rough distribution: discovery 1-2, deps 3-4, impact 5-6, risks 7-8, plan 9+
if [[ $NEXT_ITERATION -le 2 ]]; then
  NEXT_PHASE="discovery"
elif [[ $NEXT_ITERATION -le 4 ]]; then
  NEXT_PHASE="dependencies"
elif [[ $NEXT_ITERATION -le 6 ]]; then
  NEXT_PHASE="impact"
elif [[ $NEXT_ITERATION -le 8 ]]; then
  NEXT_PHASE="risks"
else
  NEXT_PHASE="planning"
fi

# Update state file
TEMP_FILE="${RESEARCH_FILE}.tmp.$$"
sed -e "s/^iteration: .*/iteration: $NEXT_ITERATION/" \
    -e "s/^phase: .*/phase: $NEXT_PHASE/" \
    "$RESEARCH_FILE" > "$TEMP_FILE"
mv "$TEMP_FILE" "$RESEARCH_FILE"

# Extract task from file (after second ---)
TASK=$(awk '/^# Research Task$/,/^---$/' "$RESEARCH_FILE" | grep -v '^#' | grep -v '^---$' | head -5 | xargs)

# Build prompt for next iteration
PHASE_INSTRUCTIONS=""
case "$NEXT_PHASE" in
  discovery)
    PHASE_INSTRUCTIONS="PHASE 1: DISCOVERY
- Search for files related to the task using Glob and Grep
- Read key files to understand current implementation
- Map the architecture and component structure
- Update the Discovery section in .claude/ralph-research.local.md"
    ;;
  dependencies)
    PHASE_INSTRUCTIONS="PHASE 2: DEPENDENCIES
- Trace imports and exports between discovered files
- Map function/method call chains
- Identify shared state, configs, and data flows
- Update the Dependencies section in .claude/ralph-research.local.md"
    ;;
  impact)
    PHASE_INSTRUCTIONS="PHASE 3: IMPACT ANALYSIS
- Identify ALL files that will need changes
- Find ALL tests that verify affected code
- List potential breaking changes for consumers
- Update the Impact Analysis section in .claude/ralph-research.local.md"
    ;;
  risks)
    PHASE_INSTRUCTIONS="PHASE 4: RISK ASSESSMENT
- Identify critical paths that could break
- List edge cases to handle
- Note backwards compatibility concerns
- Update the Risks section in .claude/ralph-research.local.md"
    ;;
  planning)
    PHASE_INSTRUCTIONS="PHASE 5: IMPLEMENTATION PLAN
- Create ordered checklist of ALL changes needed
- Specify exact files and locations to modify
- List tests to add/update
- Define verification steps
- Update the Implementation Plan section in .claude/ralph-research.local.md

If plan is complete with NO gaps, output: <promise>RESEARCH COMPLETE</promise>"
    ;;
esac

SYSTEM_MSG="🔬 Research iteration $NEXT_ITERATION/$MAX_ITERATIONS | Phase: $NEXT_PHASE | NO CODE CHANGES - research only!"

# Block exit and continue research
jq -n \
  --arg task "$TASK" \
  --arg phase "$PHASE_INSTRUCTIONS" \
  --arg msg "$SYSTEM_MSG" \
  '{
    "decision": "block",
    "reason": ("Continue researching: " + $task + "\n\n" + $phase + "\n\nRemember: Read and update .claude/ralph-research.local.md with your findings. Do NOT write any code."),
    "systemMessage": $msg
  }'

exit 0
