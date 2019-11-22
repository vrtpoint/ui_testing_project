from selenium import webdriver
import pytest


def pytest_addoption(parser):
    """Добавление различных аргументов командной строки"""
    parser.addoption("--browser", action="store", default="chrome", help="This is request browser", required=False)
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
        driver = webdriver.Firefox(options=options)
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "opera":
        driver = webdriver.Opera()

    request.addfinalizer(driver.close)
    return driver