from rest_framework import serializers


class UserVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()


class ReSendVerifyUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
