from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from statuses.models import Status


class CreateStatus(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            })
        }


class UpdateStatus(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            })
        }
