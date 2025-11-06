import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime
import os
import time
import allure


# --- 1️⃣ хук: сохраняет статус теста ---
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# --- 2️⃣ создаём браузер ---
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


# --- 3️⃣ создаём страницу ---
@pytest.fixture()
def page(browser, request):
    test_name = request.node.name.replace("/", "_")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    artifacts_dir = "artifacts"
    os.makedirs(f"{artifacts_dir}/videos", exist_ok=True)
    os.makedirs(f"{artifacts_dir}/logs", exist_ok=True)
    os.makedirs(f"{artifacts_dir}/screenshots", exist_ok=True)

    context = browser.new_context(
        viewport={"width": 1400, "height": 900},
        record_video_dir=f"{artifacts_dir}/videos"
    )
    page = context.new_page()

    # логирование консоли
    log_path = f"{artifacts_dir}/logs/{test_name}_{timestamp}.log"

    def log_console(msg):
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[console] {msg.type.upper()}: {msg.text}\n")

    page.on("console", log_console)
    yield page

    # после теста: закрываем контекст, ждём видео
    context.close()
    time.sleep(1)

    # сохраняем последнее видео
    video_path = None
    try:
        videos = sorted(
            [os.path.join(f"{artifacts_dir}/videos", f) for f in os.listdir(f"{artifacts_dir}/videos")],
            key=os.path.getmtime,
            reverse=True
        )
        if videos:
            original = videos[0]
            video_path = f"{artifacts_dir}/videos/{test_name}_{timestamp}.webm"
            os.rename(original, video_path)
            print(f"🎥 Видео сохранено: {video_path}")
    except Exception as e:
        print(f"⚠️ Видео не найдено: {e}")

    # сохраняем пути для последующего прикрепления
    request.node.video_path = video_path
    request.node.log_path = log_path
    request.node.screenshot_path = f"{artifacts_dir}/screenshots/{test_name}_{timestamp}.png"
    request.node.page = page


# --- 4️⃣ прикрепляем всё в отчёт ---
@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
    """Добавляем вложения, когда тест уже завершён и Allure в контексте."""
    if not hasattr(item, "rep_call"):
        return

    # логи
    if hasattr(item, "log_path") and os.path.exists(item.log_path):
        allure.attach.file(item.log_path, name="📄 Логи", attachment_type=allure.attachment_type.TEXT)

    # видео
    if hasattr(item, "video_path") and item.video_path and os.path.exists(item.video_path):
        allure.attach.file(item.video_path, name="🎥 Видео", attachment_type=allure.attachment_type.WEBM)

    # скриншот, если тест упал
    if item.rep_call.failed and hasattr(item, "page"):
        try:
            item.page.screenshot(path=item.screenshot_path, full_page=True)
            allure.attach.file(item.screenshot_path, name="📸 Скриншот", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"⚠️ Не удалось сделать скриншот: {e}")