from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Encuestas Empresa - Backend (FastAPI)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajustar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Encuestas Empresa - Backend running"}

# Simple health check
@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

# Companies
@app.post("/companies", response_model=schemas.CompanyOut, tags=["companies"])
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db, company)

@app.get("/companies/{company_id}", response_model=schemas.CompanyOut, tags=["companies"])
def get_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.get_company(db, company_id)
    if not db_company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return db_company

# Simple survey creation (minimal)
@app.post("/companies/{company_id}/surveys", response_model=schemas.SurveyOut, tags=["surveys"])
def create_survey(company_id: int, survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    company = crud.get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return crud.create_survey(db, company_id, survey)

@app.get("/companies/{company_id}/surveys", response_model=list[schemas.SurveyOut], tags=["surveys"])
def list_surveys(company_id: int, db: Session = Depends(get_db)):
    return crud.get_surveys_by_company(db, company_id)

# Hojas de Vida
@app.post("/companies/{company_id}/hojas-de-vida", response_model=schemas.HojaDeVidaOut, tags=["hojas-de-vida"])
def create_hoja_de_vida(company_id: int, hoja: schemas.HojaDeVidaCreate, db: Session = Depends(get_db)):
    company = crud.get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return crud.create_hoja_de_vida(db, company_id, hoja)

@app.get("/companies/{company_id}/hojas-de-vida", response_model=list[schemas.HojaDeVidaOut], tags=["hojas-de-vida"])
def list_hojas_de_vida(company_id: int, db: Session = Depends(get_db)):
    return crud.get_hojas_de_vida_by_company(db, company_id)

@app.get("/companies/{company_id}/hojas-de-vida/{hoja_id}", response_model=schemas.HojaDeVidaOut, tags=["hojas-de-vida"])
def get_hoja_de_vida(company_id: int, hoja_id: int, db: Session = Depends(get_db)):
    db_hoja = crud.get_hoja_de_vida(db, hoja_id)
    if not db_hoja or db_hoja.company_id != company_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hoja de vida not found")
    return db_hoja

