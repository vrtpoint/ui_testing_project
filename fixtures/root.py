from pages.application.shopping_cart import ShoppingCart
from pages.application.wish_list import WishList
from pages.authorization import Authorization


class DriverHelper():

    def __init__(self, driver):
        self.wd = driver
        self.wd.implicitly_wait(60)
        self.wd.maximize_window()
        self.authorization = Authorization(self)
        self.products = ShoppingCart(self)
        self.products = WishList(self)

    def open(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()