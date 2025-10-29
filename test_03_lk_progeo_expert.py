import pytest
from playwright.sync_api import Page

def test_03_lk_progeo_expert(page: Page):
    url = "https://lk.progeo.expert"

    print(f"🌐 Загружаем {url} ...")
    try:
        page.goto(url, wait_until="networkidle", timeout=60000)
    except Exception as e:
        print(f"⚠️ Ошибка загрузки: {e}")

    print("📍 Текущий адрес:", page.url)
    assert "lk.progeo.expert" in page.url

    try:
        title = page.title()
        print("🪶 Title страницы:", title)
        assert len(title) > 0
    except Exception:
        pytest.fail("❌ Не удалось получить заголовок страницы")


