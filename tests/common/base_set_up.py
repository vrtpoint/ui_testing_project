import pytest


class TestBaseSetUp:

    @pytest.fixture(scope='class')
    def action_driver(self, driver):
        self.driver = driver
        return self.driver

    def get_page(self, Page):
        return Page(self.driver)