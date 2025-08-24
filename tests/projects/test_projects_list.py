from config.base_test import BaseTest


class TestProjectsList(BaseTest):

    def test_projects_list(self):
        self.projects_list_api.get_projects_list()

    def test_create_project(self):
        project = self.projects_list_api.create_project()
        print(project)

    def test_update_project(self):
        project = self.projects_list_api.update_project(
            fullName="New Project Name",
            objectNumber="2",
            shortName="Sub New Project Name",
        )
        print(f'{project.fullName} == "New Project Name"')
