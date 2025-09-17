import time
import allure
import pytest
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


@allure.epic("Accounts")
@allure.feature("login")
@allure.story("Pages")
class OpenBusk(BasePage):

    _CLIK_BUSK = "//a[@class='shopping_cart_link']"
    @allure.step("busk open")
    def busk_page_open(self):
        click_button_busk: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._CLIK_BUSK))
        click_button_busk.click()

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="cart_page_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        time.sleep(3)
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "ошибка входа"
