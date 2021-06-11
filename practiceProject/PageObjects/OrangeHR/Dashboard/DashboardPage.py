from PageObjects.ParentPage import ParentPage

class DashboardPage(ParentPage):
    elemento_menu = "xpath"

    def hover_over_admin(self):
        menu_admin = self.driver.find_elements_by_xpath()
        user_field.send_keys(user)