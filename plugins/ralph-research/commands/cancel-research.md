---
description: "Cancel active Ralph Research"
allowed-tools: ["Bash(test -f .claude/ralph-research.local.md:*)", "Bash(sed -i '' 's/^active: true/active: false/' .claude/ralph-research.local.md)", "Read(.claude/ralph-research.local.md)"]
hide-from-slash-command-tool: "true"
---

# Cancel Research

To cancel the Ralph Research loop:

1. Check if `.claude/ralph-research.local.md` exists: `test -f .claude/ralph-research.local.md && echo "EXISTS" || echo "NOT_FOUND"`

2. **If NOT_FOUND**: Say "No active Ralph Research found."

3. **If EXISTS**:
   - Read `.claude/ralph-research.local.md` to get iteration and phase from frontmatter
   - Set active to false: `sed -i '' 's/^active: true/active: false/' .claude/ralph-research.local.md`
   - Report: "⛔ Cancelled Ralph Research (was at iteration N, phase: PHASE). All operations will stop immediately."

Note: The research file is preserved for reference with `active: false`.
