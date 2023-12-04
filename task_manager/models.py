from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import CharField, DateTimeField
from django.urls import reverse


class TaskUser(User):
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
