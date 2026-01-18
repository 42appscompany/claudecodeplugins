# Ralph Research Plugin

Deep codebase analysis and impact mapping before making changes. Uses the Ralph Loop mechanism for iterative research.

## What It Does

- **Explores** your codebase deeply to understand the task context
- **Maps** all dependencies, imports, exports, and call chains
- **Identifies** risks, critical points, and potential breaking changes
- **Creates** a comprehensive implementation plan

## What It Does NOT Do

- Does not write code
- Does not make any changes
- Only researches and documents

## Commands

### `/ralph-research <task>`

Start a research session.

```bash
/ralph-research Add rate limiting to API endpoints
/ralph-research Refactor authentication module --max-iterations 15
```

### `/cancel-research`

Cancel active research session.

### `/help`

Show detailed help.

## Output

Creates `.claude/ralph-research.local.md` with:

1. **Discovery** - Related files, architecture overview
2. **Dependencies** - Import/export map, call chains, shared state
3. **Impact Analysis** - Files to modify, tests to update, breaking changes
4. **Risks** - Critical points, edge cases, compatibility concerns
5. **Implementation Plan** - Ordered checklist, verification steps

## Example Workflow

```bash
# 1. Research the change
/ralph-research "Add WebSocket support for real-time notifications"

# 2. Review the generated plan in .claude/ralph-research.local.md

# 3. Implement using the checklist (manually or with /ralph-loop)
```

## Why Use This

- Prevents "I forgot to update X" situations
- Catches breaking changes before they happen
- Creates complete checklist for implementation
- Reduces debugging time by planning ahead
- Documents impact for code review

## Installation

This plugin is installed locally at `~/.claude/plugins/local/ralph-research/`

To enable, add to your Claude Code settings or it will be auto-discovered from the local plugins directory.
