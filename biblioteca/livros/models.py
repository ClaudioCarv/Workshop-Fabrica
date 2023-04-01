from django.db import models
from uuid import uuid3


class livros(models.Model):
    id_livro = models.UUIDField(primary_key= True, default=uuid3, editable=False)
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=300)
    lancamento = models.IntegerField()
    estado = models.CharField(max_length=20)
    pagginas = models.IntegerField()
    editora = models.CharField(max_length=300)
    criado = models.DateField(auto_now_add=True)