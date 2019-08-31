from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import exceptions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView



from encuestas.models import Encuesta, Pregunta, Respuesta, Entrada
from encuestas.api.serializers import EncuestaSerializer, PreguntaSerializer, RespuestaSerializer, EntradaSerializer

class EncuestaViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['texto']

    def perform_create(self, serializer):
        serializer.save()

class PreguntaViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['texto']
    

    def perform_create(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class RespuestaViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['texto']
    

    def perform_create(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class EntradaViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    permission_classes = [IsAdminUser]
    
