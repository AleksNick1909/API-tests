from pydantic import BaseModel


class NumerationSectionSchema(BaseModel):
    id: int
    section: str
