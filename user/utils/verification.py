import requests
from random import randint

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from config.settings import ESKIZ_URL, ESKIZ_PASSWORD, ESKIZ_EMAIL
from user.models import VerifyUser, User


def get_token():
    url = ESKIZ_URL + 'auth/login'
    body = {'email': ESKIZ_EMAIL, 'password': ESKIZ_PASSWORD}
    res = requests.post(url, json=body)
    if res.status_code == 200:
        return res.json().get('data').get('token')


def send_sms(mobile_phone: str, code: str):
    body = {
    "mobile_phone": mobile_phone,
    "message": f"Your verification code is {code}",
    "from": "4546"
    }
    url = ESKIZ_URL + "message/sms/send"
    token = get_token()
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.post(url, headers=headers, json=body)
    print(res)
    if res.status_code == 200:
        return 'success'


def send_user_verify_code(user, is_forgot_password=False):
    code = randint(100_000, 999_999)
    if is_forgot_password is False:
        VerifyUser.objects.create(
            user=user,
            code=f'verify_username_{code}',
            is_active=False
        )
    elif is_forgot_password is True:
        VerifyUser.objects.create(
            user=user,
            code=f'forgot_password_{code}',
            is_active=False
        )
    send_sms(user.phone_number, code)


def check_verify_signup_code(phone_number, code):
    check = VerifyUser.objects.filter(
        user__phone_number=phone_number,
        code=f'verify_username_{code}',
        is_active=False
    )
    if check.exists():
        verify = check.first()
        verify.is_active = True
        verify.save()
        user = verify.user
        user.is_active = True
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'detail': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)


def check_verify_forgot_password_code(phone_number, code):
    check = VerifyUser.objects.filter(
        user__phone_number=phone_number,
        code=f'forgot_password_{code}',
        is_active=False
    )
    return check.exists()


def re_send_verify_user_code(phone_number):
    try:
        user = User.objects.get(phone_number=phone_number)
        send_user_verify_code(user)
        return Response({'detail': 'successfully send new code'})
    except User.DoesNotExist:
        return Response({'detail': 'username does not exist'}, status=status.HTTP_400_BAD_REQUEST)
