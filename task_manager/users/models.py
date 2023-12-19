from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField


class TaskUser(AbstractUser):
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_full_name()
