# Generated by Django 3.2.15 on 2022-11-01 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("misago_categories", "0008_auto_20190518_1659"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="color",
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="short_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
