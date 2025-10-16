import allure
from config.base_api import BaseAPI
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_get import GetInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_create import \
    CreateInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.routes.inspections_smr_routes import InspectionsSmrRoutes
from services.projects.project.exec_doc.smr.inspections_smr.models.inspections_schema import *
from services.projects.project.exec_doc.smr.inspections_smr.models.composition_inspection_schema import *
from services.projects.project.exec_doc.smr.inspections_smr.models.commission_results_schema import *

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
    def update_inspection_smr_api(self, inspection_id: int, payload) -> InspectionSchema:
        return self.client.put(endpoint=f'{InspectionsSmrRoutes.inspections_smr_route(current_user.project_id)}/'
                                        f'{inspection_id}',
                               model=InspectionSchema,
                               json=payload)

    @allure.step('Выбор статуса инспекции')
    def update_inspection_status_api(self, inspection_id, representative_id, payload) -> CommissionResultSchema:
        return self.client.put(endpoint=f'{InspectionsSmrRoutes.status_in_inspection_route(inspection_id, 
                                                                                           representative_id)}',
                               model=CommissionResultSchema,
                               json=payload)

#  Вкладка "Состав инспекции"
    @allure.step('Получение списка материалов предъявленных к инспекции')
    def get_presents_material_api(self, inspection_id: int) -> list[PresentsMaterialsSchema]:
        return self.client.get(endpoint=f'{InspectionsSmrRoutes.presents_route(inspection_id)}'
                                        f'{InspectionsSmrRoutes.materials}',
                               model=PresentsMaterialsSchema)

    @allure.step('Получение списка работ предъявленных к инспекции')
    def get_presents_job_api(self, inspection_id: int) -> list[PresentsJobSchema]:
        return self.client.get(endpoint=f'{InspectionsSmrRoutes.presents_route(inspection_id)}'
                                        f'{InspectionsSmrRoutes.jobs}',
                               model=PresentsJobSchema)

    @allure.step('Создание объекта инспекции')
    def create_presents_api(self, inspection_id: int, payload) -> list[PresentsSchema]:
        return self.client.post(endpoint=f'{InspectionsSmrRoutes.presents_route(inspection_id)}',
                                model=PresentsSchema,
                                json=payload)

    @allure.step('Обновление объекта Материала')
    def update_presents_material_api(self, inspection_id: int, material_id: int, payload) -> PresentsMaterialsSchema:
        return self.client.patch(endpoint=f'{InspectionsSmrRoutes.presents_material_route(inspection_id, material_id)}',
                                 model=PresentsMaterialsSchema,
                                 json=payload)

    @allure.step('Обновление объекта Работы')
    def update_presents_job_api(self, inspection_id: int, job_id: int, payload) -> PresentsJobSchema:
        return self.client.patch(endpoint=f'{InspectionsSmrRoutes.presents_job_route(inspection_id, job_id)}',
                                 model=PresentsJobSchema,
                                 json=payload)

#  Вкладка "Результат комиссии"
    @allure.step('Создание участника инспекции')
    def add_representatives_in_participants_api(self, inspection_id: int, payload) -> list[CommissionResultSchema]:
        return self.client.post(endpoint=f'{InspectionsSmrRoutes.representatives_in_participants_route(inspection_id)}',
                                model=CommissionResultSchema,
                                json=payload)


