from config.links import Links
from config.auth import current_user


class StatusesInspectionsRoutes:

    statuses = '/statuses'

    @staticmethod
    def settings_inspections():
        settings_inspections_smr = f'{Links.API}/companies/{current_user.company_id}/settings/inspections'
        return settings_inspections_smr

    @staticmethod
    def get_statuses_inspections_api() -> str:
        return f'{StatusesInspectionsRoutes.settings_inspections()}{StatusesInspectionsRoutes.statuses}'
