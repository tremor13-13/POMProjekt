import time
import allure
import pytest
from pages.base_page import BasePage
from allure_commons.types import Severity
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

@allure.epic(" Accounts")
@allure.feature(" login")
@allure.story(" Pages")
class CompleteCheckout(BasePage):


    _FIRST_NAME = "//input[@id='first-name']"
    _LAST_NAME = "//input[@id='last-name']"
    _POST_CODE = "//input[@id='postal-code']"
    _ZIP_COD = "//input[@id='continue']"
    _CLICK_FINISH = "//button[@id='finish']"
    @allure.step("load checkout first name")
    def check_enter_first_name(self):
        check_first_name: WebElement = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME))
        check_first_name.send_keys(Keys.CONTROL + "A")
        check_first_name.send_keys(Keys.BACKSPACE)
        check_first_name.send_keys("Alex")


    @allure.step("load checkout last name")
    def check_enter_last_name(self):
        self.driver.find_element(*self._LAST_NAME).send_keys("Frunzik")

    @allure.step("load checkout post code")
    def check_enter_post_code(self):
        self.driver.find_element(*self._POST_CODE).send_keys("234234")
        self.driver.find_element(*self._ZIP_COD).click()

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="cart_page_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        time.sleep(3)

    @allure.step("enter checkout finish button")
    def check_enter_finish_button(self):
        self.driver.find_element(*self._CLICK_FINISH).click()
        time.sleep(2)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="cart_page_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
        time.sleep(3)
