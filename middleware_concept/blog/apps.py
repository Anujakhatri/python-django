from django.apps import AppConfig


class MiddlewareConfig(AppConfig):
    name = 'blog'

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals #import signals is ensure they are registered!
