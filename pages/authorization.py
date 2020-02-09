from locators.authorization import Authorization
from pages.helpers.base_actions import BaseActions


class ApplicationAuthorization(BaseActions):
        """Класс для работы с авторизацией пользователя"""

        auth = Authorization
        """Экземпляр класса для доступа к локаторам по работе с авторизацией"""

        def login(self, app_username, app_password):
            """Метод авторизации пользователя"""
            self._click(*self.auth.my_account_link)
            self._click(*self.auth.login_link)
            self._input(*self.auth.email_address_field, value=app_username)
            self._input(*self.auth.password_field, value=app_password)
            self._click(*self.auth.login_button)

            assert self._wd \
                .find_element(*self.auth.account_breadcrumb).text == 'Account'

        def logout(self):
            """Метод деавторизации пользователя"""
            self._click(*self.auth.my_account_link)
            self._click(*self.auth.logout_button)

            assert self._wd \
               .find_element(*self.auth.logout_breadcrumb).text == 'Logout'