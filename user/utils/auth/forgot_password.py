from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def forgot_password(request, email):
    # Look up the user by email
    user = get_object_or_404(User, email=email)

    # Check if the user is active
    if not user.is_active:
        return 'User account is not active'

    # Generate a password reset token
    token_generator = PasswordResetTokenGenerator()
    token = token_generator.make_token(user)

    # Generate a password reset link
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = request.build_absolute_uri('/reset_password/{}/{}'.format(uidb64, token))

    # Send a password reset email to the user
    subject = 'Password Reset Link'
    message = render_to_string('password_reset_email.html', {'reset_link': reset_link})
    send_mail(subject, message, 'noreply@example.com', [user.email], fail_silently=False)

    # Return a success message
    return f'Password reset link sent to {email}'
