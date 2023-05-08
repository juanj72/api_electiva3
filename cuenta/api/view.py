from rest_framework.viewsets import ModelViewSet
from cuenta.models import Cuenta
from cuenta.api.serializers import CuentaSerializer
from cuenta.api.filters import CuentasFilters
from django_filters.rest_framework import DjangoFilterBackend
from cuenta.api.permissions import isAdminOrReadOnly
from rest_framework.views import APIView

class CuentaApiViewSet(ModelViewSet):
    serializer_class= CuentaSerializer
    queryset = Cuenta.objects.all()
    #permission_classes = [isAdminOrReadOnly]
    # queryset = Cuenta.objects.filter(saldo_disponible__gte=250000)
    filter_backends=[DjangoFilterBackend]
    filterset_class=CuentasFilters


# class cuentas(APIView):
#     def post(self,request):
#         serializer =  

    