from utils.client.api_client import RequestClient
from config.links import Links
# from helpers.helper import Helper


class BaseAPI:

    client = RequestClient(base_url=Links.HOST)
    # helper = Helper()
