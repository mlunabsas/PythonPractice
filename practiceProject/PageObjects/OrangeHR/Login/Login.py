from PageObjects.ParentPage import ParentPage

class Login(ParentPage):

    def __init__(self):
        super().__init__()
        self.nombre = "son"
        self.peso = 23

    def got_to_url(self,url):
        print("aca")
        super().driver.quit()
        super().openBrowser()
        print("aca")
        super().driver.get("https://opensource-demo.orangehrmlive.com/")


