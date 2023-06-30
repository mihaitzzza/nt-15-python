from django.contrib.auth.forms import BaseUserCreationForm
from users.models import AuthUser


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = AuthUser
        fields = ("email", "first_name", "last_name")
