from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # Import the Q object


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(Q(username=username) | Q(email=username))
        except user_model.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
