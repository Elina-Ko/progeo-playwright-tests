import asyncio
from playwright.async_api import async_playwright

async def main():
    url = "https://lk.progeo.expert"

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,  # ОБЯЗАТЕЛЬНО чтобы видеть окно
            args=[
                "--ignore-certificate-errors",
                "--disable-web-security",
                "--allow-running-insecure-content",
            ]
        )

        context = await browser.new_context()
        page = await context.new_page()

        # Ловим новые вкладки (на случай, если ссылка открывает новую)
        context.on("page", lambda new_page: print(f"🆕 Новая вкладка открыта: {new_page.url}"))

        print(f"🌐 Загружаем {url} ...")
        try:
            await page.goto(url, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print(f"⚠️ Ошибка загрузки: {e}")

        # Показываем финальный адрес
        print("📍 Текущий адрес:", page.url)

        # Печатаем тайтл страницы
        try:
            title = await page.title()
            print("🪶 Title страницы:", title)
        except Exception:
            print("❌ Не удалось получить заголовок страницы")

        # Немного подождём, чтобы увидеть окно
        await page.wait_for_timeout(10000)
        await browser.close()

asyncio.run(main())