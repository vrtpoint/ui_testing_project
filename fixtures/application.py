from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main_page import Authorization, Products


class ApplicationHelper():

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.wd.maximize_window()
        self.authorization = Authorization(self)
        self.products = Products(self)

    def open(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()