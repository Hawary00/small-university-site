from django.apps import AppConfig
# from .models import *

class RegAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reg_app'
    
    def ready(self):
        import reg_app.signals