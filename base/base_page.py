from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.EC = EC

    def open(self):
        """Просто открываем страницу"""
        self.driver.get(self._PAGE_URL)



