import allure
from config.base_api import BaseAPI
from config.headers import Headers
from services.catalogs.users.payloads import Payloads
from services.catalogs.users.endpoints import Endpoints
from services.catalogs.users.models.model_user import UserResponseModel


class UsersAPI(BaseAPI):

    def __init__(self):
        self._headers = Headers()
        self._endpoint = Endpoints()
        self._payload = Payloads()

    @allure.step("Получение информации о пользователе")
    def get_user(self) -> UserResponseModel:
        user = self.client.get(
            endpoint=self._endpoint.get_user,
            model=UserResponseModel
        )
        return user
