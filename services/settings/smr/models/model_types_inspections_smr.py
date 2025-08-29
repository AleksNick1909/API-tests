from pydantic import BaseModel, Field


class TypesInspectionsSmr(BaseModel):
    code: str | None
    control_type: str | None = Field(alias='controlType')
    holder_role: str | None = Field(alias='holderRole')
    id: int
    inspection_status: str | None = Field(alias='inspectionStatus')
    name: str
    order: int
    representative_role: str | None = Field(alias='representativeRole')
    system: bool
    types: str = Field(alias='type')
