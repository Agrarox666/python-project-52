import django_filters
from django import forms

from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.AllValuesFilter(
        field_name='status__name',
        label='Статус',
        widget=forms.Select(attrs={
            'class': 'form-select is-valid'
        }))
    executor = django_filters.AllValuesFilter(
        field_name='executor__username',
        label='Исполнитель',
        widget=forms.Select(attrs={
            'class': 'form-select is-valid'
        }))
    labels = django_filters.AllValuesFilter(
        field_name='labels__name',
        label='Метка',
        widget=forms.Select(attrs={
            'class': 'form-select is-valid'
        }))

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']


class CheckBox(forms.Form):
    self_tasks = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input is-valid'
        })
    )
