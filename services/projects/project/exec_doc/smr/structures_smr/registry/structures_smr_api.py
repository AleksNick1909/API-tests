import allure
from config.base_api import BaseAPI

from services.projects.project.exec_doc.smr.structures_smr.registry.routes.structure_smr_routes import \
    StructureSmrRoutes
from services.projects.project.exec_doc.smr.structures_smr.job_card.routes.job_card_routes import JobCardRoutes
from services.projects.project.exec_doc.smr.structures_smr.registry.generators.structure_smr_get import \
    GetStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.registry.generators.structure_smr_create import \
    CreateStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.registry.generators.structure_smr_delete import \
    DeleteStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.registry.models.model_structures_smr import *
from services.projects.project.exec_doc.smr.structures_smr.job_card.models.model_jobs import JobsCardSchema


class StructuresSmrAPI(BaseAPI):

    @allure.step(f'Получение структуры СМР')
    def get_structures_smr_api(self) -> OpenStructuresSmrSchema:
        params = GetStructureSmrGen().set_page().set_count().build()
        structures_smr_list = self.client.get(endpoint=StructureSmrRoutes.structures_smr_route(),
                                              model=OpenStructuresSmrSchema,
                                              params=params)
        return structures_smr_list

    @allure.step(f'Создание структуры СМР')
    def create_structures_smr_api(self) -> StructuresSmrSchema:
        body = CreateStructureSmrGen().set_user_id().set_row_id().set_position().build()
        structures_smr = self.client.post(endpoint=StructureSmrRoutes.structures_smr_route(),
                                          model=StructuresSmrSchema,
                                          json=body)
        return structures_smr

    @allure.step(f'Обновление структуры СМР')
    def update_structures_smr_api(self, structure_smr_id: int, payload) -> StructuresSmrSchema:
        structure_smr = self.client.patch(endpoint=StructureSmrRoutes.update_structures_smr_api(structure_smr_id),
                                          model=StructuresSmrSchema,
                                          json=payload)
        return structure_smr

    @allure.step(f'Создание работы в структуре СМР')
    def create_job_in_structures_smr_api(self, payload) -> JobsCardSchema:
        job = self.client.post(endpoint=JobCardRoutes.jobs_route(),
                               model=JobsCardSchema,
                               json=payload)
        return job

    @allure.step(f'Получение данных по работе')
    def get_job_in_structures_smr_api(self, job_id: int) -> JobsCardSchema:
        jobs = self.client.get(endpoint=f'{JobCardRoutes.jobs_route()}/{job_id}',
                               model=JobsCardSchema)
        return jobs

    @allure.step(f'Обновление данных работы в структуре СМР')
    def update_job_in_structures_smr_api(self, payload) -> JobsCardSchema:
        jobs = self.client.put(endpoint=f'{JobCardRoutes.jobs_route()}',
                               model=JobsCardSchema,
                               json=payload)
        return jobs

    @allure.step(f'Удаление структуры СМР')
    def delete_structures_smr_api(self, structure_smr_id: int):
        body = DeleteStructureSmrGen().set_structure_ids(structure_smr_id).build()
        structure_smr = self.client.delete(endpoint=StructureSmrRoutes.structures_smr_route(),
                                           json=body)
        return structure_smr
