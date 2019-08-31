from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from encuestas.models import Entrada, Respuesta

@receiver(post_save, sender=Entrada)
def aumentar_votos(sender, instance, created, **kwargs):
    print("Creado: ", created)
    if created:
        respuesta = Respuesta.objects.get(pk=instance.pk_respuesta)
        print(respuesta.votos)
        respuesta.votos += 1
        respuesta.save()
        print(respuesta.votos)  