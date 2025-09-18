import json
import pathlib
import requests
import urllib3

from dotenv import load_dotenv
from config.links import Links
from config.credentials import Credential

urllib3.disable_warnings()
load_dotenv()

_TOKEN_FILE = pathlib.Path(__file__).with_name('.data_current_user.json')
_cached_data = None


def _validate_token(access_token: str) -> bool:
    """Проверяет, действителен ли токен"""
    try:
        # Делаем тестовый запрос для проверки токена
        test_resp = requests.get(
            f"{Links.HOST}/api/login/token",  # или любой другой endpoint для проверки
            headers={"Authorization": f"Bearer {access_token}"},
            verify=False,
            timeout=10
        )
        return test_resp.status_code == 200
    except requests.RequestException:
        return False


def _get_access_token():
    """Логинимся + забираем профиль и возвращаем access_token + словарь для файла."""
    body = {
        "clientId": int(Credential.CLIENT_ID),
        "login": Credential.LOGIN,
        "password": Credential.PASSWORD,
    }

    print("🔄 Выполняется новая авторизация...")

    # 1. получаем токен
    token_resp = requests.post(Links.TOKEN, json=body, verify=False, timeout=30)
    token_resp.raise_for_status()
    token_data = token_resp.json()
    access_token = token_data["access_token"]
    user_id = token_data["user_id"]

    # 2. забираем данные пользователя
    profile_resp = requests.get(
        f"{Links.HOST}/api/users/{user_id}",
        headers={"Authorization": f"Bearer {access_token}"},
        verify=False,
        timeout=30
    )
    profile_resp.raise_for_status()
    profile = profile_resp.json()

    # 3. формируем словарь в нужном виде
    def safe_nested_get(data, *keys):
        """Безопасное извлечение вложенных значений"""
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current

    file_data = {
        "company_id": safe_nested_get(profile, "company", "id"),
        "login_user_used": f"{safe_nested_get(profile, 'company', 'id')}/{user_id}",
        "user_id": user_id,
        "access_token": access_token,
        "refresh_token": token_data.get("refresh_token", ""),
        "organization_id": safe_nested_get(profile, "division", "organization", "id"),
        "partner_id": safe_nested_get(profile, "representative", "partner", "id"),
        "representative_id": safe_nested_get(profile, "representative", "id"),
        "role_id": safe_nested_get(profile, "role", "id"),
        "division_id": safe_nested_get(profile, "division", "id")
    }

    _TOKEN_FILE.write_text(json.dumps(file_data, indent=2))
    print("✅ Новый токен сохранен")
    return access_token, file_data


def _load_or_fetch():
    """Если файл есть и токен валиден – берём оттуда, иначе логинимся."""
    if _TOKEN_FILE.exists():
        try:
            data = json.loads(_TOKEN_FILE.read_text())
            access_token = data["access_token"]

            print("📁 Найден сохраненный токен, проверяем...")

            # Проверяем валидность токена
            if _validate_token(access_token):
                print("✅ Сохраненный токен действителен")
                return access_token, data
            else:
                print("❌ Сохраненный токен недействителен, получаем новый...")
                return _get_access_token()

        except (json.JSONDecodeError, KeyError) as e:
            print(f"❌ Ошибка чтения файла токена: {e}")

    print("📝 Файл токена не найден, выполняется авторизация...")
    return _get_access_token()


def get_access_token():
    """Публичная функция для получения актуального токена"""
    global _cached_data
    if _cached_data is None:
        _access_token, _cached_data = _load_or_fetch()
    return _cached_data["access_token"]


def get_user_data():
    """Публичная функция для получения данных пользователя"""
    global _cached_data
    if _cached_data is None:
        _access_token, _cached_data = _load_or_fetch()
    return _cached_data


# удобный доступ ко всем полям
def get_current_user():
    """Возвращает объект с данными текущего пользователя"""
    data = get_user_data()
    return type("CurrentUser", (), data)


def get_user_id():
    """Возвращает ID текущего пользователя"""
    return get_user_data()["user_id"]


project_id = None
current_user = get_current_user()
current_user.project_id = project_id  # Добавляем project_id в объект
user_id = get_user_id()


def set_project_id(new_project_id):
    """Устанавливает ID текущего проекта"""
    global project_id, current_user
    project_id = new_project_id
    current_user.project_id = new_project_id
    print(f"✅ Project ID установлен: {project_id}")


def get_project_id():
    """Возвращает ID текущего проекта"""
    return project_id
