from config.auth import current_user


class UpdateProjectGen:

    def __init__(self):
        self.result = {}

    def set_company_id(self, company_id: int = current_user.company_id):
        self.result['companyId'] = company_id
        return self

    def set_full_name(self, full_name: str):
        self.result['fullName'] = full_name
        return self

    def set_short_name(self, short_name: str):
        self.result['shortName'] = short_name
        return self

    def set_object_number(self, object_number: str):
        self.result['objectNumber'] = object_number
        return self

    def set_fields(self, **kwargs):
        """Добавление сразу нескольких полей"""
        for key, value in kwargs.items():
            self.result[key] = value
        return self

    def build(self):
        return self.result
