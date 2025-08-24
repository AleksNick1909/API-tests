from config.auth import current_user


class UpdateProject:

    def __init__(self):
        self.result = {}

    def set_company_id(self, company_id: int = current_user.company_id):
        self.result['companyId'] = company_id
        return self

    def set_field(self, key: str, value):
        """Универсальный метод для добавления любого поля"""
        self.result[key] = value
        return self

    def set_fields(self, **kwargs):
        """Добавление сразу нескольких полей"""
        for key, value in kwargs.items():
            self.result[key] = value
        return self

    def build(self):
        return self.result
