from rest_framework.routers import DefaultRouter
from ahorros.api.views import *

router_ahorro = DefaultRouter()

router_ahorro.register(prefix='ahorro',basename='ahorros',viewset=ahorroApiViewset)