from locators.main_page import MainPage
from pages.helpers.base import BaseActions


class Authorization(BaseActions):

        auth = MainPage

        def login(self, app_username, app_password):
            self.click(*self.auth.HeaderSection.my_account_link)
            self.click(*self.auth.HeaderSection.login_link)
            self.input(*self.auth.HeaderSection.email_address_field, value=app_username)
            self.input(*self.auth.HeaderSection.password_field, value=app_password)
            self.click(*self.auth.HeaderSection.login_button)
            assert self.wd.find_element(*self.auth.InnerSection.account_breadcrumb).text == 'Account'

        def logout(self):
            self.click(*self.auth.HeaderSection.my_account_link)
            self.click(*self.auth.HeaderSection.logout_button)
            assert self.wd.find_element(*self.auth.InnerSection.logout_breadcrumb).text == 'Logout'