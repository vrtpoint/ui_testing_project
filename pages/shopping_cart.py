from locators.authorization import Authorization
from locators.shopping_cart import ShoppingCart
from pages.helpers.base_actions import BaseActions


class ShoppingCart(BaseActions):

        shopping_cart = ShoppingCart
        auth = Authorization

        def add_to_shopping_cart(self):
            self._click(*self.auth.logo_name)
            assert self._wd.find_element(*self.auth.logo_name).is_displayed()
            cart_buttons = self._wd.find_elements(*self.shopping_cart.add_to_cart_button)

            for element in cart_buttons:
                assert element is not None
                print(element.text)

            cart_button = self._wd.find_elements(*self.shopping_cart.add_to_cart_button)[0]
            cart_button.click()
            self._click(*self.shopping_cart.cart_link)
            assert self._wd \
                .find_element(*self.shopping_cart.cart_product_name) \
                .text == 'MacBook'

        def remove_position_from_shopping_cart(self):
            self._click(*self.auth.logo_name)
            assert self._wd.find_element(*self.auth.logo_name).is_displayed()
            self._click(*self.shopping_cart.cart_link)
            self._click(*self.shopping_cart.delete_cart_position_button)
            assert self._wd \
                .find_element(*self.shopping_cart.cart_info) \
                .text == 'Shopping Cart'

