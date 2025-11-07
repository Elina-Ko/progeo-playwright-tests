from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://lk.progeo.expert/')

    # Проверяем, что поле Порт существует
    port_input = page.locator('//input[@id="port"]')
    expect(port_input).to_be_visible()

    # Заполняем поле Порт невалидным значением (заодно проверяем ввод отрицательного значения)
    port_input.fill('-2120')
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

    # Заполняем поле Пароль невалидным значением
    password_input.fill('Word1#%')
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

    # Проверяем, что появляется предупреждение об ошибке
    alert = page.locator('//div[@id="info_cont"]')
    expect(alert).to_be_visible()
    page.wait_for_timeout(1000)

    # Проверяем, предупреждение об ошибке содержит текст Нет связи с кастером
    alert_message = page.locator('//span[@id="info-mess"]')
    expect(alert_message).to_have_text('Нет связи с кастером')

    # Проверяем наличие кнопки Ок
    ok_button = alert.locator('//div[@id="confirm-ok"]')
    expect(ok_button).to_be_visible()

    # Проверяем, что кнопка активна
    expect(ok_button).to_be_enabled()

    # Проверяем, что кнопка содержит текст Ок
    expect(ok_button).to_have_text('OK')

    # Нажимаем на кнопку ОК
    ok_button.click()

    # Проверяем, что сообщение об ощибке пропало
    expect(ok_button).to_be_hidden()



