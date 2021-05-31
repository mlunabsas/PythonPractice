from selenium import webdriver
import platform

class ParentPage(object):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-startup-window")
    #driver_loader_func = None
    #driver = None
    #environment = None

    def __init__(self):
        self.driver_loader_func = None
        self.environment = None
        self.driver = self.configDriver()

    def saluda(self):
        print("Hello friend!")

    def openBrowser(self):
        self.driver=ParentPage.driver_loader_func()

    def configDriver(self):
        if (platform.system() == "Windows"):
            path = "D:\Develop\Python\practiceProject\DriverSetup\Drivers\chromedriver.exe"
        else:
            path = "DriverSetup / Drivers / chromedriver.exe"
        return webdriver.Chrome(executable_path=path, options=self.options)