from pydantic import BaseModel, Field


class DashboardsSettingsSchema(BaseModel):
    date: str
    is_all_period: bool = Field(alias='isAllPeriod')
    pnr_start_date: str | None = Field(alias='pnrStartDate')
    scale: str
    smr_start_date: str | None = Field(alias='smrStartDate')
