# Generated by Django 3.2.16 on 2022-12-13 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_avatar"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="username",
            new_name="nickname",
        ),
    ]