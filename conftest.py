import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = webdriver.ChromeOptions()



    # ВСЕ возможные настройки для блокировки
    chrome_options.add_experimental_option("excludeSwitches",
                                           ["enable-automation", "enable-logging", "ignore-certificate-errors"])

    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "password_manager_enabled": False,
        "enable-autofill": False,
        "signin": False,
        "translate": False
    })

    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-autofill-keyboard-accessory-view")
    chrome_options.add_argument("--disable-features=PasswordSave,AutofillServerCommunication,TranslateUI")
    chrome_options.add_argument("--disable-password-manager-reauthentication")
    chrome_options.add_argument("--disable-password-manager")
    chrome_options.add_argument("--disable-signin-promo")

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()