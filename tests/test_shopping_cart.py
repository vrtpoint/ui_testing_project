from tests.common.base_set_up import TestBaseSetUp
from pages.authorization import ApplicationAuthorization
from pages.shopping_cart import ShoppingCart
from decouple import config
import allure


class TestShoppingCart(TestBaseSetUp):

    @allure.feature('Работа с корзиной')
    def test_adding_to_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorization)
        auth_page.login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCart)
        shopping_page.add_to_shopping_cart()
        auth_page.logout()

    @allure.feature('Работа с корзиной')
    def test_removal_position_from_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorization)
        auth_page.login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCart)
        shopping_page.remove_position_from_shopping_cart()
        auth_page.logout()


