from config.base_test import BaseTest
from services.settings.types_inspections.fixtures.types_inspections_fixtures import *


@allure.parent_suite('API test case')
@allure.epic('API test case')
@allure.feature('Инспекции СМР')
class TestInspectionsSmr(BaseTest):

    @allure.title('Получение списка инспекций СМР')
    def test_get_inspections_smr(self):
        self.inspections_smr_api.get_inspections_smr_api()

    @allure.title('Создание инспекции СМР')
    def test_create_inspections_smr(self, fixture_get_types_inspections):
        type_inspection_smr = fixture_get_types_inspections(type_inspection='СК')
        print(type_inspection_smr)
        inspection_smr = self.inspections_smr_api.create_inspections_smr_api(type_inspection_smr)
        print(inspection_smr)
