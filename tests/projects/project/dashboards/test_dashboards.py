from config.base_test import BaseTest
from services.projects.project.dashboards.fixtures.dashboards_structure_smr_fixtures import *
from services.projects.project.dashboards.fixtures.dashboards_fixtures import *
from services.projects.project.dashboards.fixtures.dashboards_inspections_smr_fixtures import *

from services.projects.project.dashboards.generators.dashboards_update import UpdateDashboardsGen
from services.projects.project.exec_doc.smr.inspections_smr.enums.inspections_enums import *

from datetime import datetime, timedelta
today = date.today()


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

    @pytest.mark.parametrize(
        'dates, description',
        get_test_cases_dates('week')
    )
    @allure.title('п.3, Проверка отображения инспекций СК в диаграмме "Инспекции" с периодом "Неделя"')
    def test_diagram_inspections_sk_week(self,
                                         class_dashboards_client: DashboardsAPI,
                                         fixture_create_structure_smr_for_dashboard,
                                         fixture_create_inspections_for_dashboard,
                                         fixture_count_inspections,
                                         dates, description):

        with allure.step('Создание структуры СМР и работы внутри нее'):
            job = fixture_create_structure_smr_for_dashboard
        with allure.step('Создание инспекций СК со статусами "Создано", "В работе", "Принято", "Отклонено"'):
            inspection_statuses = [
                InspectionStatuses.ACCEPTED,
                InspectionStatuses.IN_WORK,
                None,  # статус по умолчанию "Создано"
                InspectionStatuses.REJECTED
            ]
            for status in inspection_statuses:
                fixture_create_inspections_for_dashboard(
                    job_id=job.id, inspection_type=InspectionTypes.SK, status_name=status)

        with allure.step('Проверка кол-ва инспекций СК за период "Неделя" в диаграмме "Инспекции"'):
            with allure.step('Выбрать период "Неделя"'):
                body = UpdateDashboardsGen().set_all_period().set_scale('week').build()
                class_dashboards_client.update_dashboard_period(payload=body)

            with allure.step(f'Подсчет кол-ва инспекций СК по статусам "Принято", "Отклонено", '
                             f'за период "Неделя" с указанием даты: {dates} ({description})'):
                end_date = (datetime.strptime(dates, '%Y-%m-%d') + timedelta(days=7)).strftime('%Y-%m-%d')
                count_sk_accepted = fixture_count_inspections(
                    InspectionTypes.SK, InspectionStatuses.ACCEPTED, fact_date=dates, end_date=end_date)
                count_sk_rejected = fixture_count_inspections(
                    InspectionTypes.SK, InspectionStatuses.REJECTED, fact_date=dates, end_date=end_date)
                count_sk_total = fixture_count_inspections(
                    InspectionTypes.SK, status=None, planned_date=dates, end_date=end_date)
                params = UpdateDashboardsGen().set_parameters('СК').set_date(dates=dates).set_scale('week').build()
                diagram_inspections_sk = class_dashboards_client.get_dashboard_diagram_inspections(params=params)

                assert count_sk_accepted == diagram_inspections_sk.accepted, (
                    f'Неверное кол-во инспекций СК (статус: "Принято") для даты {dates} ({description}). '
                    f'Ожидалось: {count_sk_accepted}, получено: {diagram_inspections_sk.accepted}')
                assert count_sk_rejected == diagram_inspections_sk.rejected, (
                    f'Неверное кол-во инспекций СК (статус: "Отклонено") для даты {dates} ({description}). '
                    f'Ожидалось: {count_sk_rejected}, получено: {diagram_inspections_sk.rejected}')
                assert count_sk_total == diagram_inspections_sk.total, (
                    f'Неверное кол-во всех инспекций СК для даты {dates} ({description}). '
                    f'Ожидалось: {count_sk_total}, получено: {diagram_inspections_sk.total}')

    @pytest.mark.parametrize(
        'dates, description',
        get_test_cases_dates('month')
    )
    @allure.title('п.4, Проверка отображения инспекций СК в диаграмме "Инспекции" с периодом "Месяц"')
    def test_diagram_inspections_sk_month(self,
                                          class_dashboards_client: DashboardsAPI,
                                          fixture_create_structure_smr_for_dashboard,
                                          fixture_create_inspections_for_dashboard, fixture_count_inspections,
                                          dates, description):

        with allure.step('Создание структуры СМР и работы внутри нее'):
            job = fixture_create_structure_smr_for_dashboard
        with allure.step('Создание инспекций СК со статусами "Создано", "В работе", "Принято", "Отклонено"'):
            inspection_statuses = [
                InspectionStatuses.ACCEPTED,
                InspectionStatuses.IN_WORK,
                None,  # статус по умолчанию "Создано"
                InspectionStatuses.REJECTED
            ]
            for status in inspection_statuses:
                fixture_create_inspections_for_dashboard(
                    job_id=job.id, inspection_type=InspectionTypes.SK, status_name=status)

        with allure.step('Проверка кол-ва инспекций СК за период "Месяц" в диаграмме "Инспекции"'):
            with allure.step('Выбрать период "Месяц"'):
                body = UpdateDashboardsGen().set_all_period().set_scale('month').build()
                class_dashboards_client.update_dashboard_period(payload=body)

            with allure.step(f'Подсчет кол-ва инспекций СК по статусам "Принято", "Отклонено", '
                             f'за период "Месяц" с указанием даты: {dates} ({description})'):
                end_date = (datetime.strptime(dates, '%Y-%m-%d') + timedelta(days=30)).strftime('%Y-%m-%d')
                count_sk_accepted = fixture_count_inspections(
                    InspectionTypes.SK, InspectionStatuses.ACCEPTED, fact_date=dates, end_date=end_date)
                count_sk_rejected = fixture_count_inspections(
                    InspectionTypes.SK, InspectionStatuses.REJECTED, fact_date=dates, end_date=end_date)
                count_sk_total = fixture_count_inspections(
                    InspectionTypes.SK, status=None, planned_date=dates, end_date=end_date)
                params = UpdateDashboardsGen().set_parameters('СК').set_date(dates=dates).set_scale('month').build()
                diagram_inspections_sk = class_dashboards_client.get_dashboard_diagram_inspections(params=params)

                assert count_sk_accepted == diagram_inspections_sk.accepted, (
                    f'Неверное кол-во инспекций СК (статус: "Принято") для даты {dates} ({description}). '
                    f'Ожидалось: {count_sk_accepted}, получено: {diagram_inspections_sk.accepted}')
                assert count_sk_rejected == diagram_inspections_sk.rejected, (
                    f'Неверное кол-во инспекций СК (статус: "Отклонено") для даты {dates} ({description}). '
                    f'Ожидалось: {count_sk_rejected}, получено: {diagram_inspections_sk.rejected}')
                assert count_sk_total == diagram_inspections_sk.total, (
                    f'Неверное кол-во всех инспекций СК для даты {dates} ({description}). '
                    f'Ожидалось: {count_sk_total}, получено: {diagram_inspections_sk.total}')
