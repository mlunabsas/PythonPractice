from PageObjects.ParentPage import ParentPage
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage(ParentPage):

    def __init__(self):
        self.menu_admin_xpath = '//*[@id="menu_admin_viewAdminModule"]/b'
        self.menu_user_management_xpath = '//*[@id="menu_admin_UserManagement"]'

    def hover_over_admin(self):
        menu_admin = self.driver.find_elements_by_xpath(self.menu_admin_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_admin)
        actions.perform()

    def user_management_click(self):
        menu_user_management = self.driver.find_elements_by_xpath(self.menu_user_management_xpath)
        menu_user_management.click()





