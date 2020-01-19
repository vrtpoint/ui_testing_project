from locators.main_page import MainPage
from pages.helpers.base_actions import BaseActions


class ShoppingCart(BaseActions):

        product = MainPage

        def add_to_shopping_cart(self):
            self._click(*self.product.HeaderSection.logo_name)
            assert self._wd.find_element(*self.product.MainSection.slide_section).is_displayed()
            cart_buttons = self._wd.find_elements(*self.product.MainSection.add_to_cart_button)

            for element in cart_buttons:
                assert element is not None
                print(element.text)

            cart_button = self._wd.find_elements(*self.product.MainSection.add_to_cart_button)[0]
            cart_button.click()
            self._click(*MainPage.HeaderSection.shopping_cart_link)
            assert self._wd \
                .find_element(*self.product.MainSection.shopping_cart_product_name) \
                .text == 'MacBook'

        def remove_position_from_shopping_cart(self):
            self._click(*self.product.HeaderSection.logo_name)
            self._click(*MainPage.HeaderSection.shopping_cart_link)
            self._click(*MainPage.InnerSection.delete_shopping_cart_position_button)
            assert self._wd \
                .find_element(*MainPage.InnerSection.shopping_cart_info) \
                .text == 'Shopping Cart'

