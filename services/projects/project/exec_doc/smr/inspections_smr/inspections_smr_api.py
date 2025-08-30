import allure
from config.base_api import BaseAPI
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_get import GetInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_create import \
    CreateInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.routes.inspections_pnr_routes import InspectionsSmrRoutes
from services.projects.project.exec_doc.smr.inspections_smr.models.inspections_schema import *


class InspectionsSmrAPI(BaseAPI):

    @allure.step(f'Получение списка инспекций СМР')
    def get_inspections_smr_api(self) -> InspectionsSchema:
        params = GetInspectionsSmrGen().set_page().set_count().build()
        inspections_smr_list = self.client.get(endpoint=InspectionsSmrRoutes.get_inspections_smr_api(),
                                               model=InspectionsSchema,
                                               params=params)
        return inspections_smr_list

    @allure.step(f'Создание инспекции СМР')
    def create_inspections_smr_api(self, type_inspection: int) -> InspectionSchema:
        body = (CreateInspectionsSmrGen().set_order().set_id_numeration().set_type_id(type_inspection).
                set_user_id().build())
        print(body)
        inspection_smr = self.client.post(endpoint=InspectionsSmrRoutes.create_inspections_smr_api(),
                                          model=InspectionSchema,
                                          json=body)
        return inspection_smr
