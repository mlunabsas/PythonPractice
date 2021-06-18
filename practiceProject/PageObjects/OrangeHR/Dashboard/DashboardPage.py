from PageObjects.ParentPage import ParentPage
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage(ParentPage):

    def __init__(self):
        self.menu_admin_xpath = '//*[@id="menu_admin_viewAdminModule"]/b'
        self.menu_user_management_xpath = '//*[@id="menu_admin_UserManagement"]'
        self.menu_option_users = "//a[@id='menu_admin_viewSystemUsers' and text()='Users']"

    def hover_over_admin(self):
        menu_admin = self.driver.find_element_by_xpath(self.menu_admin_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_admin)
        actions.perform()

    def hover_over_user_management(self):
        menu_user_management = self.driver.find_element_by_xpath(self.menu_user_management_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_user_management)
        actions.perform()

    def menu_users_click(self):
        menu_option_users = self.driver.find_element_by_xpath(self.menu_option_users)
        menu_option_users.click()





