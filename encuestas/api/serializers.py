from rest_framework import serializers
from encuestas.models import Encuesta, Pregunta, Respuesta

class RespuestaSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Respuesta
        fields = "__all__"

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


#  def create(self, validated_data):
#         order = Order.objects.get(pk=validated_data.pop('event'))
#         instance = Equipment.objects.create(**validated_data)
#         Assignment.objects.create(Order=order, Equipment=instance)
#         return instance

# def to_representation(self, instance):
#     representation = super(EquipmentSerializer, self).to_representation(instance)
#     representation['assigment'] = AssignmentSerializer(instance.assigment_set.all(), many=True).data
#     return representation 