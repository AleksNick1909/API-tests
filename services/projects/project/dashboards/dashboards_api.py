import allure

from config.base_api import BaseAPI
from services.projects.project.dashboards.routes.dashboards_routes import DashboardsRoutes
from services.projects.project.dashboards.models.model_dashboards import *
from services.projects.project.dashboards.models.model_dashboard_s_curve import DashboardsSCurveSchema
from services.projects.project.dashboards.models.model_dashboards_settings import DashboardsSettingsSchema


class DashboardsAPI(BaseAPI):

    @allure.step(f'Изменение периода')
    def update_dashboard_period(self, payload) -> DashboardsSettingsSchema:
        return self.client.put(endpoint=f'{DashboardsRoutes.dashboard()}{DashboardsRoutes.settings}',
                               model=DashboardsSettingsSchema,
                               json=payload)

    @allure.step(f'Получение основной информации дашборда')
    def get_general_information_dashboard(self) -> GeneralInfoDashboardSchema:
        return self.client.get(endpoint=DashboardsRoutes.dashboard_general_information(),
                               model=GeneralInfoDashboardSchema)

    @allure.step(f'Получение данных по диаграмме "S-кривая"')
    def get_dashboard_diagram_s_curve(self, params) -> DashboardsSCurveSchema:
        return self.client.get(endpoint=DashboardsRoutes.dashboard_s_curve(),
                               model=DashboardsSCurveSchema,
                               params=params)

    @allure.step(f'Получение данных по диаграмме "Инспекции"')
    def get_dashboard_diagram_inspections(self, params) -> InspectionDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}{DashboardsRoutes.inspection}',
                               model=InspectionDashboardSchema,
                               params=params)

    @allure.step(f'Получение данных по диаграмме "Предписания"')
    def get_dashboard_diagram_prescription(self, params) -> PrescriptionDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}{DashboardsRoutes.prescription}',
                               model=PrescriptionDashboardSchema,
                               params=params)

    @allure.step(f'Получение данных по диаграмме "Аудиты"')
    def get_dashboard_diagram_audits(self, params) -> AuditDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}{DashboardsRoutes.audit}',
                               model=AuditDashboardSchema,
                               params=params)

    @allure.step(f'Получение данных по диаграмме "Замечания, несоответствия"')
    def get_dashboard_diagram_remark(self, params) -> RemarkDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}{DashboardsRoutes.remark}',
                               model=RemarkDashboardSchema,
                               params=params)

    @allure.step(f'Получение данных "Инспекции" по диаграмме "Оборудование и материалы"')
    def get_dashboard_diagram_inspection_in_equipment(self, params) -> EquipmentMaterialsDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}'
                                        f'{DashboardsRoutes.equipment_materials_inspection}',
                               model=EquipmentMaterialsDashboardSchema,
                               params=params)

    @allure.step(f'Получение данных "Замечания" по диаграмме "Оборудование и материалы"')
    def get_dashboard_diagram_remark_in_equipment(self, params) -> EquipmentMaterialsDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}'
                                        f'{DashboardsRoutes.equipment_materials_remarks}',
                               model=EquipmentMaterialsDashboardSchema,
                               params=params)

    @allure.step(f'Получение данных "Документация" по диаграмме "Оборудование и материалы"')
    def get_dashboard_diagram_documentation_in_equipment(self, params) -> EquipmentMaterialsDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}'
                                        f'{DashboardsRoutes.equipment_materials_documentation}',
                               model=EquipmentMaterialsDashboardSchema,
                               params=params)

    @allure.step(f'Получение данных по диаграмме "Исполнительная документация"')
    def get_dashboard_diagram_exec_doc(self, params) -> ExecDocDashboardSchema:
        return self.client.get(endpoint=f'{DashboardsRoutes.dashboard_diagram()}'
                                        f'{DashboardsRoutes.executive_documentation}',
                               model=ExecDocDashboardSchema,
                               params=params)
