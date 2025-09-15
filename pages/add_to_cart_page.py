import time
import allure
import pytest
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import Severity

@allure.epic(" Accounts")
@allure.feature(" login ")
@allure.story(" Pages ")
class AddToCart(BasePage):

    _ADD_INVENTORY1 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    _ADD_INVENTORY2 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    _COUNT_PRODUCTS = "//span[text()='2']"
    @allure.step("add  inventory ")
    def add_to_cart_inventory(self):
        add_to_inventory1: WebElement =self.wait.until(EC.element_to_be_clickable(self._ADD_INVENTORY1))
        add_to_inventory1.click()
        add_to_inventory2: WebElement = self.wait.until(EC.element_to_be_clickable(self._ADD_INVENTORY2))
        add_to_inventory2.click()
        time.sleep(3)

        # здеся что бы считать из корзины .. надо проделать эти цирковые трюки :)
        #обратиться к корзине
        count_products = self.driver.find_element(*self._COUNT_PRODUCTS)
        # преобразовать в текст!
        text_count = count_products.text
        # и потом перевести в числовое
        text_count_int = int(text_count)
        # и только потом пихать его в асерт!
        assert text_count_int == 2, "не верное количиство товаров в корзине"
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "ошибка входа"
