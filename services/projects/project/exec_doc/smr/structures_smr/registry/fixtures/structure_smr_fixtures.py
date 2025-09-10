import pytest
import allure
from services.projects.project.exec_doc.smr.structures_smr.registry.structures_smr_api import StructuresSmrAPI
from services.projects.project.exec_doc.smr.structures_smr.registry.generators.jobs_create import CreateJobGen


@pytest.fixture(scope='class')
def class_structures_smr_client() -> StructuresSmrAPI:
    return StructuresSmrAPI()


@pytest.fixture(scope='function')
@allure.step(f'Создание и удаление структуры СМР')
def ficture_create_and_delete_structures_smr(class_structures_smr_client: StructuresSmrAPI, request):
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
def ficture_create_job_in_structure_smr(class_structures_smr_client: StructuresSmrAPI, request):
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
