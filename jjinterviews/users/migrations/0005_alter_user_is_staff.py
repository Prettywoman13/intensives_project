# Generated by Django 3.2.16 on 2022-12-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Moderator",
                verbose_name="staff status",
            ),
        ),
    ]
