from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.forgot_password import SendForgotPasswordAPIView, CheckForgotPasswordCodeView, ForgotPasswordView
from .views.login import LoginAPIView
from .views.signup import SignupView, CheckUsernameView
from .views.verification import VerifyUserAPIView, ReSendVerifyUserAPIView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', SignupView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('check_username/', CheckUsernameView.as_view()),
    
    path('verify_user/', VerifyUserAPIView.as_view()),
    path('resend_verify_code/', ReSendVerifyUserAPIView.as_view()),

    
    path('send_forgot_password/', SendForgotPasswordAPIView.as_view()),
    path('check_forgot_password/', CheckForgotPasswordCodeView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),    
]
