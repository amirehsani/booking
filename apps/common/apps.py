from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = 'settings.db.models.BigAutoField'
    name = 'apps.common'
