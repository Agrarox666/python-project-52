from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import TextInput, CharField, PasswordInput
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={
                'class': "form-control",
                'placeholder': _('Username'),
                'autocomplete': "new-password",
                'max_length': 150,
                'autocapitalize': "none",
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': _('Password'),
            }
        )
    )
