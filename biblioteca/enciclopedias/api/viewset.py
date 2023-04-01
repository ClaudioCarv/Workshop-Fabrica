from rest_framework import viewsets
from enciclopedias.api import serializers
from enciclopedias import models


class EnciclopediasViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.EnciclopediasSerializer
    queryset = models.Enciclopedias.objects.all()