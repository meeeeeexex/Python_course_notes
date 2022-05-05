from rest_framework import generics
from agency.serializers.UserSerializer import UserSerializer, ExcursionSerializer
from agency.models import User, Excursion, ExcursionVisiting
from django.db import transaction


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
