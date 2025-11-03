from pydantic import BaseModel
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    slug: str

class CompanyCreate(CompanyBase):
    pass

class CompanyOut(CompanyBase):
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True

class SurveyBase(BaseModel):
    title: str
    description: Optional[str] = None

class SurveyCreate(SurveyBase):
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None

class SurveyOut(SurveyBase):
    id: int
    company_id: int
    short_key: Optional[str] = None
    active: bool

    class Config:
        orm_mode = True
