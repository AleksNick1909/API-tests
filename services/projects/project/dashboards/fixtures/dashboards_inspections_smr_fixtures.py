from faker import Faker
from services.settings.smr.statuses_inspections.fixtures.statuses_inspections_fixtures import *
from services.projects.project.exec_doc.smr.inspections_smr.fixtures.inspections_fixtures import *

fake = Faker()


@pytest.fixture(scope='function')
def fixture_create_inspections_for_dashboard(class_statuses_inspections_client: StatusesInspectionsApi,
                                             fixture_create_inspection, fixture_update_inspection_smr,
                                             fixture_add_job_in_inspection, fixture_add_participant_in_inspection,
                                             fixture_select_status_inspection):
    """
        Фикстура создает полностью настроенную инспекцию для тестирования дашбордов:
            - Создает инспекцию указанного типа
            - Устанавливает плановую дату (случайную в ближайшие 30 дней)
            - Добавляет указанную работу в инспекцию
            - Добавляет участника инспекции
            - При необходимости устанавливает указанный статус
        Параметры:
            - job_id: ID работы для добавления в инспекцию
            - inspection_type: Тип создаваемой инспекции
            - status_name: Опциональное имя статуса для установки
            - job_name: Название работы (по умолчанию 'Новая работа')
        Returns:
             созданный объект инспекции
    """
    def _fixture_create_inspections_for_dashboard(job_id: int, inspection_type: str, status_name=None,
                                                  job_name='Новая работа'):

        with allure.step('Создание базовой инспекции'):
            inspection = fixture_create_inspection(type_inspection=inspection_type)
            print("Создана инспекция:", inspection.id)

        with allure.step('Установка случайной плановой даты в ближайшие 30 дней'):
            random_date = fake.date_between(start_date="today", end_date="+30d")
            planned_date_begin = random_date.strftime("%Y-%m-%d 00:00:00")
            fixture_update_inspection_smr(inspection_id=inspection.id, planned_date_begin=planned_date_begin)

        with allure.step('Добавление работы и участника'):
            fixture_add_job_in_inspection(inspection_id=inspection.id, job_id=job_id, job_name=job_name)
            participant = fixture_add_participant_in_inspection(inspection_id=inspection.id)

        with allure.step('Установка статуса'):
            if status_name:
                statuses_response = class_statuses_inspections_client.get_statuses_inspections_api()
                statuses_dict = {status.name: status for status in statuses_response}
                if status_name not in statuses_dict:
                    raise ValueError(f"Статус '{status_name}' не найден. Доступные статусы: "
                                     f"{list(statuses_dict.keys())}")
                fixture_select_status_inspection(inspection_id=inspection.id, representative_id=participant[0].id,
                                                 id_status_inspection=statuses_dict[status_name].id)
                # Второй вызов это временное решение для установки статуса в инспекции (с первого раза статус
                # не устанавливается, возможно через несколько лет пофиксят ошибку)
                # fixture_select_status_inspection(inspection_id=inspection.id, representative_id=participant[0].id,
                #                                  id_status_inspection=statuses_dict[status_name].id)
        return inspection
    return _fixture_create_inspections_for_dashboard


@pytest.fixture(scope='function')
def fixture_count_inspections(fixture_get_all_inspections):
    """
        Фикстура фильтрует и подсчитывает количество инспекций по заданным критериям:
        Параметры:
            - inspection_type: Фильтр по типу инспекции (если None - не фильтруется)
            - status: Фильтр по статусу инспекции (если None - не фильтруется)
            - planned_date: Фильтр по минимальной план дате (если None - не фильтруется)
                         Формат даты: 'YYYY-MM-DD' (сравнение по дате без времени)
            - fact_date: Фильтр по минимальной факт дате (если None - не фильтруется)
                         Формат даты: 'YYYY-MM-DD' (сравнение по дате без времени)
            - end_date: Фильтр по конечной дате (если None - не фильтруется)
                         Формат даты: 'YYYY-MM-DD' (сравнение по дате без времени)
        Returns:
            Количество инспекций, удовлетворяющих всем заданным критериям
    """
    def _fixture_count_inspections(inspection_type=None, status=None, planned_date=None, fact_date=None, end_date=None):

        all_inspections = fixture_get_all_inspections()
        filtered_inspections = all_inspections['data']
        if inspection_type:
            filtered_inspections = [
                inspection for inspection in filtered_inspections
                if inspection['inspection_type']['type'] == inspection_type
            ]
        if status:
            filtered_inspections = [
                inspection for inspection in filtered_inspections
                if inspection['status']['name'] == status
            ]
        if planned_date:
            if end_date:
                filtered_inspections = [
                    inspection for inspection in filtered_inspections
                    if planned_date <= inspection.get('plannedDateBegin', '').split('T')[0] <= end_date
                ]
            else:
                filtered_inspections = [
                    inspection for inspection in filtered_inspections
                    if inspection.get('plannedDateBegin', '').split('T')[0] >= planned_date
                ]
        if fact_date:
            if end_date:
                # Фильтр по диапазону дат (от fact_date до end_date включительно)
                filtered_inspections = [
                    inspection for inspection in filtered_inspections
                    if fact_date <= inspection.get('factDate', '').split('T')[0] <= end_date
                ]
            else:
                # Фильтр от fact_date и выше
                filtered_inspections = [
                    inspection for inspection in filtered_inspections
                    if inspection.get('factDate', '').split('T')[0] >= fact_date
                ]
        return len(filtered_inspections)
    return _fixture_count_inspections
