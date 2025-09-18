import allure
from config.base_api import BaseAPI
from config.auth import current_user, user_id
from services.projects.project.exec_doc.smr.structures_smr.job_card.routes.job_card_routes import JobCardRoutes

from services.projects.project.exec_doc.smr.structures_smr.job_card.models.model_job_card_general import \
    JobCardGeneralSchema
from services.projects.project.exec_doc.smr.structures_smr.job_card.models.model_job_card_dates. \
    model_job_card_dates_get import *


class JobInformationCardAPI(BaseAPI):

    # Вкладка общее
    @allure.step(f'Получение вкладки "Общее" окна "Данные по работе"')
    def get_job_general_api(self, job_id) -> JobCardGeneralSchema:
        return self.client.get(endpoint=f'{JobCardRoutes.job_general_route(job_id=job_id)}{JobCardRoutes.job_card}',
                               model=JobCardGeneralSchema)

    @allure.step(f'Изменение данных вкладки "Общее" окна "Данные по работе"')
    def update_job_general_api(self, payload, job_id) -> JobCardGeneralSchema:
        return self.client.patch(endpoint=f'{JobCardRoutes.job_general_route(job_id=job_id)}{JobCardRoutes.job_card}',
                                 model=JobCardGeneralSchema,
                                 json=payload)

    # Вкладка даты
    @allure.step(f'Получение данных вкладки "Даты" окна "Данные по работе"')
    def get_job_date_plan_api(self, job_id) -> JobDatesSchema:
        return self.client.get(endpoint=f'{JobCardRoutes.job_dates_route(job_id=job_id)}',
                               model=JobDatesSchema)

    @allure.step(f'Изменение данных вкладки "Даты" окна "Данные по работе"')
    def update_job_date_api(self, payload) -> JobDatesSchema:
        param = {'companyID': current_user.company_id, 'userID': user_id}
        return self.client.post(endpoint=f'{JobCardRoutes.update_job_dates_route()}',
                                model=JobDatesSchema,
                                json=payload,
                                params=param)
