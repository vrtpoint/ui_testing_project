from tests.common.base_set_up import TestBaseSetUp
from pages.authorization import ApplicationAuthorizationPage
from pages.wish_list import WishListPage
from decouple import config
import allure

class TestWishList(TestBaseSetUp):

    @allure.feature('Работа cо списком желаемых покупок')
    def test_adding_to_wish_list(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page.login(config('app_username'), config('app_password'))
        wish_list_page = self.get_page(WishListPage)
        wish_list_page.add_to_wish_list()
        auth_page.logout()

    @allure.feature('Работа cо списком желаемых покупок')
    def test_removal_position_from_wish_list(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page.login(config('app_username'), config('app_password'))
        wish_list_page = self.get_page(WishListPage)
        wish_list_page.remove_from_wish_list()
        auth_page.logout()




