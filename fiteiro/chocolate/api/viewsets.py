from rest_framework import viewsets
from chocolate.api import serializers
from chocolate import models


class ChocolateViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ChocolateSerializer
    queryset = models.Chocolate.objects.all()