from django.db import models


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=100, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
