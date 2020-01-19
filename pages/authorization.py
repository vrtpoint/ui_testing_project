from locators.main_page import MainPage
from pages.helpers.base_actions import BaseActions


class ApplicationAuthorization(BaseActions):

        auth = MainPage

        def login(self, app_username, app_password):
            self._click(*self.auth.HeaderSection.my_account_link)
            self._click(*self.auth.HeaderSection.login_link)
            self._input(*self.auth.HeaderSection.email_address_field, value=app_username)
            self._input(*self.auth.HeaderSection.password_field, value=app_password)
            self._click(*self.auth.HeaderSection.login_button)

            assert self._wd \
                .find_element(*self.auth.InnerSection.account_breadcrumb).text == 'Account'

        def logout(self):
            self._click(*self.auth.HeaderSection.my_account_link)
            self._click(*self.auth.HeaderSection.logout_button)

            assert self._wd \
               .find_element(*self.auth.InnerSection.logout_breadcrumb).text == 'Logout'