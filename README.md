# POMProjekt
Универсальный conftest.py:
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = Options()
    
    # УНИВЕРСАЛЬНЫЕ НАСТРОЙКИ (работают везде)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Автоматическое определение среды
    import os
    if os.getenv('DOCKER_RUN') == 'true':  # Запущено в Docker
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless=new")
        # Уникальная папка для избежания конфликтов
        temp_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    else:  # Локальный запуск
        chrome_options.add_argument("--start-maximized")
    
    # Общие настройки
    chrome_options.add_experimental_option("excludeSwitches", 
                                          ["enable-automation", "enable-logging"])
    
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()

