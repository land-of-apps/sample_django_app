# Generated by Django 1.11.13 on 2018-06-09 15:23
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("misago_users", "0012_audittrail")]

    operations = [
        migrations.RemoveField(model_name="online", name="current_ip"),
        migrations.RemoveField(model_name="user", name="last_ip"),
        migrations.AlterField(
            model_name="user",
            name="joined_from_ip",
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
