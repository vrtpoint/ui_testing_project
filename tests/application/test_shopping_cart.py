from resources.common.base_set_up import BaseSetUp
from resources.application.pages.authorization import ApplicationAuthorizationPage
from resources.application.pages.shopping_cart import ShoppingCartPage
from decouple import config
import allure


class TestShoppingCart(BaseSetUp):

    @allure.feature('Работа с корзиной')
    def test_adding_to_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page._login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCartPage)
        shopping_page._add_to_shopping_cart()
        auth_page._logout()

    @allure.feature('Работа с корзиной')
    def test_removal_position_from_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page._login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCartPage)
        shopping_page._remove_position_from_shopping_cart()
        auth_page._logout()


