from typing import Any
from pydantic import BaseModel, Field


class PathItem(BaseModel):
    id: int
    name: str


class Direction(BaseModel):
    id: int
    name: str
    order: float
    code: str | None
    has_children: bool | None = Field(alias='hasChildren')
    has_type_of_works: bool | None = Field(alias='hasTypeOfWorks')
    parent_id: int | None = Field(alias='parentId')
    full_path: str = Field(alias='fullPath')


class AggregatedJobsData(BaseModel):
    units: str | None
    jobs_count: int | None = Field(alias='jobsCount')
    labor_costs: float = Field(alias='laborCosts')
    total_plan_exec_schema: float = Field(alias='totalPlanExecSchema')
    percent_executive_schema: float = Field(alias='percentExecutiveSchema')
    sum_executive_schema: float = Field(alias='sumExecutiveSchema')
    qty_fact: float = Field(alias='qtyFact')
    percent_fact: float = Field(alias='percentFact')
    sum_fact: float = Field(alias='sumFact')
    labor_costs_performed: float = Field(alias='laborCostsPerformed')
    percent_inspection: float | None = Field(alias='percentInspection')
    sum_inspection: float = Field(alias='sumInspection')
    qty_exec_doc: float = Field(alias='qtyExecDoc')
    percent_exec_doc: float = Field(alias='percentExecDoc')
    sum_exec_doc: float = Field(alias='sumExecDoc')
    percent_ks2: float = Field(alias='percentKs2')
    sum_ks2: float = Field(alias='sumKs2')
    qty_contract: float | None = Field(alias='qtyContract')
    qty_inspection: float | None = Field(alias='qtyInspection')
    qty_ks2: float = Field(alias='qtyKs2')


class StructuresSmrSchema(BaseModel):
    id: int
    name: str
    number: str | None
    parent: Any | None
    is_have_children: bool = Field(alias='isHaveChildren')
    is_have_jobs: bool | None = Field(alias='isHaveJobs')
    representative: Any | None
    order: float
    total: float
    total_fact: float = Field(alias='totalFact')
    total_plan: float = Field(alias='totalPlan')
    plan_percent: float = Field(alias='planPercent')
    fact_percent: float = Field(alias='factPercent')
    sum_fact: float = Field(alias='sumFact')
    sum_plan: float = Field(alias='sumPlan')
    percent_inspection: float | None = Field(alias='percentInspection')
    sum_inspection: float | None = Field(alias='sumInspection')
    percent_execDoc: float | None = Field(alias='percentExecDoc')
    sum_exec_doc: float | None = Field(alias='sumExecDoc')
    date_begin_plan: str | None = Field(alias='dateBeginPlan')
    date_begin_fact: str | None = Field(alias='dateBeginFact')
    date_end_plan: str | None = Field(alias='dateEndPlan')
    date_end_fact: str | None = Field(alias='dateEndFact')
    aggregated_jobs_data: AggregatedJobsData | None = Field(alias='aggregatedJobsData')
    path: list[PathItem]
    direction: Direction | None
    type_of_work: Any | None = Field(alias='typeOfWork')
    sum_exec_schema: float | None = Field(alias='sumExecSchema')
    percent_exec_schema: float | None = Field(alias='percentExecSchema')
    sum_exec_schema_total: float | None = Field(alias='sumExecSchemaTotal')
    unit: Any | None
    quantity: Any | None
    performed: Any | None
    qty_inspection: Any | None = Field(alias='qtyInspection')
    qty_exec_doc: Any | None = Field(alias='qtyExecDoc')
    cipher: str | None
    identifier: str | None
    labor_costs: Any | None = Field(alias='laborCosts')
    labor_costs_performed: Any | None = Field(alias='laborCostsPerformed')
    percent_ks2: Any | None = Field(alias='percentKs2')
    sum_ls2: Any | None = Field(alias='sumKs2')
    customer: Any | None
    kit_rd_numbers: Any | None = Field(alias='kitRdNumbers')
    level: Any | None
    level_value: Any | None = Field(alias='levelValue')
    is_created_from_estimate: bool | None = Field(alias='isCreatedFromEstimate')


class ResponseData(BaseModel):
    structures: list[StructuresSmrSchema] | None
    jobs: list[Any] | None
    changeJobIds: list[Any] = []


class OpenStructuresSmrSchema(BaseModel):
    breadcrumbs: list[Any] = []
    current_page: int
    per_page: int
    data: ResponseData
