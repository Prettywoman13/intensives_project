# Generated by Django 3.2.16 on 2022-12-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
