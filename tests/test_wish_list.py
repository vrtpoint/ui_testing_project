from decouple import config


def test_adding_to_wish_list(driver):
    """Тест добавления позиции в список желаемых покупок"""
    driver.open(config('url'))
    driver.authorization.login(config('app_username'), config('app_password'))
    driver.wish_list.add_to_wish_list()
    driver.authorization.logout()

def test_removal_position_from_wish_list(driver):
    """Тест удаления позиции из списка желаемых покупок"""
    driver.open(config('url'))
    driver.authorization.login(config('app_username'), config('app_password'))
    driver.wish_list.remove_from_wish_list()
    driver.authorization.logout()



