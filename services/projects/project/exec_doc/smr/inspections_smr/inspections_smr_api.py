import allure
from config.base_api import BaseAPI
from services.projects.project.exec_doc.smr.inspections_smr.endpoints import InspectionsSmrEndpoints
from services.projects.project.exec_doc.smr.inspections_smr.payloads import InspectionsSmrPayloads
from services.projects.project.exec_doc.smr.inspections_smr.models.inspections_schema import *


class InspectionsSmrAPI(BaseAPI):
    def __init__(self):
        self._endpoint = InspectionsSmrEndpoints()
        self._payload = InspectionsSmrPayloads()

    @allure.step(f'Получение списка инспекций СМР')
    def get_inspections_smr_api(self) -> InspectionsSchema:
        inspections_smr_list = self.client.get(endpoint=self._endpoint.get_inspections_smr_api(),
                                               model=InspectionsSchema,
                                               params=self._payload.get_inspection_smr())
        return inspections_smr_list

    @allure.step(f'Создание инспекции СМР')
    def create_inspections_smr_api(self) -> InspectionSchema:
        inspection_smr = self.client.post(endpoint=self._endpoint.create_inspections_smr_api(),
                                          model=InspectionSchema,
                                          json=self._payload.create_inspection_smr(10503))  # дописать id типа инспекции
        return inspection_smr
