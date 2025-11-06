# ProGeo Playwright Tests
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Tested_with-Playwright-45ba4b?logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![Allure Report](https://img.shields.io/badge/Allure-Report-orange?logo=allure&logoColor=white)](https://docs.qameta.io/allure/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/Elina-Ko/progeo-playwright-tests/actions)

Автоматизированные UI-тесты для [ProGeo Expert] (https://progeo.expert), написанные с использованием **Playwright** и **Pytest**, с интеграцией **Allure Report**.


## Возможности
- 🧪 Автотесты для веб-интерфейса ProGeo  
- 🎥 Видео, скриншоты и логи в Allure-отчётах  
- 🐢 Управляемая скорость выполнения тестов (`slow_mo`)  
- 📊 Генерация отчётов с помощью Allure  
- ⚙️ Удобный PowerShell-скрипт для запуска и открытия отчёта  

## Стек технологий
- **Python 3.11+**  
- **Playwright**  
- **Pytest**  
- **Allure-pytest**  
- **Pillow**, **ImageIO** — для создания превью из видео  

## Структура проекта
```bash
progeo-playwright-tests/
│
├── tests/ # Тесты Playwright
│ ├── ready/ # Готовые тесты
├── artifacts/ # Скриншоты, видео, логи
├── run_tests.ps1 # Скрипт для запуска тестов и Allure отчёта
├── requirements.txt # Список зависимостей
├── conftest.py # Фикстуры и обработка артефактов
├── pytest.ini 
├── README.md # Этот файл
```

## Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/Elina-Ko/progeo-playwright-tests.git
cd progeo-playwright-tests
```

### 2. Создать виртуальное окружение
```bash
python -m venv .venv
.\.venv\Scripts\activate
```
### 4. Установить зависимости
```bash
pip install -r requirements.txt
playwright install
```
### 5. Запустить тесты и открыть отчёт
```bash
.\run_tests.ps1
```
### Отчёты и артефакты
После завершения выполнения тестов в отчёте Allure доступны:
```bash
🎥 Видео каждого теста
🖼️ Превью-кадры
📸 Скриншоты при падениях
📄 Логи браузера и сетевых запросов
```
### Автор
Elina Ko

🔗 github.com/Elina-Ko

Проект создан для демонстрации автотестов на Playwright с интеграцией Allure и удобным CI-ready запуском.
