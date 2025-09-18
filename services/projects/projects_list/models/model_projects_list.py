from pydantic import BaseModel, Field


class FolderSchema(BaseModel):
    author_id: int | None = Field(None, alias='authorId')
    author_partner_d: int | None = Field(None, alias='authorPartnerId')
    catalog: str | None = None
    children_folders: list = Field(None, alias='childrenFolders')
    company_id: int = Field(alias='companyId')
    constructions_count: int = Field(alias='constructionsCount')
    id: int
    image_path: str | None = Field(None, alias='imagePath')
    image_preview_path: str | None = Field(None, alias='imagePreviewPath')
    is_favorite: bool = Field(alias='isFavorite')
    level_id: str | None = Field(None, alias='levelId')
    name: str
    nested_constructions_count: int = Field(alias='nestedConstructionsCount')
    order: float
    parent: str | None = None


class ConstructionProjectSchema(BaseModel):
    administrative_region: str | None = Field(None, alias='administrativeRegion')
    approved_end_date: str | None = Field(None, alias='approvedEndDate')
    approved_start_date: str | None = Field(None, alias='approvedStartDate')
    author_control: str | None = Field(None, alias='authorControl')
    author_id: int | None = Field(None, alias='authorId')
    author_partner_id: int | None = Field(None, alias='authorPartnerId')
    building_control: str | None = Field(None, alias='buildingControl')
    building_permit: bool | None = Field(None, alias='buildingPermit')
    building_permit_date: str | None = Field(None, alias='buildingPermitDate')
    building_permit_editing_date: str | None = Field(None, alias='buildingPermitEditingDate')
    building_permit_issuer: str | None = Field(None, alias='buildingPermitIssuer')
    building_permit_number: str | None = Field(None, alias='buildingPermitNumber')
    building_permit_term: str | None = Field(None, alias='buildingPermitTerm')
    budget_for_smr: str | None = Field(None, alias='budgetForSmr')
    budget_queues: list | None = Field(None, alias='budgetQueues')
    category: str | None = None
    chdd: str | None = None
    company_id: int | None = Field(None, alias='companyId')
    contractors: str | None = None
    contractors_pnr: str | None = Field(None, alias='contractorsPnr')
    cost_land_plot: str | None = Field(None, alias='costLandPlot')
    cost_pir: str | None = Field(None, alias='costPir')
    cost_total: str | None = Field(None, alias='costTotal')
    cost_type: str | None = Field(None, alias='costType')
    created_at: str | None = Field(None, alias='createdAt')
    custom_attributes_values: list = Field(None, alias='customAttributesValues')
    customer: str | None = None
    designers: str | None = None
    developer: str | None = None
    division: str | None = None
    document_packs: str | None = Field(None, alias='documentPacks')
    dso: str | None = None
    end_date_fact: str | None = Field(None, alias='endDateFact')
    executive_documentation: str | None = Field(None, alias='executiveDocumentation')
    exploitating_organizations: str | None = Field(None, alias='exploitatingOrganizations')
    filial: str | None = None
    fixed_derivation_assets: list = Field(None, alias='fixedDerivationAssets')
    fixed_input_assets: list = Field(None, alias='fixedInputAssets')
    folder: str | None = None
    full_name: str | None = Field(None, alias='fullName')
    general_contractor: str | None = Field(None, alias='generalContractor')
    id: int | None = None
    identifier_gk: str | None = Field(None, alias='identifierGk')
    identifier_okc: str | None = Field(None, alias='identifierOkc')
    investor: str | None = None
    is_budget_queues_editable: bool | None = Field(None, alias='isBudgetQueuesEditable')
    is_favorite: bool | None = Field(None, alias='isFavorite')
    land_plot_cadastral_number: str | None = Field(None, alias='landPlotCadastralNumber')
    land_plot_city_number: str | None = Field(None, alias='landPlotCityNumber')
    land_plot_comment: str | None = Field(None, alias='landPlotComment')
    land_plot_purpose: str | None = Field(None, alias='landPlotPurpose')
    life_cycle_stage: str | None = Field(None, alias='lifeCycleStage')
    life_cycle_status: dict | None = Field(None, alias='lifeCycleStatus')
    location: str | None = None
    location_address: str | None = Field(None, alias='locationAddress')
    media_cover: dict | None = Field(None, alias='mediaCover')
    object_budget: str | None = Field(None, alias='objectBudget')
    object_budget_type: str | None = Field(None, alias='objectBudgetType')
    object_code: str | None = Field(None, alias='objectCode')
    object_form: dict | None = Field(None, alias='objectForm')
    object_group: str | None = Field(None, alias='objectGroup')
    object_integration: str | None = Field(None, alias='objectIntegration')
    object_number: str | None = Field(None, alias='objectNumber')
    object_type: str | None = Field(None, alias='objectType')
    oktmo: str | None = None
    order: float | None = None
    pg_conclusion_date: str | None = Field(None, alias='pgConclusionDate')
    pg_conclusion_issuer: str | None = Field(None, alias='pgConclusionIssuer')
    pg_conclusion_number: str | None = Field(None, alias='pgConclusionNumber')
    pir_end_date: str | None = Field(None, alias='pirEndDate')
    pir_start_date: str | None = Field(None, alias='pirStartDate')
    plan_cipher: str | None = Field(None, alias='planCipher')
    position_general_contractors: list = Field(None, alias='positionGeneralContractors')
    project_comment: str | None = Field(None, alias='projectComment')
    region: str | None = None
    remark: str | None = None
    short_name: str | None = Field(None, alias='shortName')
    short_project_description: str | None = Field(None, alias='shortProjectDescription')
    smr_data: str | None = Field(None, alias='smrData')
    social_significance: str | None = Field(None, alias='socialSignificance')
    source_of_financing: str | None = Field(None, alias='sourceOfFinancing')
    start_date_fact: str | None = Field(None, alias='startDateFact')
    station: str | None = None
    support_number: str | None = Field(None, alias='supportNumber')
    uuid: str | None = None
    vnd: str | None = None


class ArchiveSchema(BaseModel):
    author_id: int | None = Field(None, alias='authorId')
    author_partner_id: int | None = Field(None, alias='authorPartnerId')
    catalog: str | None = None
    children_folders: list = Field(alias='childrenFolders')
    company_id: int = Field(alias='companyId')
    constructions_count: int = Field(alias='constructionsCount')
    id: int
    image_path: str | None = Field(None, alias='imagePath')
    image_preview_path: str | None = Field(None, alias='imagePreviewPath')
    is_favorite: bool = Field(alias='isFavorite')
    level_id: str | None = Field(None, alias='levelId')
    name: str
    order: float
    parent: str | None = None


class DataSchema(BaseModel):
    archive: ArchiveSchema
    constructions: list[ConstructionProjectSchema]
    folders: list[FolderSchema]


class PaginateSchema(BaseModel):
    current_page: int = Field(alias='currentPage')
    has_more_pages: bool = Field(alias='hasMorePages')
    per_page: int = Field(alias='perPage')


class ProjectsListModel(BaseModel):
    breadcrumbs: list = []
    data: DataSchema | None = None
    paginate: PaginateSchema | None = None
