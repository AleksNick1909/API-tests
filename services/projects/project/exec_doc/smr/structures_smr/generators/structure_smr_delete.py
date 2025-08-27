

class DeleteStructureSmrGen:

    def __init__(self):
        self.result = []

    def set_structure_ids(self, *structure_ids: int):
        self.result.extend(structure_ids)
        return self

    def build(self):
        return self.result
