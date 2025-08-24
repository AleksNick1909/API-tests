from services.projects.projects_list.generators.projects_get import GetProjects
from services.projects.projects_list.generators.projects_create import CreateProject
from services.projects.projects_list.generators.projects_update import UpdateProject
from services.projects.projects_list.generators.projects_delete import DeleteProjects


class Payloads:

    def __init__(self):
        self.get = GetProjects()
        self.update = UpdateProject()
        self.create = CreateProject()
        self.delete = DeleteProjects()

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
