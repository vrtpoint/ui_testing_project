from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseActions:

    def __init__(self, app):
        self.__app = app
        self.__wd = self.__app.wd
        self.__wait = WebDriverWait(self.__wd, 30)

    def __searching_element(self, type_selector, selector):
        self.__wait.until(EC.visibility_of_element_located((type_selector, selector)))
        self.__wait.until(EC.element_to_be_clickable((type_selector, selector)))
        return self.__wd.find_element(type_selector, selector)

    def __waiting_for_element(self, type_selector, selector):
        self.__wait.until(EC.visibility_of_element_located((type_selector, selector)))

    def __click(self, type_selector, selector):
        self.__searching_element(type_selector, selector).click()

    def __input(self, type_selector, selector, value):
        self.__searching_element(type_selector, selector).clear()
        self.__searching_element(type_selector, selector).send_keys(value)