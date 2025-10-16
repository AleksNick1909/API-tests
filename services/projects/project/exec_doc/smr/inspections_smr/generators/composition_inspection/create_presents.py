

class CreatePresentsInspectionGen:

    def __init__(self):
        self.result = []
        self.presents = {}

    def set_description(self, description: str):
        self.presents['description'] = description
        return self

    def set_position(self, position='start'):
        self.presents['position'] = position
        return self

    def set_type(self, type_name='material'):
        self.presents['type'] = type_name
        return self

    def set_unit(self, unit=''):
        self.presents['unit'] = unit
        return self

    def set_volume(self, volume=''):
        self.presents['volume'] = volume
        return self

    def set_is_from_structure(self, is_from_structure=True):
        self.presents['isFromStructure'] = is_from_structure
        return self

    def set_settings_numeration(self, settings_numeration=None):
        self.presents['settings_numeration'] = settings_numeration
        return self

    def set_job_id(self, job_id):
        self.presents['job_id'] = job_id
        return self

    def set_job_parent_id(self, job_parent_id: int):
        self.presents['job_parent_id'] = job_parent_id
        return self

    def set_material_id(self, material_id: int):
        self.presents['material_id'] = material_id
        return self

    def build(self):
        self.result.append(self.presents)
        return self.result
