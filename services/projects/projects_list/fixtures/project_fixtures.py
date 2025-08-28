import pytest
import allure
from config.auth import set_project_id
from services.projects.projects_list.projects_list_api import ProjectListAPI


@pytest.fixture(scope='class')
def class_object_list_api() -> ProjectListAPI:
    return ProjectListAPI()


@pytest.fixture(scope='function')
@allure.step(f'Создание и удаление проекта')
def function_create_and_delete_project(class_object_list_api: ProjectListAPI, request):
    """
    Создает новый проект"
    Записывает id созданной стройки в config.auth.project_id
    В конце удаляет созданный проект
    """
    construction = class_object_list_api.create_project()
    project_id = construction.id
    set_project_id(project_id)

    print(f'ID созданного проекта: {project_id}')

    # Функция удаляет созданный проект
    # def cleanup():
    #     class_object_list_api.delete_project(project_id=project_id)
    # request.addfinalizer(cleanup)
    return construction
