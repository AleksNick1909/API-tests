from config.links import Links
from config.auth import current_user


class ProjectsRoutes:
    # Базовые части путей
    projects_list = f'{Links.API}/construction-objects'
    construction = '/constructions'

    # Готовые endpoints для API
    @staticmethod
    def get_projects_api() -> str:
        return f'{ProjectsRoutes.projects_list}/constructions-registry/tier'

    @staticmethod
    def create_project_api() -> str:
        return f'{ProjectsRoutes.projects_list}{ProjectsRoutes.construction}'

    @staticmethod
    def update_project_api() -> str:
        return f'{ProjectsRoutes.projects_list}{ProjectsRoutes.construction}/{current_user.project_id}'

    @staticmethod
    def delete_project_api() -> str:
        return f'{ProjectsRoutes.projects_list}{ProjectsRoutes.construction}'
