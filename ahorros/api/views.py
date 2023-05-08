from rest_framework.viewsets import ModelViewSet
from ahorros.models import Ahorro
from ahorros.api.serializers import serializadorAhorro,consulta

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView


class ahorroApiViewset(ModelViewSet):
    serializer_class=serializadorAhorro
    queryset = Ahorro.objects.all()


class viewsetConsultaAhorros(APIView):
    pass
    # def post(self, request, format=None):
    #     serializer = consulta(data=request.data)
    #     if serializer.is_valid():
    #         id = serializer.validated_data['id']
    #         evento_obj = Ahorro.objects.get(cuenta)
    #         serializer = consulta_eventos_seri(evento_obj)  # usa el mismo objeto serializer para serializar los datos del evento
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)