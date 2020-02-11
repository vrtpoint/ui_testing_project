from locators.authorization import Authorization
from locators.wish_list import WishList
from pages.helpers.base_actions import BaseActions


class WishList(BaseActions):


        wish_list = WishList
        auth = Authorization

        
        def add_to_wish_list(self):
            self._click(*self.auth.logo_name)
            assert self._wd.find_element(*self.auth.logo_name).is_displayed()
            feature_elements = self._wd.find_elements(*self.wish_list.featured_section)
            product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']

            for element in feature_elements:
                assert element.text in product_list
                print(element.text)

            feature_element = self._wd.find_elements(*self.wish_list.featured_section)[0]
            feature_element.click()
            self._click(*self.wish_list.wish_list_button)
            self._click(*self.wish_list.wish_list_link)
            assert self._wd \
                .find_element(*self.wish_list.wish_list_product_name) \
                .text == 'MacBook'

        def remove_from_wish_list(self):
            self._click(*self.auth.logo_name)
            assert self._wd.find_element(*self.auth.logo_name).is_displayed()
            feature_elements = self._wd.find_elements(*self.wish_list.featured_section)
            product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']

            for element in feature_elements:
                assert element.text in product_list
                print(element.text)

            feature_element = self._wd.find_elements(*self.wish_list.featured_section)[0]
            feature_element.click()
            self._click(*self.wish_list.wish_list_link)
            self._click(*self.wish_list.delete_wish_list_position_button)
            assert self._wd \
                .find_element(*self.wish_list.my_wish_list_breadcrumb) \
                .text == 'My Wish List'
