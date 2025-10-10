import pytest
import allure
from services.settings.smr.statuses_inspections.statuses_inspections_api import StatusesInspectionsApi


@pytest.fixture(scope='class')
def class_statuses_inspections_client() -> StatusesInspectionsApi:
    return StatusesInspectionsApi()


@pytest.fixture(scope='function')
@allure.step('Получение ID статуса инспекции по имени')
def fixture_get_statuses_inspections(class_statuses_inspections_client: StatusesInspectionsApi):
    """
        Фикстура получает ID статуса инспекции по названию статуса
    """
    def _fixture_get_statuses_inspections(status_inspection: str):
        inspections_statuses = class_statuses_inspections_client.get_statuses_inspections_api()
        for status in inspections_statuses:
            if status.name == status_inspection:
                return status.id
        raise ValueError(f"Статус инспекции '{status_inspection}' не найден")

    return _fixture_get_statuses_inspections
