import allure
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import time

class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)  # Создаем ожидание здесь
        self.EC = EC
        self.WebElement = WebElement


    def open(self):
        self.driver.get(self._PAGE_URL)
