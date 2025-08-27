from pydantic import Field, BaseModel


class InspectionRepresentativeRoleSchema(BaseModel):
    all_user_roles: bool = Field(alias='allUserRoles')
    control_types: list = Field(alias='controlTypes')
    id: int
    name: str
    order: int
    user_role: None = Field(alias='userRole')


class RepresentativeInfoSchema(BaseModel):
    fio: str | None
    name: str
    partner: str
    position: str


class AddRepresentativeInInspectionSchema(BaseModel):
    cancel_date: str | None = Field(None, alias='cancelDate')
    date_notify: str | None = Field(alias='dateNotify')
    id: int
    representative: dict | None
    signature: dict | None = None
    date_result_notify: str | None = Field(None, alias='dateResultNotify')
    signature_agreement: dict | None = Field(None, alias='signatureAgreement')
    signature_result: str | None = Field(None, alias='signatureResult')
    familiarized_signature: None = Field(None, alias='familiarizedSignature')


class StatusInspectionSchema(BaseModel):
    color: str
    id: int
    name: str
    order: float
    system: bool


class RepresentativesInInspectionSchema(BaseModel):
    able_restart: bool = Field(alias='ableRestart')
    cancel_comment: None = Field(alias='cancelComment')
    cancel_date: None = Field(alias='cancelDate')
    cancel_reason: None = Field(alias='cancelReason')
    confirmed_date: str | None = Field(alias='confirmedDate')
    date_notify: str | None = Field(alias='dateNotify')
    description: str | None
    deviation_docs: list = Field(alias='deviationDocs')
    id: int
    images: list
    inspection_remarks: list = Field(alias='inspectionRemarks')
    inspection_representative_role: InspectionRepresentativeRoleSchema = Field(alias='inspectionRepresentativeRole')
    is_always_blocked: bool = Field(alias='isAlwaysBlocked')
    is_confirmed: bool = Field(alias='isConfirmed')
    is_lazy_blocked: bool = Field(alias='isLazyBlocked')
    remain_lazy_block: bool | None = Field(alias='remainLazyBlock')
    representative: dict | None
    representative_info: RepresentativeInfoSchema = Field(alias='representativeInfo')
    representative_text: None = Field(alias='representativeText')
    signature: None
    status: StatusInspectionSchema | None
    status_after_elimination: None = Field(alias='statusAfterElimination')


class InspectionWeldingSchema(BaseModel):
    id: int
    isometric_drawing: str | None = Field(alias='isometricDrawing')
    journal_special_zhsr_records: list | None = Field(alias='journalSpecialZhsrRecords')
    line_number: int | None = Field(alias='lineNumber')
    project_number: int | None = Field(alias='projectNumber')
    spool: str | None
    welding_joints: str | None = Field(alias='weldingJoints')


class JournalSchema(BaseModel):
    id: int
    name: str
    structure: dict | None
    tom: int


class TypeOfWorkSchema(BaseModel):
    id: int
    name: str
    code: str | None
    order: float
    typical_itps: str | None = Field(alias='typicalITPs')


class InspectionTypeSchema(BaseModel):
    id: int
    name: str
    code: str | None
    order: float
    control_type: str | None = Field(alias='controlType')
    inspection_status: str | None = Field(alias='inspectionStatus')


class InspectionSchema(BaseModel):
    id: int
    qty: str | None = None
    location: str | None = None
    control_scope_text: str | None = Field(None, alias='controlScopeText')
    status: StatusInspectionSchema | None = None
    planned_date: str | None = None
    registration_date: str | None = None
    registration_number: str | None = None
    inspection_type: InspectionTypeSchema = None
    contractors: list | None = None
    customers: list | None = None
    supervisors: list | None = None
    structure: dict | None = None
    journal: JournalSchema | None = None
    journal_special: int | None = None
    entrance_journal: dict | None = Field(None, alias='entranceJournal')
    entrance_journal_act: dict | None = Field(None, alias='entranceJournalAct')
    representatives: list | None = None
    control_method: list | None = None
    control_scope: str | None = None
    zone: int | None = None
    code: int | None = None
    system: str | None = None
    other: str | None = None
    parent_inspection: dict | None = None
    order: float | None = None
    act_compositions: int | None = Field(None, alias='actCompositions')
    auto_action: int | None = Field(None, alias='autoAction')
    repeat_inspection: dict | None = Field(None, alias='repeatInspection')
    responsible_registration_contractor: dict | None = Field(None, alias='responsibleRegistrationContractor')
    responsible_registration_customer: dict | None = (Field(None, alias='responsibleRegistrationCustomer'))
    notification_date: str | None = Field(None, alias='notificationDate')
    rejection_date: str | None = Field(None, alias='rejectionDate')
    is_registered: bool | None = Field(None, alias='isRegistered')
    comment_registration: str | None = Field(None, alias='commentRegistration')
    exec_doc: dict | None = Field(None, alias='execDoc')
    direction: dict | None = None
    directions: dict | None = None
    type_of_work: TypeOfWorkSchema | None = Field(None, alias='typeOfWork')
    types_of_work: list = Field(None, alias='typesOfWork')
    jobs_string: str = Field(None, alias='jobsString')
    materials_string: str = Field(None, alias='materialsString')
    jobs_volume_accept_total: int = Field(None, alias='jobsVolumeAcceptTotal')
    control_stage_index: int | None = Field(None, alias='controlStageIndex')
    control_stage_name: str = Field(None, alias='controlStageName')
    inspection_welding: InspectionWeldingSchema | None = Field(None, alias='inspectionWelding')
    registration_verified_date: str | None = Field(None, alias='registrationVerifiedDate')
    is_blocked: bool | None = Field(None, alias='isBlocked')
    block_level: int | None = Field(None, alias='blockLevel')
    is_negative_blocked: bool | None = Field(None, alias='isNegativeBlocked')
    plan_check_number: int | None = Field(None, alias='planCheckNumber')
    auto_add_job_in_journal: bool | None = Field(None, alias='autoAddJobInJournal')
    typical_itp: str | None = Field(None, alias='typicalITP')
    fact_date: str | None = Field(None, alias='factDate')
    man_hours_duration: int = Field(None, alias='manHoursDuration')
    notification_number: str | None = Field(None, alias='notificationNumber')
    files: list | None = None
    atg: str | None = None
    author_supervisions: list | None = Field(None, alias='authorSupervisions')
    is_author_supervision_enable: bool | None = Field(None, alias='isAuthorSupervisionEnable')
    title: str | None = None
    subtitle: str | None = None
    construction: int | None = None
    line: str | None = None
    system_text: str | None = Field(None, alias='systemText')
    subsystem_text: str | None = Field(None, alias='subsystemText')
    contractor_text: str | None = Field(None, alias='contractorText')
    customer_text: str | None = Field(None, alias='customerText')
    supervisor_text: str | None = Field(None, alias='NonesupervisorText')
    participant_text: str | None = Field(None, alias='participantText')
    is_representative_statuses_blocked: bool | None = Field(None, alias='isRepresentativeStatusesBlocked')
    link: str | None = None
    contractor_number: int | None = Field(None, alias='contractorNumber')
    customer_number: int | None = Field(None, alias='customerNumber')
    was_restarted: bool = Field(None, alias='wasRestarted')
    is_empty_volume_accept: bool = Field(None, alias='isEmptyVolumeAccept')


class InspectionsSchema(BaseModel):
    current_page: int
    dashboard: dict
    data: list[InspectionSchema]
    last_page: int
    per_page: int
    total_items: int
