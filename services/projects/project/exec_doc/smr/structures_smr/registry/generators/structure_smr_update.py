

class UpdateStructureSmrGen:

    def __init__(self):
        self.result = {}

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
