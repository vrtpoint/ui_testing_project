import pytest


class BaseSetUp:

    @pytest.fixture(autouse=True)
    def action_driver(self, driver):
        self.driver = driver
        yield self.driver

    def get_page(self, Page):
        return Page(self.driver)