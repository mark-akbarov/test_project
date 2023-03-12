from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.utils.verification import send_user_verify_code


def check_username(username: str) -> bool:
    user = User.objects.filter(username__iexact=username, is_active=True).exists()
    return Response(data={'exists': user})


def signup(username: str, email: str, phone_number: str, password):
    check_email = User.objects.filter(username__iexact=username, is_active=True).exists()
    if check_email is True:
        return Response({'detail': 'username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    check_email = User.objects.filter(email=email, is_active=True).exists()
    if check_email is True:
        return Response({'detail': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = create_user(
        username=username,
        email=email,
        phone_number=phone_number,
        password=password
    )
    send_user_verify_code(user)
    return Response({'detail': 'successfully registered'}, status=status.HTTP_201_CREATED)


def create_user(
        username: str,
        email: str,
        phone_number: str,
        password=None
):
    user = User.objects.create(
        email=email,
        phone_number=phone_number,
        username=username,
        is_active=False,
        is_staff=False,
        is_superuser=False,
    )
    if password:
        user.set_password(password)
        user.save()
    return user
