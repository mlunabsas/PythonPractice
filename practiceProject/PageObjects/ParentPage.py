from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from Environment.TestVolatil import TestVolatil
import time

class ParentPage(object):

    driver = RemoteWebDriver
    test_values = TestVolatil

    def find_by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    def close(self):
        self.driver.stop_client()
        self.driver.quit()