from transaccion.api.serializers import *
from rest_framework.viewsets import ModelViewSet


class transaccionViewset(ModelViewSet):
    serializer_class=serializadorTransaccion
    queryset = Transaccion.objects.all()

class categoriaViewset(ModelViewSet):
    serializer_class=serializadorCategorias
    queryset = Categoria.objects.all()