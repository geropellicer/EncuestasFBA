from django.contrib import admin
from encuestas.models import Encuesta, Pregunta, Respuesta, Entrada
# Register your models here.
admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Entrada)
