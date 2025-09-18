from pydantic import BaseModel


class CompletionLine(BaseModel):
    completion: int
    deviation: int


class CompletionTableItem(BaseModel):
    name: str
    id: int
    plan: int
    fact: int
    children: list
    isJob: bool


class TimePeriodData(BaseModel):
    graphic: list
    completionLine: CompletionLine
    completionTable: list[CompletionTableItem]


class DashboardsSCurveSchema(BaseModel):
    week: TimePeriodData
    month: TimePeriodData
