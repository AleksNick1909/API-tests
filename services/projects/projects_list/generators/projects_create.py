from config.auth import current_user


class CreateProject:

    def __init__(self):
        self.result = {}

    def set_company_id(self, company_id: int = current_user.company_id):
        self.result['companyId'] = company_id
        return self

    def set_row_id(self, row_id: int = 0):
        self.result['rowId'] = row_id
        return self

    def build(self):
        return self.result
