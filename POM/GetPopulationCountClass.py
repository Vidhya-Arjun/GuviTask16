from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from POM.BaseClass import BaseClass


class GetPopulationCount(BaseClass):
    locator = (By.XPATH,"//div[contains(@class,'counter-ticker')]")
    def __init__(self,driver):
        super().__init__(driver)
    def OpenUrl(self,url):
        self.driver.get(url)
    def get_population_count(self):
        wait =WebDriverWait(self.driver,timeout=20,poll_frequency=1,ignored_exceptions=[StaleElementReferenceException,NoSuchElementException])
        try:
            count_population = wait.until(EC.presence_of_element_located(self.locator))
            print(count_population.text)
            self.wait
        except KeyboardInterrupt:
            print("stopped by user")
        finally:
            print("code execution completed")
