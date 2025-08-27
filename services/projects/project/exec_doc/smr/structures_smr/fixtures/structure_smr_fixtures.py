import pytest
import allure
from services.projects.project.exec_doc.smr.structures_smr.structures_smr_api import StructuresSmrAPI


@pytest.fixture(scope='class')
def class_structures_smr_api() -> StructuresSmrAPI:
    return StructuresSmrAPI()


@pytest.fixture(scope='function')
@allure.step(f'Создание и удаление проекта')
def ficture_create_and_delete_structures_smr(class_structures_smr_api: StructuresSmrAPI, request):
    """
    Фикстура создает новую структуру смр и вложенные объекты"
    В конце удаляет структуру смр
    """
    structure_smr = class_structures_smr_api.create_structures_smr_api()
    structure_smr_id = structure_smr.id

    print(f'ID созданной структуры СМР: {structure_smr_id}')

    # Функция удаляет созданный проект
    # def cleanup():
    #     class_structures_smr_api.delete_project(project_id=project_id)
    # request.addfinalizer(cleanup)
    return structure_smr
