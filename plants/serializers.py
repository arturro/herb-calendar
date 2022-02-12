from rest_framework import serializers

from .models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('pk', 'name', 'latin_name', 'notes')
