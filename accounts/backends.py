from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class CustomModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        UserModel = get_user_model()

        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))

            if user.check_password(password):
                return user

        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)