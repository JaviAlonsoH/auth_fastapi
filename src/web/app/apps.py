from django.apps import AppConfig


class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        import app.signals.handlers
        from .permissions import create_groups
        from django.contrib.auth.models import Group
