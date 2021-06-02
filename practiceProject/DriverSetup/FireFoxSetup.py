from selenium import webdriver
import platform

print (platform.system())
path=None
options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")
# options.add_argument('--headless')
# options.add_argument("window-size=1000,1000")

driver_executables = {
  "Windows": "DriverSetup/Drivers/geckodriver.exe",
  "Darwin": "DriverSetup/Drivers/geckodriver-v0.29.1-macos-aarch64.tar",
  "Linux": "DriverSetup/Drivers/geckodriver"
}

def configDriver():
        return webdriver.Firefox(executable_path=driver_executables[platform.system()], options=options)
