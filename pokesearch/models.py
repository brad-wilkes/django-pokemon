from django.contrib.auth.models import AbstractUser
from django.db import models

class Type(models.Model):
    name = models.CharField(unique=True)

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type1 = models.ManyToManyField(Type, related_name="type1")
    type2 = models.ManyToManyField(Type, related_name='type2')
    generation = models.IntegerField()

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemon"