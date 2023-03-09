from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import AccessToken


def signin(request, username, password):
    # Authenticate the user
    user = authenticate(username=username, password=password)

    # Check if authentication failed
    if user is None:
        return 'Invalid credentials'

    # Check if the user is active
    if not user.is_active:
        return 'User account is not active'

    # Login the user
    login(request, user)

    # Issue an access token using Simple JWT
    access_token = AccessToken.for_user(user)

    # Return the access token as a string
    return str(access_token)

