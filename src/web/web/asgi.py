import os

from starlette.middleware.cors import CORSMiddleware

from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi import FastAPI

from django.apps import apps
from django.config import settings
from django.core.wsgi import get_wsgi_application

from app.routers.routers import api_router

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")
app.mount("/app", WSGIMiddleware(get_wsgi_application()))
