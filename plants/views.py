from rest_framework import viewsets

from plants import models, serializers


# @permission_classes([IsAuthenticated])
class PlantViewSet(viewsets.ModelViewSet):
    queryset = models.Plant.objects.all()
    serializer_class = serializers.PlantSerializer
