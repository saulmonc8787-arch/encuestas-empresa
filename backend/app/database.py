import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://survey:survey@db:5432/surveys_db")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
