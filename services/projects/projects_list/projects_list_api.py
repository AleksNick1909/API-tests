import allure
from config.base_api import BaseAPI

from services.projects.projects_list.routes.projects_routes import ProjectsRoutes
from services.projects.projects_list.models.model_projects_list import *

from services.projects.projects_list.generators.projects_get import GetProjectsGen
from services.projects.projects_list.generators.projects_create import CreateProjectGen


class ProjectListAPI(BaseAPI):

    @allure.step('Получение списка проектов')
    def get_projects_list(self) -> ProjectsListModel:
        params = GetProjectsGen().set_count().set_page().set_company_id().build()
        projects_list = self.client.get(endpoint=ProjectsRoutes.get_projects_api(),
                                        model=ProjectsListModel,
                                        params=params)
        return projects_list

    @allure.step('Создание проекта')
    def create_project(self) -> ConstructionProjectSchema:
        body = CreateProjectGen().set_company_id().set_row_id().build()
        project = self.client.post(endpoint=ProjectsRoutes.create_project_api(),
                                   model=ConstructionProjectSchema,
                                   json=body)
        return project

    @allure.step('Обновление проекта')
    def update_project(self, payload) -> ConstructionProjectSchema:
        project = self.client.patch(endpoint=ProjectsRoutes.update_project_api(),
                                    model=ConstructionProjectSchema,
                                    json=payload)
        return project

    @allure.step('Удаление проекта')
    def delete_project(self, param):
        self.client.delete(endpoint=ProjectsRoutes.delete_project_api(),
                           params=param)
