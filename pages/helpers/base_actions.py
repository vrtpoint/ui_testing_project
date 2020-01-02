from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseActions:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd
        self.wait = WebDriverWait(self.wd, 30)

    def searching_element(self, type_selector, selector):
        self.wait.until(EC.visibility_of_element_located((type_selector, selector)))
        self.wait.until(EC.element_to_be_clickable((type_selector, selector)))
        return self.wd.find_element(type_selector, selector)

    def waiting_for_element(self, type_selector, selector):
        self.wait.until(EC.visibility_of_element_located((type_selector, selector)))

    def click(self, type_selector, selector):
        self.searching_element(type_selector, selector).click()

    def input(self, type_selector, selector, value):
        self.searching_element(type_selector, selector).clear()
        self.searching_element(type_selector, selector).send_keys(value)