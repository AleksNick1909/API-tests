

class UpdateJobGen:

    def __init__(self):
        self.job_ids = []
        self.exec_doc_ids = []
        self.update_data = {}
        self.result = {}

    def set_job_id(self, job_id: int):
        self.job_ids.append(job_id)
        return self

    def set_qty_contract(self, qty_contract):
        self.update_data['qty_contract'] = qty_contract
        return self

    def set_price_plan(self, price_plan):
        self.update_data['price_plan'] = price_plan
        return self

    def set_labor_costs(self, labor_costs):
        self.update_data['labor_costs'] = labor_costs
        return self

    def set_date_begin_plan(self, date_begin_plan):
        self.update_data['date_begin_plan'] = date_begin_plan
        return self

    def set_date_end_plan(self, date_end_plan):
        self.update_data['date_end_plan'] = date_end_plan
        return self

    def set_journal_id(self, journal_id):
        self.update_data['journal_id'] = journal_id
        return self

    def set_type_of_work_id(self, type_of_work_id):
        self.update_data['type_of_work_id'] = type_of_work_id
        return self

    def set_setting_atg_middle_id(self, setting_atg_middle_id):
        self.update_data['settingAtgMiddleId'] = setting_atg_middle_id
        return self

    def set_custom_rep_name(self, custom_rep_name):
        self.update_data['custom_rep_name'] = custom_rep_name
        return self

    def set_representative_id(self, representative_id):
        self.update_data['representative_id'] = representative_id
        return self

    def set_customer_name(self, customer_name):
        self.update_data['customer_name'] = customer_name
        return self

    def set_customer_id(self, customer_id):
        self.update_data['customer_id'] = customer_id
        return self

    def set_units(self, units):
        self.update_data['units'] = units
        return self

    def set_name(self, name):
        self.update_data['name'] = name
        return self

    def set_exec_doc_ids(self, *exec_doc_id):
        for i in exec_doc_id:
            self.exec_doc_ids.append(i)
        return self

    def set_identifier(self, identifier: str):
        self.update_data['identifier'] = identifier
        return self

    def set_cipher(self, cipher: str):
        self.update_data['cipher'] = cipher
        return self

    def build(self):
        if len(self.exec_doc_ids) > 0:
            self.update_data['exec_doc_ids'] = self.exec_doc_ids
        self.result['job_ids'] = self.job_ids
        self.result['update_data'] = self.update_data
        return self.result
