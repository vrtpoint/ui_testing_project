from locators.administrative.product_page import LoginProductPage, AdminPage
from pages.helpers.base_actions import BaseActions


class Authorization(BaseActions):

        def login(self, app_username, app_password):
            self.input(*self.LoginProductPage.login_field, value=app_username)
            self.input(*self.LoginProductPage.password_field, value=app_password)
            self.click(*self.LoginProductPage.login_button)
            assert self.wd.find_element(*self.LoginProductPage.dashboard_text).text == 'Dashboard'

        def logout(self):
            self.click(*self.AdminPage.logout_button)
            assert self.wd.find_element(*self.LoginProductPage.login_button).is_displayed()