# Generated by Django 3.2.15 on 2023-04-04 18:29

from django.db import migrations

from ..hydrators import dehydrate_value

setting = {
    "setting": "show_admin_panel_link_in_ui",
    "python_type": "bool",
    "wet_value": True,
    "is_public": False,
}


def create_settings(apps, _):
    Setting = apps.get_model("misago_conf", "Setting")

    Setting.objects.create(
        setting=setting["setting"],
        python_type=setting["python_type"],
        dry_value=dehydrate_value(setting["python_type"], setting["wet_value"]),
        is_public=setting["is_public"],
    )


def delete_settings(apps, _):
    Setting = apps.get_model("misago_conf", "Setting")

    Setting.objects.filter(setting=setting["setting"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("misago_conf", "0009_delete_oauth2_access_token_method"),
    ]

    operations = [migrations.RunPython(create_settings, delete_settings)]
