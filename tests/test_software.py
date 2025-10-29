from playwright.sync_api import Page, expect

def test_progeo_navigation(page: Page):
   
    # Открываем страницу progeo.expert
    page.goto('https://progeo.expert/')
    page.wait_for_timeout(3000)

    # Прокручиваем до элемента Программные решения
    software_link = page.locator("//a[@id='btn-fed3e558-0a9d-4fec-bf62-2d5087da9929']")
    software_link.scroll_into_view_if_needed()
    page.wait_for_timeout(3000)

    # Проверяем, что ссылка есть, активна и содержит текст "К программным решениям№
    expect(software_link).to_be_visible()
    expect(software_link).to_be_enabled()
    expect(software_link).to_have_text('К программным решениям')

    # Нажимаем на ссылку
    software_link.click()
    page.wait_for_timeout(3000)

    # Прокручиваем страницу до элемента ПроГеоСеть
    progeo_web_link = page.locator('//a[@id="btn-7c91da78-4c42-4ed8-92fe-7741b25f4ad6"]')
    progeo_web_link.scroll_into_view_if_needed()
    page.wait_for_timeout(3000)

    # Проверяем, что ссылка есть, активна и содержит текст "Подробнее"
    expect(progeo_web_link).to_be_visible()
    expect(progeo_web_link).to_be_enabled()
    expect(progeo_web_link).to_have_text('Подробнее')

    # Нажимаем на ссылку
    progeo_web_link.click()
    page.wait_for_timeout(3000)

    # Проверяем переход на страницу ПроГеоСеть
    progeo_web_title = page.locator("//div[@id='sppb-addon-d44482f2-2870-4107-b39b-a24139dcb337']")
    expect(progeo_web_title).to_be_visible()



