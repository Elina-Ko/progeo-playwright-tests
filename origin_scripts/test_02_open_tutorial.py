
import  time
from playwright.sync_api import Page, expect

def test_02_tutorial(page: Page):

    # Открываем страницу ПроГеоСеть
    page.goto('https://progeo.expert/solutions/services/progeonet')

    # Ищем Руководство пользователя и проверяем, что ссылка видна и активна
    tutorial = page.locator('//a[@id="btn-e78b1bd5-7ac1-4e89-bf22-7a34cd9d506a"]')
    expect(tutorial).to_be_visible()
    expect(tutorial).to_be_enabled()

    # Кликаем по ссылке и проверяем что документ существует (не пустой)
    tutorial.click()
    expect(page.locator('body')).not_to_be_empty()

    time.sleep(2)


