import time
import allure
import pytest
from pages.base_page import BasePage
from allure_commons.types import Severity

@allure.epic(" Accounts")
@allure.feature(" login ")
@allure.story(" Pages ")
class AddToCart(BasePage):

    _ADD_INVENTORY1 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    _ADD_INVENTORY2 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    @allure.step("add  inventory ")
    def add_to_cart_inventory(self):
        self.driver.find_element(*self._ADD_INVENTORY1).click()
        self.driver.find_element(*self._ADD_INVENTORY2).click()
        time.sleep(3)
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "ошибка входа"
