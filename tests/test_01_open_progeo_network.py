from playwright.sync_api import Page, expect
import pytest

# Проверяем открытие страницы ПроГеоСеть
def test_open_progeo_network(page: Page):
    # Открываем страницу progeo.expert
    page.goto('https://progeo.expert/')

    # Прокручиваем до элемента Программные решения
    software_link = page.locator("//a[@id='btn-fed3e558-0a9d-4fec-bf62-2d5087da9929']")
    software_link.scroll_into_view_if_needed()

    # Проверяем, что ссылка есть, активна и содержит текст "К программным решениям№
    expect(software_link).to_be_visible()
    expect(software_link).to_be_enabled()
    expect(software_link).to_have_text('К программным решениям')

    # Нажимаем на ссылку
    software_link.click()

    # Прокручиваем страницу до элемента ПроГеоСеть
    progeo_web_link = page.locator('//a[@id="btn-7c91da78-4c42-4ed8-92fe-7741b25f4ad6"]')
    progeo_web_link.scroll_into_view_if_needed()

    # Проверяем, что ссылка есть, активна и содержит текст "Подробнее"
    expect(progeo_web_link).to_be_visible()
    expect(progeo_web_link).to_be_enabled()
    expect(progeo_web_link).to_have_text('Подробнее')

    # Нажимаем на ссылку
    progeo_web_link.click()

    # Проверяем переход на страницу ПроГеоСеть
    progeo_web_title = page.locator("//div[@id='sppb-addon-d44482f2-2870-4107-b39b-a24139dcb337']")
    expect(progeo_web_title).to_be_visible()

# Проверяем открытие документа Руководство пользователя
def test_open_tutorial(page: Page):
    page.goto('https://progeo.expert/solutions/services/progeonet')

    # Ищем Руководство пользователя и проверяем, что ссылка видна и активна
    tutorial = page.locator('//a[@id="btn-e78b1bd5-7ac1-4e89-bf22-7a34cd9d506a"]')
    expect(tutorial).to_be_visible()
    expect(tutorial).to_be_enabled()

    # Кликаем по ссылке и проверяем что документ существует (не пустой)
    tutorial.click()
    expect(page.locator('body')).not_to_be_empty()

    page.wait_for_timeout(2)

# Проверяем открытие личного кабинета через документ Руководство пользователя
def test_lk_progeo_expert(page: Page):
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

    page.wait_for_timeout(2)


