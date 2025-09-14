import time
import allure
import pytest
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement



class LoginPage(BasePage):
    _PAGE_URL = "https://www.saucedemo.com"
    _USER_NAME_FILED = "//input[@id='user-name']"
    _USER_PASSWORD = "//input[@id='password']"
    _BUTTON_LOGIN = "//input[@id='login-button']"
    @allure.step("enter  login")
    def enter_user_name(self, user_name):
        name_filed = self.wait.until(EC.element_to_be_clickable(self._USER_NAME_FILED))
        name_filed.send_keys(user_name)


    @allure.step("enter  password")
    def enter_user_password(self, password):
        password_filed = self.wait.until(EC.element_to_be_clickable(self._USER_PASSWORD))
        # self.driver.find_element(*self._USER_PASSWORD).send_keys(password)

    @allure.step("click button login")
    def enter_button_login(self):
        self.driver.find_element(*self._BUTTON_LOGIN).click()

time.sleep(2)
