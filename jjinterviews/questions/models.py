from django.contrib.postgres.fields import ArrayField
from django.db import models

from .managers import ItemManager


class Item(models.Model):

    objects = ItemManager()

    type = models.CharField(verbose_name="тип", max_length=60)
    text = models.TextField(verbose_name="текст")
    path = ArrayField(models.IntegerField())

    def __str__(self) -> str:
        return f"{self.type}: {self.text}"

    class Meta:
        verbose_name = "объект"
        verbose_name_plural = "объекты"
