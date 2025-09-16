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
    _BUTTON_ZIP_CONTINE = "//input[@id='continue']"
    _CLICK_FINISH = "//button[@id='finish']"
    @allure.step("load checkout first name")
    def check_enter_first_name(self):
        check_first_name: WebElement = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME))
        check_first_name.send_keys(Keys.CONTROL + "A")
        check_first_name.send_keys(Keys.BACKSPACE)
        check_first_name.send_keys("Alex")


    @allure.step("load checkout last name")
    def check_enter_last_name(self):
        check_entet_last_name:WebElement = self.wait.until(EC.element_to_be_clickable(self._LAST_NAME))
        check_entet_last_name.send_keys(Keys.CONTROL + "A")
        check_entet_last_name.send_keys(Keys.BACKSPACE)
        check_entet_last_name.send_keys("Frunzik")

    @allure.step("load checkout post code")
    def check_enter_post_code(self):
        chek_enter_zip_code: WebElement = self.wait.until(EC.element_to_be_clickable(self._POST_CODE))
        chek_enter_zip_code.send_keys(Keys.CONTROL + "A")
        chek_enter_zip_code.send_keys(Keys.BACKSPACE)
        chek_enter_zip_code.send_keys("234234")

    @allure.step("Enter contine")
    def enter_contine(self):
        check_enter_contine: WebElement = self.wait.until(EC.element_to_be_clickable(self._BUTTON_ZIP_CONTINE))
        check_enter_contine.click()


        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="cart_page_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        time.sleep(3)

    @allure.step("enter checkout finish button")
    def check_enter_finish_button(self):
        finish_click: WebElement = self.wait.until(EC.element_to_be_clickable(self._CLICK_FINISH))
        finish_click.click()
        time.sleep(2)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="cart_page_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
        time.sleep(3)
