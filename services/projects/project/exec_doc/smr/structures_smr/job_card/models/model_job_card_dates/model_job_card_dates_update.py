# from pydantic import BaseModel, Field
#
#
# class JobDatesUpdateSchema(BaseModel):
#     accepted_gk: str | None = Field(None, alias='acceptedGk')
#     accepted_sk: str | None = Field(None, alias='acceptedSk')
#     completion_percent: int | None = Field(None, alias='completionPercent')
#     date_begin_fact: str | None = Field(None, alias='dateBeginFact')
#     date_begin_plan: str | None = Field(None, alias='dateBeginPlan')
#     date_end_fact: str | None = Field(None, alias='dateEndFact')
#     date_end_plan: str | None = Field(None, alias='dateEndPlan')
#     fact_period: list[FactPeriodItem] = Field(alias='factPeriod')
#     fact_period_general_labor_costs: int = Field(None, alias='factPeriodGeneralLaborCosts')
#     fact_smr_accumulative: str | None = Field(None, alias='factSmrAccumulative')
#     job_uploads: list = Field(None, alias='jobUploads')
#     links: list = None
#     name: str = None
#     plan_period: list[PlanPeriodItem] = Field(alias='planPeriod')
#     qty_fact: int = Field(None, alias='qtyFact')
#     qty_plan: int = Field(None, alias='qtyPlan')
#     show_all_dates: bool = Field(None, alias='showAllDates')
#     units: str = None
