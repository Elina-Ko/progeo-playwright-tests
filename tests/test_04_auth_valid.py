from playwright.sync_api import Page, expect
import allure

@allure.title("Проверяем открытие страницы ПроГеоСеть")
def test_04_auth_valid(page: Page):

    page.goto('https://lk.progeo.expert/')

    with allure.step("Проверяем, что поле Порт существует"):
        port_input = page.locator('//input[@id="port"]')
        expect(port_input).to_be_visible()

    with allure.step("Заполняем поле Порт валидным значением"):
        port_input.fill('2120')

    with allure.step("Проверяем, что поле Логин существует"):
        login_input = page.locator('//input[@id="login"]')
        expect(login_input).to_be_visible()

    with allure.step("Заполняем поле Логин валидным значением"):
        login_input.fill('TestUser')

    with allure.step("Проверяем, что поле Пароль существует"):
        password_input = page.locator('//input[@id="pswd"]')
        expect(password_input).to_be_visible()

    with allure.step("Заполняем поле Пароль валидным значением"):
        password_input.fill('passWord1#%')

    with allure.step("Проверяем, что кнопка Вход существует"):
        login_button = page.locator('//input[@id="submit"]')
        expect(login_button).to_be_visible()

    with allure.step("Проверяем, что кнопка Вход активна"):
        expect(login_button).to_be_enabled()

    with allure.step("Проверяем, что кнопка Вход содержит текст Вход"):
        expect(login_button).to_have_text('Вход')

    with allure.step("Нажимаем на кнопку Вход"):
        login_button.click()

    # Тест не проверяет вход в систему, так как отсутствуют валидные тестовые
    # данные для авторизации