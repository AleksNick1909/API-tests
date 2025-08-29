import allure
from config.base_test import BaseTest


@allure.parent_suite('API test case')
@allure.epic('API test case')
@allure.feature('Реестр проектов')
class TestProjectsList(BaseTest):

    @allure.title('Получение списка проектов')
    def test_projects_list(self):
        self.projects_list_api.get_projects_list()

    @allure.title('Создание проекта')
    def test_create_project(self):
        project = self.projects_list_api.create_project()
        assert project.full_name == 'Новый проект'

    @allure.title('Обновление проекта')
    def test_update_project(self):
        project = self.projects_list_api.update_project(
            fullName="New Project Name",
            objectNumber="2",
            shortName="Sub New Project Name",
        )
        assert project.full_name == "New Project Name"
