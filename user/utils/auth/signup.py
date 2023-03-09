from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


def signup(request, username, email, password):
    # Check if a user with the given email or username already exists
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return 'User with this email or username already exists'

    # Create a new user object
    user = User.objects.create_user(username=username, email=email, password=password)

    # Login the user
    login(request, user)

    # Issue an access token using Simple JWT
    access_token = AccessToken.for_user(user)

    # Return the access token as a string
    return str(access_token)