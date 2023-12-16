from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    UsernameField)
from django.forms import TextInput, PasswordInput, CharField

from users.models import TaskUser

fields = ['first_name',
          'last_name',
          'username',
          'password1',
          'password2']

user_credentials_widgets = {
    'first_name': TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Имя",
    }),
    'username': TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Имя пользователя"
    }),
    'last_name': TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Фамилия"
    }),
}
password_create_widget = PasswordInput(attrs={
    'class': "form-control",
    'placeholder': "Пароль",
    'autocomplete': "new-password"}
)
password_confirmation_widget = PasswordInput(attrs={
    'class': "form-control",
    'placeholder': "Подтверждение пароля",
    'autocomplete': "new-password"}
)


class CreationForm(UserCreationForm):
    password1 = CharField(
        min_length=3, label='Пароль',
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        widget=password_create_widget
    )

    password2 = CharField(
        min_length=3, label='Подтверждение пароля',
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=password_confirmation_widget
    )

    class Meta(UserCreationForm.Meta):
        model = TaskUser
        fields = fields
        widgets = user_credentials_widgets


class UpdatingForm(UserChangeForm):
    password1 = CharField(
        min_length=3, label='Пароль',
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        widget=password_create_widget
    )

    password2 = CharField(
        min_length=3, label='Подтверждение пароля',
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=password_confirmation_widget
    )
    password = None

    class Meta(UserChangeForm.Meta):
        model = TaskUser
        fields = fields
        widgets = user_credentials_widgets


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Username",
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
                'placeholder': "Password",
            }
        )
    )
