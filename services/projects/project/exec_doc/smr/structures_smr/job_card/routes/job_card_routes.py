from config.links import Links
from config.auth import current_user


class JobCardRoutes:

    job_card = 'job-card'
    job_dates = 'job-dates'

    @staticmethod
    def jobs(project_id: int) -> str:
        return f'{Links.API}/objects/{project_id}/jobs'

    @staticmethod
    def job_card_route(project_id: int) -> str:
        return f'{Links.API}/objects/{project_id}/job'

    @staticmethod
    def jobs_route() -> str:
        return f'{JobCardRoutes.jobs(project_id=current_user.project_id)}'

    @staticmethod
    def job_general_route(job_id: int) -> str:
        return f'{JobCardRoutes.job_card_route(project_id=current_user.project_id)}/{job_id}/{JobCardRoutes.job_card}'

    @staticmethod
    def job_dates_route(job_id: int) -> str:
        return f'{JobCardRoutes.jobs(project_id=current_user.project_id)}/{job_id}/{JobCardRoutes.job_dates}'

    @staticmethod
    def update_job_dates_route() -> str:
        return f'{Links.API}/jobUpdateDateTabCell'
