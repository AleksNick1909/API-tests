from config.auth import user_id


class CreateJobGen:

    def __init__(self):
        self.result = {}

    def set_structure_smr_id(self, smr_structure_id: int):
        self.result['smrStructureId'] = smr_structure_id
        return self

    def set_user_id(self, user: int = user_id):
        self.result['userId'] = user
        return self

    def build(self):
        return self.result
