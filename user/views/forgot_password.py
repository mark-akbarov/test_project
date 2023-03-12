from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Project
from user.serializers.forgot_password import (
    SendForgotPasswordCodeSerializer,
    CheckForgotPasswordCodeSerializer,
    ForgotPasswordCodeSerializer
)
from user.utils.forgot_password import (
    send_forgot_password_code,
    check_forgot_password_code,
    set_new_password
)


class SendForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SendForgotPasswordCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return send_forgot_password_code(**serializer.validated_data)


class CheckForgotPasswordCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CheckForgotPasswordCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return check_forgot_password_code(**serializer.validated_data)


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return set_new_password(**serializer.validated_data)
