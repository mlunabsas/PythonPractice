from TestCases.BaseTest import BaseTest
from PageObjects.OrangeHR.Dashboard.DashboardPage import DashboardPage
from PageObjects.OrangeHR.Login.LoginPage import LoginPage


class TestUserManagement(BaseTest):

    def test_menu_user_management(self,setUp):
        login = LoginPage()
        login.go_to_page()
        login.set_user(login.test_values.USER)
        login.set_password(login.test_values.PASS)
        login.click_login()
        menu_admin = DashboardPage()
        menu_admin.hover_over_admin()
        menu_admin.user_management_click()

        assert 1 == len(menu_admin.driver.find_elements_by_xpath('//*[@id="systemUser-information"]/a'))

