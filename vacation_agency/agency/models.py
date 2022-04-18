from django.db import models
from typing import List


def currently_available_cities() -> List[str]:
    return ['London', 'Paris', 'Berlin', 'Lisbon']


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

    # doesn't work properly
    #
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    family_size = models.IntegerField(default=1)
    wealthy_status = models.CharField(
        max_length=25,
        choices=WealthyStatus.ALL_DJANGO,
        default=WealthyStatus.NOT_SPECIFIED
    )
    # searched for some array or list of cities, so use CharFields
    # visited_cities = models.CharField(max_length=250, null=True, blank=True)
    last_date = models.DateField(null=True, blank=True)


class City:
    ALL_CITIES = ((x, x) for x in currently_available_cities())
    NOT_SPECIFIED = 'not specified'


class Accomodation(models.Model):
    def __str__(self):
        return f'{self.name, self.price}$ {self.square}m2'

    name = models.CharField(max_length=250)
    city_location = models.CharField(
        max_length=25,
        choices=City.ALL_CITIES,
        default=City.NOT_SPECIFIED
    )
    rating = models.PositiveIntegerField(null=True, blank=True)
    # decided to do it integer - not char - to provide only one counting system - only meters
    square = models.PositiveIntegerField()
    amount_of_beds = models.PositiveIntegerField(default=1)
    price = models.FloatField()


class Excursion(models.Model):
    def __str__(self):
        return f'{self.city, self.price}$ {self.duration}minutes'

    city = models.CharField(
        max_length=25,
        choices=City.ALL_CITIES,
        default=City.NOT_SPECIFIED
    )
    # we know that min duration is 30 minutes
    duration = models.PositiveSmallIntegerField(default=30)
    interests = models.CharField(max_length=250, null=True, blank=True)
    price = models.PositiveIntegerField()
    # rating is from 0 to 10
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
