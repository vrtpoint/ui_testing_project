from selenium.webdriver.common.alert import Alert
from locators.administrative.product_page import LoginProductPage, AdminPage
from pages.helpers.base_actions import BaseActions

class Products(BaseActions):

    def add_product_item(self):
        self.click(*self.AdminPage.catalog_list)
        self.click(*self.AdminPage.products_link)
        self.click(*self.AdminPage.Products.add_product_item)
        self.input(*self.AdminPage.Products.add_product_item, value = 'What is Lorem Ipsum?')
        self.input(*self.AdminPage.Products.meta_tag_title, value='What is Lorem Ipsum?')
        self.click(*self.AdminPage.Products.data_link)
        self.input(*self.AdminPage.Products.model_field, value='Product 1')
        self.click(*self.AdminPage.Products.submission_button)
        #assert
        self.click(*self.AdminPage.Products.logout_button)
        #assert

# def test_edition_product_item(driver):
#     """Тест изменения выбранного товара"""
#     driver.get(data['url'] + 'admin')
#     driver.find_element(*LoginProductPage.login_field).clear()
#     driver.find_element(*LoginProductPage.login_field).send_keys('user')
#     driver.find_element(*LoginProductPage.password_field).clear()
#     driver.find_element(*LoginProductPage.password_field).send_keys('bitnami1')
#     driver.find_element(*LoginProductPage.submit_login_button).click()
#     driver.find_element(*AdminPage.catalog_list).click()
#     driver.find_element(*AdminPage.products_link).click()
#     concrete_product = driver.find_elements(*AdminPage.Products.product_item)[1]
#     concrete_product.click()
#     edit_concrete_product = driver.find_elements(*AdminPage.Products.edit_product_item)[0]
#     edit_concrete_product.click()
#     driver.find_element(*AdminPage.Products.description_field).clear()
#     driver.find_element(*AdminPage.Products.description_field).send_keys('The Apple 30-Inch Cinema Display (Aluminum)')
#     driver.find_element(*AdminPage.Products.submition_button).click()
#     assert driver.find_element(*AdminPage.Products.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
#     driver.find_element(*AdminPage.logout_button).click()
#     assert driver.find_element(*LoginProductPage.entry_title).text == 'Please enter your login details.'
#
# def test_deletion_product_item(driver):
#     """Тест удаления выбранного товара"""
#     driver.get(data['url'] + 'admin')
#     driver.find_element(*LoginProductPage.login_field).clear()
#     driver.find_element(*LoginProductPage.login_field).send_keys('user')
#     driver.find_element(*LoginProductPage.password_field).clear()
#     driver.find_element(*LoginProductPage.password_field).send_keys('bitnami1')
#     driver.find_element(*LoginProductPage.submit_login_button).click()
#     driver.find_element(*AdminPage.catalog_list).click()
#     driver.find_element(*AdminPage.products_link).click()
#     concrete_product = driver.find_elements(*AdminPage.Products.product_item)[1]
#     concrete_product.click()
#     driver.find_element(*AdminPage.Products.delete_product_item).click()
#     Alert(driver).accept()
#     time.sleep(2)
#     assert driver.find_element(*AdminPage.Products.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
#     driver.find_element(*AdminPage.logout_button).click()
#     assert driver.find_element(*LoginProductPage.entry_title).text == 'Please enter your login details.'