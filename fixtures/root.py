from pages.shopping_cart import ShoppingCart
from pages.wish_list import WishList
from pages.authorization import ApplicationAuthorization


class DriverHelper:


    def __init__(self, driver):
        self.wd = driver
        self.wd.implicitly_wait(30)
        self.wd.maximize_window()
        self.shopping_cart = ShoppingCart(self)
        self.wish_list = WishList(self)
        self.authorization = ApplicationAuthorization(self)

    def open(self, url):
        self.wd.get(url)

    def destroy(self):
        self.wd.quit()