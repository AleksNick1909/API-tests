from services.projects.projects_list.routes.projects_routes import ProjectsRoutes
from config.auth import current_user


class Endpoints:

    @staticmethod
    def get_projects_api() -> str:
        return f'{ProjectsRoutes.get_projects_list}'

    @staticmethod
    def create_project_api() -> str:
        return f'{ProjectsRoutes.projects_list}{ProjectsRoutes.construction}'

    @staticmethod
    def update_project_api() -> str:
        return f'{ProjectsRoutes.projects_list}{ProjectsRoutes.construction}/{current_user.project_id}'

    @staticmethod
    def delete_project_api() -> str:
        return f'{ProjectsRoutes.projects_list}{ProjectsRoutes.construction}'
