from DriverSetup.DriverConfig import config_driver
from Environment.EnvironmentConfig import config_environment
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from Environment.TestVolatil import TestVolatil
import time

class ParentPage(object):

    driver = RemoteWebDriver
    test_values = TestVolatil

    @staticmethod
    def find_by_xpath(xpath):
        return ParentPage.driver.find_element_by_xpath(xpath)

    @staticmethod
    def close():
        ParentPage.driver.stop_client()
        ParentPage.driver.quit()

    @staticmethod
    def start_driver():
        ParentPage.driver=config_driver()
        ParentPage.test_values=config_environment()