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


class Products(BaseActions):

        product = MainPage

        def add_to_wish_list(self):
            self.click(*self.product.HeaderSection.logo_name)
            assert self.wd.find_element(*self.product.MainSection.slide_section).is_displayed()
            feature_elements = self.wd.find_elements(*self.product.MainSection.featured_section)
            product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']
            for element in feature_elements:
                assert element.text in product_list
                print(element.text)
            feature_element = self.wd.find_elements(*self.product.MainSection.featured_section)[0]
            feature_element.click()
            self.click(*self.product.MainSection.wish_list_button)
            self.click(*self.product.HeaderSection.wish_list_link)
            assert self.wd.find_element(*self.product.MainSection.wish_list_product_name).text == 'MacBook'

        def remove_from_wish_list(self):
            self.click(*self.product.HeaderSection.logo_name)
            assert self.wd.find_element(*self.product.MainSection.slide_section).is_displayed()
            feature_elements = self.wd.find_elements(*self.product.MainSection.featured_section)
            product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']
            for element in feature_elements:
                assert element.text in product_list
                print(element.text)
            feature_element = self.wd.find_elements(*self.product.MainSection.featured_section)[0]
            feature_element.click()
            self.click(*self.product.HeaderSection.wish_list_link)
            self.click(*self.product.InnerSection.delete_wish_list_position_button)
            assert self.wd.find_element(*self.product.InnerSection.my_wish_list_breadcrumb).text == 'My Wish List'

        def add_to_shopping_cart(self):
            self.click(*self.product.HeaderSection.logo_name)
            assert self.wd.find_element(*self.product.MainSection.slide_section).is_displayed()
            cart_buttons = self.wd.find_elements(*self.product.MainSection.add_to_cart_button)
            for element in cart_buttons:
                assert element is not None
            cart_button = self.wd.find_elements(*self.product.MainSection.add_to_cart_button)[0]
            cart_button.click()
            self.click(*MainPage.HeaderSection.shopping_cart_link)
            assert self.wd.find_element(*self.product.MainSection.shopping_cart_product_name).text == 'MacBook'

        def remove_position_from_shopping_cart(self):
            self.click(*self.product.HeaderSection.logo_name)
            self.click(*MainPage.HeaderSection.shopping_cart_link)
            self.click(*MainPage.InnerSection.delete_shopping_cart_position_button)
            assert self.wd.find_element(*MainPage.InnerSection.shopping_cart_info).text == 'Shopping Cart'

