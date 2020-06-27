"""Модуль с методами для работы с продуктами в панеле администратора"""
import os
from resources.locators.admin_panel.home import Catalog, Products
from resources.common.base_actions import BaseActions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(BaseActions):

        LOGGER_NAME = 'AdminPanelAuthorizationPage'

        catalog = Catalog
        product = Products

        def __index__(self, driver):
            super().__init__(driver, self.LOGGER_NAME)

        def add_product_item(self):
            self._click(*self.catalog.catalog_list)
            self._click(*self.catalog.products_element)
            self._click(*self.catalog.add_button)
            self._input(*self.product.product_name_field, value='test')
            self._input(*self.product.description_field, value='test')
            self._input(*self.product.meta_tag_title, value='test')
            self._click(*self.product.data_link)
            self._input(*self.product.model_field, value='test')
            self._click(*self.catalog.submit_button)
            assert self._driver.find_element(*self.product.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
            self.logger.info('product item was added into product list')

        def edit_product_item(self):
            self._click(*self.catalog.catalog_list)
            self._click(*self.catalog.products_element)
            concrete_product = self._driver.find_elements(*self.product.product_item)[19]
            concrete_product.click()
            edit_element = self._driver.find_elements(*self.catalog.edit_button)[18]
            edit_element.click()
            self._input(*self.product.product_name_field, value='test_product')
            self._input(*self.product.description_field, value='test_product')
            self._click(*self.catalog.submit_button)
            assert self._driver.find_element(*self.product.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
            self.logger.info('product item was edited into product list')

        def delete_product_item(self):
            self._click(*self.catalog.catalog_list)
            self._click(*self.catalog.products_element)
            concrete_product = self._driver.find_elements(*self.product.product_item)[19]
            concrete_product.click()
            self._click(*self.product.delete_product_item)
            Alert(self._driver).accept()
            assert self._driver.find_element(*self.product.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
            self.logger.info('product item was deleted into product list')


