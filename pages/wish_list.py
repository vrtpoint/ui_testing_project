from locators.main_page import MainPage
from pages.helpers.base_actions import BaseActions


class WishList(BaseActions):

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
