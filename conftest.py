import os
import time
import pytest
import allure
from datetime import datetime
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """Создаёт браузер с поддержкой slow_mo (если задано через переменную окружения)."""
    with sync_playwright() as p:
        slow_mo = int(os.getenv("PLAYWRIGHT_SLOWMO", "0"))  # 🐢 задержка между действиями
        headless = os.getenv("HEADLESS", "false").lower() == "true"

        browser = p.chromium.launch(headless=headless, slow_mo=slow_mo)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser, request):
    """Создаёт страницу, записывает видео, логи, скриншоты и прикрепляет их к Allure."""
    test_name = request.node.name.replace("/", "_")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    os.makedirs("artifacts/videos", exist_ok=True)
    os.makedirs("artifacts/logs", exist_ok=True)
    os.makedirs("artifacts/screenshots", exist_ok=True)

    context = browser.new_context(
        viewport={"width": 1400, "height": 900},
        record_video_dir="artifacts/videos"
    )
    page = context.new_page()

    log_file_path = f"artifacts/logs/{test_name}_{timestamp}.log"

    def log_console_message(msg):
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(f"[console] {msg.type.upper()}: {msg.text}\n")

    def log_request(request_event):
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(f"[request] {request_event.method} {request_event.url}\n")

    def log_response(response):
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(f"[response] {response.status} {response.url}\n")

    page.on("console", log_console_message)
    page.on("request", log_request)
    page.on("response", log_response)

    yield page  # 🧪 здесь выполняется тест

    # Ждём, чтобы Playwright успел записать видео
    time.sleep(1.2)

    video_path = None
    try:
        # Закрываем контекст и ждём завершения видео
        context.close()
        time.sleep(1.0)

        # Находим последнее записанное видео
        video_dir = os.path.join("artifacts", "videos")
        videos = sorted(
            [os.path.join(video_dir, f) for f in os.listdir(video_dir)],
            key=os.path.getmtime,
            reverse=True
        )

        if videos:
            original_path = videos[0]
            new_video_name = f"{test_name}_{timestamp}.webm"
            new_video_path = os.path.join(video_dir, new_video_name)
            os.rename(original_path, new_video_path)
            video_path = new_video_path
            print(f"🎥 Видео сохранено: {video_path}")

            # === Превью ===
            try:
                import imageio.v3 as iio
                from PIL import Image
                frames = list(iio.imiter(video_path))
                mid_frame = frames[len(frames) // 2]
                preview_path = os.path.join(video_dir, f"{test_name}_{timestamp}_preview.png")
                Image.fromarray(mid_frame).save(preview_path)
                allure.attach.file(preview_path, name="🖼️ Превью", attachment_type=allure.attachment_type.PNG)
                print(f"🖼️ Превью создано: {preview_path}")
            except Exception as e:
                print(f"⚠️ Не удалось создать превью: {e}")

    except Exception as e:
        print(f"⚠️ Ошибка при сохранении видео: {e}")

    # === Скриншот при падении ===
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_path = f"artifacts/screenshots/{test_name}_{timestamp}.png"
        try:
            page.screenshot(path=screenshot_path, full_page=True)
            allure.attach.file(screenshot_path, name="📸 Скриншот", attachment_type=allure.attachment_type.PNG)
            print(f"📸 Скриншот сохранён: {screenshot_path}")
        except Exception as e:
            print(f"⚠️ Не удалось сделать скриншот: {e}")

    # === Логи и видео ===
    if os.path.exists(log_file_path):
        allure.attach.file(log_file_path, name="📄 Логи", attachment_type=allure.attachment_type.TEXT)
    if video_path and os.path.exists(video_path):
        print(f"📎 Прикрепляем видео в Allure: {video_path}")
        allure.attach.file(video_path, name="🎥 Видео", attachment_type=allure.attachment_type.WEBM)