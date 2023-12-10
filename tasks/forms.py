from django.forms import ModelForm, TextInput, Textarea, Select

from tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control',
            }),
            'description': Textarea(attrs={
                'placeholder': 'Описание',
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
        }
