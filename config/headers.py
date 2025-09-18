from config.auth import get_access_token


class Headers:
    @staticmethod
    def get_basic_headers():
        """Возвращает базовые заголовки с актуальным токеном"""
        access_token = get_access_token()
        return {
            "Authorization": f"Bearer {access_token}",
        }

    @staticmethod
    def add_custom_headers(custom_headers: dict = None):
        """Возвращает базовые заголовки + дополнительные"""
        headers = Headers.get_basic_headers()
        if custom_headers:
            headers.update(custom_headers)
        return headers
