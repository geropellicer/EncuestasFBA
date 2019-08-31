from django.apps import AppConfig


class EncuestasConfig(AppConfig):
    name = 'encuestas'

    def ready(self):
        import encuestas.signals