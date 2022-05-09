from django.apps import AppConfig


class AgencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agency'

    def ready(self):
        from . import signals
        # signals.request_finished.connect(signals.update_average_excursion_rating)
        # signals.request_finished.connect(signals.confirm_user_mail)
