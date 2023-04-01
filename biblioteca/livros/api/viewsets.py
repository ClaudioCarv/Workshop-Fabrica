from rest_framework import viewsets
from livros.api import serializers
from livros import models


class LivrosViewSets(viewsets.ModelViewSet):
    serializers_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()