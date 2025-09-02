from config.links import Links
from config.auth import current_user


class TypesInspectionsRoutes:

    types = '/types'

    @staticmethod
    def settings_inspections():
        settings_inspections_smr = f'{Links.API}/companies/{current_user.company_id}/settings/inspections'
        return settings_inspections_smr

    @staticmethod
    def get_types_inspections_api() -> str:
        return f'{TypesInspectionsRoutes.settings_inspections()}{TypesInspectionsRoutes.types}'
