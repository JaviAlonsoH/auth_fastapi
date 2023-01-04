from django.db import migrations
from .permissions import create_groups


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
