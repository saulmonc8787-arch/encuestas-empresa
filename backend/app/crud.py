from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import IntegrityError
import secrets

def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(name=company.name, slug=company.slug)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def create_survey(db: Session, company_id: int, survey: schemas.SurveyCreate):
    short_key = secrets.token_urlsafe(6)
    db_survey = models.Survey(
        company_id=company_id,
        title=survey.title,
        description=survey.description,
        short_key=short_key,
        active=True
    )
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def get_surveys_by_company(db: Session, company_id: int):
    return db.query(models.Survey).filter(models.Survey.company_id == company_id).all()

def create_hoja_de_vida(db: Session, company_id: int, hoja: schemas.HojaDeVidaCreate):
    db_hoja = models.HojaDeVida(
        company_id=company_id,
        nombres=hoja.nombres,
        apellidos=hoja.apellidos,
        email=hoja.email,
        telefono=hoja.telefono,
        direccion=hoja.direccion,
        resumen=hoja.resumen,
        educacion=hoja.educacion,
        experiencia=hoja.experiencia,
        habilidades=hoja.habilidades,
    )
    db.add(db_hoja)
    db.commit()
    db.refresh(db_hoja)
    return db_hoja

def get_hojas_de_vida_by_company(db: Session, company_id: int):
    return db.query(models.HojaDeVida).filter(models.HojaDeVida.company_id == company_id).all()

def get_hoja_de_vida(db: Session, hoja_id: int):
    return db.query(models.HojaDeVida).filter(models.HojaDeVida.id == hoja_id).first()
