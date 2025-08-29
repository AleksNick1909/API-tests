from config.links import Links
from config.auth import current_user


class SettingsSmrRoutes:

    @staticmethod
    def settings_inspections_smr():
        settings_inspections_smr = f'{Links.API}/companies/{current_user.company_id}/settings/inspections'
        return settings_inspections_smr

    statuses = '/statuses'
    types = '/types'
