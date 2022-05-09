from django.shortcuts import render
from django.views.generic import TemplateView
from agency.models import User, Excursion, ExcursionVisiting


# Create your views here.
class WelcomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'users': [{
                'name': user.name,
                'last_city': user.visited_excursions.first().city
                if user.visited_excursions.first() is not None

                else "NO VISITED CITIES YET",
            }
                for user in
                User.objects.prefetch_related("visited_excursions").
                    order_by("id", "visited_excursions")[:100:-1]]
        }


class RatingView(TemplateView):
    template_name = 'ratings.html'

    def get_context_data(self, **kwargs):
        return {
            'excursions': [{
                'city': excursion.city,
                'duration': excursion.duration,
                'price': excursion.price,

            }
                for excursion in Excursion.
                                     objects.order_by("id")[:100]],

            # не описывал методы для апартаментов потому что они аналогичны -
            # и стоит сначала решить вопросы с экскурсиями - поэтому ниже код, который в дальнейшем
            # будет использоваться для экскурсий
            'apartments': [{
                'city': excursion_item.excursion.city,
                'rate': excursion_item.user_rate
            }

                for excursion_item in ExcursionVisiting.
                                          objects.order_by("user_rate")[:100]
            ]

        }


