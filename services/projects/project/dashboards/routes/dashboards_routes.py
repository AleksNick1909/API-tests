from config.auth import current_user
from config.links import Links


class DashboardsRoutes:
    @staticmethod
    def dashboard():
        return f'{Links.API}/objects/{current_user.project_id}/dashboard'

    @staticmethod
    def dashboard_construction_objects():
        return f'{Links.API}/construction-objects/constructions-registry/dashboard/tier'

    # Основная информация
    @staticmethod
    def dashboard_general_information():
        return f'{DashboardsRoutes.dashboard()}/general-information'

    # S-кривая
    @staticmethod
    def dashboard_s_curve():
        return f'{DashboardsRoutes.dashboard()}/s-curve'

    # Диаграммы
    @staticmethod
    def dashboard_diagram():
        return f'{DashboardsRoutes.dashboard()}/diagram'

    inspection = "/inspection"
    prescription = "/prescription"
    audit = "/audit"
    remark = "/remark"
    equipment_materials_inspection = "/equipment-materials-inspection"
    equipment_materials_remarks = "/equipment-materials-remarks"
    equipment_materials_documentation = "/equipment-materials-documentation"
    executive_documentation = "/executive-documentation"
    settings = "/settings"
