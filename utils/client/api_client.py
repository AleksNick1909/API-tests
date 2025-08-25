import requests
from typing import get_type_hints
from utils.logger.logger import logger
from helpers.helper import Helper
from config.headers import Headers
from pydantic import BaseModel

import urllib3
urllib3.disable_warnings()


class RequestClient:

    def __init__(self, base_url):
        self.helper = Helper()
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(Headers().get_basic_headers())
        self.session.verify = False

    def _log_request(self, method, url, **kwargs):
        logger.info(f"➡️ {method.upper()} - {url}")
        if method.upper() != "GET":
            self.helper.attach('request', kwargs["json"])

    def _log_response(self, response: requests.Response, max_expected_time: float = 3.0):
        http_log = (f'⬅️ HTTP Response: {response.request.method} {response.request.url} - '
                    f'{response.status_code} {response.reason or "OK"}')
        # Время запроса
        if hasattr(response, 'elapsed'):
            elapsed = response.elapsed.total_seconds()
            if elapsed > max_expected_time:
                http_log += f" (Time: \033[31m{elapsed:.3f}s\033[0m)"  # Красный цвет
            else:
                http_log += f" (Time: {elapsed:.3f}s)"
        # Содержимое запроса
        if 200 <= response.status_code < 300:
            # Для успешных запросов - только HTTP лог
            logger.info(http_log)
        else:
            # Для ошибок - HTTP лог + JSON с ошибкой
            logger.error(http_log)
            try:
                error_json = response.json()
                logger.error(f"Error Response: {error_json}")
            except requests.exceptions.JSONDecodeError:
                logger.error(f"Error Response: {response.text}")

    def _request(self, method, endpoint, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self._log_request(method, url, **kwargs)
        response = self.session.request(method, url, **kwargs)
        self._log_response(response)
        response.raise_for_status()
        return response

    def _validate_response(self, response: requests.Response, model: type[BaseModel], success: bool = True):
        response_data = response.json()
        self.helper.attach('response', response_data)
        # print("Response data:", response_data)  # Отладка
        if success:
            assert 200 <= response.status_code < 300, response_data
            # Список возможных ключей обёртки (при необходимости добавить, изменить)
            wrapper_keys = ['data', 'result', 'payload']
            # Проверяем поля модели
            model_fields = get_type_hints(model)
            # Проверяем, есть ли в модели поле, совпадающее с одним из ключей обёртки
            has_wrapper_field = any(key in model_fields for key in wrapper_keys)
            # Если в ответе есть словарь и один из ключей обёртки
            if not has_wrapper_field and isinstance(response_data, dict):
                # Ищем первый существующий ключ обёртки в ответе
                for key in wrapper_keys:
                    if key in response_data:
                        actual_data = response_data[key]
                        # print(f"Extracted wrapper key: {key}")  # Отладка
                        break
                else:
                    actual_data = response_data  # Если ключ обёртки не найден, берём весь ответ
            else:
                actual_data = response_data  # Модель ожидает обёртку или ответ без неё
            # print("Actual data for model:", actual_data)  # Отладка
            try:
                if isinstance(actual_data, dict):
                    return model(**actual_data)
                elif isinstance(actual_data, list):
                    return [model(**item) for item in actual_data]
            except Exception as e:
                print(f"Validation error for model {model.__name__}: {e}")  # Отладка
                raise
        else:
            assert not (200 <= response.status_code < 300), response_data

    def get(self, model, endpoint, params=None) -> BaseModel | list[BaseModel]:
        response = self._request("get", endpoint, params=params)
        return self._validate_response(model=model, response=response)

    def post(self, model, endpoint, json) -> BaseModel | list[BaseModel]:
        response = self._request("post", endpoint, json=json)
        return self._validate_response(model=model, response=response)

    def patch(self, model, endpoint, json) -> BaseModel | list[BaseModel]:
        response = self._request("patch", endpoint, json=json)
        return self._validate_response(model=model, response=response)

    def put(self, model, endpoint, json) -> BaseModel | list[BaseModel]:
        response = self._request("put", endpoint, json=json)
        return self._validate_response(model=model, response=response)

    def delete(self, endpoint, json=None, params=None) -> requests.Response:
        return self._request("delete", endpoint, json=json, params=params)
