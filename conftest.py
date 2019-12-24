import pytest
from selenium import webdriver
from fixtures.root import DriverHelper

def pytest_addoption(parser):
    """Добавление аргументов командной строки: запуск различных браузеров, запуск в режиме headless"""
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--headless", action="store", default=False, help="This is headless mode")

@pytest.fixture(scope="session")
def driver(request):
    """Фикстура запуска различных браузеров в headless режимe"""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "opera":
        driver = webdriver.Opera()

    fixture = DriverHelper(driver)
    request.addfinalizer(fixture.destroy)

    return fixture