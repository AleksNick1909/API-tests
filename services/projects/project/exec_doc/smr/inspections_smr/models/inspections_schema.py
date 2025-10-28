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
    journal_special_zhsr_records: list | None = Field(None, alias='journalSpecialZhsrRecords')
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
    code: dict | None = None
    order: float
    control_type: str | None = Field(alias='controlType')
    inspection_status: str | None = Field(alias='inspectionStatus')
    system: bool
    type: str


class InspectionSchema(BaseModel):
    act_compositions: int | None = Field(None, alias='actCompositions')
    atg: str | None = None
    author_supervisions: list | None = Field(None, alias='authorSupervisions')
    auto_action: int | None = Field(None, alias='autoAction')
    auto_add_job_in_journal: bool | None = Field(None, alias='autoAddJobInJournal')
    block_level: int | None = Field(None, alias='blockLevel')
    code: int | None = None
    comment_registration: str | None = Field(None, alias='commentRegistration')
    construction: int | None = None
    contractor_number: int | None = Field(None, alias='contractorNumber')
    contractor_text: str | None = Field(None, alias='contractorText')
    contractors: list | None = None
    control_method: list | None = None
    control_scope: str | None = None
    control_scope_text: str | None = Field(None, alias='controlScopeText')
    control_stage_index: int | None = Field(None, alias='controlStageIndex')
    control_stage_name: str = Field(None, alias='controlStageName')
    created_at: str | None = Field(None, alias='createdAt')  # Добавлено
    customer_number: int | None = Field(None, alias='customerNumber')
    customer_text: str | None = Field(None, alias='customerText')
    customers: list | None = None
    description: str | None = None
    direction: dict | None = None
    directions: list | None = None
    entrance_journal: dict | None = Field(None, alias='entranceJournal')
    entrance_journal_act: dict | None = Field(None, alias='entranceJournalAct')
    exec_doc: dict | None = Field(None, alias='execDoc')
    fact_date: str | None = Field(None, alias='factDate')
    files: list | None = None
    id: int
    inspection_type: InspectionTypeSchema = None
    inspection_welding: InspectionWeldingSchema | None = Field(None, alias='inspectionWelding')
    is_author_supervision_enable: bool | None = Field(None, alias='isAuthorSupervisionEnable')
    is_blocked: bool | None = Field(None, alias='isBlocked')
    is_empty_volume_accept: bool = Field(None, alias='isEmptyVolumeAccept')
    is_negative_blocked: bool | None = Field(None, alias='isNegativeBlocked')
    is_registered: bool | None = Field(None, alias='isRegistered')
    is_representative_statuses_blocked: bool | None = Field(None, alias='isRepresentativeStatusesBlocked')
    jobs_string: str = Field(None, alias='jobsString')
    jobs_volume_accept_total: int = Field(None, alias='jobsVolumeAcceptTotal')
    journal: JournalSchema | None = None
    journal_special: int | None = None
    line: str | None = None
    link: str | None = None
    location: str | None = None
    man_hours_duration: int = Field(None, alias='manHoursDuration')
    materials_string: str = Field(None, alias='materialsString')
    notification_date: str | None = Field(None, alias='notificationDate')
    notification_number: str | None = Field(None, alias='notificationNumber')
    order: float | None = None
    other: str | None = None
    parent_inspection: dict | None = None
    participant_text: str | None = Field(None, alias='participantText')
    plan_check_number: int | None = Field(None, alias='planCheckNumber')
    planned_date: str | None = None
    planned_date_begin: str | None = Field(None, alias='plannedDateBegin')
    planned_date_end: str | None = Field(None, alias='plannedDateEnd')
    qty: str | None = None
    registration_date: str | None = None
    registration_number: str | None = None
    registration_verified_date: str | None = Field(None, alias='registrationVerifiedDate')
    rejection_date: str | None = Field(None, alias='rejectionDate')
    repeat_inspection: dict | None = Field(None, alias='repeatInspection')
    representatives: list | None = None
    responsible_registration_contractor: dict | None = Field(None, alias='responsibleRegistrationContractor')
    responsible_registration_customer: dict | None = Field(None, alias='responsibleRegistrationCustomer')
    status: StatusInspectionSchema | None = None
    structure: dict | None = None
    subsystem_text: str | None = Field(None, alias='subsystemText')
    supervisor_text: str | None = Field(None, alias='supervisorText')
    supervisors: list | None = None
    system: str | None = None
    system_text: str | None = Field(None, alias='systemText')
    title: str | None = None
    subtitle: str | None = None
    title_structure_levels: list | None = Field(None, alias='titleStructureLevels')
    title_smr_level_value: str | None = Field(None, alias='titleSmrLevelValue')
    typical_itp: str | None = Field(None, alias='typicalITP')
    type_of_work: TypeOfWorkSchema | None = Field(None, alias='typeOfWork')
    types_of_work: list = Field(None, alias='typesOfWork')
    was_restarted: bool = Field(None, alias='wasRestarted')
    zone: int | None = None
    zone_structure_level: str | None = Field(None, alias='zoneStructureLevel')
    zone_smr_level_value: str | None = Field(None, alias='zoneSmrLevelValue')


class InspectionsSchema(BaseModel):
    current_page: int
    dashboard: dict
    data: list[InspectionSchema]
    last_page: int
    per_page: int
    total_items: int
