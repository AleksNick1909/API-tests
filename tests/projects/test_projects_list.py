import allure
import pytest
from config.base_test import BaseTest

from services.projects.projects_list.generators.projects_update import UpdateProjectGen
from services.projects.projects_list.generators.projects_delete import DeleteProjectsGen


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

    # @allure.title('Обновление проекта')
    # def test_update_project(self):
    #     with allure.step('Изменить данные проекта'):
    #         full_name = 'New Project Name'
    #         object_number = '2'
    #         short_name = 'Sub New Project Name'
    #         body = (UpdateProjectGen().set_full_name(full_name).set_object_number(object_number).
    #                 set_short_name(short_name).build())
    #         project = self.projects_list_api.update_project(payload=body)
    #         assert project.full_name == full_name
    #         assert project.object_number == object_number
    #         assert project.short_name == short_name

    @pytest.mark.parametrize('field_name, field_value, readable_name', [
        ('full_name', 'New Project Name', 'Наименование'),
        ('object_number', '2', 'Номер'),
        ('short_name', 'Sub New Project Name', 'Наименование краткое')
    ])
    def test_update_project_single_field(self, field_name, field_value, readable_name):
        allure.dynamic.title(f'Обновление поля - "{readable_name}"')

        with allure.step(f'Изменить "{readable_name}" проекта'):
            update_project_gen = UpdateProjectGen()
            setter_method = getattr(update_project_gen, f'set_{field_name}')
            setter_method(field_value)

            body = update_project_gen.build()
            project = self.projects_list_api.update_project(payload=body)

        with allure.step(f'Проверить, что "{readable_name}" обновилось корректно'):
            actual_value = getattr(project, field_name)
            assert actual_value == field_value

    @allure.title('Удаление проекта')
    def test_delete_project(self):
        with allure.step('Создать новый проект'):
            project_id = self.projects_list_api.create_project().id
        with allure.step('Удалить проект'):
            body = DeleteProjectsGen().set_selected_ids(project_id).build()
            self.projects_list_api.delete_project(payload=body)

    def test_numerations(self):
        numerations = self.project_numerations_api.get_numerations_section()
        print(numerations)
