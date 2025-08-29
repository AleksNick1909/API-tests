import allure
from config.base_api import BaseAPI
from services.projects.project.exec_doc.smr.structures_smr.registry.payloads import StructureSmrPayloads
from services.projects.project.exec_doc.smr.structures_smr.registry.endpoints import StructuresSmrEndpoints
from services.projects.project.exec_doc.smr.structures_smr.registry.models.model_structures_smr import *


class StructuresSmrAPI(BaseAPI):
    def __init__(self):
        self._endpoint = StructuresSmrEndpoints()
        self._payload = StructureSmrPayloads()

    @allure.step(f'Получение структуры СМР')
    def get_structures_smr_api(self) -> OpenStructuresSmrSchema:
        structures_smr_list = self.client.get(endpoint=self._endpoint.get_structures_smr_api(),
                                              model=OpenStructuresSmrSchema,
                                              params=self._payload.get_structure_smr())
        return structures_smr_list

    @allure.step(f'Создание структуры СМР')
    def create_structures_smr_api(self) -> StructuresSmrSchema:
        structures_smr = self.client.post(endpoint=self._endpoint.create_structures_smr_api(),
                                          model=StructuresSmrSchema,
                                          json=self._payload.create_structure_smr())
        return structures_smr

    @allure.step(f'Обновление структуры СМР')
    def update_structures_smr_api(self, structure_smr_id: int, **kwargs) -> StructuresSmrSchema:
        structure_smr = self.client.patch(endpoint=self._endpoint.update_structures_smr_api(structure_smr_id),
                                          model=StructuresSmrSchema,
                                          json=self._payload.update_structure_smr(**kwargs))
        return structure_smr

    @allure.step(f'Удаление структуры СМР')
    def delete_structures_smr_api(self, structure_smr_id: int):
        structure_smr = self.client.delete(endpoint=self._endpoint.delete_structures_smr_api(),
                                           json=self._payload.delete_structure_smr(structure_smr_id))
        return structure_smr
