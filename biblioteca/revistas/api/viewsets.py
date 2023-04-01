from rest_framework import viewsets
from revistas.api import serializers
from revistas import models


class RevistasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RevistasSerializer
    queryset = models.Revistas.objects.all()