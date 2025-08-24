

class GetStructureSmr:

    def __init__(self):
        self.result = {}

    def set_count(self, count: int = 20):
        self.result['count'] = count
        return self

    def set_page(self, page: int = 1):
        self.result['page'] = page
        return self

    def build(self):
        return self.result
