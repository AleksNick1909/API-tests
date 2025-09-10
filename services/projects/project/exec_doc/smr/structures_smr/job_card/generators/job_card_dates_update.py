

class UpdateJobDateGen:

    def __init__(self):
        self.data = {}
        self.result = {}
        self.fact = {}
        self.plan = {}

    def set_job_id(self, job_id: int):
        self.result['jobID'] = job_id
        return self

    def set_name(self, name: str):
        self.result['name'] = name
        return self

    def set_value(self, value: str | int):
        self.result['value'] = value
        return self

    def set_date(self, date: str):
        self.data['date'] = date
        return self

    def set_date_id(self, date_id: int):
        self.data['date_id'] = date_id
        return self

    def set_is_weekend(self, is_weekend: bool):
        self.data['isWeekend'] = is_weekend
        return self

    def build(self):
        self.data['plan'] = self.plan
        self.data['fact'] = self.fact
        self.result['data'] = self.data
        return self.result
