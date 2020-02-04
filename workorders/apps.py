from django.apps import AppConfig


class WorkordersConfig(AppConfig):
    name = 'maintdx.workorders'

    def ready(self):
        import maintdx.workorders.signals
