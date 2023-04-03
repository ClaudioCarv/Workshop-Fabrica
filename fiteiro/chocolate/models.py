from django.db import models
from uuid import uuid4

class Chocolate(models.Model):
    id_chocolate = models.UUIDField(primary_key= True, default=uuid4, editable=False)
    Nome = models.CharField(max_length=300)
    Preço = models.CharField(max_length=300)
    validade = models.IntegerField()
    marca = models.CharField(max_length=20)
    