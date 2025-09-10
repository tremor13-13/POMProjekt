import time
import allure
import pytest
from pages.base_page import BasePage



class LoginPage(BasePage):
    _PAGE_URL = "https://www.saucedemo.com"
    _USER_NAME_FILED = "//input[@id='user-name']"
    _USER_PASSWORD = "//input[@id='password']"
    _BUTTON_LOGIN = "//input[@id='login-button']"

    def enter_user_name(self, user_name):
        self.driver.find_element(*self._USER_NAME_FILED).send_keys(user_name)


    def enter_user_password(self, password):
        self.driver.find_element(*self._USER_PASSWORD).send_keys(password)


    def enter_button_login(self):
        self.driver.find_element(*self._BUTTON_LOGIN).click()

time.sleep(2)