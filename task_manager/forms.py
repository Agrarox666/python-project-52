from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, UsernameField
from django.forms import TextInput, PasswordInput, CharField, Form

from task_manager.models import TaskUser


class CreationForm(UserCreationForm):
    password1 = CharField(
        min_length=3, label='Пароль',
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        widget=PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Пароль",
            'autocomplete': "new-password"}
        )
    )

    password2 = CharField(
        min_length=3, label='Подтверждение пароля',
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Подтверждение пароля",
            'autocomplete': "new-password"}
        )
    )

    class Meta(UserCreationForm.Meta):
        model = TaskUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        widgets = {
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


class UpdatingForm(UserChangeForm):
    password1 = CharField(
        min_length=3, label='Пароль',
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        widget=PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Пароль",
            'autocomplete': "new-password"}
        )
    )

    password2 = CharField(
        min_length=3, label='Подтверждение пароля',
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Подтверждение пароля",
            'autocomplete': "new-password"}
        )
    )
    password = None

    class Meta(UserChangeForm.Meta):
        model = TaskUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        widgets = {
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


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': "Username",
        'autocomplete': "new-password",
        'max_length': 150,
        'autocapitalize': "none",
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Password",
    }))

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'class': "form-control",
            'placeholder': "Username",
            'autocomplete': "new-password",
            'max_length': 150,
            'autocapitalize': "none",
        })
        self.fields['password'].widget = PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Password",
        })
        '''
