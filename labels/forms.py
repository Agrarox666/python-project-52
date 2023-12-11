from django.forms import ModelForm, TextInput

from labels.models import Label


class CreateLabel(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control',
            })
        }


class UpdateLabel(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control',
            })
        }
