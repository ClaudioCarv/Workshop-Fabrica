from rest_framework import serializers
from enciclopedias import models


class EnciclopediasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enciclopedias
        fields = '__all__'