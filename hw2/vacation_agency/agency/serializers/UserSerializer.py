from agency.models import User, Excursion, ExcursionVisiting
from rest_framework import serializers


# TODO: add field to Excursion with average rate
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['surname', 'last_date']


class ExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursion
        fields = (
            'id',
            'city',
            'duration',
            'price'
        )


class ExcursionVisitingSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    excursions = ExcursionSerializer(many=True)

    def create(self, validated_data):
        ...

    class Meta:
        model = ExcursionVisiting
        # лучше ли было бы просто использовать fields = '__all__'
        fields = (
            'id',
            'users',
            'excursions',
            'user_rate'
        )
