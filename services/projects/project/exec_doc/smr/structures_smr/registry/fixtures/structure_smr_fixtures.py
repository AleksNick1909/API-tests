import pytest
import allure
from services.projects.project.exec_doc.smr.structures_smr.registry.structures_smr_api import StructuresSmrAPI
from services.projects.project.exec_doc.smr.structures_smr.registry.generators.jobs_create import CreateJobGen
from services.projects.project.exec_doc.smr.structures_smr.registry.generators.jobs_update import UpdateJobGen


@pytest.fixture(scope='class')
def class_structures_smr_client() -> StructuresSmrAPI:
    return StructuresSmrAPI()


@pytest.fixture(scope='function')
@allure.step(f'Создание и удаление структуры СМР')
def fixture_create_and_delete_structures_smr(class_structures_smr_client: StructuresSmrAPI, request):
    """
        Фикстура создает новую структуру смр и вложенные объекты"
        В конце удаляет структуру смр
    """
    structure_smr = class_structures_smr_client.create_structures_smr_api()
    structure_smr_id = structure_smr.id

    print(f'ID созданной структуры СМР: {structure_smr_id}')

    # Функция удаляет созданную структуру СМР
    def cleanup():
        class_structures_smr_client.delete_structures_smr_api(structure_smr_id=structure_smr_id)
    request.addfinalizer(cleanup)
    return structure_smr


@pytest.fixture(scope='function')
@allure.step(f'Создание работы в структуре СМР')
def fixture_create_job_in_structure_smr(class_structures_smr_client: StructuresSmrAPI, request):
    """
        Фикстура создает новую работу в структуре смр"
        В конце удаляет структуру смр
    """
    structure_smr = class_structures_smr_client.create_structures_smr_api()
    structure_smr_id = structure_smr.id
    print(f'ID созданной структуры СМР: {structure_smr_id}')

    body = CreateJobGen().set_structure_smr_id(structure_smr_id).set_user_id().build()
    job = class_structures_smr_client.create_job_in_structures_smr_api(payload=body)
    print(f'ID созданной работы: {job.id}')

    # Функция удаляет созданную структуру СМР
    def cleanup():
        class_structures_smr_client.delete_structures_smr_api(structure_smr_id=structure_smr_id)
    request.addfinalizer(cleanup)
    return job


@pytest.fixture(scope='function')
@allure.step(f'Изменение данных в работе')
def fixture_update_job(class_structures_smr_client: StructuresSmrAPI):
    def _fixture_update_job(job_id, qty=None, price=None, labor_costs=None, date_begin_plan=None, date_end_plan=None,
                            journal_id=None, type_of_work_id=None, setting_atg_middle_id=None, custom_rep_name=None,
                            representative_id=None, customer_name=None, customer_id=None, units=None,
                            exec_doc_ids=None):
        body = (UpdateJobGen().set_job_id(job_id).set_qty_contract(qty).set_price_plan(price).set_labor_costs(
            labor_costs).set_date_begin_plan(date_begin_plan).set_date_end_plan(date_end_plan).set_journal_id(
            journal_id).set_type_of_work_id(type_of_work_id).set_setting_atg_middle_id(setting_atg_middle_id)
                .set_custom_rep_name(custom_rep_name).set_representative_id(representative_id).set_customer_name(
            customer_name).set_customer_id(customer_id).set_units(units).set_exec_doc_ids(exec_doc_ids).build())
        class_structures_smr_client.update_job_in_structures_smr_api(payload=body)
    return _fixture_update_job
