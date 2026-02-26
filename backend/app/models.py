from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    surveys = relationship("Survey", back_populates="company")
    hojas_de_vida = relationship("HojaDeVida", back_populates="company")

class Survey(Base):
    __tablename__ = "surveys"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    description = Column(Text)
    active = Column(Boolean, default=True)
    valid_from = Column(TIMESTAMP(timezone=True), nullable=True)
    valid_to = Column(TIMESTAMP(timezone=True), nullable=True)
    short_key = Column(String, unique=True, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    company = relationship("Company", back_populates="surveys")

class HojaDeVida(Base):
    __tablename__ = "hojas_de_vida"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"))
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=True)
    direccion = Column(String, nullable=True)
    resumen = Column(Text, nullable=True)
    educacion = Column(JSONB, nullable=True)
    experiencia = Column(JSONB, nullable=True)
    habilidades = Column(JSONB, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    company = relationship("Company", back_populates="hojas_de_vida")
