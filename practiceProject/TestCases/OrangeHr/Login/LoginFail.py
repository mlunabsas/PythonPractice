from TestCases.BaseTest import BaseTest
from PageObjects.OrangeHR.Login.LoginPage import LoginPage

class Test(BaseTest):

    def test_insert_name(self, setUp):
        login = LoginPage()
        login.go_to_page()
        login.set_user(login.test_values.USER)
        login.set_password("Mamberto")
        login.click_login()

        assert 1 == len(login.driver.find_elements_by_xpath("//span[contains(.,'Invalid credentials')]"))