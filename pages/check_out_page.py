import time
import allure
import pytest
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement

@allure.epic(" Accounts")
@allure.feature(" login")
@allure.story(" Pages")
class CheckOut(BasePage):


    _CHECK_OUT_BUTTON = "//button[@id='checkout']"

    @allure.step("open  checkout")
    def open_checkout_page(self):
        click_check_out_button: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._CHECK_OUT_BUTTON))
        click_check_out_button.click()
        time.sleep(2)
        expected_checkout_url = "https://www.saucedemo.com/checkout-step-one.html"

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="cart_page_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        time.sleep(3)

        assert self.driver.current_url == expected_checkout_url, \
            f"Ожидалась страница checkout ({expected_checkout_url}), но открыт {self.driver.current_url}"