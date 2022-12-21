# Generated by Django 3.2.16 on 2022-12-20 12:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interviews", "0005_alter_interviewstatistic_completion_percentage"),
    ]

    operations = [
        migrations.AddField(
            model_name="interview",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]