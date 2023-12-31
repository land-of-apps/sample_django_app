# Generated by Django 1.10.5 on 2017-02-19 16:39
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("misago_users", "0006_update_settings")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="limits_private_thread_invites_to",
            field=models.PositiveIntegerField(
                choices=[(0, "Everybody"), (1, "Users I follow"), (2, "Nobody")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="subscribe_to_replied_threads",
            field=models.PositiveIntegerField(
                choices=[(0, "No"), (1, "Notify"), (2, "Notify with e-mail")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="subscribe_to_started_threads",
            field=models.PositiveIntegerField(
                choices=[(0, "No"), (1, "Notify"), (2, "Notify with e-mail")], default=0
            ),
        ),
    ]
