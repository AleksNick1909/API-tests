from config.links import Links
from config.auth import current_user


class InspectionsSmrRoutes:

    @staticmethod
    def inspections_smr_route(project_id: int):
        inspections_smr = f'{Links.API}/objects/{project_id}/inspections'
        return inspections_smr

#  Вкладка "Состав инспекции"
    jobs = '/jobs'
    presents = '/presents'
    materials = '/materials'

    @staticmethod
    def presents_route(inspection_id: int) -> str:
        return (f"{InspectionsSmrRoutes.inspections_smr_route(current_user.project_id)}/"
                f"{inspection_id}{InspectionsSmrRoutes.presents}")

    @staticmethod
    def presents_material_route(inspection_id: int, material_id: int) -> str:
        return f"{InspectionsSmrRoutes.presents_route(inspection_id)}{InspectionsSmrRoutes.materials}/{material_id}"

    @staticmethod
    def presents_job_route(inspection_id: int, job_id: int) -> str:
        return f"{InspectionsSmrRoutes.presents_route(inspection_id)}{InspectionsSmrRoutes.jobs}/{job_id}"

#  Вкладка "Инспекция"
    @staticmethod
    def status_in_inspection_route(inspection_id: int, representative_id: int) -> str:
        return (f"{InspectionsSmrRoutes.inspections_smr_route(current_user.project_id)}/{inspection_id}"
                f"/representatives/{representative_id}")

#  Вкладка "Результат комиссии"
    representatives = '/representatives'
    notify_registration = '/notify-registration'
    notify = '/notify'

    @staticmethod
    def representatives_in_participants_route(inspection_id: int) -> str:
        return (f"{InspectionsSmrRoutes.inspections_smr_route(current_user.project_id)}/{inspection_id}"
                f"{InspectionsSmrRoutes.representatives}")

    @staticmethod
    def notify_registration_route(inspection_id: int) -> str:
        return (f"{InspectionsSmrRoutes.inspections_smr_route(current_user.project_id)}/{inspection_id}"
                f"{InspectionsSmrRoutes.notify_registration}")

    @staticmethod
    def notify_representatives_route(inspection_id: int) -> str:
        return (f"{InspectionsSmrRoutes.inspections_smr_route(current_user.project_id)}/{inspection_id}"
                f"{InspectionsSmrRoutes.notify}")
