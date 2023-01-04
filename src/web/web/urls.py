from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles import views

from fastapi import APIRouter


urlpatterns = [
    path("app/admin/", admin.site.urls),
    path("", include('app.urls')),
    path("", include('django.contrib.auth.urls'))
]

api_router = APIRouter()
