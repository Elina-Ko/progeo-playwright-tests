from playwright.sync_api import Page
import allure

@allure.title("Проверка обязательности полей ввода в форме авторизации'")
def test_fields_required(page: Page):
    page.goto('https://lk.progeo.expert/')


    with allure.step("Проверяем наличие атрибута required у поля 'Порт'"):
        port_input = page.locator('//input[@id="port"]')
        port_req =  port_input.get_attribute('required')
        if port_req is None:
            allure.attach(
                body="Атрибут required отсутствует у поля 'Порт'.",
                name="❌ Ошибка проверки обязательности",
                attachment_type=allure.attachment_type.TEXT
            )
            raise AssertionError("❌ Поле 'Порт' должно быть обязательным (атрибут required отсутствует).")
        else:
            allure.attach(
                body="Атрибут required найден. Всё ок ✅",
                name="✅ Проверка обязательности прошла успешно",
                attachment_type=allure.attachment_type.TEXT
            )
    with allure.step("Проверяем наличие атрибута required у поля 'Логин'"):
        login_input = page.locator('//input[@id="login"]')
        login_req = login_input.get_attribute('required')
        if login_req is None:
            allure.attach(
                body="Атрибут required отсутствует у поля 'Логин'.",
                name="❌ Ошибка проверки обязательности",
                attachment_type=allure.attachment_type.TEXT
            )
            raise AssertionError("❌ Поле 'Логин' должно быть обязательным (атрибут required отсутствует).")
        else:
            allure.attach(
                body="Атрибут required найден. Всё ок ✅",
                name="✅ Проверка обязательности прошла успешно",
                attachment_type=allure.attachment_type.TEXT
            )
    with allure.step("Проверяем наличие атрибута required у поля 'Пароль'"):
        password_input = page.locator('//input[@id="pswd"]')
        password_req = password_input.get_attribute('required')
        if password_req is None:
            allure.attach(
                body="Атрибут required отсутствует у поля 'Пароль'.",
                name="❌ Ошибка проверки обязательности",
                attachment_type=allure.attachment_type.TEXT
            )
            raise AssertionError("❌ Поле 'Пароль' должно быть обязательным (атрибут required отсутствует).")
        else:
            allure.attach(
                body="Атрибут required найден. Всё ок ✅",
                name="✅ Проверка обязательности прошла успешно",
                attachment_type=allure.attachment_type.TEXT
            )



