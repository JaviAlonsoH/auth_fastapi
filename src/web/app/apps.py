from django.apps import AppConfig


class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        from app.routers.properties_router import router
        from web.urls import api_router

        api_router.include_router(router, tags=[self.name])
