from rest_framework import serializers


class SendForgotPasswordCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class CheckForgotPasswordCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()


class ForgotPasswordCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()
    new_password = serializers.CharField()
