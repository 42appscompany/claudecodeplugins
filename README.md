# 42apps Plugins for Claude Code

Collection of productivity plugins for Claude Code by [42apps](https://42apps.io).

## Installation

Add this marketplace to Claude Code:

```bash
/plugin marketplace add 42appscompany/claudecodeplugins
```

Then browse and install plugins:

```bash
/plugin
```

## Available Plugins

| Plugin | Description | Command |
|--------|-------------|---------|
| [ralph-research](./plugins/ralph-research) | Deep codebase research and impact analysis | `/ralph-research` |

## ralph-research

Deep codebase research and impact analysis before making changes. Iteratively explores code, maps all dependencies, identifies risks and critical points, and creates a comprehensive implementation plan.

**Features:**
- 5-phase research methodology (Discovery, Dependencies, Impact Analysis, Risk Assessment, Implementation Plan)
- Iterative exploration with configurable max iterations
- Creates detailed implementation plans
- Does NOT write code - only researches and plans

**Usage:**
```bash
/ralph-research "Your task description" --max-iterations 15
```

**Commands:**
- `/ralph-research <task>` - Start research session
- `/cancel-research` - Cancel active research
- `/ralph-research:help` - Show help

## Adding New Plugins

1. Create plugin folder in `plugins/`
2. Add `.claude-plugin/plugin.json` with metadata
3. Update `marketplace.json` with plugin entry
4. Commit and push

## License

MIT
