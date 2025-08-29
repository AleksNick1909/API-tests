import pytest
import allure
from services.settings.smr.settings_smr_api import SettingsSmrApi


@pytest.fixture(scope='class')
def class_settings_smr_client() -> SettingsSmrApi:
    return SettingsSmrApi()


@pytest.fixture(scope='function')
@allure.step('Получение ID типа инспекции СМР по имени')
def fixture_get_types_inspections_smr(class_settings_smr_client: SettingsSmrApi):
    """
        Фикстура получает ID типа инспекции СМР по названию
    """
    def _fixture_get_types_inspections_smr(type_inspection_smr: str):
        inspections_smr = class_settings_smr_client.get_types_inspections_smr_api()
        for inspection in inspections_smr:
            if inspection.name == type_inspection_smr:
                return inspection.id
        raise ValueError(f"Тип инспекции '{type_inspection_smr}' не найден")

    return _fixture_get_types_inspections_smr
