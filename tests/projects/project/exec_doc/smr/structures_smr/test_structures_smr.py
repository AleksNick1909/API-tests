from config.base_test import BaseTest
from config.auth import current_user

from services.projects.project.exec_doc.smr.structures_smr.registry.generators. \
    structure_smr_update import UpdateStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.registry.fixtures.structure_smr_fixtures import *
from datetime import date

today_date = str(date.today())


@allure.parent_suite('API test case')
@allure.epic('API test case')
@allure.feature('Структура СМР')
class TestStructuresSmr(BaseTest):

    @allure.title('Получение данных структуры СМР')
    def test_get_structures_smr(self):
        structures_smr = self.structures_smr_api.get_structures_smr_api()
        print(structures_smr)

    @allure.title('Создание нового раздела в структуре СМР')
    def test_create_structures_smr(self):
        structures_smr = self.structures_smr_api.create_structures_smr_api()
        print(structures_smr)

    @allure.title('Обновление раздела в структуре СМР')
    def test_update_structures_smr(self, fixture_create_and_delete_structures_smr):
        with allure.step('Создать новый раздел'):
            new_structure_smr = fixture_create_and_delete_structures_smr
        with allure.step('Обновить данные раздела'):
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

    @allure.title('Создание работы в структуре СМР')
    def test_create_job_in_structures_smr(self, fixture_create_and_delete_structures_smr):
        with allure.step('Создать новый раздел в структуре СМР'):
            new_structure_smr = fixture_create_and_delete_structures_smr.id
        with allure.step('Создать работу внутри раздела'):
            body = CreateJobGen().set_structure_smr_id(new_structure_smr).set_user_id().build()
            job_id = self.structures_smr_api.create_job_in_structures_smr_api(payload=body).id
        with allure.step('Получить данные по работе'):
            job = self.structures_smr_api.get_job_in_structures_smr_api(job_id=job_id)
            assert today_date in job.date

    @allure.title('Обновление данных работы в структуре СМР')
    def test_update_job_in_structure_smr(self, fixture_create_job_in_structure_smr):
        with allure.step('Создать новый раздел, внутри раздела создать работу'):
            job = fixture_create_job_in_structure_smr
        with allure.step('Обновить данные работы'):
            fild_identifier = 'id_1'
            fild_cipher = 'Шифр_1'
            body = UpdateJobGen().set_job_id(job.id).set_identifier(fild_identifier).set_cipher(fild_cipher).build()
            job = self.structures_smr_api.update_job_in_structures_smr_api(payload=body)
            assert job[0].identifier == fild_identifier
            assert job[0].cipher == fild_cipher

    @allure.title('Удаление раздела в структуре СМР')
    def test_create_and_delete_structures_smr(self):
        with allure.step('Создать раздел в структуре СМР'):
            structures_smr = self.structures_smr_api.create_structures_smr_api()
        with allure.step('Удалить раздел в структуре СМР'):
            self.structures_smr_api.delete_structures_smr_api(structure_smr_id=structures_smr.id)
