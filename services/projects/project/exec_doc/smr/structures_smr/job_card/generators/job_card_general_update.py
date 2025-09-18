

class UpdateJobGeneralGen:

    def __init__(self):
        self.result = {}

    def set_price_fact(self, price_fact: int):
        self.result['priceFact'] = price_fact
        return self

    def set_representative_id(self, representative_id):
        self.result['representativeId'] = representative_id
        return self

    def set_customer_rep_id(self, customer_rep_id):
        self.result['customerRepId'] = customer_rep_id
        return self

    def set_type_of_work_id(self, type_of_work_id):
        self.result['typeOfWorkId'] = type_of_work_id
        return self

    def set_qty_contract(self, qty_contract):
        self.result['qtyContract'] = qty_contract
        return self

    def set_date_begin_contract(self, date_begin_contract):
        self.result['dateBeginContract'] = date_begin_contract
        return self

    def set_date_end_contract(self, date_end_contract):
        self.result['dateEndContract'] = date_end_contract
        return self

    def set_price_plan(self, price_plan: int):
        self.result['pricePlan'] = price_plan
        return self

    def set_identifier(self, identifier: str):
        self.result['identifier'] = identifier
        return self

    def build(self):
        return self.result
