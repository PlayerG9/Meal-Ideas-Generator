import fastapi
from fastapi.middleware.cors import CORSMiddleware
from .api_models import *


def getDescription() -> str:
    from os.path import dirname, join
    with open(join(dirname(__file__), 'description.md')) as file:
        return file.read()


api = fastapi.FastAPI(
    title="Meal-Idea-Generator",
    description=getDescription(),
    version="0.0.0",
    docs_url="/swagger",
    redoc_url="/docs",
    terms_of_service=None,  # URL to the Terms of Service for the API
    contact=None,  # {name: str, url: str, email: str}
    license_info=None,  # {name: str, url: str}
)


api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

from .routes import users
from .routes import meals

api.include_router(users.router)
api.include_router(meals.router)
