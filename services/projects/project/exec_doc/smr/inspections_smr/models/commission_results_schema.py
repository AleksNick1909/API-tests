from pydantic import BaseModel
from typing import List, Optional, Any


class User(BaseModel):
    active: bool
    certificate: Optional[str] = None
    division: Optional[str] = None
    email: str
    fio: str
    id: int
    name: str
    phone: str
    position: str
    representative: Optional[str] = None
    role: int


class CreationAuthor(BaseModel):
    act_edit: bool
    active: bool
    active_sc: bool
    companyID: int
    created_at: str
    deleted: bool
    division_id: Optional[str] = None
    email: str
    FIO: str
    id: int
    is_admin: bool
    keycloak_id: Optional[str] = None
    language: str
    last_activity_time: str
    last_login_date: str
    ldap: bool
    login: str
    name: str
    order: int
    parentID: int
    personnel_number: Optional[str] = None
    phone: str
    position: str
    profile_email: Optional[str] = None
    repID: int
    roleID: int
    settings_ldap_id: Optional[str] = None
    updated_at: str
    uuid: str


class Partner(BaseModel):
    address: Optional[str] = None
    author: Optional[str] = None
    branchStation: Optional[str] = None
    branchStationId: Optional[str] = None
    code: Optional[str] = None
    code2: Optional[str] = None
    comments: Optional[str] = None
    contractDate: Optional[str] = None
    contractNumber: Optional[str] = None
    creationAuthor: CreationAuthor
    creationDate: str
    email: Optional[str] = None
    eso: Optional[str] = None
    eso_date_to: Optional[str] = None
    FIO: Optional[str] = None
    files: List[Any] = []
    group: Optional[str] = None
    id: int
    INN: Optional[str] = None
    indexMail: Optional[str] = None
    isFolder: bool
    isPartnerIntegration: bool
    kpp: Optional[str] = None
    kpp2: Optional[str] = None
    kppSro: Optional[str] = None
    liquidationDate: Optional[str] = None
    logoName: Optional[str] = None
    modificationAuthor: Optional[str] = None
    modificationDate: Optional[str] = None
    name: str
    name_eng: Optional[str] = None
    ogrn: Optional[str] = None
    okfs: Optional[str] = None
    okopf: Optional[str] = None
    okpo: Optional[str] = None
    oktmo: Optional[str] = None
    okved: Optional[str] = None
    order: int
    organization: Optional[str] = None
    organizationPurchasing: Optional[str] = None
    organizationType: Optional[str] = None
    parentOrganizationCode: Optional[str] = None
    passportIssuedBy: Optional[str] = None
    passportIssuedDate: Optional[str] = None
    passportNumber: Optional[str] = None
    permissions: Optional[str] = None
    phone: Optional[str] = None
    purchaseOrganizer: Optional[str] = None
    region: Optional[str] = None
    registration_authority: Optional[str] = None
    registrationDate: Optional[str] = None
    registrationNumber: Optional[str] = None
    shortName: Optional[str] = None
    short_name_eng: Optional[str] = None
    sro: Optional[str] = None
    sroInn: Optional[str] = None
    sroOgrn: Optional[str] = None
    status: Optional[str] = None
    type: int
    typePartners: Optional[str] = None
    uuid: str


class Representative(BaseModel):
    activeDecree: Optional[str] = None
    address: Optional[str] = None
    attestationLevel: Optional[str] = None
    attestationPlace: Optional[str] = None
    attachments: List[Any] = []
    certificate_begin_date: Optional[str] = None
    certificate_job: Optional[str] = None
    certificate_number: Optional[str] = None
    documentsConfirms: List[Any] = []
    education: Optional[str] = None
    email: str
    entry_date: Optional[str] = None
    exception_date: Optional[str] = None
    fio: str
    id: int
    name: str
    nationalRegisterNumber: Optional[str] = None
    numberNationalCertificate: Optional[str] = None
    partner: Partner
    passportIssuedBy: Optional[str] = None
    passportIssuedDate: Optional[str] = None
    passportNumber: Optional[str] = None
    personal_stamp_number: Optional[str] = None
    phone: str
    position: str
    positions: List[Any] = []
    special: Optional[str] = None
    specialty: Optional[str] = None
    user: User
    welder: Optional[str] = None
    work_type: Optional[str] = None


class RepresentativeInfo(BaseModel):
    fio: str
    name: str
    partner: str
    position: str


class Status(BaseModel):
    color: str
    id: int
    name: str
    order: float
    system: bool


class CommissionResultSchema(BaseModel):
    ableRestart: bool
    cancelComment: Optional[str] = None
    cancelDate: Optional[str] = None
    cancelReason: Optional[str] = None
    confirmedDate: Optional[str] = None
    dateNotify: Optional[str] = None
    description: Optional[str] = None
    deviationDocs: List[Any] = []
    id: int
    images: List[Any] = []
    inspectionRemarks: List[Any] = []
    inspectionRepresentativeRole: Optional[str] = None
    isAlwaysBlocked: bool
    isConfirmed: bool | None
    isLazyBlocked: bool
    representative: Representative
    representativeInfo: RepresentativeInfo
    representativeText: Optional[str] = None
    remainLazyBlock: Optional[str] = None
    signature: Optional[str] = None
    status: Status | None = None
    statusAfterElimination: Optional[str] = None
