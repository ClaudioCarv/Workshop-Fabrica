from rest_framework import serializers
from dvd import models

class DvdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dvd
        fields = '__all__'