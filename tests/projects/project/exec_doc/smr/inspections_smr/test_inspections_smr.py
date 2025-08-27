from config.base_test import BaseTest


class TestInspectionsSmr(BaseTest):

    def test_get_inspections_smr(self):

        inspections_smr = self.inspections_smr_api.get_inspections_smr_api()
        print(inspections_smr)

    def test_create_inspections_smr(self):
        new_inspection_smr = self.inspections_smr_api.create_inspections_smr_api()
        print(new_inspection_smr)
