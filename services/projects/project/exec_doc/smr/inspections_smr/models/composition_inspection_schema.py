from pydantic import Field, BaseModel

from services.projects.project.exec_doc.smr.inspections_smr.models.inspections_schema import InspectionSchema


class FileQualityDocumentsSchema(BaseModel):
    document_version_approval_result: None = Field(alias='documentVersionApprovalResult')
    extension: str
    folderId: int
    id: int
    name: str | None
    number: str | None
    path: str
    public: bool


class QualityDocumentsSchema(BaseModel):
    date: str | None
    file: FileQualityDocumentsSchema | None
    id: int
    lists: int | None
    name: str | None
    number: str | None
    registry: bool | None
    validity_period: str | None = Field(alias='validityPeriod')


class JobSchema(BaseModel):
    id: int
    name: str
    units: str | None
    price: float
    calculate_method_materials: str | None = Field(None, alias="calculateMethodMaterials")
    structure: dict | None = None
    fact_materials: list | None = Field(None, alias="factMaterials")
    dates_fact: list | None = Field(None, alias="datesFact")
    dates_plan: list | None = Field(None, alias="datesPlan")
    direction: str | None
    type_of_work: dict | None = Field(alias="typeOfWork")
    records: list = []
    contract_number: int | None = Field(alias="contractNumber")
    qty_fact: float = Field(alias="qtyFact")
    element: str | None = None
    cipher: str | None = None
    cipher_rd: str | None = Field(alias="cipherRd")
    first_job_document: str | None = Field(alias="firstJobDocument")
    qty_inspection: float = Field(alias="qtyInspection")
    qty_inspection_gk: float = Field(alias="qtyInspectionGk")
    code: str | None = None
    unit_rates: list | None = Field(None, alias="unitRates")
    constructive: list = []
    identifier: str | None = None


class PresentsJobSchema(BaseModel):
    actual_name: None = Field(alias='actualName')
    constructive: str | None
    has_materials: bool = Field(alias='hasMaterials')
    id: int
    inspection_volume: int | None = Field(alias='inspectionVolume')
    inspections: list[InspectionSchema] | None
    is_from_structure: bool = Field(alias='isFromStructure')
    is_volume_blocked: bool = Field(alias='isVolumeBlocked')
    job: JobSchema | None
    job_fact_date: None = Field(alias='jobFactDate')
    note: None
    volume: int
    volume_accept: int = Field(alias='volumeAccept')
    volume_not_accept: int = Field(alias='volumeNotAccept')


class MaterialSchema(BaseModel):
    acts: list
    contractor: None
    contractor_name: str | None = Field(alias='contractorName')
    id: int
    product_name: str | None = Field(alias='productName')
    quality_documents: list[QualityDocumentsSchema] = Field(alias='qualityDocuments')
    quantity: str | None
    quantity_inspection: int | None = Field(alias='quantityInspection')
    remainder: str | None
    units: str | None


class PresentsMaterialsSchema(BaseModel):
    actual_name: None = Field(alias='actualName')
    constructive: None
    description: str
    id: int
    inspection_volume: None = Field(alias='inspectionVolume')
    inspections: list[InspectionSchema]
    is_new_material: bool = Field(alias='isNewMaterial')
    job_fact_date: None = Field(alias='jobFactDate')
    material: MaterialSchema
    material_type: str = Field(alias='materialType')
    note: None
    quantity_per_job: int | None = Field(alias='quantityPerJob')
    remainder: int
    unit: str | None
    volume: int | None
    volume_accept: int | None = Field(alias='volumeAccept')
    volume_not_accept: int = Field(alias='volumeNotAccept')


class PresentsSchema(BaseModel):
    actual_name: None = Field(alias='actualName')
    attachments: list
    constructive: str | None
    description: str
    has_materials: bool = Field(alias='hasMaterials')
    id: int
    inspection_volume: int | None
    inspections: list[InspectionSchema] | None
    is_new_material: bool | None = Field(alias='isNewMaterial')
    is_volume_blocked: None = Field(alias='isVolumeBlocked')
    job: JobSchema | None
    job_fact_date: None = Field(alias='jobFactDate')
    material: MaterialSchema | None
    material_type: str | None = Field(alias='materialType')
    note: None
    order: float
    parent_id: int | None
    quantity_per_job: None = Field(alias='quantityPerJob')
    remainder: int | None
    representative: None
    type: str
    unit: str | None
    volume: float | None
    volume_accept: float | None
    volume_not_accept: float | None
