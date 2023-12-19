from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Task(models.Model):
    executor = models.ForeignKey(get_user_model(),
                                 on_delete=models.PROTECT,
                                 related_name='task_executor',
                                 blank=True,
                                 null=True)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.PROTECT,
                               related_name='task_author', )
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               related_name='task_status',
                               null=True)
    labels = models.ManyToManyField(Label, blank=True)

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
