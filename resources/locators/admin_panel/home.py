"""Модуль с локаторами панели администратора"""
from selenium.webdriver.common.by import By


class Menu:

    dashboard_title = (By.CSS_SELECTOR, '.page-header h1')
    logout_button = (By.CSS_SELECTOR, '.navbar-right .fa-sign-out')


class Catalog:

    catalog_list = (By.CSS_SELECTOR, '#menu-catalog .collapsed')
    products_element = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) a')
    downloads_element = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(8) a')
    add_button = (By.CSS_SELECTOR, '.container-fluid .pull-right .btn-primary i')
    edit_button = (By.CSS_SELECTOR, '.table-responsive tr [data-original-title="Edit"]')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')


class Products:

    products_list = (By.CSS_SELECTOR, '#form-product .table-responsive tr td:nth-child(3)')
    product_item = (By.CSS_SELECTOR, '.table-responsive tr input[type="checkbox"]')
    description_field = (By.CSS_SELECTOR, '.note-editor .panel-body')
    delete_product_item = (By.CSS_SELECTOR, '.container-fluid .pull-right .btn-danger')
    operation_status = (By.CSS_SELECTOR, '.alert-success.alert-dismissible')
    product_name_field = (By.CSS_SELECTOR, '#input-name1')
    meta_tag_title = (By.CSS_SELECTOR, '#input-meta-title1')
    data_link = (By.CSS_SELECTOR, '.nav-tabs li:nth-child(2)')
    model_field = (By.CSS_SELECTOR, '#input-model')
    image_link = (By.CSS_SELECTOR, '#form-product ul li:nth-child(9)')
    image_userpicture = (By.CSS_SELECTOR, '#thumb-image')
    edit_userpicture_button = (By.CSS_SELECTOR, '#button-image')



