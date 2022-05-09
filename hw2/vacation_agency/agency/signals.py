from django.db.models.signals import post_save
from django.dispatch import receiver
from agency.models import ExcursionVisiting, ExcursionRating, User
from agency.tasks import email_confirmation
from django.core.signals import request_finished


@receiver(post_save, sender=ExcursionRating)
def update_average_excursion_rating(instance: ExcursionRating, created, *args, **kwargs):
    if created is True:
        ExcursionVisiting.objects.get(
            user_id=instance.user_id,
            excursion_id=instance.excursion_id
        ).update_user_rate(instance.score)


@receiver(post_save, sender=User)
def confirm_user_mail(instance: User, created, *args, **kwargs):
    if created is True:
        if instance.email is not None and instance.email != "":
            email_confirmation.delay(instance.email, instance.name)
