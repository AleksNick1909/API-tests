import allure
from config.base_api import BaseAPI
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_get import GetInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_create import \
    CreateInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.routes.inspections_smr_routes import InspectionsSmrRoutes
from services.projects.project.exec_doc.smr.inspections_smr.models.inspections_schema import *
from config.auth import current_user


class InspectionsSmrAPI(BaseAPI):

    @allure.step('Получение списка инспекций СМР')
    def get_inspections_smr_api(self) -> InspectionsSchema:
        params = GetInspectionsSmrGen().set_page().set_count().build()
        inspections_smr_list = self.client.get(
            endpoint=InspectionsSmrRoutes.inspections_smr_route(current_user.project_id),
            model=InspectionsSchema,
            params=params)
        return inspections_smr_list

    @allure.step('Создание инспекции СМР')
    def create_inspections_smr_api(self, type_inspection: int) -> list[InspectionSchema]:
        body = (CreateInspectionsSmrGen().set_order().set_id_numeration().set_area_id().set_type_id(type_inspection).
                set_user_id().build())
        inspection_smr = self.client.post(endpoint=InspectionsSmrRoutes.inspections_smr_route(current_user.project_id),
                                          model=InspectionSchema,
                                          json=body)
        return inspection_smr

    @allure.step('Обновление инспекции СМР')
    def update_inspection_smr_api(self, inspection_id, payload) -> InspectionSchema:
        return self.client.put(endpoint=f'{InspectionsSmrRoutes.inspections_smr_route(current_user.project_id)}/'
                                        f'{inspection_id}',
                               model=InspectionSchema,
                               json=payload)
