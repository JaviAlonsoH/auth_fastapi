from django.urls import path
from app import views
from app.routers.properties_router import *

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.sign_up, name='signup'),
    path('create-property', views.create_property, name='create-property'),
    path('properties', get_properties, name='properties')
]
