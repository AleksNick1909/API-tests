from services.projects.project.exec_doc.prescriptions.enums.prescriptions_enums import *

from datetime import date

now_date = str(date.today()) + 'T00:00:00.000Z'


class UpdateDashboardsGen:

    def __init__(self):
        self.result = {}

    def set_all_period(self, all_period: bool = False):
        self.result['is_all_period'] = all_period
        return self

    def set_scale(self, scale: str):
        self.result['scale'] = scale
        return self

    def set_date(self, dates: str = None):
        self.result['date'] = dates
        return self

    def set_parameters(self, parameters: str):
        self.result['parameters[tab]'] = parameters
        return self

    def set_parameters_type(self, parameters_type: str):
        self.result['parameters[type][0]'] = parameters_type
        return self

    def set_parameters_all_type(self):
        for i, type_value in enumerate(PrescriptionsType):
            self.result[f'parameters[type][{i}]'] = type_value.value
        return self

    def set_start_period(self, start_period: str = now_date):
        self.result['start_period'] = start_period
        return self

    def set_end_period(self, end_period: str = now_date):
        self.result['end_period'] = end_period
        return self

    def build(self):
        return self.result
