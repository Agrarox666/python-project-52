from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import CharField, TextInput, PasswordInput
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import TaskUser

fields = ['first_name',
          'last_name',
          'username',
          'password1',
          'password2']
user_credentials_widgets = {
    'first_name': TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Name'),
    }),
    'username': TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Username')
    }),
    'last_name': TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Last name')
    }),
}
password_create_widget = PasswordInput(attrs={
    'class': "form-control",
    'placeholder': _('Password'),
    'autocomplete': "new-password"}
)
password_confirmation_widget = PasswordInput(attrs={
    'class': "form-control",
    'placeholder': _('Password confirmation'),
    'autocomplete': "new-password"}
)


class CreationForm(UserCreationForm):
    password1 = CharField(
        min_length=3, label=_('Password'),
        help_text=_('Your password must contain at least 3 characters'),
        widget=password_create_widget
    )

    password2 = CharField(
        min_length=3, label=_('Password confirmation'),
        help_text=_('To confirm, please enter your password again'),
        widget=password_confirmation_widget
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.full_name = f'{user.first_name} {user.last_name}'
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user

    class Meta(UserCreationForm.Meta):
        model = TaskUser
        fields = fields
        widgets = user_credentials_widgets


class UpdatingForm(UserChangeForm):
    password1 = CharField(
        min_length=3, label='Пароль',
        help_text=_('Your password must contain at least 3 characters'),
        widget=password_create_widget
    )

    password2 = CharField(
        min_length=3, label='Подтверждение пароля',
        help_text=_('To confirm, please enter your password again'),
        widget=password_confirmation_widget
    )
    password = None

    class Meta(UserChangeForm.Meta):
        model = TaskUser
        fields = fields
        widgets = user_credentials_widgets
