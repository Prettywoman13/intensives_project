# Generated by Django 3.2.16 on 2022-12-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interviews", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="interview",
            name="closed",
            field=models.BooleanField(default=False),
        ),
    ]
