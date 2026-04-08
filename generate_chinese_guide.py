from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Chinese font
for fp in ["C:/Windows/Fonts/msjh.ttc", "C:/Windows/Fonts/msyh.ttc"]:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont("CJK", fp, subfontIndex=0))
            break
        except:
            continue

f = "CJK"
styles = getSampleStyleSheet()

title = ParagraphStyle('T', fontName=f, fontSize=26, spaceAfter=4, textColor=HexColor('#1a1a2e'), alignment=TA_CENTER)
sub = ParagraphStyle('S', fontName=f, fontSize=11, spaceAfter=14, textColor=HexColor('#666'), alignment=TA_CENTER)
h1 = ParagraphStyle('H1', fontName=f, fontSize=18, spaceBefore=16, spaceAfter=8, textColor=HexColor('#16213e'))
h2 = ParagraphStyle('H2', fontName=f, fontSize=13, spaceBefore=12, spaceAfter=6, textColor=HexColor('#0f3460'))
b = ParagraphStyle('B', fontName=f, fontSize=10, spaceAfter=5, leading=16, textColor=HexColor('#333'))
c = ParagraphStyle('C', fontName='Courier', fontSize=10, spaceAfter=4, backColor=HexColor('#f0f0f0'), borderPadding=6, leftIndent=8)
cb = ParagraphStyle('CB', fontName='Courier', fontSize=12, spaceAfter=6, backColor=HexColor('#e8f4f8'), borderPadding=10, leftIndent=8)
hl = ParagraphStyle('HL', fontName=f, fontSize=10, backColor=HexColor('#e8f4f8'), borderPadding=10, leftIndent=8, rightIndent=8, spaceAfter=10, leading=16, textColor=HexColor('#333'))
warn = ParagraphStyle('W', fontName=f, fontSize=10, backColor=HexColor('#fff3cd'), borderPadding=10, leftIndent=8, rightIndent=8, spaceAfter=10, leading=16, textColor=HexColor('#333'))
st = ParagraphStyle('ST', fontName=f, fontSize=12, textColor=HexColor('#16213e'), spaceBefore=10, spaceAfter=4)
you = ParagraphStyle('You', fontName='Courier', fontSize=11, textColor=HexColor('#0f3460'), backColor=HexColor('#e8f4f8'), borderPadding=8, leftIndent=8, spaceAfter=4)
ai = ParagraphStyle('AI', fontName=f, fontSize=9.5, leftIndent=10, textColor=HexColor('#444'), leading=15, spaceAfter=6)
ft = ParagraphStyle('FT', fontName=f, fontSize=9, alignment=TA_CENTER, textColor=HexColor('#999'))

def hr():
    return HRFlowable(width="100%", thickness=1, color=HexColor('#ddd'), spaceAfter=8, spaceBefore=8)

P = lambda t, s=b: Paragraph(t, s)

def T(data, cw=None):
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), HexColor('#16213e')),
        ('TEXTCOLOR', (0,0), (-1,0), HexColor('#fff')),
        ('FONTNAME', (0,0), (-1,-1), f),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#ccc')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor('#fff'), HexColor('#f9f9f9')]),
    ]))
    return t

out = os.path.expanduser("~/Desktop/Claude_Dev_Toolkit_CN.pdf")
doc = SimpleDocTemplate(out, pagesize=A4, topMargin=22*mm, bottomMargin=18*mm, leftMargin=18*mm, rightMargin=18*mm)
s = []

# ═══ 封面 ═══
s.append(Spacer(1, 50))
s.append(P("Claude Dev Toolkit", title))
s.append(P("AI 開發工具包 — 安裝 + 使用指南", sub))
s.append(hr())
s.append(P(
    "<b>前置需求</b>：Python 3.10+ / Node.js 18+ / Git / Claude Code<br/>"
    "<b>倉庫</b>：github.com/esmatcm/claude-dev-toolkit",
    hl
))
s.append(Spacer(1, 16))
s.append(P(
    "一個指令，讓 Claude 變成完整開發團隊：<br/><br/>"
    "- 知識圖譜：秒懂任何程式碼架構<br/>"
    "- UX 審計：開真實瀏覽器，模擬用戶操作，找出所有問題<br/>"
    "- PM 分析：站在老闆角度，排出優先級<br/>"
    "- 前端 QA：改完程式碼自動驗收，通過了才通知你", b))
s.append(PageBreak())

# ═══ 安裝 ═══
s.append(P("一、安裝（新電腦只做一次）", h1))
s.append(hr())
s.append(P("1. 確認前置需求已安裝：", b))
s.append(P("python --version    # 需要 3.10+", c))
s.append(P("node --version      # 需要 18+", c))
s.append(P("git --version", c))
s.append(Spacer(1, 8))
s.append(P("2. 下載並安裝工具包：", b))
s.append(P("git clone https://github.com/esmatcm/claude-dev-toolkit.git", cb))
s.append(P("cd claude-dev-toolkit", cb))
s.append(P(".\\install.ps1                  # Windows", cb))
s.append(P("./install.sh                   # macOS / Linux", cb))
s.append(Spacer(1, 8))
s.append(P("安裝完成後，可以刪除下載的資料夾。技能已經永久安裝到 Claude Code 中。", ai))
s.append(PageBreak())

# ═══ 每個新專案 ═══
s.append(P("二、每個新專案（只需一行）", h1))
s.append(hr())
s.append(P("打開 Claude Code，切換到你的專案目錄，輸入：", b))
s.append(Spacer(1, 4))
s.append(P("/setup-project", cb))
s.append(Spacer(1, 8))
s.append(P(
    "Claude 會自動執行 4 個階段：<br/>"
    "Phase 1：建立知識圖譜（理解程式碼架構）<br/>"
    "Phase 2：安裝 UX 審計 + 7 個 PM 技能<br/>"
    "Phase 3：安裝前端 QA（8 個 AI 子代理）<br/>"
    "Phase 4：配置 hooks、MCP、CLAUDE.md", hl))
s.append(Spacer(1, 8))
s.append(P("完成後，關閉 Claude Code 再重新打開一次（載入 Playwright）。", warn))
s.append(PageBreak())

# ═══ 指令速查 ═══
s.append(P("三、指令速查表", h1))
s.append(hr())

s.append(P("找問題（用戶視角）", h2))
s.append(T([
    [P("<b>你說</b>"), P("<b>Claude 做什麼</b>"), P("<b>時間</b>")],
    [P("ux audit [網址]"), P("模擬真人操作網站，找出所有摩擦點"), P("20-40 分鐘")],
    [P("ux audit [網址] quick"), P("快速檢查，只走主要流程"), P("5-10 分鐘")],
    [P("ux audit [網址] thorough"), P("深度審計：所有頁面、多角色、響應式"), P("1-3 小時")],
    [P("ux audit [網址] exhaustive"), P("窮舉：每個頁面的每個按鈕都點一遍"), P("4-8+ 小時")],
    [P("qa sweep"), P("系統性測試所有頁面的 CRUD 和狀態"), P("30-60 分鐘")],
], cw=[150, 220, 100]))
s.append(Spacer(1, 10))

s.append(P("分析優化（老闆/PM 視角）", h2))
s.append(T([
    [P("<b>你說</b>"), P("<b>Claude 做什麼</b>")],
    [P("prioritization-advisor"), P("用 RICE 框架排出「該先改什麼」的優先級清單")],
    [P("customer-journey-map"), P("畫出用戶旅程地圖，找出流失點")],
    [P("product-strategy-session"), P("完整產品策略工作坊：定位、問題、路線圖")],
    [P("jobs-to-be-done"), P("分析用戶真正想用這個產品做什麼")],
    [P("positioning-statement"), P("產出清晰的產品價值定位")],
    [P("competitive-analysis"), P("跟競品比較，找出差異化優勢")],
    [P("discovery-process"), P("結構化的用戶需求探索流程")],
], cw=[160, 310]))
s.append(Spacer(1, 10))

s.append(P("開發與測試", h2))
s.append(T([
    [P("<b>你說</b>"), P("<b>Claude 做什麼</b>")],
    [P("（直接說要改什麼）"), P("改程式碼 → 自動開瀏覽器驗收 → 通過才告訴你")],
    [P("/frontend-dev"), P("完整閉環：改 → 測 → AI 看 → 修 → 再測（最多 5 次）")],
    [P("/test-frontend"), P("快速驗證當前畫面狀態")],
    [P("/graphify ."), P("手動重建知識圖譜")],
], cw=[160, 310]))
s.append(PageBreak())

# ═══ 情境模擬 ═══
s.append(P("四、完整情境模擬", h1))
s.append(hr())
s.append(P("場景：你有一個網站 ai.xxcvd.com，想全面優化它。", b))
s.append(Spacer(1, 10))

# 情境1
s.append(P("<b>第一步：找問題</b>", st))
s.append(P("ux audit ai.xxcvd.com", you))
s.append(P(
    "Claude 開瀏覽器，模擬用戶操作每個頁面，產出報告：<br/><br/>"
    "Critical：首頁載入 4.2 秒 / 手機版導航點不開<br/>"
    "High：登入按鈕太小 / 表單提交沒回饋<br/>"
    "Medium：暗色模式對比度不足 / 搜尋欄沒提示<br/><br/>"
    "第一件該修的事：手機版導航<br/>"
    "用戶會回來嗎？不太可能，手機體驗太差", ai))
s.append(Spacer(1, 10))

# 情境2
s.append(P("<b>第二步：排優先級</b>", st))
s.append(P("prioritization-advisor", you))
s.append(P(
    "Claude 問你產品階段和用戶量，然後用 RICE 框架排序：<br/><br/>"
    "1. 修手機版導航　　影響:高　信心:高　工作量:小　→ 先做<br/>"
    "2. 加表單提交回饋　影響:高　信心:高　工作量:小　→ 第二<br/>"
    "3. 首頁載入優化　　影響:高　信心:中　工作量:大　→ 第三<br/>"
    "4. 暗色模式對比度　影響:低　信心:高　工作量:小　→ 有空再做", ai))
s.append(Spacer(1, 10))

# 情境3
s.append(P("<b>第三步：開始修（自動驗收）</b>", st))
s.append(P("Fix the mobile nav menu", you))
s.append(P(
    "Claude 自動：<br/>"
    "1. 查知識圖譜 → 找到 SiteNav.tsx<br/>"
    "2. 讀程式碼 → 發現缺少 mobile toggle<br/>"
    "3. 修改程式碼<br/>"
    "4. Hook 自動觸發 → 開瀏覽器 → 切到手機寬度 → 截圖<br/>"
    "5. AI 看截圖：「導航可以開了，但遮住 logo」<br/>"
    "6. 自動修 z-index → 再截圖 → 通過<br/>"
    "7. 給你看最終截圖", ai))
s.append(Spacer(1, 10))

# 情境4
s.append(P("<b>第四步：確認，繼續下一個</b>", st))
s.append(P("OK, next. Add form submit feedback.", you))
s.append(P("Claude 重複相同的自動驗收流程。", ai))
s.append(Spacer(1, 10))

# 情境5
s.append(P("<b>第五步：看全局</b>", st))
s.append(P("customer-journey-map", you))
s.append(P(
    "用戶旅程：首頁 → 瀏覽功能 → 註冊 → 首次使用 → 回訪<br/><br/>"
    "流失點：註冊 → 首次使用（65% 流失）<br/>"
    "原因：註冊後沒有引導，用戶不知道下一步<br/>"
    "建議：加新手引導流程", ai))
s.append(PageBreak())

# ═══ 自動機制 ═══
s.append(P("五、哪些事是自動的（你不用管）", h1))
s.append(hr())
s.append(T([
    [P("<b>觸發時機</b>"), P("<b>自動做什麼</b>")],
    [P("你問架構問題"), P("自動查知識圖譜，不用逐一讀檔案")],
    [P("任何前端檔案被修改"), P("自動開瀏覽器截圖 → AI 驗收 → 有問題自動修")],
    [P("git commit"), P("自動重建知識圖譜")],
    [P("切換 git 分支"), P("自動重建知識圖譜")],
    [P("每天早上 ~9:17"), P("定時重建知識圖譜")],
], cw=[160, 310]))
s.append(Spacer(1, 20))

s.append(P("總結", h2))
s.append(P(
    "新電腦：裝一次 install.ps1<br/>"
    "新專案：打一次 /setup-project<br/>"
    "之後：直接說話，其他都是自動的", hl))

s.append(Spacer(1, 30))
s.append(P("github.com/esmatcm/claude-dev-toolkit", ft))

doc.build(s)
print(f"PDF saved to: {out}")
