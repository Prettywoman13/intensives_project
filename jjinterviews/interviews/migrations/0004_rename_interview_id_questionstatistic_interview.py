# Generated by Django 3.2.16 on 2022-12-19 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("interviews", "0003_auto_20221219_1408"),
    ]

    operations = [
        migrations.RenameField(
            model_name="questionstatistic",
            old_name="interview_id",
            new_name="interview",
        ),
    ]
