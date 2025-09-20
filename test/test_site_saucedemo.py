import time
import os
import pytest
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCart
from pages.shopping_cart_link_page import OpenBusk
from pages.check_out_page import CheckOut
from pages.checkout_page import CompleteCheckout
from pages.cookie_manager import CookieManager



#@pytest.mark.usefixtures("driver")
class TestSite:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.add_to_cart_page = AddToCart(self.driver)
        self.shopping_cart_link_page = OpenBusk(self.driver)
        self.chek_out_page = CheckOut(self.driver)
        self.complete_check = CompleteCheckout(self.driver)
        self.cookie_manager = CookieManager(self.driver)


    def test_login(self):
        self.login_page.open()
        self.login_page.enter_user_name("standard_user")
        self.login_page.enter_user_password("secret_sauce")
        self.login_page.enter_button_login()
        self.cookie_manager.save()

        time.sleep(2)
    def test_add_to_cart(self):
        # Сначала открываем ЛЮБУЮ страницу сайта
        self.login_page.open()
        # Открываем главную страницу
        # self.driver.get("https://www.saucedemo.com")

        # Загружаем куки через менеджер
        self.cookie_manager.load()

        # Переходим на нужную страницу
        self.add_to_cart_page.open()
        time.sleep(3)
        self.add_to_cart_page.add_to_cart_inventory()
        self.cookie_manager.save()

    def test_busk_clik(self):
        self.driver.get("https://www.saucedemo.com")

        self.cookie_manager.load()
        time.sleep(3)
        self.shopping_cart_link_page.open()
        time.sleep(3)

    def test_check_out_clik(self):
        self.driver.get("https://www.saucedemo.com")

        self.cookie_manager.load()

        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.complete_check.check_enter_first_name()
        self.complete_check.check_enter_last_name()
        self.complete_check.check_enter_post_code()
        self.complete_check.enter_contine()
        self.complete_check.check_enter_finish_button()

