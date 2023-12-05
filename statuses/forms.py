from django.forms import ModelForm, TextInput

from statuses.models import Status


class CreateStatus(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control',
            })
        }


class UpdateStatus(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control',
            })
        }
