import fastapi
from fastapi.middleware.cors import CORSMiddleware

from .utils import getApiDescription

from sqlalchemy.orm import Session
from .database import SessionLocal, DatabaseModelClass, engine as databaseEngine


DatabaseModelClass.metadata.create_all(bind=databaseEngine)


api = fastapi.FastAPI(
    title="Meal-Idea-Generator",
    description=getApiDescription(),
    version="0.0.0",
    docs_url="/swagger",
    redoc_url="/docs",  # I prefer redoc as the main documentation
    terms_of_service=None,  # URL to the Terms of Service for the API
    contact=None,  # {name: str, url: str, email: str}
    license_info=None,  # {name: str, url: str}
)


# dependency
def getDatabase():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

from .routes import users
from .routes import images
from .routes import meals

api.include_router(users.router)
api.include_router(images.router)
api.include_router(meals.router)
