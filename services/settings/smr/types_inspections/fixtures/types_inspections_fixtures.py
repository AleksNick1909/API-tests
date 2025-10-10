import pytest
import allure
from services.settings.smr.types_inspections.types_inspections_api import TypesInspectionsApi


@pytest.fixture(scope='class')
def class_type_inspections_client() -> TypesInspectionsApi:
    return TypesInspectionsApi()


@pytest.fixture(scope='function')
@allure.step('Получение ID типа инспекции по имени')
def fixture_get_types_inspections(class_type_inspections_client: TypesInspectionsApi):
    """
        Фикстура получает ID типа инспекции по названию инспекции
    """
    def _fixture_get_types_inspections(type_inspection: str):
        inspections_types = class_type_inspections_client.get_types_inspections_api()
        for inspection in inspections_types:
            if inspection.name == type_inspection:
                return inspection.id
        raise ValueError(f"Тип инспекции '{type_inspection}' не найден")
    return _fixture_get_types_inspections
