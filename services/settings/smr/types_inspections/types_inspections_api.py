import allure
from config.base_api import BaseAPI
from services.settings.smr.types_inspections.routes.types_inspections_routes import TypesInspectionsRoutes
from services.settings.smr.types_inspections.models.model_types_inspections import *


class TypesInspectionsApi(BaseAPI):

    @allure.step(f'Получение типов инспекций')
    def get_types_inspections_api(self) -> list[TypesInspectionsSchema]:
        types_inspections = self.client.get(endpoint=TypesInspectionsRoutes.get_types_inspections_api(),
                                            model=TypesInspectionsSchema)
        return types_inspections
