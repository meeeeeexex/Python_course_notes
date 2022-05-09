from django.db import models
from typing import List


# from django.utils import timezone


def currently_available_cities() -> List[str]:
    return ['London', 'Paris', 'Berlin', 'Lisbon']


class City:
    ALL_CITIES = ((x, x) for x in currently_available_cities())
    NOT_SPECIFIED = 'not specified'


# описательный класс экскурсии
class Excursion(models.Model):
    def __str__(self):
        return f'{self.city}, {self.price}$ {self.duration} minutes'

    class Meta:
        ordering = ['-id']

    city = models.CharField(
        max_length=25,
        choices=City.ALL_CITIES,
        default=City.NOT_SPECIFIED
    )
    # we know that min duration is 30 minutes
    duration = models.PositiveSmallIntegerField(default=30)
    interests = models.CharField(max_length=250, null=True, blank=True)
    price = models.PositiveIntegerField()


# класс для опознания кто побывал на какой экскурсии
class ExcursionVisiting(models.Model):
    def __str__(self):
        return f"{self.user.name} visited {self.excursion.city} with {self.excursion.duration}"

    class Meta:
        ordering = ['-user_rate']

    user = models.ForeignKey('agency.User', on_delete=models.CASCADE, related_name='users')
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, related_name='excursions')
    user_rate = models.FloatField(null=True, blank=True)

    def update_user_rate(self, score):
        self.user_rate = score
        self.save(update_fields=['user_rate'])


# класс для опознания кто отдыхал в каких апартаментах
class AccommodationVisiting(models.Model):
    def __str__(self):
        return f"{self.user.name} visited {self.excursion.city} with {self.excursion.duration}"

    user = models.ForeignKey('agency.User', on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE)
    user_rate = models.FloatField(null=True, blank=True)

    def update_user_rate(self):
        ...


# описательный класс пользователя
class User(models.Model):
    def __str__(self):
        return f"{self.id} {self.name}"

    class WealthyStatus:
        LOW = 'low'
        MEDIUM = 'medium'
        HIGH = 'high'
        NOT_SPECIFIED = 'not specified'

        ALL = (LOW, MEDIUM, HIGH, NOT_SPECIFIED)
        ALL_DJANGO = ((x, x) for x in ALL)

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, null=True, blank=True)
    surname = models.CharField(max_length=250)
    family_size = models.IntegerField(default=1)
    wealthy_status = models.CharField(
        max_length=25,
        choices=WealthyStatus.ALL_DJANGO,
        default=WealthyStatus.NOT_SPECIFIED
    )

    visited_excursions = models.ManyToManyField(Excursion, through=ExcursionVisiting)
    last_date = models.DateField(null=True, blank=True)


# описательный класс апартаментов
class Accommodation(models.Model):
    def __str__(self):
        return f'{self.name, self.price}$ {self.square}m2'

    name = models.CharField(max_length=250)
    city_location = models.CharField(
        max_length=25,
        choices=City.ALL_CITIES,
        default=City.NOT_SPECIFIED
    )

    square = models.PositiveIntegerField()
    amount_of_beds = models.PositiveIntegerField(default=1)
    price = models.FloatField()


# класс с помощью которого хранятся рейтинги оставленные той или иной экскурсии
class ExcursionRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE)
    score = models.FloatField(default=0)


# класс с помощью которого хранятся рейтинги оставленные тем или иным апартаментам
class AccommodationRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
