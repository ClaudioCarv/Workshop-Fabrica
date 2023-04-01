from django.db import models
from uuid import uuid4


class Enciclopedias(models.Model):
    id_enciclopedias = models.UUIDField(primary_key= True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=300)
    lancamento = models.IntegerField()
    estado = models.CharField(max_length=20)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=300)
    criado = models.DateField(auto_now_add=True)
    