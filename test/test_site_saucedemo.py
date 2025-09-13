import time
import pytest
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCart
from pages.shopping_cart_link_page import OpenBusk
from pages.check_out_page import CheckOut
from pages.checkout_page import CompleteCheckout


# @pytest.mark.usefixtures("driver")
class TestSite:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.add_to_cart_page = AddToCart(self.driver)
        self.busk_page = OpenBusk(self.driver)
        self.chek_out_page = CheckOut(self.driver)
        self.complete_check = CompleteCheckout(self.driver)

    def test_login(self):
        self.login_page.open()
        self.login_page.enter_user_name("standard_user")
        self.login_page.enter_user_password("secret_sauce")
        self.login_page.enter_button_login()
        
        time.sleep(5)
    # def test_add_to_cart(self):
        #нужно ли добавлять метод открытия, проверить после тестирования теста
        self.add_to_cart_page.add_to_cart_inventory()

    # def test_busk_clik(self):
        self.busk_page.busk_page_open()

    # def test_check_out_clik(self):
        self.chek_out_page.open_checkout_page()
        self.complete_check.check_enter_first_name()
        self.complete_check.check_enter_last_name()
        self.complete_check.check_enter_post_code()
        self.complete_check.check_enter_finish_button()

