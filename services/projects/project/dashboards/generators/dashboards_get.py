from config.auth import current_user


class GetDashboardsGen:

    def __init__(self):
        self.result = {}

    def set_company_id(self, company_id: int = current_user.company_id):
        self.result['companyId'] = company_id
        return self

    def set_page(self, page: int = 1):
        self.result['page'] = page
        return self

    def set_count(self, count: int = 100):
        self.result['count'] = count
        return self

    def build(self):
        return self.result
