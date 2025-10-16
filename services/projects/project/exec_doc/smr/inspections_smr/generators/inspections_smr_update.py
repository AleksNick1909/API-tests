

class UpdateInspectionsSmrGen:

    def __init__(self):
        self.result = {}

    def set_planned_date_begin(self, planned_date_begin: str):
        self.result['plannedDateBegin'] = planned_date_begin
        return self

    def set_timezone(self, timezone: int = 3):
        self.result['timezone'] = timezone
        return self

    def set_registration_date(self, registration_date: str):
        self.result['registration_date'] = registration_date
        return self

    def set_description(self, description):
        self.result['description'] = description
        return self

    def set_status(self, status_id):
        self.result['status_id'] = int(status_id)
        return self

    def build(self):
        return self.result
