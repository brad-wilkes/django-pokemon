from django.contrib.auth.models import AbstractUser
from django.db import models

class Type(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type1 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="type1_pokemon", null=True)
    type2 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type2_pokemon', null=True)
    generation = models.IntegerField()

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemon"