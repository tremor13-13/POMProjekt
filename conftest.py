import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = Options()

    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Отключаем сохранение паролей
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })


    # ## Добавь для Docker:
    # chrome_options.add_argument("--headless")  # ← Без графического интерфейса
    chrome_options.add_argument("--no-sandbox")  # ← Обязательно для Docker
    chrome_options.add_argument("--disable-dev-shm-usage")  # ← Для ограниченной памяти
    chrome_options.add_argument("--disable-gpu")  # ← Отключаем GPU
    chrome_options.add_argument("--window-size=1920,1080")  # ← Фиксируем размер окна

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()
