from config.links import Links
from config.auth import current_user


class StructureSmrRoutes:

    @staticmethod
    def structures_smr(project_id: int) -> str:
        structures_smr = f'{Links.API}/objects/{project_id}/smr-structures'
        return structures_smr

    @staticmethod
    def get_structures_smr_api() -> str:
        return StructureSmrRoutes.structures_smr(project_id=current_user.project_id)

    @staticmethod
    def create_structures_smr_api() -> str:
        return StructureSmrRoutes.structures_smr(project_id=current_user.project_id)

    @staticmethod
    def update_structures_smr_api(structure_smr_id: int) -> str:
        return f'{StructureSmrRoutes.structures_smr(project_id=current_user.project_id)}/{structure_smr_id}'

    @staticmethod
    def delete_structures_smr_api() -> str:
        return StructureSmrRoutes.structures_smr(project_id=current_user.project_id)
