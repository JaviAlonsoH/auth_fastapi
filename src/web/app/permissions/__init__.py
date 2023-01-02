from django.contrib.auth.models import Permission


def create_groups(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    add_property = Permission.objects.get(codename='add_property')
    change_property = Permission.objects.get(codename='change_property')
    delete_property = Permission.objects.get(codename='delete_property')
    view_property = Permission.objects.get(codename='view_property')

    mod_permissions = [
        add_property,
        change_property,
        delete_property,
        view_property,
    ]

    mods = Group(name='mod')
    mods.save()

    mods.permissions.set(mod_permissions)

    for user in User.objects.all():
        if user.role == 'MOD':
            mods.user_set.add(user)
