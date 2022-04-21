from django.shortcuts import render
from django.views.generic import TemplateView
from agency.models import User, ExcursionVisiting


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
    ...
