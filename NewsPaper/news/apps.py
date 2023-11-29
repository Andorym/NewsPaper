from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

class SubscribersConfig(AppConfig):
    name = 'subscribers'

    def ready(self):
        import subscribers.signals