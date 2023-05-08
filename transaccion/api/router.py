from rest_framework.routers import DefaultRouter
from transaccion.api.views import *

router_transaccion=DefaultRouter()

router_transaccion.register(prefix='transacciones',basename='transaccion',viewset=transaccionViewset)

router_categorias=DefaultRouter()

router_categorias.register(prefix='categorias',basename='categoria',viewset=categoriaViewset)