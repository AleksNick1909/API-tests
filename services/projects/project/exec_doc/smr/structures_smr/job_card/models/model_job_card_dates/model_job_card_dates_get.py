from pydantic import BaseModel, Field


class PartnerSchema(BaseModel):
    id: int
    name: str


class RepresentativeSchema(BaseModel):
    fio: str | None = None
    id: int
    name: str
    partner: PartnerSchema
    position: str
    user: dict | None = None


class PlanPeriodItem(BaseModel):
    date: str
    date_id: int
    id: int
    is_weekend: bool | None
    job_id: int
    measure: str | None = None
    qty: float | None = None


class FactPeriodItem(BaseModel):
    completion_percent: str | None = Field(None, alias='completionPercent')
    date: str
    date_id: int
    fact_confirmer: str | None = Field(None, alias='factConfirmer')
    fact_confirmer_sign: str | None = Field(None, alias='factConfirmerSign')
    fact_name: str | None
    general_labor_costs: str | None = Field(None, alias='generalLaborCosts')
    id: int
    is_weekend: bool | None
    job_id: int
    ks2_acts: list = Field(None, alias='ks2Acts')
    ks2_fact_qty: str | None = Field(None, alias='ks2FactQty')
    qty: int
    representative: RepresentativeSchema | None
    selected_job_contents: list = Field(alias='selectedJobContents')
    selected_job_parts: list = Field(alias='selectedJobParts')
    signature: dict | None = None
    uuid: str = None


class JobDatesSchema(BaseModel):
    accepted_gk: str | None = Field(None, alias='acceptedGk')
    accepted_sk: str | None = Field(None, alias='acceptedSk')
    completion_percent: int | None = Field(None, alias='completionPercent')
    date_begin_fact: str | None = Field(None, alias='dateBeginFact')
    date_begin_plan: str | None = Field(None, alias='dateBeginPlan')
    date_end_fact: str | None = Field(None, alias='dateEndFact')
    date_end_plan: str | None = Field(None, alias='dateEndPlan')
    fact_period: list[FactPeriodItem] = Field(alias='factPeriod')
    fact_period_general_labor_costs: int = Field(None, alias='factPeriodGeneralLaborCosts')
    fact_smr_accumulative: str | None = Field(None, alias='factSmrAccumulative')
    job_uploads: list = Field(None, alias='jobUploads')
    links: list = None
    name: str = None
    plan_period: list[PlanPeriodItem] = Field(alias='planPeriod')
    qty_fact: int = Field(None, alias='qtyFact')
    qty_plan: int = Field(None, alias='qtyPlan')
    show_all_dates: bool = Field(None, alias='showAllDates')
    units: str | None = None
