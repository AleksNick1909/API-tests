from config.links import Links
from config.auth import current_user


class InspectionsSmrRoutes:

    @staticmethod
    def inspections_smr(project_id: int):
        inspections_smr = f'{Links.API}/objects/{project_id}/inspections'
        return inspections_smr

    @staticmethod
    def get_inspections_smr_api() -> str:
        return f'{InspectionsSmrRoutes.inspections_smr(project_id=current_user.project_id)}'

    @staticmethod
    def create_inspections_smr_api() -> str:
        return f'{InspectionsSmrRoutes.inspections_smr(project_id=current_user.project_id)}'
