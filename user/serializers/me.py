from rest_framework import serializers
from models.base import User


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number',
            )