from typing import Any
from pydantic import BaseModel, Field


class PathItem(BaseModel):
    id: int
    name: str


class SmrStructure(BaseModel):
    id: int
    name: str
    number: int | None = None
    path: list[PathItem] | None


class Partner(BaseModel):
    id: int
    partner_id: int = Field(alias='partnerId')
    partner_name: str = Field(alias='partnerName')
    rep_fio: str = Field(alias='repFio')
    rep_name: str | None = Field(alias='repName')
    rep_position: str | None = Field(alias='repPosition')


class Parent(BaseModel):
    id: int
    name: str
    is_system: bool = Field(alias='isSystem')
    typical_itps: list[Any] = Field(alias='typicalITPs')
    journal_special_types: list[Any] = Field(alias='journalSpecialTypes')
    parent: dict | None
    code: str | None
    order: float
    is_crucial: bool = Field(alias='isCrucial')
    unit_measure: str | None = Field(alias='unitMeasure')


class TypeOfWork(BaseModel):
    id: int
    name: str
    is_system: bool = Field(alias='isSystem')
    typical_itps: list[Any] = Field(alias='typicalITPs')
    journal_special_types: list[Any] = Field(alias='journalSpecialTypes')
    parent: dict | None
    code: str | None
    order: float
    is_crucial: bool = Field(alias='isCrucial')
    unit_measure: str | None = Field(alias='unitMeasure')


class Direction(BaseModel):
    id: int
    name: str
    order: float
    type_of_works: list[TypeOfWork] = Field(alias='typeOfWorks')
    code: str | None
    hasChildren: str | None = Field(alias='hasChildren')
    has_type_of_works: bool = Field(alias='hasTypeOfWorks')
    parent_id: int
    fullPath: str


class JobsCardSchema(BaseModel):
    calculate_method_machines: str | None
    calculate_method_materials: str | None
    calculate_method_people: str | None
    cipher: str | None
    cipher_project: str | None = Field(alias='cipherProject')
    cipher_rd: str | None = Field(alias='cipherRd')
    code: str | None
    code_plan: str | None
    comments: str | None
    conditions_of_work: str | None = Field(alias='conditionsOfWork')
    constructive: list[Any]
    contractor_name: str | None
    contractor_signature: str | None = Field(alias='contractorSignature')
    custom_customer_name: str | None = Field(alias='customCustomerName')
    custom_rep_name: str | None = Field(alias='customRepName')
    customer: str | None
    customer_signature: str | None = Field(alias='customerSignature')
    date: str
    date_begin_fact: str | None
    date_begin_plan: str | None
    date_end_fact: str | None
    date_end_plan: str | None
    direction: str | None
    documents: list[Any]
    documents_aosr: list[Any] = Field(alias='documentsAosr')
    documents_files_jobs: list[Any] = Field(alias='documentsFilesJobs')
    documents_files_jobs_aosr: list[Any] = Field(alias='documentsFilesJobsAosr')
    element: str | None
    element_code: str | None = Field(alias='elementCode')
    estimate_name: str | None = Field(alias='estimateName')
    exec_doc_dates: list[Any] = Field(alias='execDocDates')
    executive_documentation: list | None = Field(alias='executiveDocumentation')
    fact_dates: list | None
    fact_qty_percent: int | None
    from_journal_spec_id: str | None = Field(alias='fromJournalSpecId')
    from_journal_spec_record_ids: list[Any] = Field(alias='fromJournalSpecRecordIds')
    id: int
    id_plan: str | None = Field(alias='idPlan')
    id_position_plan: str | None = Field(alias='idPositionPlan')
    identifier: str | None
    inspection_dates: list[Any] = Field(alias='inspectionDates')
    inspections_tests_plan: list | None
    journal: dict | None
    journal_order: float | None
    journal_special_type_id: str | None = Field(alias='JournalSpecialTypeId')
    journal_structure_order: str | None
    ks2: list[Any]
    labor_costs: float | None = Field(alias='laborCosts')
    labor_costs_per_unit: float | None = Field(alias='laborCostsPerUnit')
    labor_costs_performed: float | None = Field(alias='laborCostsPerformed')
    lot_plan_qty: str | None = Field(alias='lotPlanQty')
    lot_total_qty: str | None = Field(alias='lotTotalQty')
    lots: list[Any]
    name: str | None
    note: str | None
    number: str | None
    number_plan: str | None
    order: float
    percent_exec_doc: int | None = Field(alias='percentExecDoc')
    percent_executive_schema: str | None = Field(alias='percentExecutiveSchema')
    percent_fact: str | None = Field(alias='percentFact')
    percent_inspection: int | None = Field(alias='percentInspection')
    percent_ks2: str | None = Field(alias='percentKs2')
    percent_plan: float | None = Field(alias='percentPlan')
    performed_fact: str | None = Field(alias='performedFact')
    plan_dates: list[Any]
    plan_name: str | None = Field(alias='planName')
    price_fact: int | str | None
    price_plan: str | int | None
    qty_by_delivery: str | None = Field(alias='qtyByDelivery')
    qty_contract: int | None
    qty_fact: int | None
    qty_ks2: str | None = Field(alias='qtyKs2')
    qty_plan: float
    representative: str | None
    representative_sign: str | None = Field(alias='representativeSign')
    setting_atg: str | None = Field(alias='settingAtg')
    setting_atg_middle: str | None = Field(alias='settingAtgMiddle')
    sign_dates: list[Any] | None
    smr_structure: SmrStructure | None = Field(alias='smrStructure')
    structure: dict | None
    sum_exec_doc: str | None = Field(alias='sumExecDoc')
    sum_executive_schema: str | None = Field(alias='sumExecutiveSchema')
    sum_fact: str | None = Field(alias='sumFact')
    sum_inspection: str | None = Field(alias='sumInspection')
    sum_plan: float | None = Field(alias='sumPlan')
    sum_qty_exec_doc: int | None = Field(alias='sumQtyExecDoc')
    sum_qty_inspection: int | None = Field(alias='sumQtyInspection')
    total: str | None
    total_plan: str | int | None = Field(alias='totalPlan')
    total_plan_for_executive_schema: str | None = Field(alias='totalPlanForExecutiveSchema')
    total_fact: str | None = Field(alias='totalFact')
    type_of_work: dict | None = Field(alias='typeOfWork')
    unit_rates: list[Any] = Field(alias='unitRates')
    units: str | None
    uploads_records: list[Any] = Field(alias='uploadsRecords')
