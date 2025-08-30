from config.base_test import BaseTest
from config.auth import current_user

from services.projects.project.exec_doc.smr.structures_smr.registry.generators. \
    structure_smr_update import UpdateStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.registry.fixtures.structure_smr_fixtures import *


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

    @allure.title('Обновление структуры СМР')
    def test_update_structures_smr(self, ficture_create_and_delete_structures_smr):
        with allure.step('Создание структуры СМР'):
            new_structure_smr = ficture_create_and_delete_structures_smr
        with allure.step('Обновление структуры СМР'):
            fild_identifier = 'id_1'
            fild_cipher = 'Шифр_1'
            body = (UpdateStructureSmrGen().set_identifier(fild_identifier).set_cipher(fild_cipher).
                    set_representative_id().set_customer_id().build())
            structure_smr = self.structures_smr_api.update_structures_smr_api(
                structure_smr_id=new_structure_smr.id, payload=body)

            assert structure_smr.identifier == 'id_1'
            assert structure_smr.cipher == 'Шифр_1'
            assert structure_smr.representative.id == current_user.representative_id
            assert structure_smr.customer.id == current_user.representative_id

    @allure.title('Удаление структуры СМР')
    def test_create_and_delete_structures_smr(self):
        structures_smr = self.structures_smr_api.create_structures_smr_api()
        self.structures_smr_api.delete_structures_smr_api(structure_smr_id=structures_smr.id)
