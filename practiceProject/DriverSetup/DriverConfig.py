import runner
import importlib

drivers_dict = {
  "chrome": "DriverSetup.ChromeSetup",
  "firefox": "DriverSetup.FireFoxSetup",
  "edge": "DriverSetup.EdgeSetup"
}

def config_driver():
    print("Loading driver: "+runner.actual_browser)
    setup = importlib.import_module(drivers_dict[runner.actual_browser])
    return setup.configDriver()