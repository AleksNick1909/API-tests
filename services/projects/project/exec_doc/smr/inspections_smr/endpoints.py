from services.projects.project.exec_doc.smr.inspections_smr.routes.inspections_pnr_routes import InspectionsSmrRoutes
from config.auth import current_user


class InspectionsSmrEndpoints:

    @staticmethod
    def get_inspections_smr_api() -> str:
        return f'{InspectionsSmrRoutes.inspections_smr(project_id=current_user.project_id)}'

    @staticmethod
    def create_inspections_smr_api() -> str:
        return f'{InspectionsSmrRoutes.inspections_smr(project_id=current_user.project_id)}'
