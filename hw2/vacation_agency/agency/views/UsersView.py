from rest_framework import generics
from agency.serializers.UserSerializer import UserSerializer, ExcursionSerializer
from agency.models import User, Excursion, ExcursionVisiting
from agency.views.CustomPaginator import CustomPagination


class UserViewRest(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    # используем здесь prefetch_related тк как имеем поле visited_excursions,
    # которое описано с помощью ManyToManyField
    queryset = User.objects.prefetch_related('visited_excursions')


class ExcursionViewRest(generics.ListAPIView):
    serializer_class = ExcursionSerializer
    queryset = Excursion.objects.all()
