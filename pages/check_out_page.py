import time
import allure
import pytest
from pages.base_page import BasePage


class CheckOut(BasePage):


    _CHECK_OUT_BUTTON = "//button[@id='checkout']"


    def open_checkout_page(self):
        self.driver.find_element(*self._CHECK_OUT_BUTTON).click()
        time.sleep(2)
        expected_checkout_url = "https://www.saucedemo.com/checkout-step-one.html"
        assert self.driver.current_url == expected_checkout_url, \
            f"Ожидалась страница checkout ({expected_checkout_url}), но открыт {self.driver.current_url}"