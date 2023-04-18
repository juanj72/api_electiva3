from django_filters import NumberFilter,FilterSet
from cuenta.models import *

class CuentasFilters(FilterSet):
    saldo = NumberFilter(field_name='saldo_disponible',lookup_expr='gt')
    class Meta:
        model = Cuenta
        fields=['saldo']