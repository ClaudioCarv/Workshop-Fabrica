from rest_framework import serializers
from livros import models

class livrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.livros
        fields = '__all__'