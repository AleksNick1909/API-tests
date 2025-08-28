from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_get import GetStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_update import UpdateStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_create import CreateStructureSmrGen
from services.projects.project.exec_doc.smr.structures_smr.generators.structure_smr_delete import DeleteStructureSmrGen


class StructureSmrPayloads:

    def __init__(self):
        self.get = GetStructureSmrGen()
        self.update = UpdateStructureSmrGen()
        self.create = CreateStructureSmrGen()
        self.delete = DeleteStructureSmrGen()

    def get_structure_smr(self):
        params = self.get.set_page().set_count().build()
        return params

    def create_structure_smr(self):
        body = self.create.set_user_id().set_row_id().set_position().build()
        return body

    def delete_structure_smr(self, structure_ids):
        body = self.delete.set_structure_ids(structure_ids).build()
        return body
