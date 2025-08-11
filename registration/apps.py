from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration'

    def ready(self):
        import sys
        # Avoid running during migrations or shell
        if 'runserver' in sys.argv or 'shell' in sys.argv:
            from .models import save_codes
            save_codes()
