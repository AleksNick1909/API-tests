from pydantic import BaseModel


class FolderSchema(BaseModel):
    authorId: int | None = None
    authorPartnerId: int | None = None
    catalog: str | None = None
    childrenFolders: list = []
    companyId: int
    constructionsCount: int
    id: int
    imagePath: str | None = None
    imagePreviewPath: str | None = None
    isFavorite: bool
    levelId: str | None = None
    name: str
    nestedConstructionsCount: int
    order: float
    parent: str | None = None


class ConstructionProjectSchema(BaseModel):
    administrativeRegion: str | None = None
    approvedEndDate: str | None = None
    approvedStartDate: str | None = None
    authorControl: str | None = None
    authorId: int | None = None
    authorPartnerId: int | None = None
    buildingControl: str | None = None
    buildingPermit: bool | None = None
    buildingPermitDate: str | None = None
    buildingPermitEditingDate: str | None = None
    buildingPermitIssuer: str | None = None
    buildingPermitNumber: str | None = None
    buildingPermitTerm: str | None = None
    budgetForSmr: str | None = None
    budgetQueues: list | None = None
    category: str | None = None
    chdd: str | None = None
    companyId: int | None = None
    contractors: str | None = None
    contractorsPnr: str | None = None
    costLandPlot: str | None = None
    costPir: str | None = None
    costTotal: str | None = None
    costType: str | None = None
    createdAt: str | None = None
    customAttributesValues: list = []
    customer: str | None = None
    designers: str | None = None
    developer: str | None = None
    division: str | None = None
    documentPacks: str | None = None
    dso: str | None = None
    endDateFact: str | None = None
    executiveDocumentation: str | None = None
    exploitatingOrganizations: str | None = None
    filial: str | None = None
    fixedDerivationAssets: list = []
    fixedInputAssets: list = []
    folder: str | None = None
    fullName: str | None = None
    generalContractor: str | None = None
    id: int | None = None
    identifierGk: str | None = None
    identifierOkc: str | None = None
    investor: str | None = None
    isBudgetQueuesEditable: bool | None = None
    isFavorite: bool | None = None
    landPlotCadastralNumber: str | None = None
    landPlotCityNumber: str | None = None
    landPlotComment: str | None = None
    landPlotPurpose: str | None = None
    lifeCycleStage: str | None = None
    lifeCycleStatus: str | None = None
    location: str | None = None
    locationAddress: str | None = None
    mediaCover: str | None = None
    objectBudget: str | None = None
    objectBudgetType: str | None = None
    objectCode: str | None = None
    objectForm: str | None = None
    objectGroup: str | None = None
    objectIntegration: str | None = None
    objectNumber: str | None = None
    objectType: str | None = None
    oktmo: str | None = None
    order: float | None = None
    pgConclusionDate: str | None = None
    pgConclusionIssuer: str | None = None
    pgConclusionNumber: str | None = None
    pirEndDate: str | None = None
    pirStartDate: str | None = None
    planCipher: str | None = None
    positionGeneralContractors: list = []
    projectComment: str | None = None
    region: str | None = None
    remark: str | None = None
    shortName: str | None = None
    shortProjectDescription: str | None = None
    smrData: str | None = None
    socialSignificance: str | None = None
    sourceOfFinancing: str | None = None
    startDateFact: str | None = None
    station: str | None = None
    supportNumber: str | None = None
    uuid: str | None = None
    vnd: str | None = None


class ArchiveSchema(BaseModel):
    authorId: int | None = None
    authorPartnerId: int | None = None
    catalog: str | None = None
    childrenFolders: list = []
    companyId: int
    constructionsCount: int
    id: int
    imagePath: str | None = None
    imagePreviewPath: str | None = None
    isFavorite: bool
    levelId: str | None = None
    name: str
    order: float
    parent: str | None = None


class DataSchema(BaseModel):
    archive: ArchiveSchema
    constructions: list[ConstructionProjectSchema]
    folders: list[FolderSchema]


class PaginateSchema(BaseModel):
    currentPage: int
    hasMorePages: bool
    perPage: int


class ProjectsListModel(BaseModel):
    breadcrumbs: list = []
    data: DataSchema | None = None
    paginate: PaginateSchema | None = None
