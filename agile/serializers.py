from rest_framework import serializers
from agile.models import Agile


class AgileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agile
        fields = '__all__'


