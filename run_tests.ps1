param(
    [switch]$Slow,
    [string]$TestPath = "tests"   # ← новый параметр
)

# ======================================
# 🚀 ProGeo UI Autotests — Run Script
# ======================================

Write-Host "🧹 Очистка старых данных..." -ForegroundColor Yellow

$foldersToClean = @(
    "allure-results",
    "allure-report",
    "artifacts",
    "playwright-report",
    "test-results",
    "reports",
    "pytest_cache"
)

foreach ($folder in $foldersToClean) {
    if (Test-Path $folder) {
        Write-Host "  - Удаляем $folder ..." -ForegroundColor DarkYellow
        Remove-Item $folder -Recurse -Force -ErrorAction SilentlyContinue
    }
}

Write-Host "✅ Очистка завершена!" -ForegroundColor Green
Start-Sleep -Seconds 1

# ======================================
# ⚙️ Настройка режима запуска
# ======================================
$env:PLAYWRIGHT_SLOWMO = if ($Slow) { "500" } else { "0" }

if ($Slow) {
    Write-Host "🐢 Режим замедленного выполнения включён (slow_mo=500)" -ForegroundColor Cyan
} else {
    Write-Host "⚡ Обычный режим выполнения (без замедления)" -ForegroundColor Gray
}

Start-Sleep -Seconds 1

# ======================================
# 🔥 Запуск тестов
# ======================================
Write-Host "🚀 Запускаем тесты Playwright..." -ForegroundColor Green

pytest $TestPath --alluredir=allure-results --disable-warnings -v

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Все тесты успешно завершены!" -ForegroundColor Green
} else {
    Write-Host "⚠️ Есть упавшие тесты." -ForegroundColor Red
}

# ======================================
# 📊 Генерация и просмотр отчёта Allure
# ======================================
Write-Host "📊 Генерируем и открываем Allure отчёт..." -ForegroundColor Cyan
Start-Sleep -Seconds 2

allure serve allure-results