from services.settings.smr.routes.settings_smr_routes import SettingsSmrRoutes


class SettingsSmrEndpoints:

    @staticmethod
    def get_types_inspections_smr_api() -> str:
        return f'{SettingsSmrRoutes.settings_inspections_smr()}{SettingsSmrRoutes.types}'

