from transaccion.models import *
from rest_framework import serializers


class serializadorTransaccion(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields='__all__'


class serializadorCategorias(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields='__all__'