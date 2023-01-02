from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.staticfiles import views

urlpatterns = [
    path("app/admin/", admin.site.urls),
    path("", include('app.urls')),
    path("", include('django.contrib.auth.urls'))
]
