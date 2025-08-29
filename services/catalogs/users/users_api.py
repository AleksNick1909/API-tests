import allure
from config.base_api import BaseAPI

from services.catalogs.users.routes.users_routes import UsersRoutes
from services.catalogs.users.models.model_user import UserResponseModel


class UsersAPI(BaseAPI):

    @allure.step("Получение информации о пользователе")
    def get_user(self) -> UserResponseModel:
        user = self.client.get(endpoint=UsersRoutes.get_user,
                               model=UserResponseModel)
        return user
