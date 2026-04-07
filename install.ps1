$skillDir = "$env:USERPROFILE\.claude\skills\setup-project"
if (!(Test-Path $skillDir)) { New-Item -ItemType Directory -Path $skillDir -Force | Out-Null }
Copy-Item -Path "$PSScriptRoot\SKILL.md" -Destination "$skillDir\SKILL.md" -Force

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Claude Dev Toolkit installed!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Skill location: $skillDir\SKILL.md" -ForegroundColor Gray
Write-Host ""
Write-Host "  USAGE:" -ForegroundColor Yellow
Write-Host "  Open Claude Code in any project directory and type:" -ForegroundColor White
Write-Host ""
Write-Host "    /setup-project" -ForegroundColor Green
Write-Host ""
Write-Host "  This single command installs and configures:" -ForegroundColor White
Write-Host "    Phase 1: Knowledge Graph  (understand codebase)" -ForegroundColor Gray
Write-Host "    Phase 2: Site Optimizer   (UX audit + PM analysis)" -ForegroundColor Gray
Write-Host "    Phase 3: Frontend QA      (auto-test on code change)" -ForegroundColor Gray
Write-Host "    Phase 4: Integration      (hooks + MCP + CLAUDE.md)" -ForegroundColor Gray
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
