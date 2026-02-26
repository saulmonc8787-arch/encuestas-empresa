from pydantic import BaseModel, field_validator
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

class HojaDeVidaBase(BaseModel):
    nombres: str
    apellidos: str
    email: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    resumen: Optional[str] = None

    @field_validator("email")
    @classmethod
    def email_must_be_valid(cls, v: str) -> str:
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError("email inválido")
        return v

class EducacionItem(BaseModel):
    institucion: str
    titulo: str
    anio_inicio: Optional[int] = None
    anio_fin: Optional[int] = None

class ExperienciaItem(BaseModel):
    empresa: str
    cargo: str
    anio_inicio: Optional[int] = None
    anio_fin: Optional[int] = None
    descripcion: Optional[str] = None

class HabilidadItem(BaseModel):
    nombre: str
    nivel: Optional[str] = None

class HojaDeVidaCreate(HojaDeVidaBase):
    educacion: Optional[list[EducacionItem]] = None
    experiencia: Optional[list[ExperienciaItem]] = None
    habilidades: Optional[list[HabilidadItem]] = None

class HojaDeVidaOut(HojaDeVidaBase):
    id: int
    company_id: int
    educacion: Optional[list] = None
    experiencia: Optional[list] = None
    habilidades: Optional[list] = None

    class Config:
        orm_mode = True
