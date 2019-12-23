from pages.application.shopping_cart import ShoppingCart
from pages.application.wish_list import WishList
from pages.application.authorization import ApplicationAuthorization
from pages.administrative.authorization import AdminPageAuthorization
from pages.administrative.products import Products



class DriverHelper():

    def __init__(self, driver):
        self.wd = driver
        self.wd.implicitly_wait(60)
        self.wd.maximize_window()
        self.authorization = ApplicationAuthorization(self)
        self.authorization = AdminPageAuthorization(self)
        self.products = ShoppingCart(self)
        self.products = WishList(self)
        self.products = Products(self)

    def open(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()