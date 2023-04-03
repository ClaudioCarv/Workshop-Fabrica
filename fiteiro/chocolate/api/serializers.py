from rest_framework import serializers
from chocolate import models

class ChocolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chocolate
        fields = '__all__'