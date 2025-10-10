import random
from faker import Faker
from datetime import date
from services.projects.project.exec_doc.smr.structures_smr.registry.fixtures.structure_smr_fixtures import *
from services.projects.project.exec_doc.smr.structures_smr.job_card.fixtures.job_card_fixtures import *

fake = Faker()
now_date = str(date.today())


# Структура СМР
@pytest.fixture(scope='function')
def fixture_create_structure_smr_for_dashboard(class_structures_smr_client: StructuresSmrAPI,
                                               fixture_create_job_in_structure_smr, fixture_update_job,
                                               fixture_get_date_plan_job, fixture_update_date_job):
    """
        Фикстура создает тестовую структуру СМР с работами и заполняет данные:
            - Создает уровень структуры СМР
            - Добавляет работу в структуру
            - Заполняет основные параметры работы (количество, стоимость, трудозатраты, даты)
            - Распределяет фактические значения выполнения работы по дням планового периода
        Returns:
            созданную работу для использования в тестах дашбордов
    """
    with allure.step('Создание базовой структуры СМР и работы'):
        job = fixture_create_job_in_structure_smr
        allure.attach(str(job.id), "Job ID", allure.attachment_type.TEXT)

    with allure.step('Генерация случайных параметров работы'):
        qty_in_job = random.randint(100, 1000)
        price_in_job = random.randint(10, 100)
        labor_costs_in_job = random.randint(1000, 2000)
        random_date_end = str(fake.date_between(start_date="today", end_date="+8d"))
        allure.attach(f"Количество: {qty_in_job}, Цена: {price_in_job}, Трудозатраты: {labor_costs_in_job}",
                      "Параметры работы", allure.attachment_type.TEXT)

    with allure.step('Обновление основных параметров работы'):
        fixture_update_job(job_id=job.id, qty=qty_in_job, price=price_in_job, labor_costs=labor_costs_in_job,
                           date_begin_plan=now_date, date_end_plan=random_date_end)
        jobs = class_structures_smr_client.get_job_in_structures_smr_api(job_id=job.id)

    with allure.step('Получение плана периода'):
        date_plan = fixture_get_date_plan_job(job_id=jobs.id)
        job_data_plan = date_plan.qty_plan
        plan_periods = date_plan.plan_period

    with allure.step('Распределение фактических значений по дням'):
        for i, dates in enumerate(plan_periods):
            if i == len(plan_periods) - 1:
                random_value = job_data_plan
            else:
                random_value = random.randint(1, job_data_plan - (len(plan_periods) - i - 1))
                job_data_plan -= random_value
            fixture_update_date_job(job_id=job.id, date=dates.date, date_id=dates.id, name_field='qtyFact',
                                    value=random_value, is_weekend=dates.is_weekend)
    return jobs
