from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Label


class CreateLabel(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            })
        }
        labels = {
            'name':  _('Name'),
        }


class UpdateLabel(ModelForm):
    class Meta:
        model = Label
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