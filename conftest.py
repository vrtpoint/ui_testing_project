""" Модуль с фикстурой для работы браузера и условиями запуска из командной строки"""
import pytest
import logging
from fixtures.browser import Browser


def pytest_addoption(parser):
    """Добавление различных аргументов командной строки"""
    parser.addoption("--browser", action="store", default="chrome",
                     help="This is request browser", required=False)
    parser.addoption("--implicitly_wait", action="store", default="3",
                     help="waiting time in the seconds", required=False)
    parser.addoption("--headless", action="store", default=False,
                     help="This is headless mode")
    parser.addoption("--file", action='store', default=None,
                     help='file with log report')


@pytest.fixture()
def driver(request):
    """Фикстура запуска различных браузеров"""
    active_browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    headless = request.config.getoption("--headless")
    filename = request.config.getoption('--file')

    active_browser = Browser(browser=active_browser, wait=wait, headless=headless )
    logging.basicConfig(level=logging.INFO, filename=filename)
    active_browser.browser_log.info(f'{active_browser} is starting!')

    yield active_browser.driver
    active_browser.driver.quit()
    active_browser.browser_log.info(f'{active_browser} is stopping!')




# import pytest
# from selenium import webdriver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="firefox",
#                      help="This is request browser", required=False)
#     parser.addoption("--headless", action="store", default=False,
#                      help="This is headless mode")
#
# @pytest.fixture(scope="session")
# def driver(request):
#     browser = request.config.getoption("--browser")
#     headless = request.config.getoption("--headless")
#     if browser == 'chrome':
#         if headless == False:
#             driver = webdriver.Chrome()
#         else:
#             options = webdriver.ChromeOptions()
#             options.add_argument("--headless")
#             driver = webdriver.Chrome(options=options)
#     elif browser == "firefox":
#         if headless == False:
#            driver = webdriver.Firefox()
#         else:
#             options = webdriver.FirefoxOptions()
#             options.add_argument("--headless")
#             driver = webdriver.Firefox(options=options)
#     elif browser == "safari":
#         driver = webdriver.Safari()
#     elif browser == "opera":
#         driver = webdriver.Opera()
#
#     request.addfinalizer(driver.close)
#
#     return driver