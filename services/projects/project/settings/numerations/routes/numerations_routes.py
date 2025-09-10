from config.links import Links
from config.auth import current_user


class NumerationsRoutes:

    numerations = f'{Links.API}/companies/{current_user.company_id}/settings/numerations'

    @staticmethod
    def get_numerations_route() -> str:
        return NumerationsRoutes.numerations
