import pytest
import allure
from config.auth import set_project_id
from services.projects.projects_list.projects_list_api import ProjectListAPI
from services.projects.projects_list.generators.projects_delete import DeleteProjectsGen


@pytest.fixture(scope='class')
def class_object_list_client() -> ProjectListAPI:
    return ProjectListAPI()


@pytest.fixture(scope='class')
@allure.step(f'Создание и удаление проекта')
def function_create_and_delete_project(class_object_list_client: ProjectListAPI, request):
    """
        Фикстура оздает новый проект"
        Записывает id созданной стройки в config.auth.project_id
        В конце удаляет созданный проект
    """
    construction = class_object_list_client.create_project()
    project_id = construction.id
    set_project_id(project_id)

    # Функция удаляет созданный проект
    def cleanup():
        param = DeleteProjectsGen().set_selected_ids(project_id).build()
        class_object_list_client.delete_project(param=param)
    request.addfinalizer(cleanup)
    return construction
