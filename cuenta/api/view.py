from rest_framework.viewsets import ModelViewSet
from cuenta.models import Cuenta
from cuenta.api.serializers import CuentaSerializer

class CuentaApiViewSet(ModelViewSet):
    serializer_class= CuentaSerializer
    queryset = Cuenta.objects.all()
    