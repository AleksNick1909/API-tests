import allure
from config.base_api import BaseAPI


# from config.headers import Headers
from services.projects.projects_list.payloads import Payloads
from services.projects.projects_list.endpoints import Endpoints
from services.projects.projects_list.models.model_projects_list import *


class ProjectListAPI(BaseAPI):

    def __init__(self):
        # self._headers = Headers()
        self._endpoint = Endpoints()
        self._payload = Payloads()

    @allure.step('Получение списка проектов')
    def get_projects_list(self) -> ProjectsListModel:
        projects_list = self.client.get(
            endpoint=self._endpoint.get_projects_api(),
            model=ProjectsListModel,
            params=self._payload.get_projects()
        )
        return projects_list

    @allure.step('Создание проекта')
    def create_project(self):
        project = self.client.post(
            endpoint=self._endpoint.create_project_api(),
            model=ConstructionProjectSchema,
            json=self._payload.create_project()
        )
        return project

    @allure.step('Обновление проекта')
    def update_project(self, **kwargs):
        project = self.client.patch(
            endpoint=self._endpoint.update_project_api(),
            model=ConstructionProjectSchema,
            json=self._payload.update_project(**kwargs)
        )
        return project

    @allure.step('Удаление проекта')
    def delete_project(self, project_id):
        project = self.client.delete(
            endpoint=self._endpoint.delete_project_api(),
            params=self._payload.delete_project(project_id)
        )
        return project
