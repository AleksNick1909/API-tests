import allure
from config.base_api import BaseAPI

from services.settings.smr.statuses_inspections.routes.statuses_inspections_routes import StatusesInspectionsRoutes
from services.settings.smr.statuses_inspections.models.model_statuses_inspections import StatusesInspectionsSchema


class StatusesInspectionsApi(BaseAPI):

    @allure.step(f'Получение статусов инспекций')
    def get_statuses_inspections_api(self) -> list[StatusesInspectionsSchema]:
        statuses_inspections = self.client.get(endpoint=StatusesInspectionsRoutes.get_statuses_inspections_api(),
                                               model=StatusesInspectionsSchema)
        return statuses_inspections
