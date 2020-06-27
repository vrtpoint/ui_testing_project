"""Модуль с методами для работы с корзиной покупок приложения"""
from resources.locators.application.authorization import AuthorizationLocators
from resources.locators.application.shopping_cart import ShoppingCartLocators
from resources.common.base_actions import BaseActions


class ShoppingCartPage(BaseActions):

        shopping_cart = ShoppingCartLocators
        auth = AuthorizationLocators

        def add_to_shopping_cart(self):
            self._click(*self.auth.logo_name)
            assert self._driver.find_element(*self.auth.logo_name).is_displayed()
            cart_buttons = self._driver.find_elements(*self.shopping_cart.add_to_cart_button)

            for element in cart_buttons:
                assert element is not None
                print(element.text)

            cart_button = self._driver.find_elements(*self.shopping_cart.add_to_cart_button)[0]
            cart_button.click()
            self._click(*self.shopping_cart.cart_link)
            assert self._driver \
                .find_element(*self.shopping_cart.cart_product_name) \
                .text == 'MacBook'

        def remove_position_from_shopping_cart(self):
            self._click(*self.auth.logo_name)
            assert self._driver.find_element(*self.auth.logo_name).is_displayed()
            self._click(*self.shopping_cart.cart_link)
            self._click(*self.shopping_cart.delete_cart_position_button)
            assert self._driver \
                .find_element(*self.shopping_cart.cart_info) \
                .text == 'Shopping Cart'

