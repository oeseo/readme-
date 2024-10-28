from django.contrib.auth.models import AbstractUser
from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    is_dismissed = models.BooleanField(default=False)
    dismissal_date = models.DateField(null=True, blank=True)
