from django.db import models

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type1 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="type1_pokemon", null=True)
    type2 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type2_pokemon', null=True)
    generation = models.IntegerField()

    class Meta:
        db_table = 'pokemon'
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemon"

    def __str__(self):
        return self.name
