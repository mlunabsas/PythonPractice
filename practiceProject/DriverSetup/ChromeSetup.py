from selenium import webdriver
import platform

print (platform.system())
path=None
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument('--headless')
# options.add_argument("window-size=1000,1000")

driver_executables = {
  "Windows": "DriverSetup/Drivers/chromedriver.exe",
  "Darwin": "DriverSetup/Drivers/chromedriver",
  "Linux": "DriverSetup/Drivers/chromedriver"
}

def configDriver():
        return webdriver.Chrome(executable_path=driver_executables[platform.system()], options=options)
