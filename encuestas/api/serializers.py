from rest_framework import serializers
from encuestas.models import Encuesta, Pregunta, Respuesta, Entrada

class RespuestaSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Respuesta
        exclude = ('votos',)
        

    def create(self, validated_data):
        preguntas_data = validated_data.pop('preguntas')
        encuesta = Encuesta.objects.create(**validated_data)
        for pregunta_data in preguntas_data:
            Pregunta.objects.create(encuesta=encuesta, **pregunta_data)
        return encuesta

class PreguntaSerializer(serializers.ModelSerializer):
    respuestas = RespuestaSerializer(many=True)

    class Meta():
        model = Pregunta
        fields = "__all__"

    def create(self, validated_data):
        respuestas_data = validated_data.pop('respuestas')
        pregunta = Pregunta.objects.create(**validated_data)
        for respuesta_data in respuestas_data:
            Respuesta.objects.create(pregunta=pregunta, **respuesta_data)
        return pregunta

class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True)

    class Meta():
        model = Encuesta
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)


class EntradaSerializer(serializers.ModelSerializer):

    class Meta():
        model = Entrada
        fields = "__all__"