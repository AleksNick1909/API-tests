import pytest
from services.catalogs.users.users_api import UsersAPI
from services.projects.projects_list.projects_list_api import ProjectListAPI
from services.projects.project.exec_doc.smr.structures_smr.registry.structures_smr_api import StructuresSmrAPI
from services.projects.project.exec_doc.smr.inspections_smr.inspections_smr_api import InspectionsSmrAPI
from services.projects.project.settings.numerations.numeration_api import ProjectNumerationsAPI
from services.projects.project.dashboards.dashboards_api import DashboardsAPI

from services.settings.smr.types_inspections.types_inspections_api import TypesInspectionsApi


@pytest.mark.usefixtures('function_create_and_delete_project')
class BaseTest:

    def setup_method(self):
        self.users_api = UsersAPI()
        self.projects_list_api = ProjectListAPI()
        self.structures_smr_api = StructuresSmrAPI()
        self.inspections_smr_api = InspectionsSmrAPI()
        self.settings_smr_api = TypesInspectionsApi()
        self.project_numerations_api = ProjectNumerationsAPI()
        self.dashboards_api = DashboardsAPI()
