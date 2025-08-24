from pydantic import BaseModel, Field


# Вложенные модели
class Role(BaseModel):
    id: int
    name: str


class Organization(BaseModel):
    id: int
    name: str
    partner_id: int = Field(alias="partnerId")


class Division(BaseModel):
    id: int
    name: str
    organization: Organization


class SettingsSignaturesActs(BaseModel):
    acts_exec_docs: bool = Field(alias="actsExecDocs")
    acts_entrance_control: bool = Field(alias="actsEntranceControl")
    acts_pnr: bool = Field(alias="actsPnr")


class Company(BaseModel):
    id: int
    name: str
    is_system: bool = Field(alias="isSystem")
    settings_signatures_acts: SettingsSignaturesActs = Field(alias="settingsSignaturesActs")


class Partner(BaseModel):
    id: int
    name: str


class Representative(BaseModel):
    id: int
    name: str
    fio: str
    position: str
    partner: Partner | None = None
    documents_confirms: list | None = Field(None, alias="documentsConfirms")
    user: str | None = None
    phone: str


# Основная модель пользователя
class UserResponseModel(BaseModel):
    id: int
    login: str | None = None
    name: str
    fio: str
    position: str
    email: str
    phone: str
    role: Role
    division: Division
    company: Company
    active: bool
    activeSc: bool
    representative: Representative
    certificate: str | None = None
    power_of_attorney: str | None = Field(None, alias="powerOfAttorney")
    language: str
    profile_email: str | None = Field(None, alias="profileEmail")
    division_id: int | None = Field(None, alias="divisionId")
    last_login_date: str | None = Field(None, alias="lastLoginDate")
