import pytest


class TestBaseSetUp:

    @pytest.fixture(autouse=True)
    def action_driver(self, driver):
        self.driver = driver
        return self.driver

    def get_page(self, Page):
        return Page(self.driver)