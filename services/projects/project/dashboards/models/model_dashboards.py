from pydantic import BaseModel, Field


class GeneralInfoDashboardSchema(BaseModel):
    start_smr_plan: str | None = Field(alias='startSmrPlan')
    start_smr_fact: str | None = Field(alias='startSmrFact')
    start_pnr_plan: str | None = Field(alias='startPnrPlan')
    start_pnr_fact: str | None = Field(alias='startPnrFact')
    cost_smr: float | None = Field(None, alias='costSmr')
    contributed_smr: int = Field(alias='contributedSmr')
    done_smr: int = Field(alias='doneSmr')
    signed_exec_doc: int = Field(alias='signedExecDoc')
    signed_kc: int = Field(alias='signedKC')


class InspectionDashboardSchema(BaseModel):
    accepted: int
    rejected: int
    total: int


class PrescriptionDashboardSchema(BaseModel):
    not_completed: int = Field(alias='NotCompleted')
    completed_not_verified: int = Field(alias='completedNotVerified')
    completed_not_verified_overdue: int = Field(alias='completedNotVerifiedOverdue')
    completed_verified: int = Field(alias='completedVerified')
    completed_verified_overdue: int = Field(alias='completedVerifiedOverdue')
    date_completion_include_current_period: int = Field(alias='dateCompletionIncludeCurrentPeriod')
    date_completion_not_include_current_period: int | None = Field(None, alias='dateCompletionNotIncludeCurrentPeriod')
    rejected: int
    repeated: int
    total: int


class AuditDashboardSchema(BaseModel):
    completed: int
    planned: int
    total: int


class RemarkDashboardSchema(BaseModel):
    completed_not_verified: int = Field(alias='completedNotVerified')
    completed_not_verified_overdue: int = Field(alias='completedNotVerifiedOverdue')
    completed_verified: int = Field(alias='completedVerified')
    completed_verified_overdue: int = Field(alias='completedVerifiedOverdue')
    date_completion_include_current_period: int = Field(alias='dateCompletionIncludeCurrentPeriod')
    declined: int
    repeated: int
    total: int


class EquipmentMaterialsDashboardSchema(BaseModel):
    completed: int
    completed_overdue: int = Field(alias='completedOverdue')
    created_not_in_work: int = Field(alias='createdNotInWork')
    created_not_in_work_overdue: int = Field(alias='createdNotInWorkOverdue')
    date_fact_include_period: int = Field(alias='dateFactIncludePeriod')
    in_work: int = Field(alias='inWork')
    in_work_overdue: int = Field(alias='inWorkOverdue')
    total: int


class ExecDocDashboardSchema(BaseModel):
    readiness: int
    readiness_by_level: list = Field(alias='readinessByLevel')
