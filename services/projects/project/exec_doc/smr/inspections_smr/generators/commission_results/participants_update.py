
class UpdateParticipantsGen:

    def __init__(self):
        self.result = {}
        self.representatives = []

    def set_representative(self, *representative_ids):
        for ids in representative_ids:
            self.representatives.append(int(ids))
        return self

    def set_role(self, role_id):
        self.result['role_id'] = role_id
        return self

    def build(self):
        if len(self.representatives) > 0:
            self.result['representative_ids'] = self.representatives
        return self.result
