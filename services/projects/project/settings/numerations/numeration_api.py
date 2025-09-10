import allure
import time
from config.base_api import BaseAPI
from config.auth import current_user

from services.projects.project.settings.numerations.routes.numerations_routes import NumerationsRoutes
from services.projects.project.settings.numerations.models.model_numerations_section import *
from services.projects.project.settings.numerations.generators.numerations_get import GetNumerationsSectionGen


class ProjectNumerationsAPI(BaseAPI):

    # Такая реализация связана с тем что в проект данные подтягиваются с задержкой
    @allure.step('Получение секции нумерации')
    def get_numerations_section(self) -> list[NumerationSectionSchema]:
        params = GetNumerationsSectionGen().set_object_id(current_user.project_id).build()
        intervals = [0, 1, 2, 3, 5]
        max_total_time = 30  # Максимум 30 секунд общего времени
        start_time = time.time()
        for interval in intervals:
            # Проверяем общее время перед ожиданием
            if time.time() - start_time >= max_total_time:
                break
            if interval > 0:
                time.sleep(interval)
            # Проверяем общее время после ожидания
            if time.time() - start_time >= max_total_time:
                break
            response = self.client.get(model=NumerationSectionSchema,
                                       endpoint=NumerationsRoutes.get_numerations_route(),
                                       params=params)
            if response:
                return response
        return []
