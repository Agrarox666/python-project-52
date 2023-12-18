from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


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
        labels = {
            'name': _('Name'),
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
        labels = {
            'name': _('Name'),
        }
