#!/bin/bash

# Ralph Research Setup Script
# Creates state file for deep codebase research loop

set -euo pipefail

# Parse arguments
TASK_PARTS=()
MAX_ITERATIONS=10

while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
      cat << 'HELP_EOF'
Ralph Research - Deep codebase analysis before making changes

USAGE:
  /ralph-research [TASK...] [OPTIONS]

ARGUMENTS:
  TASK...    Description of the change/feature you want to implement

OPTIONS:
  --max-iterations <n>    Maximum research iterations (default: 10)
  -h, --help              Show this help message

DESCRIPTION:
  Starts an iterative research session that:
  - Explores your codebase deeply
  - Maps all dependencies and connections
  - Identifies risks and critical points
  - Creates a comprehensive implementation plan

  DOES NOT write code - only researches and plans.

EXAMPLES:
  /ralph-research Add user authentication to the API
  /ralph-research Refactor the payment processing module --max-iterations 15
  /ralph-research "Migrate database from MySQL to PostgreSQL"

OUTPUT:
  Creates .claude/ralph-research.local.md with:
  - Task description
  - Discovered files
  - Dependency map
  - Risk analysis
  - Implementation plan (checklist)

STOPPING:
  Research completes when plan is ready, or after --max-iterations
  Use /cancel-research to stop early

HELP_EOF
      exit 0
      ;;
    --max-iterations)
      if [[ -z "${2:-}" ]] || ! [[ "$2" =~ ^[0-9]+$ ]]; then
        echo "Error: --max-iterations requires a positive integer" >&2
        exit 1
      fi
      MAX_ITERATIONS="$2"
      shift 2
      ;;
    *)
      TASK_PARTS+=("$1")
      shift
      ;;
  esac
done

TASK="${TASK_PARTS[*]}"

if [[ -z "$TASK" ]]; then
  echo "Error: No task provided" >&2
  echo "" >&2
  echo "Usage: /ralph-research <task description>" >&2
  echo "Example: /ralph-research Add caching to the API layer" >&2
  exit 1
fi

# Create state file
mkdir -p .claude

cat > .claude/ralph-research.local.md <<EOF
---
active: true
iteration: 1
max_iterations: $MAX_ITERATIONS
phase: discovery
started_at: "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
---

# Research Task

$TASK

---

# Phase 1: Discovery

## Files Found
(To be filled during research)

## Architecture Overview
(To be filled during research)

---

# Phase 2: Dependencies

## Import/Export Map
(To be filled during research)

## Call Chains
(To be filled during research)

## Shared State
(To be filled during research)

---

# Phase 3: Impact Analysis

## Files to Modify
(To be filled during research)

## Tests to Update
(To be filled during research)

## Breaking Changes Risk
(To be filled during research)

---

# Phase 4: Risks

## Critical Points
(To be filled during research)

## Edge Cases
(To be filled during research)

## Compatibility Concerns
(To be filled during research)

---

# Phase 5: Implementation Plan

## Checklist
(To be filled during research)

## Order of Changes
(To be filled during research)

## Verification Steps
(To be filled during research)

EOF

cat <<EOF
🔬 Ralph Research activated!

Task: $TASK
Max iterations: $MAX_ITERATIONS

RESEARCH MODE - No code changes allowed!

Phases:
1. Discovery - Find related files
2. Dependencies - Map connections
3. Impact - What will be affected
4. Risks - Critical points and edge cases
5. Plan - Implementation checklist

Output file: .claude/ralph-research.local.md

When research is complete, output:
  <promise>RESEARCH COMPLETE</promise>

Starting Phase 1: Discovery...
EOF
