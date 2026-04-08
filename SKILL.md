---
name: setup-project
description: One-command full dev toolkit — knowledge graph + codebase understanding + frontend QA + site optimizer. Installs everything, configures hooks, builds graph, ready to work.
trigger: /setup-project
---

# /setup-project

Install the complete AI development toolkit for the current project in one command. Combines knowledge graph, codebase understanding, frontend QA, and site optimization into a single automated setup.

## Usage

```
/setup-project                    # full setup (all 3 modules)
/setup-project --graph-only       # only knowledge graph
/setup-project --qa-only          # only frontend QA
/setup-project --optimizer-only   # only site optimizer
/setup-project --status           # check what's installed
```

## What You Must Do When Invoked

Execute ALL steps in order. Do not skip. Do not ask for confirmation between steps. Print progress as you go.

Print this banner first:

```
============================================================
  CLAUDE DEV TOOLKIT - Full Project Setup
============================================================
  Phase 1: Knowledge Graph (understand code structure)
  Phase 2: Codebase Understanding (understand business logic)
  Phase 3: Site Optimizer (UX audit + product analysis)
  Phase 4: Frontend QA (closed-loop auto-testing)
  Phase 5: Integration (hooks + CLAUDE.md + schedule)
============================================================
```

---

## PHASE 1: Knowledge Graph (graphify)

**Purpose**: Build a structural map of the codebase so Claude reads only what matters.

### 1.1 Install graphify package (skip if already importable)

```bash
python -c "import graphify" 2>/dev/null
if [ $? -ne 0 ]; then
  python -m pip install graphifyy -q 2>&1 | tail -3
fi
```

If `python` not found, try `python3`. Store the working command.

### 1.2 Install graphify skill + Claude Code integration

Find the graphify executable:
```bash
python -c "import sys, os; print(os.path.join(os.path.dirname(sys.executable), 'Scripts' if os.name == 'nt' else '', 'graphify'))"
```

Then run:
```bash
graphify install
graphify claude install
```

### 1.3 Initialize git if needed

```bash
[ -d .git ] || git init
```

Create `.gitignore` if not exists (include node_modules/, dist/, build/, .env, *.log, graphify-out/cache/).

Create `.graphifyignore`:
```
node_modules/
dist/
build/
.git/
graphify-out/
*.lock
*.min.js
package-lock.json
```

### 1.4 Install git hooks for auto-rebuild

```bash
graphify hook install
```

### 1.5 Build the knowledge graph

Run the full pipeline using Python API:

```python
import json, os
from pathlib import Path
from graphify.detect import detect
from graphify.extract import extract
from graphify.build import build
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html

root = Path('.')
detection = detect(root)
code_files = [Path(f) for f in detection['files']['code']]
ast_result = extract(code_files)
G = build([ast_result])
communities = cluster(G)
cohesion = score_all(G, communities)
community_labels = {cid: f'Community {cid}' for cid in communities}
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
questions = suggest_questions(G, communities, community_labels)
token_cost = {
    'corpus_tokens': detection['total_words'],
    'graph_tokens': G.number_of_nodes() * 50,
    'reduction': round(detection['total_words'] / max(G.number_of_nodes() * 50, 1), 1)
}
outdir = Path('graphify-out')
outdir.mkdir(exist_ok=True)
report_text = generate(G, communities, cohesion, community_labels, gods, surprises, detection, token_cost, str(root), questions)
with open(outdir / 'GRAPH_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(report_text)
to_json(G, communities, str(outdir / 'graph.json'))
to_html(G, communities, str(outdir / 'graph.html'), community_labels)
```

Print: node count, edge count, community count, token reduction.

### 1.6 Schedule daily rebuild

Create a scheduled task `graphify-rebuild` that runs the above pipeline daily at ~9:17 AM.

Print: `[Phase 1 DONE] Knowledge graph: X nodes, Y edges, Z communities`

---

## PHASE 2: Codebase Understanding (Understand-Anything)

**Purpose**: Understand business logic, data flows, and how frontend connects to backend.

### 2.1 Install Understand-Anything skills (skip if exists)

Check if `~/.claude/skills/understand/SKILL.md` exists. If not:

```bash
git clone https://github.com/Lum1104/Understand-Anything.git /tmp/understand-anything-temp
for skill in understand understand-chat understand-dashboard understand-diff understand-domain understand-explain understand-onboard; do
  mkdir -p ~/.claude/skills/$skill
  cp -r /tmp/understand-anything-temp/understand-anything-plugin/skills/$skill/* ~/.claude/skills/$skill/
done
rm -rf /tmp/understand-anything-temp
```

### 2.2 Run initial analysis

After installation, run the understand skill on the current project:

```
/understand
```

This produces an interactive knowledge graph showing:
- Architecture layers (API, Service, Data, UI)
- Business domains and process flows
- Component relationships and dependencies
- Frontend-to-backend data flow connections

Print: `[Phase 2 DONE] Codebase understanding: architecture + business logic mapped`

---

## PHASE 3: Site Optimizer (UX Audit + Product Analysis)

**Purpose**: Enable Claude to browse the site as a real user and think like a PM/boss.

### 2.1 Install ux-audit skill (skip if exists)

Check `~/.claude/skills/ux-audit/SKILL.md`. If not:

```bash
git clone https://github.com/jezweb/claude-skills.git /tmp/jezweb-skills-temp
mkdir -p ~/.claude/skills/ux-audit
cp -r /tmp/jezweb-skills-temp/plugins/dev-tools/skills/ux-audit/* ~/.claude/skills/ux-audit/
rm -rf /tmp/jezweb-skills-temp
```

### 2.2 Install PM skills (skip if exists)

```bash
git clone https://github.com/deanpeters/Product-Manager-Skills.git /tmp/pm-skills-temp
for skill in customer-journey-map prioritization-advisor product-strategy-session discovery-process competitive-analysis jobs-to-be-done positioning-statement; do
  [ -f "$HOME/.claude/skills/$skill/SKILL.md" ] || {
    mkdir -p "$HOME/.claude/skills/$skill"
    cp -r "/tmp/pm-skills-temp/skills/$skill/"* "$HOME/.claude/skills/$skill/"
  }
done
rm -rf /tmp/pm-skills-temp
```

### 2.3 Install playwright-skill (skip if exists)

Check `~/.claude/skills/playwright-skill/SKILL.md`. If not:

```bash
git clone https://github.com/lackeyjb/playwright-skill.git /tmp/playwright-skill-temp
mkdir -p ~/.claude/skills/playwright-skill
cp -r /tmp/playwright-skill-temp/skills/playwright-skill/* ~/.claude/skills/playwright-skill/
rm -rf /tmp/playwright-skill-temp
cd ~/.claude/skills/playwright-skill && npm install
```

Print: `[Phase 2 DONE] UX audit + 7 PM skills + browser automation installed`

---

## PHASE 4: Frontend QA (Closed-Loop Auto-Testing)

**Purpose**: After code changes, automatically test in real browser, AI validates, auto-fix, re-test.

### 3.1 Install frontend-dev plugin (skip if exists)

Check `~/.claude/plugins/frontend-dev/`. If not:

```bash
git clone https://github.com/hemangjoshi37a/claude-code-frontend-dev.git ~/.claude/plugins/frontend-dev
```

### 3.2 Fix Windows encoding issue

**CRITICAL on Windows**: The `auto_visual_test.py` hook uses emoji that crash on cp950/cp936.

Edit `~/.claude/plugins/frontend-dev/hooks/auto_visual_test.py`:
1. Change shebang: `#!/usr/bin/env python3` → `#!/usr/bin/env python`
2. Add before first print in the `if frontend_files:` block:
   ```python
   import io
   sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
   ```
3. Replace emoji in print statements with plain text:
   - `🎨 FRONTEND FILE MODIFIED` → `[VISUAL TEST] FRONTEND FILE MODIFIED`
   - `🚀 Automatically launching` → `Automatically launching`

### 3.3 Install Playwright browser (skip if exists)

```bash
npm list -g playwright 2>/dev/null || npm install -g playwright
npx playwright install chromium
```

Print: `[Phase 3 DONE] Frontend QA plugin + Playwright browser installed`

---

## PHASE 5: Integration

**Purpose**: Wire everything together with hooks, MCP, and CLAUDE.md.

### 4.1 Configure Playwright MCP server

Create or merge `.mcp.json` in the project directory:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@executeautomation/playwright-mcp-server"],
      "env": {
        "PLAYWRIGHT_HEADLESS": "false"
      }
    }
  }
}
```

Merge into existing `.mcp.json` if present. Do NOT overwrite other MCP servers.

### 4.2 Configure hooks in .claude/settings.json

Read existing `.claude/settings.json`. Merge these hooks (do NOT remove existing hooks):

**PreToolUse** — graphify consult before file search:
```json
{
  "matcher": "Glob|Grep",
  "hooks": [{
    "type": "command",
    "command": "[ -f graphify-out/graph.json ] && echo 'graphify: Knowledge graph exists. Read graphify-out/GRAPH_REPORT.md for god nodes and community structure before searching raw files.' || true"
  }]
}
```

**PostToolUse** — auto-trigger visual testing on frontend file changes:
```json
{
  "matcher": "Edit|Write",
  "hooks": [{
    "type": "command",
    "command": "python \"$HOME/.claude/plugins/frontend-dev/hooks/auto_visual_test.py\"",
    "description": "Auto-trigger visual testing when frontend files are modified"
  }]
}
```

### 4.3 Update CLAUDE.md

Read existing CLAUDE.md (or create new). Write/merge ALL of these sections:

**Section 1 — graphify**:
```markdown
## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md
- After modifying code files, run `python -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"` to keep the graph current
```

**Section 2 — Project Architecture**: Read GRAPH_REPORT.md and write a summary of god nodes and core subsystems.

**Section 3 — Frontend QA**:
```markdown
## Frontend QA (closed-loop)

- After modifying frontend files, PostToolUse hook auto-triggers visual testing
- `/frontend-dev` for full closed-loop: implement → test → AI validate → auto-fix → re-test
- `/test-frontend` for quick validation
- Playwright MCP configured in .mcp.json
```

**Section 4 — Site Optimizer**:
```markdown
## Site Optimization & UX Audit

UX Audit (user perspective):
- `ux audit` or `dogfood this` — walkthrough as real user
- `/ux-audit quick|standard|thorough|exhaustive` — 4 depth levels

Product Analysis (boss/PM perspective):
- `customer-journey-map` — map user journey, find drop-offs
- `prioritization-advisor` — what to fix first
- `product-strategy-session` — strategy + roadmap
- `jobs-to-be-done` — JTBD analysis
```

### 4.4 Final verification

Check each component and print a status table:

```bash
# Skills
for s in ux-audit customer-journey-map prioritization-advisor product-strategy-session discovery-process jobs-to-be-done positioning-statement playwright-skill; do
  [ -f "$HOME/.claude/skills/$s/SKILL.md" ] && echo "[OK] $s" || echo "[MISSING] $s"
done

# Plugin
[ -d "$HOME/.claude/plugins/frontend-dev" ] && echo "[OK] frontend-dev plugin" || echo "[MISSING] frontend-dev"

# Graph
[ -f "graphify-out/graph.json" ] && echo "[OK] knowledge graph built" || echo "[MISSING] graph"

# Config
[ -f ".mcp.json" ] && echo "[OK] .mcp.json" || echo "[MISSING] .mcp.json"
[ -f ".claude/settings.json" ] && echo "[OK] settings.json hooks" || echo "[MISSING] hooks"
[ -f "CLAUDE.md" ] && echo "[OK] CLAUDE.md" || echo "[MISSING] CLAUDE.md"
```

### 4.5 Print final report

```
============================================================
  SETUP COMPLETE
============================================================

Phase 1 - Knowledge Graph:
  [OK] graphify package installed
  [OK] Graph: X nodes, Y edges, Z communities
  [OK] Git hooks: post-commit + post-checkout auto-rebuild
  [OK] Daily scheduled rebuild at ~9:17 AM

Phase 2 - Codebase Understanding:
  [OK] understand-anything (7 skills)
  [OK] Architecture + business logic mapped

Phase 3 - Site Optimizer:
  [OK] ux-audit (4 depth levels)
  [OK] 7 PM skills (journey map, prioritization, strategy...)
  [OK] playwright-skill (model-invoked browser automation)

Phase 4 - Frontend QA:
  [OK] frontend-dev plugin (8 AI sub-agents)
  [OK] Playwright Chromium browser
  [OK] PostToolUse hook (auto-test on file change)

Phase 5 - Integration:
  [OK] Playwright MCP server → .mcp.json
  [OK] PreToolUse hook → consult graph before search
  [OK] PostToolUse hook → auto-test frontend changes
  [OK] CLAUDE.md → all rules and commands documented

============================================================
  HOW TO USE
============================================================

  UNDERSTAND THE CODEBASE:
    /understand                    Full codebase analysis (architecture + business logic)
    /understand-domain             Extract business domains and flows
    /understand-chat [question]    Ask questions about the codebase
    /understand-explain [path]     Deep-dive into specific file
    /understand-diff               Analyze what changed and impact
    /understand-dashboard          Open interactive explorer

  UX AUDIT (user perspective):
    "ux audit [url]"               Standard walkthrough
    "ux audit [url] thorough"      Overnight deep audit
    "ux audit [url] exhaustive"    Every element on every page
    "qa sweep"                     Test all pages systematically

  PRODUCT ANALYSIS (boss perspective):
    "customer-journey-map"         User flow + drop-off points
    "prioritization-advisor"       What to fix first
    "product-strategy-session"     Full strategy workshop
    "jobs-to-be-done"              What users hire the product for

  DEVELOP & AUTO-TEST:
    Just write code normally. Frontend changes auto-trigger:
    1. Browser opens → 2. Screenshot → 3. AI validates →
    4. Auto-fix if needed → 5. Re-test → 6. Report to you

    /frontend-dev                  Full closed-loop development
    /test-frontend                 Quick visual validation

============================================================
IMPORTANT: Restart Claude Code to load the Playwright MCP server.
After restart, run /mcp to verify Playwright tools are available.
============================================================
```
