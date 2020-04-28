from rest_framework import viewsets
from agile.serializers import AgileSerializer
from agile.models import Agile


class AgileViewSet(viewsets.ModelViewSet):
    queryset = Agile.objects.all()
    serializer_class = AgileSerializer
