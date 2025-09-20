import time
import os
import pytest
import allure
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCart
from pages.shopping_cart_link_page import OpenBusk
from pages.check_out_page import CheckOut
from pages.checkout_page import CompleteCheckout
from pages.cookie_manager import CookieManager


class TestSite:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.add_to_cart_page = AddToCart(self.driver)
        self.shopping_cart_link_page = OpenBusk(self.driver)
        self.chek_out_page = CheckOut(self.driver)
        self.complete_check = CompleteCheckout(self.driver)
        self.cookie_manager = CookieManager(self.driver)

    @allure.epic("Saucedemo Tests")
    @allure.feature("Авторизация")
    @allure.story("Успешный логин")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        with allure.step("Открываем страницу логина"):
            self.login_page.open()

        with allure.step("Вводим логин и пароль"):
            self.login_page.enter_user_name("standard_user")
            self.login_page.enter_user_password("secret_sauce")
            self.login_page.enter_button_login()

        with allure.step("Сохраняем куки для следующих тестов"):
            self.cookie_manager.save()

        time.sleep(2)

    @allure.epic("Saucedemo Tests")
    @allure.feature("Корзина")
    @allure.story("Добавление товаров в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart(self):
        with allure.step("Открываем страницу и загружаем куки"):
            self.login_page.open()
            self.cookie_manager.load()
            self.add_to_cart_page.open()
            time.sleep(3)

        with allure.step("Добавляем товары в корзину"):
            self.add_to_cart_page.add_to_cart_inventory()

        with allure.step("Сохраняем состояние корзины"):
            self.cookie_manager.save()

    @allure.epic("Saucedemo Tests")
    @allure.feature("Корзина")
    @allure.story("Переход в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    def test_busk_clik(self):
        with allure.step("Загружаем куки и открываем корзину"):
            self.driver.get("https://www.saucedemo.com")
            self.cookie_manager.load()
            time.sleep(3)
            self.shopping_cart_link_page.open()
            time.sleep(3)

    @allure.epic("Saucedemo Tests")
    @allure.feature("Оформление заказа")
    @allure.story("Полный процесс checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_out_clik(self):
        with allure.step("Загружаем куки и переходим к оформлению"):
            self.driver.get("https://www.saucedemo.com")
            self.cookie_manager.load()
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

        with allure.step("Заполняем данные для доставки"):
            self.complete_check.check_enter_first_name()
            self.complete_check.check_enter_last_name()
            self.complete_check.check_enter_post_code()

        with allure.step("Завершаем оформление заказа"):
            self.complete_check.enter_contine()
            self.complete_check.check_enter_finish_button()