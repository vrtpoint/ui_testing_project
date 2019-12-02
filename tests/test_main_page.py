from config import setUpConfig


data = setUpConfig()

def test_adding_to_wish_list(driver):
    """Тест добавления позиции в список желаемых покупок"""
    driver.authorization.login(data['app_username'], data['app_password'])
    driver.products.add_to_wish_list()
    driver.authorization.logout()

def test_removal_position_from_wish_list(driver):
    """Тест удаления позиции из списка желаемых покупок"""
    driver.authorization.login(data['app_username'], data['app_password'])
    driver.products.remove_from_wish_list()
    driver.authorization.logout()

def test_adding_to_shopping_cart(driver):
    """Тест добавления позиции в корзину покупок"""
    driver.authorization.login(data['app_username'], data['app_password'])
    driver.products.add_to_shopping_cart()
    driver.authorization.logout()

def test_removal_position_from_shopping_cart(driver):
    """Тест удаления позиции из корзины покупок"""
    driver.authorization.login(data['app_username'], data['app_password'])
    driver.products.remove_position_from_shopping_cart()
    driver.authorization.logout()


