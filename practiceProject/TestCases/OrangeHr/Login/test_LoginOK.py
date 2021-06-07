from TestCases.BaseTest import BaseTest
from PageObjects.OrangeHR.Login.LoginPage import LoginPage

class Test(BaseTest):

    def test_insert_name(self, setUp):
        login = LoginPage()
        login.go_to_page()
        login.set_user(login.test_values.USER)
        login.set_password(login.test_values.PASS)
        login.click_login()

        assert 1 == len(login.driver.find_elements_by_xpath("//h1[text()='Dashboard']"))

    def test_insert_name2(self, setUp):
        login = LoginPage()
        login.go_to_page()
        login.set_user(login.test_values.USER)
        login.set_password(login.test_values.PASS)
        login.click_login()

        assert 2 == len(login.driver.find_elements_by_xpath("//h1[text()='Dashboard']"))
