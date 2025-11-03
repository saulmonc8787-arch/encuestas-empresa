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
