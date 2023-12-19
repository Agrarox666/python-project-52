from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DateTimeField
import django.db.models


class TaskUser(AbstractUser):
    created_at = DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.get_full_name()




