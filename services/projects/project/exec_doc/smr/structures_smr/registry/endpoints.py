from services.projects.project.exec_doc.smr.structures_smr.registry.routes. \
    structure_smr_routes import StructureSmrRoutes
from config.auth import current_user


class StructuresSmrEndpoints:

    @staticmethod
    def get_structures_smr_api() -> str:
        return f'{StructureSmrRoutes.structures_smr(project_id=current_user.project_id)}'

    @staticmethod
    def create_structures_smr_api() -> str:
        return f'{StructureSmrRoutes.structures_smr(project_id=current_user.project_id)}'

    @staticmethod
    def delete_structures_smr_api() -> str:
        return f'{StructureSmrRoutes.structures_smr(project_id=current_user.project_id)}'
