from PageObjects.OrangeHR.Login.LoginPage import Login

login = Login()
login.go_to_page()
login.set_user(login.test_values.USER)
login.set_password(login.test_values.PASS)
login.click_login()

assert 1 == len(login.driver.find_elements_by_xpath("//h1[text()='Dashboard']"))

login.driver.quit()
