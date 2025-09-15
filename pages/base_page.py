import allure
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time

class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)  # Создаем ожидание здесь

    def open(self):
        self.driver.get(self._PAGE_URL)

    # # Базовые методы ожидания
    # def wait_for_element(self, locator, timeout=10):
    #     """Ждет появления элемента в DOM"""
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.presence_of_element_located(locator)
    #     )
    #
    # def wait_for_visible(self, locator, timeout=10):
    #     """Ждет видимости элемента"""
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.visibility_of_element_located(locator)
    #     )
    #
    # def wait_for_clickable(self, locator, timeout=10):
    #     """Ждет кликабельности элемента"""
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.element_to_be_clickable(locator)
    #     )
    #
    # def wait_for_invisible(self, locator, timeout=10):
    #     """Ждет исчезновения элемента"""
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.invisibility_of_element_located(locator)
    #     )
    #
    # def wait_for_text(self, locator, text, timeout=10):
    #     """Ждет появления текста в элементе"""
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.text_to_be_present_in_element(locator, text)
    #     )
    #
    # # Удобные методы-обертки для часто используемых действий
    # @allure.step("Кликнуть на элемент {locator}")
    # def click(self, locator, timeout=10):
    #     """Кликает на элемент после ожидания кликабельности"""
    #     element = self.wait_for_clickable(locator, timeout)
    #     element.click()
    #
    # @allure.step("Ввести текст '{text}' в элемент {locator}")
    # def type(self, locator, text, timeout=10):
    #     """Вводит текст в поле после ожидания видимости"""
    #     element = self.wait_for_visible(locator, timeout)
    #     element.clear()
    #     element.send_keys(text)
    #
    # @allure.step("Получить текст элемента {locator}")
    # def get_text(self, locator, timeout=10):
    #     """Получает текст элемента после ожидания видимости"""
    #     element = self.wait_for_visible(locator, timeout)
    #     return element.text
    #
    # @allure.step("Получить атрибут '{attribute}' элемента {locator}")
    # def get_attribute(self, locator, attribute, timeout=10):
    #     """Получает атрибут элемента"""
    #     element = self.wait_for_presence(locator, timeout)
    #     return element.get_attribute(attribute)
    #
    # # Дополнительные полезные методы
    # def is_element_present(self, locator, timeout=5):
    #     """Проверяет наличие элемента без выброса исключения"""
    #     try:
    #         self.wait_for_element(locator, timeout)
    #         return True
    #     except:
    #         return False
    #
    # def is_element_visible(self, locator, timeout=5):
    #     """Проверяет видимость элемента без выброса исключения"""
    #     try:
    #         self.wait_for_visible(locator, timeout)
    #         return True
    #     except:
    #         return False
    #
    # @allure.step("Выбрать значение '{value}' в выпадающем списке {locator}")
    # def select_dropdown_by_value(self, locator, value, timeout=10):
    #     """Выбирает значение в выпадающем списке"""
    #     element = self.wait_for_clickable(locator, timeout)
    #     select = Select(element)
    #     select.select_by_value(value)
    #
    # @allure.step("Выбрать текст '{text}' в выпадающем списке {locator}")
    # def select_dropdown_by_text(self, locator, text, timeout=10):
    #     """Выбирает текст в выпадающем списке"""
    #     element = self.wait_for_clickable(locator, timeout)
    #     select = Select(element)
    #     select.select_by_visible_text(text)







# import allure
# from metaclasses.meta_locator import MetaLocator
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# import pytest
# import time
#
#
#
# class BasePage(metaclass=MetaLocator):
#
#     def __init__(self, driver):
#         self.driver: WebDriver = driver
#
#     def open(self):
#         self.driver.get(self._PAGE_URL)

    # def login(self):
    #     """Вспомогательный метод для авторизации"""
    #     self.driver.get("https://www.saucedemo.com")
    #     self.driver.find_element(*self._USER_NAME_FILED).send_keys("standard_user")
    #     self.driver.find_element(*self._USER_PASSWORD).send_keys("secret_sauce")
    #     self.driver.find_element(*self._BUTTON_LOGIN).click()
    #     time.sleep(2)
#
#     def select_dropdown_option(self, locator, option_text=None, option_value=None, option_index=None):
#         """
#         Универсальный метод для работы с выпадающими списками
#         """
#         element = self.driver.find_element(*locator)
#
#         select = Select(element)
#         if option_text:
#             print(f"Попытка выбрать по тексту: '{option_text}'")
#             select.select_by_visible_text(option_text)
#         elif option_value:
#             select.select_by_value(option_value)
#         elif option_index is not None:
#             select.select_by_index(option_index)
#         else:
#             raise ValueError("Не указан параметр для выбора")
#
#         selected = select.first_selected_option.text
#         return selected
#
# class LoginAllStep:
#
#     _USER_NAME_FILED = "//input[@id='user-name']"
#     _USER_PASSWORD = "//input[@id='password']"
#     _BUTTON_LOGIN ="//input[@id='login-button']"
#     def all_login(self):
#         """Вспомогательный метод для авторизации"""
#         self.driver.get("https://www.saucedemo.com")
#         self.driver.find_element(*self._USER_NAME_FILED ).send_keys("standard_user")
#         self.driver.find_element(*self._USER_PASSWORD).send_keys("secret_sauce")
#         self.driver.find_element(*self._BUTTON_LOGIN).click()
#         time.sleep(2)

