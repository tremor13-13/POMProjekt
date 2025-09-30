from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCart
from pages.shopping_cart_link_page import OpenBusk
from pages.check_out_page import CheckOut
from pages.checkout_page import CompleteCheckout
from pages.cookie_manager import CookieManager


class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.add_to_cart_page = AddToCart(self.driver)
        self.shopping_cart_link_page = OpenBusk(self.driver)
        self.chek_out_page = CheckOut(self.driver)
        self.complete_check = CompleteCheckout(self.driver)
        self.cookie_manager = CookieManager(self.driver)