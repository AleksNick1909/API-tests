from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_get import GetStructureSmr
from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_update import UpdateStructureSmr
from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_create import CreateStructureSmr
from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_delete import DeleteStructureSmr
from config.auth import user_id


class StructureSmrPayloads:

    def __init__(self):
        self.get = GetStructureSmr()
        self.update = UpdateStructureSmr()
        self.create = CreateStructureSmr()
        self.delete = DeleteStructureSmr()

    def get_structure_smr(self):
        params = self.get.set_page().set_count().build()
        return params

    def create_structure_smr(self):
        body = self.create.set_user_id().set_row_id().set_position().build()
        return body
