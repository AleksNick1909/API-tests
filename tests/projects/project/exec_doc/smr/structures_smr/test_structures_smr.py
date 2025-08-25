from config.base_test import BaseTest


class TestStructuresSmr(BaseTest):

    def test_get_structures_smr(self):

        structures_smr = self.structures_smr_api.get_structures_smr_api()
        print(structures_smr)

    def test_create_structures_smr(self):
        structures_smr = self.structures_smr_api.create_structures_smr_api()
        print(structures_smr)
