from utils.client.api_client import RequestClient
from config.links import Links


class BaseAPI:

    client = RequestClient(base_url=Links.HOST)
