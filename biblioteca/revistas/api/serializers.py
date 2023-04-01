from rest_framework import serializers
from revistas import models

class RevistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Revistas
        fields = '__all__'
