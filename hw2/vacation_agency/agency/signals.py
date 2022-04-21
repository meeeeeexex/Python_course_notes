from django.db.models.signals import post_save
from django.dispatch import receiver
from agency.models import ExcursionVisiting, ExcursionRating
from django.core.signals import request_finished


@receiver(post_save, sender=ExcursionRating)
def update_average_excursion_rating(instance: ExcursionRating, created, *args, **kwargs):
    print('Entered to console')
    if created is True:
        print('Entered to console')
        ExcursionVisiting.objects.get(
            user_id=instance.user_id,
            excursion_id=instance.excursion_id
        ).update_user_rate()
