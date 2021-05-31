from DriverSetup.DriverConfig import config_driver
from PageObjects.ParentPage import ParentPage

def config_run(browser,env,cases):
    config_driver(browser)
    ParentPage.environment = env
    print("Browser en el page object:", ParentPage.driver_loader_func)
    print("Environment en el page object:" + ParentPage.environment)
    #for case in cases:
    #    exec(open(case).read())