from selenium import webdriver
import platform

print (platform.system())
path=None
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

def configDriver():
        if (platform.system()=="Windows"):
                path= "D:\Develop\Python\practiceProject\DriverSetup\Drivers\chromedriver.exe"
        else:
                path= "DriverSetup / Drivers / chromedriver.exe"
        return webdriver.Chrome(executable_path=path, options=options)
