from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass():
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,timeout)

    def locate_element(self,locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator))
