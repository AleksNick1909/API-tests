import allure
from config.base_api import BaseAPI
from services.settings.smr.endpoints import SettingsSmrEndpoints
from services.settings.smr.payloads import SettingsSmrPayloads
from services.settings.smr.models.model_types_inspections_smr import *


class SettingsSmrApi(BaseAPI):
    def __init__(self):
        self._endpoint = SettingsSmrEndpoints()
        self._payload = SettingsSmrPayloads()

    @allure.step(f'Получение типов инспекции СМР')
    def get_types_inspections_smr_api(self) -> list[TypesInspectionsSmr]:
        types_inspections_smr = self.client.get(endpoint=self._endpoint.get_types_inspections_smr_api(),
                                                model=TypesInspectionsSmr)
        return types_inspections_smr
