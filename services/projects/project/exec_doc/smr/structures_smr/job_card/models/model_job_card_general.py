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


class JobCardGeneralSchema(BaseModel):
    cipher: str | None
    cipher_rd: str | None = Field(alias='cipherRd')
    code: str | None
    code_plan: str | None = Field(alias='codePlan')
    contract_date_end: str | None = Field(alias='contractDateEnd')
    contract_date_start: str | None = Field(alias='contractDateStart')
    contract_number: str | None = Field(alias='contractNumber')
    contractor_signature: list[Any] | None = Field(alias='contractorSignature')
    custom_customer_name: str | None = Field(alias="customCustomerName")
    custom_rep_name: str | None = Field(alias='customRepName')
    customer: dict | None
    customer_signature: str | None = Field(alias='customerSignature')
    date_begin_contract: str | None = Field(alias='dateBeginContract')
    date_begin_plan: str | None = Field(alias='dateBeginPlan')
    date_end_contract: str | None = Field(alias='dateEndContract')
    date_end_plan: str | None = Field(alias='dateEndPlan')
    direction: Direction | None
    discipline: str | None
    element: str | None
    element_code: str | None = Field(alias='elementCode')
    element_qty: float | None = Field(alias='elementQty')
    estimate_name: str | None = Field(alias='estimateName')
    garancy_date: str | None = Field(alias='garancyDate')
    garancy_number: str | None = Field(alias='garancyNumber')
    go_completion_date: str | None = Field(alias='goCompletionDate')
    go_physical_volume: str | None = Field(alias='goPhysicalVolume')
    id: int
    id_plan: str | None = Field(alias='idPlan')
    identifier: str | None
    kit_rd_number: str | None = Field(alias='kitRdNumber')
    name: str
    number_plan: str | None = Field(alias='numberPlan')
    partner: Partner | None
    plan_name: str | None = Field(alias='planName')
    price_fact: float | None = Field(alias='priceFact')
    price_plan: float | None = Field(alias='pricePlan')
    pv_per_element: str | None = Field(alias='pvPerElement')
    qty_contract: float | None = Field(alias='qtyContract')
    qty_fact: float | None = Field(alias='qtyFact')
    qty_plan: float | None = Field(alias='qtyPlan')
    sign_dates: list[Any] = Field(alias='signDates')
    smr_structure: SmrStructure = Field(alias='smrStructure')
    sum_fact: float | None = Field(alias='sumFact')
    sum_plan: str | None = Field(alias='sumPlan')
    title: str | None
    type_of_work: TypeOfWork | None = Field(alias='typeOfWork')
    type_of_work_in_use: bool = Field(alias='typeOfWorkInUse')
    units: str | None
    zone: str | None