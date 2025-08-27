from services.projects.projects_list.generators.projects_get import GetProjectsGen
from services.projects.projects_list.generators.projects_create import CreateProjectGen
from services.projects.projects_list.generators.projects_update import UpdateProjectGen
from services.projects.projects_list.generators.projects_delete import DeleteProjectsGen


class Payloads:

    def __init__(self):
        self.get = GetProjectsGen()
        self.update = UpdateProjectGen()
        self.create = CreateProjectGen()
        self.delete = DeleteProjectsGen()

    def get_projects(self):
        params = self.get.set_count().set_page().set_company_id().build()
        return params

    def create_project(self):
        body = self.create.set_company_id().set_row_id().build()
        return body

    def update_project(self, **kwargs):
        body = self.update.set_fields(**kwargs).build()
        return body

    def delete_project(self, project_id):
        body = self.delete.set_selected_ids(project_id).build()
        return body
