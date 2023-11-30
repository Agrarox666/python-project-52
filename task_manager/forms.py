import django.forms
from django.forms import ModelForm, TextInput, PasswordInput, CharField

from task_manager.models import User


class UserForm(ModelForm):
    password2 = CharField(
        min_length=3, label='Подтверждение пароля',
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Подтверждение пароля",
            'autocomplete': "new-password"}
        )
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
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
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': "Пароль",
                'autocomplete': "new-password",
                'min_length': 3}
            )
        }
        help_texts = {
            'username': 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        }
        labels = {
            'first_name': "Имя",
            'last_name': "Фамилия",
            'username': "Имя пользователя",
            'password': "Пароль",
        }