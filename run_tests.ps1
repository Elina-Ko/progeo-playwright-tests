Write-Host "🧹 Очищаем папку allure-results..." -ForegroundColor Yellow
if (Test-Path "allure-results") { Remove-Item "allure-results" -Recurse -Force }

Write-Host "🚀 Запускаем тесты Playwright..." -ForegroundColor Green
pytest --alluredir=allure-results --disable-warnings -v

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Все тесты успешно завершены!" -ForegroundColor Green
} else {
    Write-Host "⚠️ Есть упавшие тесты." -ForegroundColor Red
}

Write-Host "📊 Генерируем и открываем Allure отчёт..." -ForegroundColor Cyan
Start-Sleep -Seconds 2
allure serve allure-results
