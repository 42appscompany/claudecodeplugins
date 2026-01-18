---
description: "Start deep codebase research for a task"
argument-hint: "TASK [--max-iterations N]"
allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/setup-research.sh:*)"]
hide-from-slash-command-tool: "true"
---

# Ralph Research Command

Execute the setup script to initialize the research loop:

```!
"${CLAUDE_PLUGIN_ROOT}/scripts/setup-research.sh" $ARGUMENTS
```

## Your Mission: Deep Research Only

You are in RESEARCH MODE. Your goal is to deeply investigate the codebase and create a comprehensive implementation plan.

**CRITICAL RULES:**
1. DO NOT write any code or make any changes
2. DO NOT use Edit, Write, or NotebookEdit tools
3. ONLY use: Read, Glob, Grep, Task (with Explore agent), WebSearch, WebFetch
4. Focus on understanding, not implementing

## Research Phases

### Phase 1: Discovery
- Find all files related to the task
- Understand the current architecture
- Identify entry points and main components

### Phase 2: Dependency Mapping
- Trace imports and exports
- Map function/method call chains
- Identify shared state and data flows

### Phase 3: Impact Analysis
- Find all places that will be affected
- Identify tests that need updates
- Spot potential breaking changes
- Note API contracts and interfaces

### Phase 4: Risk Assessment
- Critical paths that could break
- Edge cases to consider
- Backwards compatibility concerns
- Performance implications

### Phase 5: Implementation Plan
- Ordered list of changes needed
- Files to modify with specific locations
- New files to create (if any)
- Tests to add/update
- Checklist format for execution

## Output Format

Update the research file (`.claude/ralph-research.local.md`) with your findings after each iteration. Accumulate information - don't overwrite previous findings.

When research is complete, output:
```
<promise>RESEARCH COMPLETE</promise>
```

Only output this promise when you have:
- Mapped ALL relevant dependencies
- Identified ALL risks and critical points
- Created a COMPLETE implementation plan
- Left NO gaps that could cause issues during implementation
