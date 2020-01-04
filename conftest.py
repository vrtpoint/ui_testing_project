import pytest
from selenium import webdriver
from fixtures.root import DriverHelper

def pytest_addoption(parser):
    """Добавление аргументов командной строки: запуск различных браузеров, запуск в режиме headless"""
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--headless", action="store", default=False, help="This is headless mode")

@pytest.fixture(scope="session")
def driver(request):
    """Фикстура запуска различных браузеров в обычном и headless режимах"""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser == 'chrome':
        if headless == False:
            driver = webdriver.Chrome()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        if headless == False:
           driver = webdriver.Firefox()
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "opera":
        driver = webdriver.Opera()

    fixture = DriverHelper(driver)
    request.addfinalizer(fixture.destroy)

    return fixture