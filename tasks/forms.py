from django.forms import ModelForm, TextInput, Textarea, Select, SelectMultiple
from django.utils.translation import gettext_lazy as _
from tasks.models import Task


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            }),
            'description': Textarea(attrs={
                'placeholder': _('Description'),
                'class': 'form-control',
                'cols': 40,
                'rows': 10,
            }),
            'status': Select(attrs={
                'class': 'form-select',
            }),
            'executor': Select(attrs={
                'class': 'form-select',
            }),
            'labels': SelectMultiple(attrs={
                'class': 'form-select',
            })
        }
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
