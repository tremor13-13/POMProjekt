import time
import allure
import pytest
from pages.base_page import BasePage


class OpenBusk(BasePage):

    _CLIK_BUSK = "//a[@class='shopping_cart_link']"

    def busk_page_open(self):
        self.driver.find_element(*self._CLIK_BUSK).click()

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="cart_page_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        time.sleep(3)
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "ошибка входа"
