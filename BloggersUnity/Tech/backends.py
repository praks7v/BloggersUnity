from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # Import the Q object


class CustomAuthenticationBackend(ModelBackend):
    """
    Custom Authentication Backend for Django.

    This authentication backend allows users to log in using either their username or email.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate a user based on their username or email and password.

        Args:
            request (HttpRequest): The current request object.
            username (str): The username or email provided for authentication.
            password (str): The user's password.

        Returns:
            User: The authenticated user or None if authentication fails.
        """
        user_model = get_user_model()
        try:
            user = user_model.objects.get(Q(username=username) | Q(email=username))
        except user_model.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
