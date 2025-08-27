from config.auth import user_id


class CreateInspectionsSmrGen:

    def __init__(self):
        self.result = []
        self.inspection = {}
        self.settings_numeration = {}
        self.parts = []

    def set_id_numeration(self, id_numeration=0):
        self.settings_numeration['id'] = id_numeration
        return self

    def set_order(self, order=0):
        self.inspection['order'] = order
        return self

    def set_type_id(self, type_id):
        self.inspection['type_id'] = int(type_id)
        return self

    def set_user_id(self, id_user=user_id):
        self.inspection['user_id'] = int(id_user)
        return self

    def build(self):
        self.settings_numeration['parts'] = self.parts
        self.inspection['settings_numeration'] = self.settings_numeration
        self.result.append(self.inspection)
        request = self.result
        return request
