from django.contrib import admin

from app.models import property_models


@admin.register(property_models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("_id", "title")

# Register your models here.
