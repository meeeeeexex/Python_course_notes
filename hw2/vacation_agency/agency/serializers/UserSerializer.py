from agency.models import User, Excursion, ExcursionVisiting
from rest_framework import serializers


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
            'price',
            'avg_rate',
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
