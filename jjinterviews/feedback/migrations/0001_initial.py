# Generated by Django 3.2.16 on 2022-12-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedBack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="содержимое")),
                (
                    "mail",
                    models.EmailField(max_length=150, verbose_name="почта"),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "обратная связь",
                "verbose_name_plural": "обратная связь",
            },
        ),
    ]