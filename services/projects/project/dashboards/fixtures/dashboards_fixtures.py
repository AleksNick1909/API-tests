import pytest
from services.projects.project.dashboards.dashboards_api import DashboardsAPI
from datetime import date, timedelta

now_date = str(date.today())


@pytest.fixture(scope='class')
def class_dashboards_client() -> DashboardsAPI:
    return DashboardsAPI()


# Метод для параметризации в тестах (get_test_cases_dates('week'), get_test_cases_dates('month'))
def get_test_cases_dates(period: str):
    today = date.today()

    if period == 'week':
        tomorrow = str(today + timedelta(days=1))
        yesterday = str(today - timedelta(days=1))
        eight_days_ago = str(today - timedelta(days=8))
        week_ago = str(today - timedelta(days=7))
        return [
            (now_date, 'текущая дата'),
            (tomorrow, 'завтра'),
            (yesterday, 'вчера'),
            (eight_days_ago, '8 дней назад'),
            (week_ago, 'неделя назад')
        ]

    elif period == 'month':
        tomorrow = str(today + timedelta(days=1))
        yesterday = str(today - timedelta(days=1))
        thirty_two_ago = str(today - timedelta(days=32))
        # Вычисляем дату месяц назад
        if today.month == 1:
            month_ago = today.replace(year=today.year - 1, month=12)
        else:
            month_ago = today.replace(month=today.month - 1)
        month_ago = str(month_ago)
        return [
            (now_date, 'текущая дата'),
            (tomorrow, 'завтра'),
            (yesterday, 'вчера'),
            (thirty_two_ago, 'более месяца назад'),
            (month_ago, 'месяц назад')
        ]


@pytest.fixture(scope='function')
def fixture_get_test_cases_dates():
    """
        Простая фикстура для получения тестовых дат
        Использование: fixture_get_test_cases_dates('week') или fixture_get_test_cases_dates('month')
    """
    return get_test_cases_dates
