from django.urls import path, include
from rest_framework.routers import DefaultRouter
from encuestas.api.views import EncuestaViewSet, PreguntaViewSet, RespuestaViewSet

router = DefaultRouter()
router.register(r"encuestas", EncuestaViewSet)
router.register(r"preguntas", PreguntaViewSet)
router.register(r"respuestas", RespuestaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]