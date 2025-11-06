from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://lk.progeo.expert/')

    # Проверяем, что поле Порт существует
    port_input = page.locator('//input[@id="port"]')
    expect(port_input).to_be_visible()

    # Заполняем поле Порт валидным значением
    port_input.fill('2120')
    page.wait_for_timeout(1000)

    # Проверяем, что поле Логин существует
    login_input = page.locator('//input[@id="login"]')
    expect(login_input).to_be_visible()

    # Заполняем поле Логин валидным значением
    login_input.fill('TestUser')
    page.wait_for_timeout(1000)

    # Проверяем, что поле Пароль существует
    password_input = page.locator('//input[@id="pswd"]')
    expect(password_input).to_be_visible()

    # Заполняем поле Пароль валидным значением
    password_input.fill('passWord1#%')
    page.wait_for_timeout(1000)

    # Проверяем, что кнопка Вход существует
    login_button = page.locator('//input[@id="submit"]')
    expect(login_button).to_be_visible()

    # Проверяем, что кнопка Вход активна
    expect(login_button).to_be_enabled()

    # Проверяем, что кнопка Вход содержит текст Вход
    expect(login_button).to_have_text('Вход')

    # Нажимаем на кнопку Вход
    login_button.click()

    page.wait_for_timeout(1000)

    # Тест не проверяет вход в систему, так как отсутствуют валидные тестовые
    # данные для авторизации