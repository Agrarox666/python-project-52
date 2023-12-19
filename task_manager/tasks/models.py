from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import TaskUser


class Task(models.Model):
    executor = models.ForeignKey(TaskUser,
                                 on_delete=models.PROTECT,
                                 related_name='task_executor',
                                 verbose_name=_('Executor'),
                                 blank=True,
                                 null=True)
    author = models.ForeignKey(TaskUser,
                               on_delete=models.PROTECT,
                               related_name='task_author',
                               verbose_name=_('Author'))
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               related_name='task_status',
                               verbose_name=_('Status'),
                               null=True)
    labels = models.ManyToManyField(Label,
                                    blank=True,
                                    verbose_name=_('Labels'))

    name = models.CharField(_('Name'), max_length=150, unique=True)
    description = models.TextField(_('Description'), default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
