# Generated by Django 2.2.1 on 2019-05-19 00:08

from django.db import migrations, models
from django.db.models import F


def set_default_dry_value(apps, _):
    Setting = apps.get_model("misago_conf", "Setting")
    Setting.objects.filter(dry_value__isnull=True, default_value__isnull=False).update(
        dry_value=F("default_value")
    )


class Migration(migrations.Migration):
    dependencies = [("misago_conf", "0002_cache_version")]

    operations = [
        migrations.RemoveField(model_name="setting", name="description"),
        migrations.RemoveField(model_name="setting", name="field_extra"),
        migrations.RemoveField(model_name="setting", name="form_field"),
        migrations.RemoveField(model_name="setting", name="group"),
        migrations.RemoveField(model_name="setting", name="legend"),
        migrations.RemoveField(model_name="setting", name="name"),
        migrations.RemoveField(model_name="setting", name="order"),
        migrations.RunPython(set_default_dry_value),
        migrations.RemoveField(model_name="setting", name="default_value"),
        migrations.DeleteModel(name="SettingsGroup"),
        migrations.AddField(
            model_name="setting",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="conf",
                height_field="image_height",
                width_field="image_width",
            ),
        ),
        migrations.AddField(
            model_name="setting",
            name="image_size",
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="setting",
            name="image_width",
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="setting",
            name="image_height",
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
