from DriverSetup.DriverConfig import config_driver
from PageObjects.ParentPage import ParentPage
import importlib

def config_run(browser,env,cases):
    config_driver(browser)

    environment_module = importlib.import_module("Environment."+env)
    environment_class = getattr(environment_module, env)
    ParentPage.test_values = environment_class()
    print("Browser en el page object:", ParentPage.driver)
    print("Environment en el page object:", ParentPage.test_values)
    # for case in cases:
    exec(open(cases).read())