from pages.shopping_cart import ShoppingCart
from pages.wish_list import WishList
from pages.authorization import ApplicationAuthorization


class DriverHelper:
    """Класс драйвера браузера"""

    def __init__(self, driver):
        """Инициализирующий конструктор класса драйвера браузера"""
        self.wd = driver
        self.wd.implicitly_wait(30)
        self.wd.maximize_window()
        self.shopping_cart = ShoppingCart(self)
        self.wish_list = WishList(self)
        self.authorization = ApplicationAuthorization(self)

    def open(self, url):
        """Метод перехода по заданному URL-адресу"""
        self.wd.get(url)

    def destroy(self):
        """Метод закрытия браузера"""
        self.wd.quit()