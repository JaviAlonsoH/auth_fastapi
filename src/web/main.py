import os

from importlib.util import find_spec
from django.apps import apps
from django.core.wsgi import get_wsgi_application
from web import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from fastapi.middleware.wsgi import WSGIMiddleware
from app.middlewares.auth import BasicAuthBackend

apps.populate(settings.INSTALLED_APPS)


from app.routers.properties_router import router

app = FastAPI(middleware=[Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())])

app.mount('/static',
          StaticFiles(
              directory=os.path.normpath(
                  os.path.join(
                      find_spec('django.contrib.admin').origin, '..', 'static')
              )
          ),
          name='static',
          )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api")
app.mount("/app", WSGIMiddleware(get_wsgi_application()))
