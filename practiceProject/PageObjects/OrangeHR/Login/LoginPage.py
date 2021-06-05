from PageObjects.ParentPage import ParentPage

class LoginPage(ParentPage):
    user_field_xpath = "//input[@id='txtUsername']"
    pass_field_xpath = "//input[@id='txtPassword']"
    login_button_xpath = "//input[@id='btnLogin']"

    def go_to_page(self):
        #ACA! "missing 1 required positional argument: 'self'" ocurre porque driver no esta inicializado a este punto
        self.driver.maximize_window()
        self.driver.get(self.test_values.URL)

    def set_user(self,user):
        user_field = self.find_by_xpath(self.user_field_xpath)
        user_field.send_keys(user)

    def set_password(self,pass_word):
        pass_field = self.find_by_xpath(self.pass_field_xpath)
        pass_field.send_keys(pass_word)

    def click_login(self):
        login_button = self.find_by_xpath(self.login_button_xpath)
        login_button.click()