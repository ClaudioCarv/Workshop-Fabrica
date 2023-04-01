from rest_framework import viewsets
from livros.api import serializers
from livros import models


class livrosViewSets(viewsets.ModelViewSet):
    serializers_class = serializers.livrosSerializer
    queryset = models.livros.objects.all()