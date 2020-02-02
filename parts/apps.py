from django.apps import AppConfig

class PartsConfig(AppConfig):
    name = 'maintdx.parts'

    def ready(self):
        import maintdx.parts.signals
