

class DeleteProjectsGen:

    def __init__(self):
        self.result = {}

    def set_selected_ids(self, selected_ids: int):
        self.result['selectedIds[]'] = selected_ids
        return self

    def build(self):
        return self.result
