from django.contrib.auth.models import User
from django.db import models

from labels.models import Label
from statuses.models import Status


# Create your models here.
class Task(models.Model):
    executor = models.ForeignKey(User,
                                 on_delete=models.SET_DEFAULT,
                                 related_name='task_executor',
                                 default=None,)
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               related_name='task_author',
                               default=None)
    status = models.ForeignKey(Status,
                               on_delete=models.SET_DEFAULT,
                               related_name='task_status',
                               default=None)
    labels = models.ManyToManyField(Label)

    name = models.CharField(max_length=150, unique=False)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
