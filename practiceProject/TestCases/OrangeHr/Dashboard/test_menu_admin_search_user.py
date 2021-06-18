# import webdriver
from selenium import webdriver
# from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
# import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
# import ExpectedConditions
from selenium.webdriver.support import expected_conditions as EC
# import
from selenium.webdriver.common.by import By


# assign webdriver
driver = webdriver.Chrome("/Users/josipa/PycharmProjects/pythonProject/py_selenium/selenium_project/Resources/Drivers/chromedriver")
# set time to load the page
driver.set_page_load_timeout(10)


# options = ChromeOptions()
# options.add_argument("--start-maximized")
# driver.create_options(options)
# chrome_driver = webdriver.Chrome(options=options)

# go to URL
driver.get("https://opensource-demo.orangehrmlive.com/")
# maximize window
driver.maximize_window()


# insert username ok
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")

# insert password ok
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")

# click on login button
driver.find_element_by_xpath("//input[@id='btnLogin']").click()

# hover mouse over Admin
menu_admin = driver.find_element_by_css_selector("#menu_admin_viewAdminModule > b")
actions = ActionChains(driver)
actions.move_to_element(menu_admin)
actions.perform()

# hover mouse over User Management
menu_user_management = driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement' and text()='User Management']")
actions = ActionChains(driver)
actions.move_to_element(menu_user_management)
actions.perform()

# hover mouse over Users and click on it
driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers' and text()='Users']").click()

# view system users page
system_users_text = driver.find_element_by_xpath("//h1[text()='System Users']").text
assert "System Users" in system_users_text

# insert user name to search for
driver.find_element_by_xpath("//input[@id='searchSystemUser_userName' and @name='searchSystemUser[userName]']").send_keys("Admin")

# click on Search button
driver.find_element_by_xpath("//input[@id='searchBtn' and @name='_search']").click()

# view correct result(s)
amount_search_results_Admin = len(driver.find_elements_by_xpath("//a[contains(text(), 'Admin')]"))
assert amount_search_results_Admin == 1

# click on Add user button
driver.find_element_by_xpath("//input[@id='btnAdd' and @name='btnAdd']").click()

#  insert employee name
driver.find_element_by_xpath("//input[@id='systemUser_employeeName_empName' and @name='systemUser[employeeName][empName]']").send_keys("Orange ")

# select existing employee name
driver.find_element_by_xpath("//strong[text()='Orange ']").click()

# insert username
driver.find_element_by_xpath("//input[@id='systemUser_userName' and @name='systemUser[userName]']").send_keys("Orange7")

# insert password
driver.find_element_by_xpath("//input[@id='systemUser_password' and @name='systemUser[password]']").send_keys("Orange123")

# confirm password
driver.find_element_by_xpath("//input[@id='systemUser_confirmPassword' and @name='systemUser[confirmPassword]']").send_keys("Orange123")

# click on save button
driver.find_element_by_xpath("//input[@id='btnSave' and @name='btnSave']").click()

# wait
# import time
# time.sleep(2)
# explicit wait for input field field
wait = WebDriverWait(driver, 10);
wait.until(EC.visibility_of_element_located(By.XPATH, "//div[@class='message success fadable' and contains(text(), 'Successfully Saved')]"));


# assert OK message
succesfully_saved_message = len(driver.find_elements_by_xpath("//div[@class='message success fadable' and contains(text(), 'Successfully Saved')]"))
print("Cantidad de resultados ", succesfully_saved_message)
assert succesfully_saved_message == 1

# close browser and quit
driver.quit()