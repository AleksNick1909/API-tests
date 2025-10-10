from services.projects.project.exec_doc.smr.inspections_smr.inspections_smr_api import InspectionsSmrAPI
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_update import \
    UpdateInspectionsSmrGen
from services.settings.smr.types_inspections.fixtures.types_inspections_fixtures import *

from faker import Faker
fake = Faker()


@pytest.fixture(scope='class')
def class_inspections_client() -> InspectionsSmrAPI:
    return InspectionsSmrAPI()


@pytest.fixture(scope='function')
def fixture_create_inspection(class_inspections_client: InspectionsSmrAPI,
                              fixture_get_types_inspections):
    def _fixture_create_inspection(type_inspection: str = 'СК'):
        types_inspections = fixture_get_types_inspections(type_inspection=type_inspection)
        inspection = class_inspections_client.create_inspections_smr_api(type_inspection=types_inspections)[0]
        return inspection
    return _fixture_create_inspection


# подкорректировать фикстуру
@pytest.fixture(scope='function')
def fixture_update_inspection_smr(class_inspections_client: InspectionsSmrAPI):
    def _fixture_update_inspection(inspection_id, registration_number=None, registration_date=None,
                                   typical_itp_id=None, planned_date_begin=None, fact_date=None, journal_id=None,
                                   exec_doc_id=None):
        if registration_number is None:
            registration_number = fake.building_number()
        body = (UpdateInspectionsSmrGen().set_timezone().
                set_registration_date(registration_date).
                set_planned_date_begin(planned_date_begin).build())
        inspection_update = class_inspections_client.update_inspection_smr_api(
            inspection_id=inspection_id, payload=body)
        return inspection_update
    return _fixture_update_inspection


@pytest.fixture(scope='function')
def fixture_get_all_inspections_smr(class_inspections_client: InspectionsSmrAPI):
    def _fixture_get_all_inspections_smr():
        all_inspections_smr = class_inspections_client.get_inspections_smr_api()
        return all_inspections_smr
    return _fixture_get_all_inspections_smr


# Состав инспекции добавление работы
# @pytest.fixture(scope='function')
# def fixture_add_job_in_inspection(class_inspections_client: InspectionsSmrAPI):
#     def _fixture_add_job_in_inspection(inspection_id, job_name, job_id, volume_accept=None, inspection_volume=None,
#                                        pkk_record_id=None):
#         body = CreatePresentsInspectionGen().set_description(job_name).set_position().set_unit().set_volume().set_type(
#             "job").set_is_from_structure().set_job_id(job_id).set_settings_numeration().build()
#         job = class_inspections_client.create_presents_api(payload=body, inspection_id=inspection_id)
#         body = UpdatePresentsJobsGen().set_inspection_volume(inspection_volume).set_volume_accept(
#             volume_accept)
#         if pkk_record_id:
#             if isinstance(pkk_record_id, tuple):
#                 body.set_record_and_inspection(*pkk_record_id, inspection=inspection_id)
#             else:
#                 body.set_record_and_inspection(pkk_record_id, inspection=inspection_id)
#         body_finish = body.build()
#         update_job = class_inspections_client.update_presents_job_api(
#             payload=body_finish, inspection_id=inspection_id, present_id=job[0]['id'])
#         return update_job
#     return _fixture_add_job_in_inspection
