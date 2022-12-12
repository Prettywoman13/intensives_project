from django.contrib.postgres.fields import ArrayField
from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=60)
    text = models.TextField()
    path = ArrayField(models.IntegerField())
