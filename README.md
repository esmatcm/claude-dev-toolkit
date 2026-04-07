# Claude Dev Toolkit

One command to set up a complete AI development environment for any project.

```
/setup-project
```

That's it. Everything else is automatic.

## What It Does

```
/setup-project
    |
    v
Phase 1: Knowledge Graph ──── Understand the codebase
    |                          - AST extraction (191+ node types)
    |                          - Community detection
    |                          - God nodes & architecture map
    |                          - Auto-rebuild on git commit
    v
Phase 2: Site Optimizer ────── UX audit + product analysis
    |                          - Browse site as real user
    |                          - 4 depth levels (5min → 8hrs)
    |                          - 7 PM skills (journey, priority, strategy)
    |                          - "Would I come back?" evaluation
    v
Phase 3: Frontend QA ───────── Closed-loop auto-testing
    |                          - 8 AI sub-agents
    |                          - Auto-trigger on file change
    |                          - AI validates screenshots
    |                          - Auto-fix → re-test (up to 5x)
    v
Phase 4: Integration ───────── Wire everything together
                               - Playwright MCP server
                               - PreToolUse hook (consult graph)
                               - PostToolUse hook (auto-test)
                               - CLAUDE.md (all rules documented)
```

## Install (one time only)

```powershell
# Windows
git clone https://github.com/esmatcm/claude-dev-toolkit.git
cd claude-dev-toolkit
.\install.ps1
```

```bash
# macOS / Linux
git clone https://github.com/esmatcm/claude-dev-toolkit.git
cd claude-dev-toolkit
chmod +x install.sh && ./install.sh
```

## Usage: New Project Workflow

### Step 1: Enter project directory
```bash
cd /path/to/your/project
claude
```

### Step 2: Run setup
```
/setup-project
```

### Step 3: Restart Claude Code (once)
```
exit
claude
```
This loads the Playwright MCP server. Verify with `/mcp`.

### Step 4: Work normally

From now on, everything is automatic:

```
# Ask about architecture → Knowledge graph consulted automatically
"How does the auth system work?"

# Audit the site → Real browser, real user simulation
"ux audit"
"ux audit thorough"          # overnight deep audit

# Think like a boss → Prioritized optimization
"what should we fix first?"
"map the customer journey"

# Write code → Auto-tested
You: "Add a dark mode toggle"
Claude: [implements] → [auto-tests] → [AI validates] → [fixes issues] → [reports]

# Or explicitly test
/frontend-dev
/test-frontend
```

## What Gets Installed

```
~/.claude/
├── plugins/
│   └── frontend-dev/              # 8 AI agents for visual testing
├── skills/
│   ├── setup-project/             # This skill (the installer)
│   ├── graphify/                  # Knowledge graph skill
│   ├── ux-audit/                  # UX walkthrough & QA sweep
│   ├── playwright-skill/          # Browser automation
│   ├── customer-journey-map/      # PM: user journey mapping
│   ├── prioritization-advisor/    # PM: what to fix first
│   ├── product-strategy-session/  # PM: strategy workshop
│   ├── discovery-process/         # PM: user need discovery
│   ├── jobs-to-be-done/           # PM: JTBD framework
│   ├── positioning-statement/     # PM: value proposition
│   └── competitive-analysis/      # PM: competitor analysis

your-project/
├── .mcp.json                      # Playwright MCP server
├── .claude/settings.json          # PreToolUse + PostToolUse hooks
├── .graphifyignore                # Excluded paths for graph
├── .gitignore                     # Standard ignores
├── CLAUDE.md                      # All rules + architecture summary
└── graphify-out/
    ├── GRAPH_REPORT.md            # God nodes, communities, gaps
    ├── graph.json                 # Queryable graph data
    └── graph.html                 # Interactive visualization
```

## Hooks (automatic, no action needed)

| Hook | Trigger | Action |
|------|---------|--------|
| PreToolUse | Before Glob/Grep | Consult knowledge graph first |
| PostToolUse | After Edit/Write | Auto-trigger visual testing |
| post-commit | After git commit | Rebuild knowledge graph |
| post-checkout | After branch switch | Rebuild knowledge graph |
| Daily schedule | ~9:17 AM | Full graph rebuild |

## Prerequisites

- Node.js 18+
- Python 3.10+
- Git
- Claude Code

## Credits

- [graphify](https://github.com/safishamsi/graphify) — Knowledge graph engine
- [claude-code-frontend-dev](https://github.com/hemangjoshi37a/claude-code-frontend-dev) — Visual testing plugin
- [playwright-skill](https://github.com/lackeyjb/playwright-skill) — Browser automation
- [jezweb/claude-skills](https://github.com/jezweb/claude-skills) — UX Audit skill
- [Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) — PM skills framework
