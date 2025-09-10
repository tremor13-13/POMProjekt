import time
import allure
import pytest
from pages.base_page import BasePage
from allure_commons.types import Severity


class CompleteCheckout(BasePage):


    _FIRST_NAME = "//input[@id='first-name']"
    _LAST_NAME = "//input[@id='last-name']"
    _POST_CODE = "//input[@id='postal-code']"
    _ZIP_COD = "//input[@id='continue']"
    _CLICK_FINISH = "//button[@id='finish']"

    def check_out(self):
        self.driver.find_element(*self._FIRST_NAME).send_keys("Alex")
        self.driver.find_element(*self._LAST_NAME).send_keys("Frunzik")
        self.driver.find_element(*self._POST_CODE).send_keys("234234")
        self.driver.find_element(*self._ZIP_COD).click()
        self.driver.find_element(*self._CLICK_FINISH).click()
        time.sleep(2)
