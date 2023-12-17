from django.db import models
from django.db.models import DateTimeField, CharField


# Create your models here.
class Status(models.Model):
    name = CharField(max_length=100, unique=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
