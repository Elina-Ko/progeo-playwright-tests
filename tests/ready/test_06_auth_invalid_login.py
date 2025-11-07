from playwright.sync_api import Page, expect

def test_06_auth_invalid_login(page: Page):

    page.goto('https://lk.progeo.expert/')

    # Проверяем, что поле Порт существует
    port_input = page.locator('//input[@id="port"]')
    expect(port_input).to_be_visible()

    # Заполняем поле Порт валидным значением
    port_input.fill('2120')

    # Проверяем, что поле Логин существует
    login_input = page.locator('//input[@id="login"]')
    expect(login_input).to_be_visible()

    # Заполняем поле Логин невалидным значением (заодно проверяем регистрозависимость)
    login_input.fill('testuser')

    # Проверяем, что поле Пароль существует
    password_input = page.locator('//input[@id="pswd"]')
    expect(password_input).to_be_visible()

    # Заполняем поле Пароль валидным значением
    password_input.fill('passWord1#%')

    # Проверяем, что кнопка Вход существует
    login_button = page.locator('//input[@id="submit"]')
    expect(login_button).to_be_visible()

    # Проверяем, что кнопка Вход активна
    expect(login_button).to_be_enabled()

    # Проверяем, что кнопка Вход содержит текст Вход
    expect(login_button).to_have_text('Вход')

    # Нажимаем на кнопку Вход
    login_button.click()

    # Проверяем, что появляется предупреждение об ошибке
    alert = page.locator('//div[@id="info_cont"]')
    expect(alert).to_be_visible()

    # Проверяем, предупреждение об ошибке содержит текст Неверные учётные данные
    alert_message = page.locator('//span[@id="info-mess"]')
    expect(alert_message).to_have_text('Неверные учётные данные')

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



