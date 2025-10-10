from pydantic import BaseModel, Field


class StatusesInspectionsSchema(BaseModel):
    color: str | None
    id: int
    inspection_types: list | None = Field(alias='inspectionTypes')
    is_available_to_all_types: bool = Field(alias='isAvailableToAllTypes')
    name: str
    order: float
    system: bool
