import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    '''status = django_filters.AllValuesFilter(
        field_name='status__name',
        label=_('Status'),
        widget=forms.Select(attrs={
            'class': 'form-select is-valid'
        }))
    executor = django_filters.AllValuesFilter(
        field_name='executor__full_name',
        label=_('Executor'),
        widget=forms.Select(attrs={
            'class': 'form-select is-valid'
        }))
    labels = django_filters.AllValuesFilter(
        field_name='labels__name',
        label=_('Label'),
        widget=forms.Select(attrs={
            'class': 'form-select is-valid'
        }))'''

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
