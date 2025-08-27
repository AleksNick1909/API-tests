import pytest
from services.catalogs.users.users_api import UsersAPI
from services.projects.projects_list.projects_list_api import ProjectListAPI
from services.projects.project.exec_doc.smr.structures_smr.structures_smr_api import StructuresSmrAPI
from services.projects.project.exec_doc.smr.inspections_smr.inspections_smr_api import InspectionsSmrAPI


@pytest.mark.usefixtures('function_create_and_delete_project')
class BaseTest:

    def setup_method(self):
        self.users_api = UsersAPI()
        self.projects_list_api = ProjectListAPI()
        self.structures_smr_api = StructuresSmrAPI()
        self.inspections_smr_api = InspectionsSmrAPI()
