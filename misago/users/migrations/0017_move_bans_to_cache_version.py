# Generated by Django 1.11.16 on 2018-11-29 20:28
from django.db import migrations, models

from .. import BANS_CACHE


def populate_cache_version(apps, _):
    BanCache = apps.get_model("misago_users", "BanCache")
    BanCache.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("misago_users", "0016_cache_version")]

    operations = [
        migrations.RemoveField(model_name="bancache", name="bans_version"),
        migrations.RunPython(populate_cache_version, migrations.RunPython.noop),
        migrations.AddField(
            model_name="bancache",
            name="cache_version",
            field=models.CharField(max_length=8),
        ),
    ]
