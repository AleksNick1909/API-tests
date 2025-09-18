import pytest
from services.projects.project.exec_doc.smr.structures_smr.job_card.job_card_api import JobInformationCardAPI
from services.projects.project.exec_doc.smr.structures_smr.job_card.generators.job_card_dates_update import \
    UpdateJobDateGen
from services.projects.project.exec_doc.smr.structures_smr.job_card.generators.job_card_general_update import \
    UpdateJobGeneralGen


@pytest.fixture(scope='class')
def class_job_card_client() -> JobInformationCardAPI:
    return JobInformationCardAPI()


# Вкладка Общее
@pytest.fixture(scope='function')
def fixture_update_job_general(class_job_card_client: JobInformationCardAPI):
    def _fixture_update_job_general(job_id, price_fact=None, representative_id=None, customer_rep_id=None,
                                    type_of_work_id=None, qty_contract=None, date_begin_contract=None,
                                    date_end_contract=None, price_plan=None):
        body = (UpdateJobGeneralGen().set_price_fact(price_fact).set_representative_id(representative_id).
                set_customer_rep_id(customer_rep_id).set_type_of_work_id(type_of_work_id).set_qty_contract(
            qty_contract).set_date_begin_contract(date_begin_contract).set_date_end_contract(date_end_contract).
                set_price_plan(price_plan).build())
        job = class_job_card_client.update_job_general_api(payload=body, job_id=job_id)
        return job
    return _fixture_update_job_general


# Вкладка Даты
@pytest.fixture(scope='function')
def fixture_get_date_plan_job(class_job_card_client: JobInformationCardAPI):
    def _fixture_get_date_plan_job(job_id):
        date_plan_job = class_job_card_client.get_job_date_plan_api(job_id=job_id)
        return date_plan_job
    return _fixture_get_date_plan_job


@pytest.fixture(scope='function')
def fixture_update_date_job(class_job_card_client: JobInformationCardAPI):
    def _fixture_update_date_job(job_id, date, name_field, value, is_weekend, date_id=None):
        body = (UpdateJobDateGen().set_job_id(job_id).set_date(date).set_date_id(date_id).set_name(name_field).
                set_value(value).set_is_weekend(is_weekend).build())
        job = class_job_card_client.update_job_date_api(payload=body)
        return job
    return _fixture_update_date_job
