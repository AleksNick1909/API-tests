import os
from dotenv import load_dotenv

load_dotenv()


class Credential:

    environment = os.environ.get('ENV', 'cloud_dev')  # Принимает 'cloud_dev' если в .env нет нужного окружения

    if environment == 'dev':
        LOGIN = os.getenv('DEV_LOGIN')
        PASSWORD = os.getenv('DEV_PASSWORD')
        CLIENT_ID = os.getenv('DEV_CLIENT_ID')

    elif environment == 'cloud_dev':
        LOGIN = os.getenv('CLOUD_LOGIN')
        PASSWORD = os.getenv('CLOUD_PASSWORD')
        CLIENT_ID = os.getenv('CLOUD_CLIENT_ID')

    elif environment == 'stage':
        LOGIN = os.getenv('STAGE_LOGIN')
        PASSWORD = os.getenv('STAGE_PASSWORD')
        CLIENT_ID = os.getenv('STAGE_CLIENT_ID')
