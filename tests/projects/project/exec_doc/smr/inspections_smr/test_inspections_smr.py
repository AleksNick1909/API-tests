from config.base_test import BaseTest
from services.settings.smr.types_inspections.fixtures.types_inspections_fixtures import *
from services.projects.project.exec_doc.smr.inspections_smr.fixtures.inspections_fixtures import *


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
        inspection_smr = self.inspections_smr_api.create_inspections_smr_api(type_inspection_smr)[0]
        print(inspection_smr.id)

    # def test_inspections_smr(self, fixture_create_inspection, fixture_update_inspection_smr):
    #     inspection = fixture_create_inspection(type_inspection='СК')
    #     print(inspection)
    #     random_date = fake.date_between(start_date="today", end_date="+30d")
    #     planned_date_begin = random_date.strftime("%Y-%m-%d 00:00:00")
    #     fixture_update_inspection_smr(inspection_id=inspection.id, planned_date_begin=planned_date_begin)
