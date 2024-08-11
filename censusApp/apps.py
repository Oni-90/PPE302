from django.apps import AppConfig


class CensusappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'censusApp'

    def ready(self):
        import censusApp.signals #noqa: F401
