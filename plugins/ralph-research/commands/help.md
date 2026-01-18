---
description: "Explain Ralph Research plugin and available commands"
---

# Ralph Research Plugin Help

Please explain the following to the user:

## What is Ralph Research?

Ralph Research is a deep codebase analysis tool that uses the Ralph Loop mechanism for **iterative research** before making changes. It does NOT write code - it only investigates and plans.

**Core concept:**
- You describe a task/change you want to make
- Ralph Research iteratively explores your codebase
- Maps all dependencies and connections
- Identifies risks and critical points
- Creates a comprehensive implementation plan

**Why use it:**
- Prevents "I forgot to update X" situations
- Catches breaking changes before they happen
- Creates a complete checklist for implementation
- Reduces debugging time by planning ahead

## Available Commands

### /ralph-research <TASK> [OPTIONS]

Start a deep research session for a task.

**Usage:**
```
/ralph-research "Add user authentication to the API"
/ralph-research "Refactor the payment module" --max-iterations 15
```

**Options:**
- `--max-iterations <n>` - Max research iterations (default: 10)

**Output:**
Creates `.claude/ralph-research.local.md` with:
- Discovered files and their roles
- Dependency map
- Risk analysis
- Complete implementation plan

---

### /cancel-research

Cancel an active research session.

**Usage:**
```
/cancel-research
```

---

## Research Phases

1. **Discovery** - Find all related files and understand architecture
2. **Dependency Mapping** - Trace imports, exports, call chains
3. **Impact Analysis** - What will be affected, tests to update
4. **Risk Assessment** - Critical paths, edge cases, compatibility
5. **Implementation Plan** - Ordered checklist of all changes needed

## Example

```
/ralph-research "Add rate limiting to all API endpoints"
```

Ralph Research will:
- Find all API endpoint files
- Map middleware chain and request flow
- Identify shared utilities and configs
- Find tests that verify API behavior
- Check for existing rate limiting patterns
- Create a plan covering: middleware creation, endpoint updates, config changes, tests to add

## When to Use

**Good for:**
- Any non-trivial code change
- Refactoring existing features
- Adding features that touch multiple files
- Changes to shared/core code
- Before starting complex implementations

**Not needed for:**
- Simple single-file changes
- Adding isolated new files
- Documentation updates
- Obvious bug fixes

## After Research

Once research is complete, you have a full implementation plan. You can:
1. Execute the plan manually step by step
2. Use `/ralph-loop` to implement the changes iteratively
3. Work through the checklist in your preferred order

The research file stays in `.claude/` for reference during implementation.
