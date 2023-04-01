from django.db import models
from uuid import uuid4

class Dvd(models.Model):
    id_dvd = models.UUIDField(primary_key= True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=300)
    lancamento = models.IntegerField()
    estado = models.CharField(max_length=20)
    