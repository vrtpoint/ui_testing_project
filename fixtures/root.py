from pages.application.shopping_cart import Products
from pages.authorization import Authorization


class DriverHelper():

    def __init__(self, driver):
        self.wd = driver
        self.wd.implicitly_wait(60)
        self.wd.maximize_window()
        self.authorization = Authorization(self)
        self.products = Products(self)

    def open(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()