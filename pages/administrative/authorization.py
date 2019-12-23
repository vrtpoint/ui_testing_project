from locators.administrative.product_page import LoginProductPage, AdminPage
from pages.helpers.base_actions import BaseActions


class AdminPageAuthorization(BaseActions):

        auth = LoginProductPage
        deauth = AdminPage

        def login(self, app_username, app_password):
            self.input(*self.auth.login_field, value=app_username)
            self.input(*self.auth.password_field, value=app_password)
            self.click(*self.auth.login_button)
            #assert self.wd.find_element(*self.auth.entry_title).text == 'Dashboard'

        def logout(self):
            self.click(*self.deauth.logout_button)
            assert self.wd.find_element(*self.LoginProductPage.login_button).is_displayed()