from rest_framework import viewsets
from dvd.api import serializers
from dvd import models

class DvdViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.DvdSerializer
    queryset = models.Dvd.objects.all()