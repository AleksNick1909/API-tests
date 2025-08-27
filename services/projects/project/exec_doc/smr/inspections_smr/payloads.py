
from services.projects.project.exec_doc.smr.inspections_smr.generators. \
    inspections_smr_get import GetInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.generators. \
    inspections_smr_update import UpdateInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.generators. \
    inspections_smr_create import CreateInspectionsSmrGen
from services.projects.project.exec_doc.smr.inspections_smr.generators. \
    inspections_smr_delete import DeleteInspectionsSmrGen


class InspectionsSmrPayloads:

    def __init__(self):
        self.get = GetInspectionsSmrGen()
        self.update = UpdateInspectionsSmrGen()
        self.create = CreateInspectionsSmrGen()
        self.delete = DeleteInspectionsSmrGen()

    def get_inspection_smr(self):
        params = self.get.set_page().set_count().build()
        return params

    def create_inspection_smr(self, id_type_inspection: int):
        body = self.create.set_order().set_id_numeration().set_type_id(id_type_inspection).set_user_id().build()
        return body
