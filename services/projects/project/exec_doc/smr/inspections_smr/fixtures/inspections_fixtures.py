from config.auth import current_user
from services.projects.project.exec_doc.smr.inspections_smr.inspections_smr_api import InspectionsSmrAPI
from services.projects.project.exec_doc.smr.inspections_smr.generators.inspections_smr_update import \
    UpdateInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.generators.commission_results.participants_update import \
    UpdateParticipantsGen
from services.projects.project.exec_doc.smr.inspections_smr.generators.composition_inspection.create_presents import \
    CreatePresentsInspectionGen
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
@pytest.fixture(scope='function')
def fixture_add_job_in_inspection(class_inspections_client: InspectionsSmrAPI):
    def _fixture_add_job_in_inspection(inspection_id, job_id, job_name):
        body = CreatePresentsInspectionGen().set_description(job_name).set_position().set_unit().set_volume().set_type(
            "job").set_is_from_structure().set_job_id(job_id).set_settings_numeration().build()
        job = class_inspections_client.create_presents_api(inspection_id=inspection_id, payload=body)
        return job
    return _fixture_add_job_in_inspection


# Результат комиссии добавление участника
@pytest.fixture(scope='function')
def fixture_add_participant_in_inspection(class_inspections_client: InspectionsSmrAPI):
    def _fixture_agreement_inspection(inspection_id):
        body = UpdateParticipantsGen().set_representative(current_user.representative_id).build()
        participant = class_inspections_client.add_representatives_in_participants_api(
            inspection_id=inspection_id, payload=body)
        return participant
    return _fixture_agreement_inspection


# Выбор статуса инспекции
@pytest.fixture(scope='function')
def fixture_select_status_inspection(class_inspections_client: InspectionsSmrAPI):
    def _fixture_select_status_inspection(inspection_id, representative_id, id_status_inspection):
        construction_comment = fake.text(max_nb_chars=50)
        body = UpdateInspectionsSmrGen().set_description(construction_comment).build()
        comment = class_inspections_client.update_inspection_status_api(
            inspection_id=inspection_id, representative_id=representative_id,
            payload=body)
        body = UpdateInspectionsSmrGen().set_status(id_status_inspection).build()
        status = class_inspections_client.update_inspection_status_api(
            inspection_id=inspection_id, representative_id=representative_id,
            payload=body)
        return comment, status
    return _fixture_select_status_inspection
