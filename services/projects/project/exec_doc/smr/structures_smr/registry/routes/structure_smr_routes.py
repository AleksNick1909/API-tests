from config.links import Links


class StructureSmrRoutes:

    @staticmethod
    def structures_smr(project_id: int):
        structures_smr = f'{Links.API}/objects/{project_id}/smr-structures'
        return structures_smr
