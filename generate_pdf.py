from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Register Chinese font
font_paths = [
    "C:/Windows/Fonts/msjh.ttc",      # Microsoft JhengHei
    "C:/Windows/Fonts/msyh.ttc",      # Microsoft YaHei
    "C:/Windows/Fonts/simsun.ttc",    # SimSun
    "C:/Windows/Fonts/mingliu.ttc",   # MingLiU
]

font_name = "Helvetica"
for fp in font_paths:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont("CJK", fp, subfontIndex=0))
            font_name = "CJK"
            break
        except:
            continue

# Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle', parent=styles['Title'],
    fontName=font_name, fontSize=28, spaceAfter=6,
    textColor=HexColor('#1a1a2e'), alignment=TA_CENTER
)
subtitle_style = ParagraphStyle(
    'Subtitle', parent=styles['Normal'],
    fontName=font_name, fontSize=12, spaceAfter=20,
    textColor=HexColor('#666666'), alignment=TA_CENTER
)
h1_style = ParagraphStyle(
    'H1', parent=styles['Heading1'],
    fontName=font_name, fontSize=18, spaceBefore=20, spaceAfter=10,
    textColor=HexColor('#16213e')
)
h2_style = ParagraphStyle(
    'H2', parent=styles['Heading2'],
    fontName=font_name, fontSize=14, spaceBefore=14, spaceAfter=8,
    textColor=HexColor('#0f3460')
)
body_style = ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontName=font_name, fontSize=10, spaceAfter=6,
    leading=16, textColor=HexColor('#333333')
)
code_style = ParagraphStyle(
    'Code', parent=styles['Code'],
    fontName='Courier', fontSize=9, spaceAfter=4,
    backColor=HexColor('#f5f5f5'), borderPadding=4,
    leftIndent=10, textColor=HexColor('#2d2d2d')
)
bullet_style = ParagraphStyle(
    'Bullet', parent=body_style,
    leftIndent=20, bulletIndent=10, spaceAfter=4
)
highlight_style = ParagraphStyle(
    'Highlight', parent=body_style,
    backColor=HexColor('#e8f4f8'), borderPadding=8,
    leftIndent=10, rightIndent=10, spaceAfter=10
)

def hr():
    return HRFlowable(width="100%", thickness=1, color=HexColor('#e0e0e0'), spaceAfter=10, spaceBefore=10)

def make_table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#16213e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f9f9f9')]),
    ]))
    return t

# Build PDF
output_path = os.path.expanduser("~/Desktop/Claude_Dev_Toolkit_Guide.pdf")
doc = SimpleDocTemplate(output_path, pagesize=A4,
    topMargin=25*mm, bottomMargin=20*mm, leftMargin=20*mm, rightMargin=20*mm)

story = []

# ── Cover ──
story.append(Spacer(1, 80))
story.append(Paragraph("Claude Dev Toolkit", title_style))
story.append(Spacer(1, 8))
story.append(Paragraph("Complete AI Development Environment Guide", subtitle_style))
story.append(Spacer(1, 10))
story.append(hr())
story.append(Spacer(1, 10))

cover_info = [
    "Knowledge Graph + Frontend QA + Site Optimizer",
    "One command. Full setup. Automatic everything.",
    "",
    "github.com/esmatcm/claude-dev-toolkit",
]
for line in cover_info:
    story.append(Paragraph(line, ParagraphStyle('CoverLine', parent=body_style, alignment=TA_CENTER, fontSize=11)))

story.append(Spacer(1, 40))

# Quick start box
story.append(Paragraph(
    "<b>Quick Start</b><br/>"
    "1. Install (once):  git clone github.com/esmatcm/claude-dev-toolkit  then run install.ps1<br/>"
    "2. New project:  /setup-project<br/>"
    "3. Restart Claude Code once<br/>"
    "4. Start working",
    highlight_style
))

story.append(PageBreak())

# ── Table of Contents ──
story.append(Paragraph("Table of Contents", h1_style))
story.append(hr())
toc_items = [
    "1. Installation",
    "2. The 4 Phases",
    "3. Daily Workflow",
    "4. Command Reference",
    "5. Usage Scenario Walkthrough",
    "6. Architecture Overview",
    "7. All Installed Components",
]
for item in toc_items:
    story.append(Paragraph(item, ParagraphStyle('TOC', parent=body_style, fontSize=12, spaceAfter=8, leftIndent=20)))
story.append(PageBreak())

# ── 1. Installation ──
story.append(Paragraph("1. Installation", h1_style))
story.append(hr())

story.append(Paragraph("One-time setup (permanent):", h2_style))
story.append(Paragraph("git clone https://github.com/esmatcm/claude-dev-toolkit.git", code_style))
story.append(Paragraph("cd claude-dev-toolkit", code_style))
story.append(Paragraph(".\\install.ps1          # Windows", code_style))
story.append(Paragraph("./install.sh           # macOS / Linux", code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Per-project setup:", h2_style))
story.append(Paragraph("Open Claude Code in your project directory, then type:", body_style))
story.append(Paragraph("/setup-project", code_style))
story.append(Spacer(1, 6))
story.append(Paragraph("After setup completes, restart Claude Code once to load Playwright MCP.", body_style))
story.append(PageBreak())

# ── 2. The 4 Phases ──
story.append(Paragraph("2. The 4 Phases", h1_style))
story.append(hr())

phases = [
    ("Phase 1: Knowledge Graph (graphify)",
     "Builds a structural map of the codebase using AST extraction and community detection. "
     "Claude consults the graph before searching files, making responses faster and more accurate.",
     ["Auto-rebuild on git commit (post-commit hook)",
      "Daily scheduled rebuild at ~9:17 AM",
      "PreToolUse hook: consult graph before Glob/Grep"]),

    ("Phase 2: Site Optimizer (UX Audit + PM Analysis)",
     "Enables Claude to browse your site in a real browser as a real user, and analyze from "
     "both user and boss/PM perspective using professional frameworks.",
     ["UX Audit: 4 depth levels (quick/standard/thorough/exhaustive)",
      "6 evaluation dimensions: comprehension, wayfinding, flow, trust, efficiency, recovery",
      "7 PM skills: journey map, prioritization, strategy, JTBD, positioning, discovery, competitive analysis"]),

    ("Phase 3: Frontend QA (Closed-Loop Auto-Testing)",
     "After any frontend file is modified, automatically opens a browser, takes screenshots, "
     "AI validates the result, and auto-fixes issues up to 5 iterations.",
     ["8 AI sub-agents (coordinator, tester, validator, UX, SEO, auth...)",
      "PostToolUse hook: auto-trigger on .tsx/.jsx/.vue/.css changes",
      "Playwright browser automation with headed mode"]),

    ("Phase 4: Integration",
     "Wires everything together with hooks, MCP server config, and CLAUDE.md instructions.",
     ["Playwright MCP server in .mcp.json",
      "PreToolUse + PostToolUse hooks in settings.json",
      "CLAUDE.md with all rules and architecture summary"]),
]

for title, desc, bullets in phases:
    story.append(Paragraph(title, h2_style))
    story.append(Paragraph(desc, body_style))
    for b in bullets:
        story.append(Paragraph(f"  - {b}", bullet_style))
    story.append(Spacer(1, 8))

story.append(PageBreak())

# ── 3. Daily Workflow ──
story.append(Paragraph("3. Daily Workflow", h1_style))
story.append(hr())

story.append(Paragraph(
    "After /setup-project is done, your daily workflow is simple. "
    "You just talk to Claude naturally. Everything else is automatic.",
    body_style
))
story.append(Spacer(1, 10))

workflow_data = [
    [Paragraph("<b>Step</b>", body_style), Paragraph("<b>You</b>", body_style), Paragraph("<b>Claude (automatic)</b>", body_style)],
    [Paragraph("1", body_style), Paragraph("See a problem on the site", body_style), Paragraph("-", body_style)],
    [Paragraph("2", body_style), Paragraph("Tell Claude what to fix", body_style), Paragraph("Consults knowledge graph, finds relevant files", body_style)],
    [Paragraph("3", body_style), Paragraph("-", body_style), Paragraph("Modifies code", body_style)],
    [Paragraph("4", body_style), Paragraph("-", body_style), Paragraph("PostToolUse hook triggers browser test", body_style)],
    [Paragraph("5", body_style), Paragraph("-", body_style), Paragraph("AI validates screenshot, auto-fixes if needed", body_style)],
    [Paragraph("6", body_style), Paragraph("Review final result", body_style), Paragraph("Reports with screenshots", body_style)],
    [Paragraph("7", body_style), Paragraph("OK, next task", body_style), Paragraph("-", body_style)],
]
story.append(make_table(workflow_data, col_widths=[30, 170, 270]))
story.append(PageBreak())

# ── 4. Command Reference ──
story.append(Paragraph("4. Command Reference", h1_style))
story.append(hr())

story.append(Paragraph("UX Audit (User Perspective)", h2_style))
cmd_ux = [
    [Paragraph("<b>Command</b>", body_style), Paragraph("<b>Description</b>", body_style), Paragraph("<b>Duration</b>", body_style)],
    [Paragraph("ux audit [url]", body_style), Paragraph("Standard walkthrough as real user", body_style), Paragraph("20-40 min", body_style)],
    [Paragraph("ux audit [url] quick", body_style), Paragraph("Quick spot check, happy path only", body_style), Paragraph("5-10 min", body_style)],
    [Paragraph("ux audit [url] thorough", body_style), Paragraph("All pages, multiple personas, overnight mode", body_style), Paragraph("1-3 hours", body_style)],
    [Paragraph("ux audit [url] exhaustive", body_style), Paragraph("Every interactive element on every page", body_style), Paragraph("4-8+ hours", body_style)],
    [Paragraph("qa sweep", body_style), Paragraph("Systematic test of all pages, CRUD, states", body_style), Paragraph("30-60 min", body_style)],
    [Paragraph("dogfood this", body_style), Paragraph("Same as ux audit", body_style), Paragraph("20-40 min", body_style)],
]
story.append(make_table(cmd_ux, col_widths=[140, 230, 100]))
story.append(Spacer(1, 14))

story.append(Paragraph("Product Analysis (Boss/PM Perspective)", h2_style))
cmd_pm = [
    [Paragraph("<b>Command</b>", body_style), Paragraph("<b>Description</b>", body_style)],
    [Paragraph("prioritization-advisor", body_style), Paragraph("What to fix first (RICE/ICE framework)", body_style)],
    [Paragraph("customer-journey-map", body_style), Paragraph("Map user journey, find drop-off points", body_style)],
    [Paragraph("product-strategy-session", body_style), Paragraph("Full strategy + roadmap workshop", body_style)],
    [Paragraph("jobs-to-be-done", body_style), Paragraph("What job users hire the product for", body_style)],
    [Paragraph("positioning-statement", body_style), Paragraph("Clear value proposition", body_style)],
    [Paragraph("competitive-analysis", body_style), Paragraph("Compare with competitors", body_style)],
    [Paragraph("discovery-process", body_style), Paragraph("User need discovery cycle", body_style)],
]
story.append(make_table(cmd_pm, col_widths=[170, 300]))
story.append(Spacer(1, 14))

story.append(Paragraph("Development & Testing", h2_style))
cmd_dev = [
    [Paragraph("<b>Command</b>", body_style), Paragraph("<b>Description</b>", body_style)],
    [Paragraph("/frontend-dev", body_style), Paragraph("Full closed-loop: code > test > AI validate > auto-fix > re-test", body_style)],
    [Paragraph("/test-frontend", body_style), Paragraph("Quick visual validation of current state", body_style)],
    [Paragraph("/graphify .", body_style), Paragraph("Rebuild knowledge graph", body_style)],
    [Paragraph("/setup-project", body_style), Paragraph("Full setup (new project)", body_style)],
]
story.append(make_table(cmd_dev, col_widths=[170, 300]))
story.append(PageBreak())

# ── 5. Usage Scenario ──
story.append(Paragraph("5. Usage Scenario Walkthrough", h1_style))
story.append(hr())
story.append(Paragraph("Example: Optimizing ai.xxcvd.com", h2_style))
story.append(Spacer(1, 6))

scenarios = [
    ("Step 1: Setup", "/setup-project", "Auto-runs 4 phases, builds knowledge graph, installs all tools"),
    ("Step 2: Find Problems", "ux audit ai.xxcvd.com", "Opens browser, simulates real user, produces ranked friction report"),
    ("Step 3: Prioritize", "prioritization-advisor", "Uses RICE framework to rank: mobile nav > form feedback > page speed > dark mode"),
    ("Step 4: Fix", "Fix mobile nav menu", "Consults graph > finds SiteNav.tsx > modifies > auto-tests > auto-fixes > reports"),
    ("Step 5: Confirm", "OK, next", "You only see final passing result"),
    ("Step 6: Big Picture", "customer-journey-map", "Maps full user journey, finds 65% drop-off at onboarding, suggests guided tour"),
]

for step_title, you_say, claude_does in scenarios:
    story.append(Paragraph(f"<b>{step_title}</b>", body_style))
    story.append(Paragraph(f"You say:  {you_say}", ParagraphStyle('YouSay', parent=code_style, textColor=HexColor('#0f3460'))))
    story.append(Paragraph(f"Claude:  {claude_does}", ParagraphStyle('ClaudeDoes', parent=body_style, leftIndent=10, textColor=HexColor('#555555'))))
    story.append(Spacer(1, 8))

story.append(PageBreak())

# ── 6. Architecture ──
story.append(Paragraph("6. Architecture Overview", h1_style))
story.append(hr())

story.append(Paragraph("File Structure After Setup", h2_style))
file_struct = [
    "~/.claude/",
    "  plugins/frontend-dev/          # 8 AI agents for visual testing",
    "  skills/",
    "    setup-project/               # This toolkit (the installer)",
    "    graphify/                     # Knowledge graph skill",
    "    ux-audit/                     # UX walkthrough & QA sweep",
    "    playwright-skill/             # Browser automation",
    "    customer-journey-map/         # PM: user journey",
    "    prioritization-advisor/       # PM: what to fix first",
    "    product-strategy-session/     # PM: strategy workshop",
    "    discovery-process/            # PM: need discovery",
    "    jobs-to-be-done/              # PM: JTBD framework",
    "    positioning-statement/        # PM: value proposition",
    "    competitive-analysis/         # PM: competitor analysis",
    "",
    "your-project/",
    "  .mcp.json                       # Playwright MCP server",
    "  .claude/settings.json           # PreToolUse + PostToolUse hooks",
    "  .graphifyignore                 # Excluded paths for graph",
    "  CLAUDE.md                       # All rules + architecture summary",
    "  graphify-out/",
    "    GRAPH_REPORT.md               # God nodes, communities, gaps",
    "    graph.json                    # Queryable graph data",
    "    graph.html                    # Interactive visualization",
]
for line in file_struct:
    story.append(Paragraph(line, code_style))

story.append(Spacer(1, 14))

story.append(Paragraph("Hooks (Automatic)", h2_style))
hooks_data = [
    [Paragraph("<b>Hook</b>", body_style), Paragraph("<b>Trigger</b>", body_style), Paragraph("<b>Action</b>", body_style)],
    [Paragraph("PreToolUse", body_style), Paragraph("Before Glob/Grep", body_style), Paragraph("Consult knowledge graph first", body_style)],
    [Paragraph("PostToolUse", body_style), Paragraph("After Edit/Write", body_style), Paragraph("Auto-trigger visual testing", body_style)],
    [Paragraph("post-commit", body_style), Paragraph("After git commit", body_style), Paragraph("Rebuild knowledge graph", body_style)],
    [Paragraph("post-checkout", body_style), Paragraph("Branch switch", body_style), Paragraph("Rebuild knowledge graph", body_style)],
    [Paragraph("Daily schedule", body_style), Paragraph("~9:17 AM", body_style), Paragraph("Full graph rebuild", body_style)],
]
story.append(make_table(hooks_data, col_widths=[100, 130, 240]))

story.append(PageBreak())

# ── 7. All Components ──
story.append(Paragraph("7. All Installed Components", h1_style))
story.append(hr())

components = [
    [Paragraph("<b>Component</b>", body_style), Paragraph("<b>Source</b>", body_style), Paragraph("<b>Purpose</b>", body_style)],
    [Paragraph("graphify", body_style), Paragraph("safishamsi/graphify", body_style), Paragraph("Code knowledge graph engine", body_style)],
    [Paragraph("frontend-dev", body_style), Paragraph("hemangjoshi37a/claude-code-frontend-dev", body_style), Paragraph("8 AI sub-agents, closed-loop testing", body_style)],
    [Paragraph("playwright-skill", body_style), Paragraph("lackeyjb/playwright-skill", body_style), Paragraph("Model-invoked browser automation", body_style)],
    [Paragraph("ux-audit", body_style), Paragraph("jezweb/claude-skills", body_style), Paragraph("Real-user UX walkthrough + QA sweep", body_style)],
    [Paragraph("customer-journey-map", body_style), Paragraph("deanpeters/Product-Manager-Skills", body_style), Paragraph("User journey + drop-off analysis", body_style)],
    [Paragraph("prioritization-advisor", body_style), Paragraph("deanpeters/Product-Manager-Skills", body_style), Paragraph("RICE/ICE prioritization", body_style)],
    [Paragraph("product-strategy-session", body_style), Paragraph("deanpeters/Product-Manager-Skills", body_style), Paragraph("Strategy + roadmap workshop", body_style)],
    [Paragraph("discovery-process", body_style), Paragraph("deanpeters/Product-Manager-Skills", body_style), Paragraph("User need discovery", body_style)],
    [Paragraph("jobs-to-be-done", body_style), Paragraph("deanpeters/Product-Manager-Skills", body_style), Paragraph("JTBD framework", body_style)],
    [Paragraph("positioning-statement", body_style), Paragraph("deanpeters/Product-Manager-Skills", body_style), Paragraph("Value proposition clarity", body_style)],
    [Paragraph("competitive-analysis", body_style), Paragraph("deanpeters/Product-Manager-Skills", body_style), Paragraph("Competitor comparison", body_style)],
    [Paragraph("Playwright MCP", body_style), Paragraph("executeautomation", body_style), Paragraph("Browser automation server", body_style)],
]
story.append(make_table(components, col_widths=[120, 180, 170]))

story.append(Spacer(1, 30))
story.append(hr())
story.append(Paragraph(
    "GitHub: github.com/esmatcm/claude-dev-toolkit",
    ParagraphStyle('Footer', parent=body_style, alignment=TA_CENTER, textColor=HexColor('#999999'))
))

# Build
doc.build(story)
print(f"PDF saved to: {output_path}")
