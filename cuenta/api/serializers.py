from rest_framework import serializers
from cuenta.models import Cuenta

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['id','usuario','nombre','tipo_cuenta','saldo_disponible']
        