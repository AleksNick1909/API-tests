from config.base_test import BaseTest
import allure
from services.projects.project.dashboards.fixtures.dashboards_inspections_fixtures import *


@allure.parent_suite('API test case')
@allure.epic('API test case')
@allure.feature('Дашборды')
class TestDashboards(BaseTest):

    @allure.title('Получение основной информации в Дашборде')
    def test_open_dashboard(self):
        general_info = self.dashboards_api.get_general_information_dashboard()
        assert 0 == general_info.contributed_smr
        assert 0 == general_info.done_smr
        assert 0 == general_info.signed_exec_doc
        assert 0 == general_info.signed_kc
        assert general_info.cost_smr is None
        assert general_info.start_pnr_fact is None
        assert general_info.start_pnr_plan is None
        assert general_info.start_smr_fact is None
        assert general_info.start_smr_plan is None

    @allure.title('Получение основной информации в Дашборде')
    def test_dashboards(self, fixture_create_structure_smr_for_dashboard):
        job_id = fixture_create_structure_smr_for_dashboard
        print(job_id)
