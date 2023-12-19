from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Task(models.Model):
    executor = models.ForeignKey(get_user_model(),
                                 on_delete=models.SET_DEFAULT,
                                 related_name='task_executor',
                                 verbose_name=_('Executor'),
                                 default=None, )
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.SET_DEFAULT,
                               related_name='task_author',
                               verbose_name=_('Author'),
                               default=None)
    status = models.ForeignKey(Status,
                               on_delete=models.SET_DEFAULT,
                               related_name='task_status',
                               verbose_name=_('Status'),
                               default=None)
    labels = models.ManyToManyField(Label, default=None, blank=True, verbose_name=_('Label'))

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
