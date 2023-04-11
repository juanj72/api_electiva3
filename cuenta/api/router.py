from rest_framework.routers import DefaultRouter
from cuenta.api.view import CuentaApiViewSet

router_cuentas = DefaultRouter()

router_cuentas.register(prefix='cuentas',basename='cuentas', viewset=CuentaApiViewSet)
