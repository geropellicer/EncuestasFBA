from django.urls import path, include
from rest_framework.routers import DefaultRouter
from encuestas.api.views import EncuestaViewSet, PreguntaViewSet, RespuestaViewSet, EntradaViewSet

router = DefaultRouter()
router.register(r"encuestas", EncuestaViewSet)
router.register(r"preguntas", PreguntaViewSet)
router.register(r"respuestas", RespuestaViewSet)
router.register(r"entradas", EntradaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]