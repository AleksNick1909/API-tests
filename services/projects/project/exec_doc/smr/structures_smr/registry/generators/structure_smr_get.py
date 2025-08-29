

class GetStructureSmrGen:

    def __init__(self):
        self.result = {}

    def set_count(self, count: int = 20):
        self.result['count'] = count
        return self

    def set_page(self, page: int = 1):
        self.result['page'] = page
        return self

    def set_parent_id(self, parent_id: int):
        self.result['parentId'] = parent_id
        return self

    def build(self):
        return self.result
