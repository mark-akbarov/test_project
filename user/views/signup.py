from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from user.serializers.signup import SignupSerializer, CheckUsernameSerializer

from user.utils.signup import signup, check_username


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return signup(**serializer.validated_data)


class CheckUsernameView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CheckUsernameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return check_username(**serializer.validated_data)
