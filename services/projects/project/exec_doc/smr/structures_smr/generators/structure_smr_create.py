from config.auth import user_id


class CreateStructureSmr:
    def __init__(self):
        self.result = {}

    def set_row_id(self, row_id: int = 1):
        self.result['rowId'] = row_id
        return self

    def set_position(self, position: str = 'end'):
        self.result['position'] = position
        return self

    def set_user_id(self, id_user: int = user_id):
        self.result['userId'] = id_user
        return self

    def build(self):
        return self.result
