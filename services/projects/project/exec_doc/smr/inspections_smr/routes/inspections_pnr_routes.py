from config.links import Links


class InspectionsSmrRoutes:

    @staticmethod
    def inspections_smr(project_id: int):
        inspections_smr = f'{Links.API}/objects/{project_id}/inspections'
        return inspections_smr
