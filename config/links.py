import os


class Links:

    environment = os.environ.get('ENV', 'stage')

    HOSTS = {
        'cloud_dev': 'https://aid-dev-new.infra.gk-adept.ru',
        'dev': 'https://10.145.1.150:5005',
        'stage': 'https://10.145.1.150:5006'
    }

    HOST = HOSTS.get(environment)
    API = '/api'

    if HOST:
        TOKEN = f'{HOST}/api/login/token'
        LOGIN_PAGE = f'{HOST}/login'
        PROJECTS_PAGE = f'{HOST}/projects/tier'
        NORMATIVES_PAGE = f'{HOST}/catalogs/partners'
        SETTINGS_PAGE = f'{HOST}/settings/constructions/projects-levels'

    else:
        raise ValueError(f'Unknown environment: {environment}')
