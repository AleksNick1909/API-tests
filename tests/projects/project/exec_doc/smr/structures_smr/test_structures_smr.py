import allure
from config.base_test import BaseTest


@allure.parent_suite('API test case')
@allure.epic('API test case')
@allure.feature('Структура СМР')
class TestStructuresSmr(BaseTest):

    @allure.title('Получение структуры СМР')
    def test_get_structures_smr(self):
        structures_smr = self.structures_smr_api.get_structures_smr_api()
        print(structures_smr)

    @allure.title('Создание структуры СМР')
    def test_create_structures_smr(self):
        structures_smr = self.structures_smr_api.create_structures_smr_api()
        print(structures_smr)

    @allure.title('Удаление структуры СМР')
    def test_create_and_delete_structures_smr(self):
        structures_smr = self.structures_smr_api.create_structures_smr_api()
        self.structures_smr_api.delete_structures_smr_api(structure_smr_id=structures_smr.id)
