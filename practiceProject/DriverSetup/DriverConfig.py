from PageObjects.ParentPage import ParentPage
import importlib

drivers_dict = {
  "chrome": "DriverSetup.ChromeSetup",
  "firefox": "DriverSetup.FireFoxSetup",
  "edge": "DriverSetup.EdgeSetup"
}

def config_driver(driver_kind):
    print("Loading driver: "+driver_kind)
    setup = importlib.import_module(drivers_dict[driver_kind])
    ParentPage.driver=setup.configDriver()