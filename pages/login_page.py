import allure
import json

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):
    _PAGE_URL = "https://www.saucedemo.com"
    _USER_NAME_FILED = "//input[@id='user-name']"
    _USER_PASSWORD = "//input[@id='password']"
    _BUTTON_LOGIN = "//input[@id='login-button']"
    @allure.step("enter  login")
    def enter_user_name(self, user_name):
        name_filed: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._USER_NAME_FILED))
        name_filed.send_keys(user_name)

    @allure.step("enter  password")
    def enter_user_password(self, password):
        password_field: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._USER_PASSWORD))
        password_field.send_keys(password)

    @allure.step("click button login")
    def enter_button_login(self):
        button_login: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._BUTTON_LOGIN))
        button_login.click()







