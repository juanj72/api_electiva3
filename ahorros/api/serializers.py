from rest_framework import serializers
from ahorros.models import Ahorro


class serializadorAhorro(serializers.ModelSerializer):
    class Meta:
        model=Ahorro
        fields = '__all__'

class consulta(serializers.Serializer):
    id = serializers.IntegerField()