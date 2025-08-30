from config.auth import current_user


class UpdateStructureSmrGen:

    def __init__(self):
        self.result = {}

    def set_identifier(self, identifier: str):
        self.result['identifier'] = identifier
        return self

    def set_cipher(self, cipher: str):
        self.result['cipher'] = cipher
        return self

    def set_representative_id(self, representative_id: int = current_user.representative_id):
        self.result['representativeId'] = representative_id
        return self

    def set_customer_id(self, customer_id: int = current_user.representative_id):
        self.result['customerId'] = customer_id
        return self

    def set_fields(self, **kwargs):
        """Добавление сразу нескольких полей"""
        for key, value in kwargs.items():
            self.result[key] = value
        return self

    def build(self):
        return self.result
