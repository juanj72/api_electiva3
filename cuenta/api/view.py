from rest_framework.viewsets import ModelViewSet
from cuenta.models import Cuenta
from cuenta.api.serializers import CuentaSerializer
from cuenta.api.filters import CuentasFilters
from django_filters.rest_framework import DjangoFilterBackend

class CuentaApiViewSet(ModelViewSet):
    serializer_class= CuentaSerializer
    queryset = Cuenta.objects.all()

    # queryset = Cuenta.objects.filter(saldo_disponible__gte=250000)
    filter_backends=[DjangoFilterBackend]
    filterset_class=CuentasFilters
    