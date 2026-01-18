---
description: "Cancel active Ralph Research"
allowed-tools: ["Bash(test -f .claude/ralph-research.local.md:*)", "Bash(rm .claude/ralph-research.local.md)", "Read(.claude/ralph-research.local.md)"]
hide-from-slash-command-tool: "true"
---

# Cancel Research

To cancel the Ralph Research loop:

1. Check if `.claude/ralph-research.local.md` exists using Bash: `test -f .claude/ralph-research.local.md && echo "EXISTS" || echo "NOT_FOUND"`

2. **If NOT_FOUND**: Say "No active Ralph Research found."

3. **If EXISTS**:
   - Read `.claude/ralph-research.local.md` to get the current iteration number from the `iteration:` field in frontmatter
   - Show a summary of what was researched so far (the task and current phase)
   - Ask user if they want to keep the research file for reference or delete it
   - If deleting: `rm .claude/ralph-research.local.md`
   - Report: "Cancelled Ralph Research (was at iteration N, phase: PHASE)"

Note: The research findings accumulated in the file may still be valuable even if cancelled early.
