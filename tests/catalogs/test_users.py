import allure
from config.base_test import BaseTest


@allure.parent_suite('API test case')
@allure.epic('API test case')
@allure.feature('Пользователи')
class TestUsers(BaseTest):

    @allure.title('Получение информации о пользователе')
    def test_get_user(self):
        user = self.users_api.get_user()
