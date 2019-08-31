from django.db import models
from django.db.models import constraints

# Create your models here.
class Encuesta(models.Model):
    texto = models.CharField(max_length=50)
    codigo = models.PositiveSmallIntegerField(unique=True)
    #array de preguntas

    def __str__(self):
        return self.texto
    

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    codigo = models.PositiveSmallIntegerField()
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name="preguntas")
    cantidad_respondidas = models.PositiveSmallIntegerField(blank=True, null=True)
    #array de respuestass

    class Meta():
        constraints = [
            constraints.UniqueConstraint(fields=['encuesta', 'codigo'], name='codigo_unico') 
        ]

    def __str__(self):
        return self.texto
    

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="respuestas")
    texto = models.CharField(max_length=200)
    codigo = models.PositiveSmallIntegerField()
    votos = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta():
        constraints = [
            constraints.UniqueConstraint(fields=['pregunta', 'codigo'], name='codigo_unico') 
        ]

    def __str__(self):
        return self.texto
    