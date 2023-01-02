import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Localdev")

application = get_wsgi_application()
