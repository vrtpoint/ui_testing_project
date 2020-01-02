from decouple import config
import allure


@allure.feature('Работа с корзиной')
def test_adding_to_shopping_cart(driver):
    """Тест добавления позиции в корзину покупок"""
    driver.open(config('url'))
    driver.authorization.login(config('app_username'), config('app_password'))
    driver.shopping_cart.add_to_shopping_cart()
    driver.authorization.logout()

@allure.feature('Работа с корзиной')
def test_removal_position_from_shopping_cart(driver):
    """Тест удаления позиции из корзины покупок"""
    driver.open(config('url'))
    driver.authorization.login(config('app_username'), config('app_password'))
    driver.shopping_cart.remove_position_from_shopping_cart()
    driver.authorization.logout()


