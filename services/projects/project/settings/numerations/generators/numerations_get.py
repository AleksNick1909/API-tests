

class GetNumerationsSectionGen:

    def __init__(self):
        self.result = {}

    def set_object_id(self, object_id: int):
        self.result['objectId'] = object_id
        return self

    def build(self):
        return self.result
