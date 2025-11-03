# Backend (FastAPI) — encuestas-empresa

Requisitos
- Python 3.11 (cuando ejecutes local sin Docker)
- Docker + docker-compose (recomendado)

Archivos principales
- app/main.py: aplicación FastAPI
- app/models.py: modelos SQLAlchemy mínimos (Company, Survey)
- app/schemas.py: pydantic schemas
- app/crud.py: funciones CRUD mínimas
- app/database.py: engine y session
- requirements.txt: dependencias

Ejecutar con Docker Compose (recomendado)
1. En la raíz del repo (donde está infra/docker-compose.yml):
   docker-compose up --build

2. Abrir: http://localhost:8000/docs para ver la documentación interactiva de OpenAPI (Swagger).

Ejecutar local (sin Docker)
1. Crear y activar un virtualenv
2. pip install -r requirements.txt
3. Ajustar DATABASE_URL en backend/.env o exportar la variable
4. Ejecutar:
   uvicorn app.main:app --reload --port 8000

Notas
- Este scaffold es mínimo. Añadir autenticación, migraciones Alembic y tests antes de producción.
