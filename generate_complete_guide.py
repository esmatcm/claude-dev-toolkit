from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Register Chinese font
font_paths = [
    "C:/Windows/Fonts/msjh.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/simsun.ttc",
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

styles = getSampleStyleSheet()

title_style = ParagraphStyle('T', parent=styles['Title'], fontName=font_name, fontSize=26, spaceAfter=4, textColor=HexColor('#1a1a2e'), alignment=TA_CENTER)
subtitle_style = ParagraphStyle('Sub', parent=styles['Normal'], fontName=font_name, fontSize=11, spaceAfter=16, textColor=HexColor('#666'), alignment=TA_CENTER)
h1 = ParagraphStyle('H1', parent=styles['Heading1'], fontName=font_name, fontSize=18, spaceBefore=16, spaceAfter=8, textColor=HexColor('#16213e'))
h2 = ParagraphStyle('H2', parent=styles['Heading2'], fontName=font_name, fontSize=13, spaceBefore=12, spaceAfter=6, textColor=HexColor('#0f3460'))
body = ParagraphStyle('B', parent=styles['Normal'], fontName=font_name, fontSize=10, spaceAfter=5, leading=15, textColor=HexColor('#333'))
code = ParagraphStyle('C', parent=styles['Code'], fontName='Courier', fontSize=9, spaceAfter=3, backColor=HexColor('#f0f0f0'), borderPadding=4, leftIndent=8)
code_big = ParagraphStyle('CB', parent=code, fontSize=11, spaceAfter=6, borderPadding=8)
bullet = ParagraphStyle('BL', parent=body, leftIndent=18, bulletIndent=8, spaceAfter=3)
highlight = ParagraphStyle('HL', parent=body, backColor=HexColor('#e8f4f8'), borderPadding=10, leftIndent=8, rightIndent=8, spaceAfter=10)
warn = ParagraphStyle('W', parent=body, backColor=HexColor('#fff3cd'), borderPadding=10, leftIndent=8, rightIndent=8, spaceAfter=10)
step_title = ParagraphStyle('ST', parent=body, fontSize=12, fontName=font_name, textColor=HexColor('#16213e'), spaceBefore=10, spaceAfter=4)
you_style = ParagraphStyle('You', parent=code, textColor=HexColor('#0f3460'), fontSize=10, borderPadding=6)
ai_style = ParagraphStyle('AI', parent=body, leftIndent=10, textColor=HexColor('#444'), fontSize=9.5)

def hr():
    return HRFlowable(width="100%", thickness=1, color=HexColor('#ddd'), spaceAfter=8, spaceBefore=8)

def make_table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#16213e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#fff')),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#ccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#fff'), HexColor('#f9f9f9')]),
    ]))
    return t

P = lambda t, s=body: Paragraph(t, s)

output_path = os.path.expanduser("~/Desktop/Claude_Dev_Toolkit_Complete_Guide.pdf")
doc = SimpleDocTemplate(output_path, pagesize=A4,
    topMargin=22*mm, bottomMargin=18*mm, leftMargin=18*mm, rightMargin=18*mm)

story = []

# ═══════ COVER ═══════
story.append(Spacer(1, 60))
story.append(P("Claude Dev Toolkit", title_style))
story.append(P("Complete Guide: Installation + Usage", subtitle_style))
story.append(hr())
story.append(Spacer(1, 10))
story.append(P(
    "<b>Prerequisites</b>: Python 3.10+ / Node.js 18+ / Git / Claude Code (Desktop or CLI)<br/>"
    "<b>GitHub</b>: github.com/esmatcm/claude-dev-toolkit<br/>"
    "<b>Install time</b>: ~5 minutes (one-time) + ~3 minutes per project",
    highlight
))
story.append(Spacer(1, 20))
story.append(P(
    "<b>What is this?</b><br/><br/>"
    "A single command that turns Claude into a full development team:<br/>"
    "- Knowledge Graph: understand any codebase instantly<br/>"
    "- UX Audit: browse your site as a real user, find friction<br/>"
    "- PM Analysis: think like a boss, prioritize what to fix<br/>"
    "- Frontend QA: auto-test after every code change<br/><br/>"
    "After setup, you just talk. Everything else is automatic.",
    body
))
story.append(PageBreak())

# ═══════ PART 1: INSTALLATION ═══════
story.append(P("Part 1: Installation (New Computer)", h1))
story.append(hr())

story.append(P(
    "IMPORTANT: This section only needs to be done ONCE per computer. "
    "After installation, the skill is permanently available across all projects.",
    warn
))

story.append(P("Step 1: Check Prerequisites", h2))
story.append(P("Open a terminal and verify:", body))
story.append(P("python --version        # needs 3.10+", code))
story.append(P("node --version           # needs 18+", code))
story.append(P("git --version", code))
story.append(P("If any is missing, install from python.org / nodejs.org / git-scm.com", body))

story.append(P("Step 2: Clone and Install the Toolkit", h2))
story.append(P("git clone https://github.com/esmatcm/claude-dev-toolkit.git", code_big))
story.append(P("cd claude-dev-toolkit", code_big))
story.append(Spacer(1, 4))
story.append(P("Windows (PowerShell):", body))
story.append(P(".\\install.ps1", code_big))
story.append(P("macOS / Linux:", body))
story.append(P("chmod +x install.sh && ./install.sh", code_big))
story.append(Spacer(1, 6))
story.append(P(
    "This copies the skill file to ~/.claude/skills/setup-project/SKILL.md<br/>"
    "You can delete the cloned folder after install.",
    ai_style
))

story.append(P("Step 3: Verify", h2))
story.append(P("Open Claude Code (desktop or CLI) in any directory and check:", body))
story.append(P("Type: /setup-project --status", code))
story.append(P("If it responds, the skill is installed.", body))

story.append(P(
    "Installation complete. Now go to Part 2 for per-project setup.",
    highlight
))
story.append(PageBreak())

# ═══════ PART 2: PER-PROJECT SETUP ═══════
story.append(P("Part 2: Per-Project Setup", h1))
story.append(hr())
story.append(P("Every time you enter a new project, run this ONE command:", body))
story.append(Spacer(1, 4))
story.append(P("/setup-project", code_big))
story.append(Spacer(1, 6))

story.append(P("What happens automatically:", body))
phase_data = [
    [P("<b>Phase</b>"), P("<b>What it does</b>"), P("<b>Duration</b>")],
    [P("1. Knowledge Graph"), P("AST extract, community detect, build graph, install git hooks"), P("30-60 sec")],
    [P("2. Site Optimizer"), P("Install UX audit + 7 PM skills + Playwright browser"), P("1-2 min")],
    [P("3. Frontend QA"), P("Install 8 AI sub-agents, fix Windows encoding, Playwright"), P("1-2 min")],
    [P("4. Integration"), P("Configure MCP, hooks (Pre+Post), update CLAUDE.md"), P("10 sec")],
]
story.append(make_table(phase_data, col_widths=[110, 260, 100]))
story.append(Spacer(1, 10))
story.append(P(
    "IMPORTANT: After setup, close and reopen Claude Code ONCE.<br/>"
    "This loads the Playwright MCP server. Verify with /mcp.",
    warn
))
story.append(P("After restart, you are ready. Go to Part 3.", body))
story.append(PageBreak())

# ═══════ PART 3: USAGE ═══════
story.append(P("Part 3: Daily Usage (Just Talk)", h1))
story.append(hr())
story.append(P(
    "After setup, you never need to type commands again. Just talk to Claude naturally. "
    "The following scenarios show exactly what to say.",
    body
))
story.append(Spacer(1, 10))

# ── Scenario: Full Optimization ──
story.append(P("Scenario: Full Website Optimization", h2))
story.append(P("You have a website (e.g. ai.xxcvd.com) and want to fully optimize it.", body))
story.append(Spacer(1, 8))

# Step 1
story.append(P("<b>Step 1: Find All Problems</b>", step_title))
story.append(P("You:", body))
story.append(P("ux audit ai.xxcvd.com", you_style))
story.append(P(
    "Claude opens a real browser, navigates every page as a first-time user, "
    "tracks friction (confusion, anxiety, dead ends), tests responsive layouts, "
    "checks console errors, and produces a ranked report:",
    ai_style
))
story.append(Spacer(1, 4))
report_data = [
    [P("<b>Severity</b>"), P("<b>Issue</b>")],
    [P("Critical"), P("Homepage loads in 4.2s - users will leave")],
    [P("Critical"), P("Mobile nav menu does not open")],
    [P("High"), P("Login button too small - took 3 taps to hit")],
    [P("High"), P("No feedback after form submit - user unsure if it worked")],
    [P("Medium"), P("Dark mode text contrast too low")],
    [P("Medium"), P("Search field has no placeholder hint")],
    [P(""), P("")],
    [P("<b>Fix first</b>"), P("Mobile nav menu")],
    [P("<b>Would user return?</b>"), P("Unlikely - mobile experience too poor")],
]
story.append(make_table(report_data, col_widths=[110, 360]))
story.append(Spacer(1, 12))

# Step 2
story.append(P("<b>Step 2: Decide What to Fix First</b>", step_title))
story.append(P("You:", body))
story.append(P("prioritization-advisor", you_style))
story.append(P("Claude asks about your product stage and user count, then:", ai_style))
story.append(Spacer(1, 4))
pri_data = [
    [P("<b>#</b>"), P("<b>Task</b>"), P("<b>Impact</b>"), P("<b>Confidence</b>"), P("<b>Effort</b>"), P("<b>Priority</b>")],
    [P("1"), P("Fix mobile nav"), P("High"), P("High"), P("Small"), P("Do first")],
    [P("2"), P("Add form feedback"), P("High"), P("High"), P("Small"), P("Second")],
    [P("3"), P("Optimize page load"), P("High"), P("Medium"), P("Large"), P("Third")],
    [P("4"), P("Dark mode contrast"), P("Low"), P("High"), P("Small"), P("Later")],
]
story.append(make_table(pri_data, col_widths=[25, 120, 65, 80, 65, 115]))
story.append(Spacer(1, 12))

# Step 3
story.append(P("<b>Step 3: Fix It (Auto-Verified)</b>", step_title))
story.append(P("You:", body))
story.append(P("Fix the mobile nav menu so it opens on phones", you_style))
story.append(P(
    "Claude automatically:<br/>"
    "1. Consults knowledge graph -> finds SiteNav.tsx<br/>"
    "2. Reads code -> missing mobile menu toggle<br/>"
    "3. Modifies SiteNav.tsx<br/>"
    "4. PostToolUse hook auto-triggers -><br/>"
    "5. Opens browser at 375px mobile width -> screenshot<br/>"
    "6. AI validates: 'Nav opens but covers logo'<br/>"
    "7. Auto-fixes z-index<br/>"
    "8. Re-screenshots -> PASS<br/>"
    "9. Reports to you with screenshot proof",
    ai_style
))
story.append(Spacer(1, 8))

# Step 4
story.append(P("<b>Step 4: Confirm and Continue</b>", step_title))
story.append(P("You:", body))
story.append(P("OK. Add form submit feedback next.", you_style))
story.append(P("Claude repeats the same auto-verified cycle for the next task.", ai_style))
story.append(Spacer(1, 8))

# Step 5
story.append(P("<b>Step 5: See the Big Picture</b>", step_title))
story.append(P("You:", body))
story.append(P("customer-journey-map", you_style))
story.append(P(
    "Claude maps the full user journey:<br/><br/>"
    "Homepage -> Browse Features -> Sign Up -> First Use -> Return Visit<br/><br/>"
    "Drop-off point: Sign Up -> First Use (65% lost)<br/>"
    "Reason: No onboarding guide after registration<br/>"
    "Suggestion: Add guided first-use tutorial",
    ai_style
))

story.append(PageBreak())

# ═══════ COMMAND REFERENCE ═══════
story.append(P("Part 4: Command Quick Reference", h1))
story.append(hr())

story.append(P("Find Problems (User Perspective)", h2))
cmd1 = [
    [P("<b>You say</b>"), P("<b>What happens</b>"), P("<b>Time</b>")],
    [P("ux audit [url]"), P("Standard user walkthrough"), P("20-40 min")],
    [P("ux audit [url] quick"), P("Quick spot check"), P("5-10 min")],
    [P("ux audit [url] thorough"), P("Deep audit, all pages, 3 personas"), P("1-3 hrs")],
    [P("ux audit [url] exhaustive"), P("Every element on every page"), P("4-8+ hrs")],
    [P("qa sweep"), P("Systematic test: all pages, CRUD, states"), P("30-60 min")],
    [P("dogfood this"), P("Same as ux audit"), P("20-40 min")],
]
story.append(make_table(cmd1, col_widths=[150, 210, 110]))
story.append(Spacer(1, 10))

story.append(P("Analyze (Boss/PM Perspective)", h2))
cmd2 = [
    [P("<b>You say</b>"), P("<b>What happens</b>")],
    [P("prioritization-advisor"), P("RICE/ICE framework: what to fix first, ranked by impact")],
    [P("customer-journey-map"), P("Map full user journey, find drop-off points")],
    [P("product-strategy-session"), P("Full strategy workshop: positioning, roadmap, planning")],
    [P("jobs-to-be-done"), P("What job are users hiring the product for?")],
    [P("positioning-statement"), P("Create clear value proposition")],
    [P("competitive-analysis"), P("Compare with competitors")],
    [P("discovery-process"), P("Structured user need discovery cycle")],
]
story.append(make_table(cmd2, col_widths=[160, 310]))
story.append(Spacer(1, 10))

story.append(P("Develop & Test", h2))
cmd3 = [
    [P("<b>You say</b>"), P("<b>What happens</b>")],
    [P("(describe what to fix)"), P("Claude modifies code -> auto-tests -> auto-fixes -> reports")],
    [P("/frontend-dev"), P("Full closed-loop: code > test > AI validate > auto-fix > re-test")],
    [P("/test-frontend"), P("Quick visual validation of current state")],
    [P("/graphify ."), P("Rebuild knowledge graph manually")],
    [P("/setup-project"), P("Full setup for a new project")],
]
story.append(make_table(cmd3, col_widths=[160, 310]))
story.append(Spacer(1, 10))

story.append(P("Full-check (one sentence)", h2))
story.append(P(
    "Copy and paste this to Claude for a comprehensive site audit:",
    body
))
story.append(Spacer(1, 4))
story.append(P(
    "ux audit ai.xxcvd.com",
    code_big
))
story.append(P("Replace ai.xxcvd.com with your actual URL.", ai_style))
story.append(PageBreak())

# ═══════ WHAT'S AUTOMATIC ═══════
story.append(P("Part 5: What Happens Automatically", h1))
story.append(hr())
story.append(P("After /setup-project, these hooks run without you doing anything:", body))
story.append(Spacer(1, 8))

auto_data = [
    [P("<b>Trigger</b>"), P("<b>What happens</b>"), P("<b>Why</b>")],
    [P("You ask about architecture"), P("Claude checks knowledge graph first"), P("Faster, more accurate answers")],
    [P("Any .tsx/.jsx/.css is modified"), P("Browser opens, screenshots, AI validates"), P("Auto-verify before you see it")],
    [P("git commit"), P("Knowledge graph rebuilds"), P("Graph stays current")],
    [P("Branch switch"), P("Knowledge graph rebuilds"), P("Graph matches branch")],
    [P("Daily ~9:17 AM"), P("Full graph rebuild"), P("Stay fresh")],
]
story.append(make_table(auto_data, col_widths=[150, 190, 130]))
story.append(Spacer(1, 14))

story.append(P("Summary: Your Role vs Claude's Role", h2))
you_vs_ai = [
    [P("<b>You</b>"), P("<b>Claude (automatic)</b>")],
    [P("See a problem"), P("-")],
    [P("Describe what to fix"), P("Finds files via knowledge graph")],
    [P("-"), P("Modifies code")],
    [P("-"), P("Opens browser, tests, screenshots")],
    [P("-"), P("AI validates result")],
    [P("-"), P("Auto-fixes if issues found")],
    [P("-"), P("Re-tests until pass")],
    [P("Review final result"), P("Reports with screenshots")],
    [P("Say OK or give feedback"), P("-")],
]
story.append(make_table(you_vs_ai, col_widths=[200, 270]))
story.append(Spacer(1, 20))

story.append(P(
    "You talk. Claude does everything else.<br/><br/>"
    "GitHub: github.com/esmatcm/claude-dev-toolkit",
    ParagraphStyle('Footer', parent=body, alignment=TA_CENTER, textColor=HexColor('#999'), fontSize=10)
))

doc.build(story)
print(f"PDF saved to: {output_path}")
